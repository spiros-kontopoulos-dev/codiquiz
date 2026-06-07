# AI generation planner contract and entrypoint
# Source: quiz-api/app/ai_generation/planner_service.py (excerpt lines 22-130)
# Public portfolio excerpt; not standalone application code.

class AllocationUnit:
    # Generation contract mode. Normal mode targets a known path; reverse mode
    # can target a broader path and expects future AI classification metadata.
    generation_mode: str

    # Legacy compatibility target. language_id remains required by the current
    # ai_generation_plan_items table, but the admin UI now chooses the new
    # taxonomy. For Python, this is resolved from Technology.slug/name.
    language_id: int | None
    category_id: int | None
    topic_id: int | None

    # New content taxonomy target.
    technology_id: int | None
    technology_domain_id: int | None
    technology_module_id: int | None
    technology_topic_id: int | None
    technology_subtopic_id: int | None
    primary_concept_id: int | None

    # Assessment / generation settings.
    question_type_id: int | None
    difficulty: str | None
    prompt_context: str | None


class PlanValidationError(ValueError):
    pass


def build_ai_generation_plan(
    db: Session,
    payload: AIGenerationPlanCreate,
) -> AIGenerationPlanPreview:
    """Normalize a flexible AI-generation request into concrete plan items.

    The active generation target is now the new content taxonomy:
    Technology -> Domain -> Module -> Topic -> optional Concept. Question type
    and difficulty stay separate assessment settings. Legacy Language/Category/
    Topic fields are still accepted temporarily for older clients and saved
    batches, but the admin UI should no longer send them.
    """

    rng = random.Random(payload.random_seed)

    if payload.allocation_strategy == "manual":
        plan_items = _build_manual_plan(db, payload)
    else:
        plan_items = _build_distributed_plan(db, payload, rng)

    planned_count = sum(item.requested_count for item in plan_items)
    if planned_count != payload.requested_count:
        raise PlanValidationError(
            f"planned_count ({planned_count}) must equal requested_count ({payload.requested_count})"
        )

    return AIGenerationPlanPreview(
        requested_count=payload.requested_count,
        planned_count=planned_count,
        generation_mode=payload.generation_mode,
        plan_item_count=len(plan_items),
        allocation_strategy=payload.allocation_strategy,
        plan_items=plan_items,
    )


def _build_manual_plan(
    db: Session,
    payload: AIGenerationPlanCreate,
) -> list[AIGenerationPlanItemPreview]:
    if payload.plan_items:
        items = payload.plan_items
    else:
        # Keep the simple version first-class: one payload can still say
        # "generate 20 Python / Lists / Predict Output / Beginner questions"
        # without needing a nested allocation plan.
        items = [
            AIGenerationPlanItemInput(
                requested_count=payload.requested_count,
                generation_mode=payload.generation_mode,
                language_id=payload.language_id,
                category_id=payload.category_ids[0] if payload.category_ids else None,
                topic_id=payload.topic_ids[0] if payload.topic_ids else None,
                technology_id=payload.technology_id,
                technology_domain_id=payload.technology_domain_ids[0] if payload.technology_domain_ids else None,
                technology_module_id=payload.technology_module_ids[0] if payload.technology_module_ids else None,
                technology_topic_id=payload.technology_topic_ids[0] if payload.technology_topic_ids else None,
                technology_subtopic_id=payload.technology_subtopic_ids[0] if payload.technology_subtopic_ids else None,
                primary_concept_id=payload.primary_concept_ids[0] if payload.primary_concept_ids else None,
                question_type_id=payload.question_type_ids[0]
                if payload.question_type_ids
                else None,
                difficulty=payload.difficulties[0] if payload.difficulties else None,
                prompt_context=payload.prompt_instructions,
            )
        ]

    plan_items: list[AIGenerationPlanItemPreview] = []
    for position, item in enumerate(items, start=1):
        unit = AllocationUnit(
            generation_mode=item.generation_mode or payload.generation_mode,
            language_id=item.language_id or payload.language_id,
            category_id=item.category_id,
            topic_id=item.topic_id,
            technology_id=item.technology_id or payload.technology_id,
            technology_domain_id=item.technology_domain_id,
            technology_module_id=item.technology_module_id,
            technology_topic_id=item.technology_topic_id,
            technology_subtopic_id=item.technology_subtopic_id,

# AI generation allocation helpers
# Source: quiz-api/app/ai_generation/planner_service.py (excerpt lines 227-315)
# Public portfolio excerpt; not standalone application code.

def _allocate_group_counts(
    total_count: int,
    groups: list[AIGenerationAllocationGroupInput],
    strategy: str,
    rng: random.Random,
) -> list[int]:
    explicit_total = sum(group.requested_count or 0 for group in groups)
    if explicit_total > total_count:
        raise PlanValidationError("group requested counts cannot exceed requested_count")

    missing_indexes = [index for index, group in enumerate(groups) if group.requested_count is None]
    counts = [group.requested_count or 0 for group in groups]

    if missing_indexes:
        remaining = total_count - explicit_total
        missing_groups = [groups[index] for index in missing_indexes]
        distributed = _allocate_count_for_groups(remaining, missing_groups, strategy, rng)
        for index, count in zip(missing_indexes, distributed, strict=True):
            counts[index] = count
    elif explicit_total != total_count:
        raise PlanValidationError("explicit group requested counts must sum to requested_count")

    return counts


def _allocate_count_for_groups(
    total_count: int,
    groups: list[AIGenerationAllocationGroupInput],
    strategy: str,
    rng: random.Random,
) -> list[int]:
    if strategy == "weighted":
        return _allocate_weighted_count(total_count, [group.weight or 1 for group in groups])

    return _allocate_count(total_count, len(groups), strategy, rng)


def _allocate_count(
    total_count: int,
    bucket_count: int,
    strategy: str,
    rng: random.Random,
) -> list[int]:
    if bucket_count <= 0:
        raise PlanValidationError("cannot allocate questions without target buckets")

    if total_count < 0:
        raise PlanValidationError("cannot allocate a negative question count")

    if strategy == "random":
        counts = [0 for _ in range(bucket_count)]
        for _ in range(total_count):
            counts[rng.randrange(bucket_count)] += 1
        return counts

    # Equal and weighted-without-inner-weights both use the same fair split
    # inside one group. For exact custom per-combination counts, the UI can send
    # manual plan_items.
    base_count = total_count // bucket_count
    remainder = total_count % bucket_count

    return [base_count + (1 if index < remainder else 0) for index in range(bucket_count)]


def _allocate_weighted_count(total_count: int, weights: list[int]) -> list[int]:
    if not weights:
        raise PlanValidationError("weighted allocation needs at least one group")

    if any(weight <= 0 for weight in weights):
        raise PlanValidationError("group weights must be positive integers")

    weight_total = sum(weights)
    raw_allocations = [(total_count * weight) / weight_total for weight in weights]
    counts = [int(value) for value in raw_allocations]
    remainder = total_count - sum(counts)

    # Largest-remainder allocation keeps the total exact while respecting the
    # requested weights as closely as possible.
    remainder_order = sorted(
        range(len(weights)),
        key=lambda index: (raw_allocations[index] - counts[index], weights[index]),
        reverse=True,
    )
    for index in remainder_order[:remainder]:
        counts[index] += 1

    return counts
