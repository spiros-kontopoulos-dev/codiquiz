# Blueprint default target and priority excerpt
# Source: quiz-api/app/blueprint/coverage_service.py (excerpt lines 806-1110)
# Public portfolio excerpt; not standalone application code.

def _target_budget_rule_sort_key(rule: models.BlueprintTargetBudgetRule) -> tuple[int, int, int]:
    return (
        1 if rule.importance_tier != "any" else 0,
        1 if rule.suitability_tier != "any" else 0,
        rule.priority,
    )


def _target_budget_rule_for_cell(
        cell: CoverageCell,
        policy: TargetPolicy,
) -> models.BlueprintTargetBudgetRule | None:
    importance_tier = _concept_importance_tier(cell)
    suitability_tier = cell.suitability.tier
    matching_rules = [
        rule
        for rule in policy.budget_rules
        if rule.importance_tier in {importance_tier, "any"}
        and rule.suitability_tier in {suitability_tier, "any"}
    ]
    if not matching_rules:
        return None

    return max(matching_rules, key=_target_budget_rule_sort_key)


def _default_target_result(
        cell: CoverageCell,
        policy: TargetPolicy,
) -> tuple[int, list[str]]:
    """Generate a raw default target for one eligible cell.

    TAX 1.6b moves the magic numbers out of this helper and into seeded/admin
    Blueprint target-budget rules. The helper now only validates whether a cell
    may participate in the active policy mode. The per-concept distribution step
    then spends the selected rule's concept budget across the highest-ranked
    allowed question-type/difficulty cells.
    """

    importance_score = _concept_importance_score(cell)
    importance_tier = _concept_importance_tier(cell)
    suitability_score = cell.suitability.score or 0.0
    difficulty_weight = cell.suitability.difficulty_weight
    budget_rule = _target_budget_rule_for_cell(cell, policy)

    reasons: list[str] = [
        f"policy mode {policy.mode}",
        f"importance {importance_score:g} ({importance_tier})",
        f"{cell.suitability.tier} suitability",
    ]
    if cell.suitability.base_score is not None:
        reasons.append(f"base suitability {cell.suitability.base_score:g}")
    if cell.suitability.score is not None:
        reasons.append(f"effective suitability {suitability_score:g}")
    if difficulty_weight != 1.0:
        reasons.append(f"difficulty weight {difficulty_weight:g}")
    if cell.suitability.difficulty_allowed is False:
        reasons.append("difficulty is blocked by eligibility policy")
        return 0, reasons

    if importance_tier == "excluded" or importance_score < 40:
        reasons.append("importance below automatic target threshold")
        return 0, reasons

    if budget_rule is None:
        reasons.append("no active target-budget rule matched this cell")
        return 0, reasons

    reasons.append(
        "target-budget rule "
        f"{budget_rule.importance_tier}+{budget_rule.suitability_tier} "
        f"{budget_rule.min_target_questions}-{budget_rule.max_target_questions}"
    )

    if budget_rule.max_target_questions <= 0 or budget_rule.max_cells_per_concept <= 0:
        reasons.append("target-budget rule disables automatic targets for this category")
        return 0, reasons

    if cell.suitability.target_mode != "recommended":
        reasons.append("suitability is not recommended for automatic generation")
        return 0, reasons

    return 1, reasons


def _default_cell_rank(
        cell: CoverageCell,
        policy: TargetPolicy,
) -> tuple[int, int, float, float, float, int, str, int]:
    budget_rule = _target_budget_rule_for_cell(cell, policy)
    raw_target, _ = _default_target_result(cell, policy)
    return (
        budget_rule.priority if budget_rule is not None else -1,
        1 if cell.suitability.tier == "strong" else 0,
        float(cell.suitability.score or 0.0),
        float(cell.suitability.base_score or 0.0),
        float(cell.suitability.difficulty_weight),
        raw_target,
        cell.question_type.name.lower(),
        -DIFFICULTY_ORDER.index(cell.difficulty),
    )


def _concept_target_budget(
        concept_cells: list[CoverageCell],
        policy: TargetPolicy,
) -> tuple[int, int, models.BlueprintTargetBudgetRule | None]:
    matching_rules = [
        rule
        for cell in concept_cells
        if (rule := _target_budget_rule_for_cell(cell, policy)) is not None
        and _default_target_result(cell, policy)[0] > 0
    ]
    if not matching_rules:
        return 0, 0, None

    selected_rule = max(
        matching_rules,
        key=lambda rule: (rule.max_target_questions, rule.max_cells_per_concept, rule.priority),
    )
    return selected_rule.max_target_questions, selected_rule.max_cells_per_concept, selected_rule


def _select_default_targets(
        cells: list[CoverageCell],
        policy: TargetPolicy,
) -> dict[DefaultTargetKey, SelectedDefaultTarget]:
    """Choose default targets by spending concept-level budget into best cells."""

    cells_by_concept: dict[int, list[CoverageCell]] = defaultdict(list)
    for cell in cells:
        if _default_target_result(cell, policy)[0] > 0:
            cells_by_concept[cell.concept_context.concept_id].append(cell)

    selected: dict[DefaultTargetKey, SelectedDefaultTarget] = {}
    for concept_cells in cells_by_concept.values():
        if not concept_cells:
            continue

        concept_budget, cell_budget, concept_rule = _concept_target_budget(concept_cells, policy)
        if concept_budget <= 0 or cell_budget <= 0:
            continue

        remaining_questions = concept_budget
        selected_cells = 0

        for cell in sorted(concept_cells, key=lambda item: _default_cell_rank(item, policy), reverse=True):
            if selected_cells >= cell_budget or remaining_questions <= 0:
                break

            raw_target, rationale = _default_target_result(cell, policy)
            if raw_target <= 0:
                continue

            suggested_target = min(raw_target, remaining_questions)
            if suggested_target <= 0:
                continue

            selected[_default_target_key(cell)] = (
                suggested_target,
                rationale + [
                    f"selected within concept budget {concept_budget}",
                    f"selected within cell budget {cell_budget}",
                    f"concept budget source rule {concept_rule.id if concept_rule is not None else 'none'}",
                ],
            )
            remaining_questions -= suggested_target
            selected_cells += 1

    return selected


def get_generated_question_blueprint_alignment(
        db: Session,
        concept_id: int | None,
        question_type_id: int | None,
        difficulty: str | None,
        expansion_multiplier: int = 5,
) -> GeneratedQuestionBlueprintAlignment:
    """Classify one generated draft against the active Blueprint target policy.

    The classification is intentionally non-blocking. A full gap becomes an
    expansion label, not a rejection reason. The target selection is calculated
    across all active cells first, then the requested cell is looked up; this
    avoids changing concept-budget selection by filtering down to a single cell.
    """

    normalized_difficulty = difficulty.strip().casefold() if difficulty else None
    if concept_id is None or question_type_id is None or normalized_difficulty not in DIFFICULTIES:
        return GeneratedQuestionBlueprintAlignment(
            status="needs_mapping_review",
            target_count=None,
            approved_count=None,
            pending_review_count=None,
            effective_gap_count=None,
            expansion_cap_count=None,
            reason="Draft is missing a resolved concept, question type, or supported difficulty.",
        )

    cells = _build_cells(db=db, include_inactive=False)
    policy = _load_target_policy(db)
    selected_targets = _select_default_targets(cells, policy)
    target_key: DefaultTargetKey = (concept_id, question_type_id, normalized_difficulty)
    cell = next((candidate for candidate in cells if _default_target_key(candidate) == target_key), None)

    if cell is None:
        return GeneratedQuestionBlueprintAlignment(
            status="outside_blueprint_target",
            target_count=None,
            approved_count=None,
            pending_review_count=None,
            effective_gap_count=None,
            expansion_cap_count=None,
            reason="No active Blueprint coverage cell exists for this concept/question type/difficulty.",
        )

    if target_key not in selected_targets:
        return GeneratedQuestionBlueprintAlignment(
            status="outside_blueprint_target",
            target_count=0,
            approved_count=cell.approved_count,
            pending_review_count=cell.pending_review_count,
            effective_gap_count=0,
            expansion_cap_count=0,
            reason="The active Blueprint target policy does not currently select this cell for automatic coverage.",
        )

    target_count, rationale = selected_targets[target_key]
    effective_gap_count = max(target_count - cell.approved_count - cell.pending_review_count, 0)
    expansion_cap_count = max(target_count * max(expansion_multiplier, 1), target_count)
    existing_count = cell.approved_count + cell.pending_review_count

    if effective_gap_count > 0:
        status = "gap_fill"
        reason = f"Blueprint effective gap is {effective_gap_count}; this draft helps fill the minimum target."
    elif existing_count < expansion_cap_count:
        status = "expansion"
        reason = (
            "Blueprint minimum is already covered, but this draft is still under "
            f"the soft expansion cap ({existing_count}/{expansion_cap_count} existing approved/pending)."
        )
    else:
        status = "over_expansion_cap"
        reason = (
            "Blueprint minimum is already covered and the soft expansion cap has been reached "
            f"({existing_count}/{expansion_cap_count} existing approved/pending)."
        )

    if rationale:
        reason = f"{reason} Policy: {'; '.join(rationale[:4])}."

    return GeneratedQuestionBlueprintAlignment(
        status=status,
        target_count=target_count,
        approved_count=cell.approved_count,
        pending_review_count=cell.pending_review_count,
        effective_gap_count=effective_gap_count,
        expansion_cap_count=expansion_cap_count,
        reason=reason,
    )


def _default_target_count(
        cell: CoverageCell,
        policy: TargetPolicy,
) -> int:
    target_count, _ = _default_target_result(cell, policy)
    return target_count

def _default_hard_gap(cell: CoverageCell, policy: TargetPolicy) -> int:
    return max(_default_target_count(cell, policy) - cell.approved_count, 0)


def _default_effective_gap(cell: CoverageCell, policy: TargetPolicy) -> int:
    return max(_default_target_count(cell, policy) - cell.approved_count - cell.pending_review_count, 0)


def _default_generation_priority(
        cell: CoverageCell,
        policy: TargetPolicy,
        target_count: int | None = None,
) -> priority_service.GenerationPriority:
    default_target_count = _default_target_count(cell, policy) if target_count is None else target_count
    return priority_service.calculate_generation_priority(
        target_count=default_target_count,
        approved_count=cell.approved_count,
        pending_review_count=cell.pending_review_count,
        hard_gap_count=max(default_target_count - cell.approved_count, 0),
        effective_gap_count=max(default_target_count - cell.approved_count - cell.pending_review_count, 0),
        suitability_score=cell.suitability.score,
        suitability_tier=cell.suitability.tier,
        rule_priority=cell.rule.priority,
    )

def _sort_cells(
        cells: list[CoverageCell],
        sort_by: schemas.BlueprintCoverageSortBy,
        sort_dir: schemas.BlueprintCoverageSortDirection,
) -> list[CoverageCell]:
    # Keep deterministic secondary ordering while allowing the primary sort to change.
    cells = sorted(
        cells,
        key=lambda cell: (
            cell.concept_context.concept.name.lower(),
            cell.question_type.name.lower(),
