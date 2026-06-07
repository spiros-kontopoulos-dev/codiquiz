# Blueprint generation candidate bridge
# Source: quiz-api/app/blueprint/generation_candidate_service.py (excerpt lines 1-170)
# Public portfolio excerpt; not standalone application code.

from app import schemas
from app.blueprint import coverage_service
from sqlalchemy.orm import Session


DEFAULT_GENERATION_MODE = "normal"


def _candidate_plan_item(
        row: schemas.BlueprintCoverageCellRead,
        requested_count: int,
) -> schemas.BlueprintGenerationCandidatePlanItemRead | None:
    path = row.path

    # Blueprint generation candidates are concept-level targets. If a taxonomy
    # path is incomplete, keep the coverage row visible elsewhere but do not
    # emit a planner-ready item that would fail AI planner validation.
    if (
        path.technology is None
        or path.domain is None
        or path.module is None
        or path.topic is None
        or path.concept is None
    ):
        return None

    return schemas.BlueprintGenerationCandidatePlanItemRead(
        requested_count=requested_count,
        generation_mode=DEFAULT_GENERATION_MODE,
        technology_id=path.technology.id,
        technology_domain_id=path.domain.id,
        technology_module_id=path.module.id,
        technology_topic_id=path.topic.id,
        technology_subtopic_id=path.subtopic.id if path.subtopic is not None else None,
        primary_concept_id=row.concept_id,
        question_type_id=row.question_type_id,
        difficulty=row.difficulty,
        prompt_context=None,
    )


def _candidate_from_row(
        *,
        rank: int,
        row: schemas.BlueprintCoverageCellRead,
        max_questions_per_candidate: int,
) -> schemas.BlueprintGenerationCandidateRead | None:
    if row.suitability_target_mode != "recommended":
        return None
    if row.effective_gap_count <= 0:
        return None
    if row.generation_priority_score <= 0:
        return None

    requested_count = min(row.effective_gap_count, max_questions_per_candidate)
    if requested_count <= 0:
        return None

    plan_item = _candidate_plan_item(row, requested_count)
    if plan_item is None:
        return None

    return schemas.BlueprintGenerationCandidateRead(
        rank=rank,
        requested_count=requested_count,
        concept_id=row.concept_id,
        concept_slug=row.concept_slug,
        concept_name=row.concept_name,
        path=row.path,
        question_type_id=row.question_type_id,
        question_type_code=row.question_type_code,
        question_type_name=row.question_type_name,
        difficulty=row.difficulty,
        target_count=row.target_count,
        approved_count=row.approved_count,
        pending_review_count=row.pending_review_count,
        hard_gap_count=row.hard_gap_count,
        effective_gap_count=row.effective_gap_count,
        suitability_score=row.suitability_score,
        suitability_tier=row.suitability_tier,
        generation_priority_score=row.generation_priority_score,
        generation_priority_bucket=row.generation_priority_bucket,
        generation_priority_reasons=row.generation_priority_reasons,
        rule_id=row.rule_id,
        rule_scope_key=row.rule_scope_key,
        rule_priority=row.rule_priority,
        plan_item=plan_item,
    )


def get_generation_candidates(
        *,
        db: Session,
        page: int = 1,
        page_size: int = 10,
        max_questions_per_candidate: int = 5,
        technology_id: int | None = None,
        technology_domain_id: int | None = None,
        technology_module_id: int | None = None,
        technology_topic_id: int | None = None,
        technology_subtopic_id: int | None = None,
        concept_id: int | None = None,
        question_type_id: int | None = None,
        difficulty: schemas.BlueprintRuleDifficulty | None = None,
        search: str | None = None,
        suitability_tier: schemas.BlueprintSuitabilityTierFilter = "recommended",
) -> schemas.BlueprintGenerationCandidatesRead:
    """Return ranked, planner-ready Blueprint generation candidates.

    This is intentionally a read-only bridge between Blueprint coverage and AI
    generation planning. It does not create a generation batch. It only converts
    actionable recommended Blueprint gaps into the same plan-item shape that the
    AI generation planner already accepts.
    """

    safe_page = max(page, 1)
    safe_page_size = max(min(page_size, 100), 1)
    safe_max_questions = max(min(max_questions_per_candidate, 20), 1)

    # Generation candidates are a paged, read-only view over the ranked
    # recommended Blueprint coverage gaps. Keep pagination aligned with the
    # coverage service so admins can browse beyond the initial dashboard-sized
    # candidate preview without loading the whole candidate universe.
    coverage = coverage_service.get_blueprint_coverage(
        db=db,
        include_inactive=False,
        only_gaps=True,
        technology_id=technology_id,
        technology_domain_id=technology_domain_id,
        technology_module_id=technology_module_id,
        technology_topic_id=technology_topic_id,
        technology_subtopic_id=technology_subtopic_id,
        concept_id=concept_id,
        question_type_id=question_type_id,
        difficulty=difficulty,
        search=search,
        coverage_status="all",
        suitability_tier=suitability_tier,
        sort_by="generation_priority",
        sort_dir="desc",
        page=safe_page,
        page_size=safe_page_size,
    )

    candidates: list[schemas.BlueprintGenerationCandidateRead] = []
    for row in coverage.rows:
        candidate = _candidate_from_row(
            rank=((safe_page - 1) * safe_page_size) + len(candidates) + 1,
            row=row,
            max_questions_per_candidate=safe_max_questions,
        )
        if candidate is None:
            continue
        candidates.append(candidate)
        if len(candidates) >= safe_page_size:
            break

    plan_items = [candidate.plan_item for candidate in candidates]
    requested_count = sum(item.requested_count for item in plan_items)

    return schemas.BlueprintGenerationCandidatesRead(
        total_candidate_count=coverage.page.total_count,
        page=schemas.BlueprintGenerationCandidatesPageRead(
            page=safe_page,
            page_size=safe_page_size,
            total_count=coverage.page.total_count,
        ),
        returned_candidate_count=len(candidates),
        requested_count=requested_count,
        generation_mode=DEFAULT_GENERATION_MODE,
