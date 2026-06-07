"""Selected sanitized excerpt from Codiquiz Blueprint coverage router.

The router exposes coverage rows, default target preview, and top generation candidates
that power the admin Blueprint and AI Generation Create pages.
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app import schemas
from app.blueprint import coverage_service, generation_candidate_service
from app.database import get_db

router = APIRouter(prefix="/admin/blueprint", tags=["admin-blueprint"])


@router.get("/coverage", response_model=schemas.BlueprintCoverageRead)
def get_blueprint_coverage(
        include_inactive: bool = Query(default=False),
        only_gaps: bool = Query(default=True),
        technology_id: int | None = Query(default=None),
        technology_domain_id: int | None = Query(default=None),
        technology_module_id: int | None = Query(default=None),
        technology_topic_id: int | None = Query(default=None),
        technology_subtopic_id: int | None = Query(default=None),
        concept_id: int | None = Query(default=None),
        question_type_id: int | None = Query(default=None),
        difficulty: schemas.BlueprintRuleDifficulty | None = Query(default=None),
        search: str | None = Query(default=None, max_length=160),
        coverage_status: schemas.BlueprintCoverageStatusFilter = Query(default="all"),
        suitability_tier: schemas.BlueprintSuitabilityTierFilter = Query(default="recommended"),
        sort_by: schemas.BlueprintCoverageSortBy = Query(default="generation_priority"),
        sort_dir: schemas.BlueprintCoverageSortDirection = Query(default="desc"),
        page: int = Query(default=1, ge=1),
        page_size: int = Query(default=25, ge=1, le=100),
        db: Session = Depends(get_db),
):
    return coverage_service.get_blueprint_coverage(
        db=db,
        include_inactive=include_inactive,
        only_gaps=only_gaps,
        technology_id=technology_id,
        technology_domain_id=technology_domain_id,
        technology_module_id=technology_module_id,
        technology_topic_id=technology_topic_id,
        technology_subtopic_id=technology_subtopic_id,
        concept_id=concept_id,
        question_type_id=question_type_id,
        difficulty=difficulty,
        search=search,
        coverage_status=coverage_status,
        suitability_tier=suitability_tier,
        sort_by=sort_by,
        sort_dir=sort_dir,
        page=page,
        page_size=page_size,
    )


@router.get("/default-targets", response_model=schemas.BlueprintDefaultTargetsRead)
def get_blueprint_default_targets(
        include_inactive: bool = Query(default=False),
        only_gaps: bool = Query(default=True),
        technology_id: int | None = Query(default=None),
        technology_domain_id: int | None = Query(default=None),
        technology_module_id: int | None = Query(default=None),
        technology_topic_id: int | None = Query(default=None),
        technology_subtopic_id: int | None = Query(default=None),
        concept_id: int | None = Query(default=None),
        question_type_id: int | None = Query(default=None),
        difficulty: schemas.BlueprintRuleDifficulty | None = Query(default=None),
        search: str | None = Query(default=None, max_length=160),
        suitability_tier: schemas.BlueprintSuitabilityTierFilter = Query(default="recommended"),
        min_importance_score: int | None = Query(default=None, ge=0, le=100),
        sort_by: schemas.BlueprintDefaultTargetSortBy = Query(default="generation_priority"),
        sort_dir: schemas.BlueprintCoverageSortDirection = Query(default="desc"),
        page: int = Query(default=1, ge=1),
        page_size: int = Query(default=25, ge=1, le=100),
        db: Session = Depends(get_db),
):
    return coverage_service.get_blueprint_default_targets(
        db=db,
        include_inactive=include_inactive,
        only_gaps=only_gaps,
        technology_id=technology_id,
        technology_domain_id=technology_domain_id,
        technology_module_id=technology_module_id,
        technology_topic_id=technology_topic_id,
        technology_subtopic_id=technology_subtopic_id,
        concept_id=concept_id,
        question_type_id=question_type_id,
        difficulty=difficulty,
        search=search,
        suitability_tier=suitability_tier,
        min_importance_score=min_importance_score,
        sort_by=sort_by,
        sort_dir=sort_dir,
        page=page,
        page_size=page_size,
    )


@router.get("/generation-candidates", response_model=schemas.BlueprintGenerationCandidatesRead)
def get_blueprint_generation_candidates(
        page: int = Query(default=1, ge=1),
        page_size: int = Query(default=10, ge=1, le=100),
        max_questions_per_candidate: int = Query(default=5, ge=1, le=20),
        technology_id: int | None = Query(default=None),
        technology_domain_id: int | None = Query(default=None),
        technology_module_id: int | None = Query(default=None),
        technology_topic_id: int | None = Query(default=None),
        technology_subtopic_id: int | None = Query(default=None),
        concept_id: int | None = Query(default=None),
        question_type_id: int | None = Query(default=None),
        difficulty: schemas.BlueprintRuleDifficulty | None = Query(default=None),
        search: str | None = Query(default=None, max_length=160),
        suitability_tier: schemas.BlueprintSuitabilityTierFilter = Query(default="recommended"),
        db: Session = Depends(get_db),
):
    return generation_candidate_service.get_generation_candidates(
        db=db,
        page=page,
        page_size=page_size,
        max_questions_per_candidate=max_questions_per_candidate,
        technology_id=technology_id,
        technology_domain_id=technology_domain_id,
        technology_module_id=technology_module_id,
        technology_topic_id=technology_topic_id,
        technology_subtopic_id=technology_subtopic_id,
        concept_id=concept_id,
        question_type_id=question_type_id,
        difficulty=difficulty,
        search=search,
        suitability_tier=suitability_tier,
    )
