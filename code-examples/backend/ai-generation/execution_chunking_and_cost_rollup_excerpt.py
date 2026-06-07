# AI generation execution chunking and cost rollups
# Source: quiz-api/app/ai_generation/execution_service.py (excerpt lines 1-249)
# Public portfolio excerpt; not standalone application code.

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable


NORMAL_API_EXECUTION_MODE = "normal_api"
BATCH_API_EXECUTION_MODE = "batch_api"
LEGACY_NORMAL_EXECUTION_MODE = "normal"

NORMAL_API_MAX_QUESTIONS_PER_REQUEST = 10
BATCH_API_MAX_QUESTIONS_PER_REQUEST = 25

BATCH_API_PENDING_SUBMISSION_STATUS = "pending_batch_submission"
BATCH_API_SUBMITTED_STATUS = "submitted_to_batch"
BATCH_API_PROCESSING_STATUS = "batch_processing"
BATCH_API_COMPLETED_STATUS = "batch_completed"
BATCH_API_FAILED_STATUS = "batch_failed"
BATCH_API_EXPIRED_STATUS = "batch_expired"
BATCH_API_CANCELLED_STATUS = "batch_cancelled"
BATCH_API_BATCH_STATUS = "pending_batch_submission"
BATCH_API_RESULTS_COLLECTED_STATUS = "batch_results_collected"
BATCH_API_RESULT_COLLECTED_STATUS = "batch_result_collected"
BATCH_API_RESULT_FAILED_STATUS = "batch_result_failed"

OPENAI_BATCH_STATUS_TO_APP_STATUS = {
    "validating": BATCH_API_PROCESSING_STATUS,
    "in_progress": BATCH_API_PROCESSING_STATUS,
    "finalizing": BATCH_API_PROCESSING_STATUS,
    "completed": BATCH_API_COMPLETED_STATUS,
    "failed": BATCH_API_FAILED_STATUS,
    "expired": BATCH_API_EXPIRED_STATUS,
    "cancelled": BATCH_API_CANCELLED_STATUS,
    "cancelling": BATCH_API_PROCESSING_STATUS,
}
TERMINAL_BATCH_API_APP_STATUSES = {
    BATCH_API_COMPLETED_STATUS,
    BATCH_API_FAILED_STATUS,
    BATCH_API_EXPIRED_STATUS,
    BATCH_API_CANCELLED_STATUS,
    BATCH_API_RESULTS_COLLECTED_STATUS,
    BATCH_API_RESULT_COLLECTED_STATUS,
    BATCH_API_RESULT_FAILED_STATUS,
}

RETRYABLE_EXECUTION_JOB_STATUSES = {"failed"}
SUPPORTED_EXECUTION_MODES = {NORMAL_API_EXECUTION_MODE, BATCH_API_EXECUTION_MODE}


def normalize_execution_mode(value: str | None) -> str:
    """Normalize persisted/admin execution mode values.

    Earlier BQE milestones stored ``normal`` before the mode name was made
    explicit. Keep that value readable while new writes use ``normal_api`` so
    Batch API can be represented clearly next to it.
    """

    cleaned_value = (value or NORMAL_API_EXECUTION_MODE).strip().lower()
    if cleaned_value == LEGACY_NORMAL_EXECUTION_MODE:
        return NORMAL_API_EXECUTION_MODE
    if cleaned_value in SUPPORTED_EXECUTION_MODES:
        return cleaned_value
    raise ValueError("execution_mode must be either 'normal_api' or 'batch_api'")


def is_batch_api_execution_mode(value: str | None) -> bool:
    return normalize_execution_mode(value) == BATCH_API_EXECUTION_MODE


def app_status_for_openai_batch_status(value: str | None) -> str:
    """Map OpenAI Batch API lifecycle statuses to Codiquiz statuses."""

    cleaned_value = (value or "").strip().lower()
    return OPENAI_BATCH_STATUS_TO_APP_STATUS.get(cleaned_value, BATCH_API_PROCESSING_STATUS)


def pricing_mode_for_execution_mode(value: str | None) -> str:
    """Map app execution mode values to pricing snapshot keys."""

    return "batch" if is_batch_api_execution_mode(value) else "normal"


@dataclass(frozen=True)
class AIGenerationExecutionChunk:
    """One provider/API call needed to satisfy a plan item."""

    chunk_index: int
    chunk_count: int
    requested_count: int


@dataclass(frozen=True)
class AIGenerationExecutionUsageRollup:
    """Summed execution-job usage for one plan item or batch.

    Execution jobs are the billable provider attempts. The rollup intentionally
    includes retries and failed attempts that returned token/cost metadata,
    because those attempts can still spend credits even when they do not produce
    approved questions.
    """

    job_count: int
    retry_job_count: int
    completed_job_count: int
    failed_job_count: int
    running_job_count: int
    requested_count: int
    generated_count: int
    actual_input_tokens: int | None
    actual_output_tokens: int | None
    actual_total_tokens: int | None
    actual_cost_usd: Decimal | None
    model_used: str | None
    pricing_snapshot_json: str | None


def split_normal_api_chunks(
    requested_count: int,
    max_questions_per_request: int = NORMAL_API_MAX_QUESTIONS_PER_REQUEST,
) -> list[AIGenerationExecutionChunk]:
    """Split a plan-item request into safe normal-API chunks.

    Normal provider calls should stay small and predictable. The plan item keeps
    the admin's desired total count, while each returned chunk becomes one
    execution job/provider request. The hard cap stays at 10 for normal API;
    future Batch API/Celery execution can use a different splitter.
    """

    if requested_count < 1:
        raise ValueError("requested_count must be at least 1")

    safe_max = max(1, min(max_questions_per_request, NORMAL_API_MAX_QUESTIONS_PER_REQUEST))
    chunk_counts: list[int] = []
    remaining = requested_count

    while remaining > 0:
        current_count = min(safe_max, remaining)
        chunk_counts.append(current_count)
        remaining -= current_count

    chunk_total = len(chunk_counts)
    return [
        AIGenerationExecutionChunk(
            chunk_index=index,
            chunk_count=chunk_total,
            requested_count=count,
        )
        for index, count in enumerate(chunk_counts, start=1)
    ]


def split_batch_api_chunks(
    requested_count: int,
    max_questions_per_request: int = BATCH_API_MAX_QUESTIONS_PER_REQUEST,
) -> list[AIGenerationExecutionChunk]:
    """Split a plan item into Batch API request units.

    Batch API is asynchronous and can handle larger work queues than the
    interactive path, but each JSONL request should still stay reviewable and
    parseable. This foundation deliberately uses a conservative cap instead of
    asking for very large single responses.
    """

    if requested_count < 1:
        raise ValueError("requested_count must be at least 1")

    safe_max = max(1, min(max_questions_per_request, BATCH_API_MAX_QUESTIONS_PER_REQUEST))
    chunk_counts: list[int] = []
    remaining = requested_count

    while remaining > 0:
        current_count = min(safe_max, remaining)
        chunk_counts.append(current_count)
        remaining -= current_count

    chunk_total = len(chunk_counts)
    return [
        AIGenerationExecutionChunk(
            chunk_index=index,
            chunk_count=chunk_total,
            requested_count=count,
        )
        for index, count in enumerate(chunk_counts, start=1)
    ]


def split_execution_chunks(
    requested_count: int,
    execution_mode: str | None,
) -> list[AIGenerationExecutionChunk]:
    if is_batch_api_execution_mode(execution_mode):
        return split_batch_api_chunks(requested_count)
    return split_normal_api_chunks(requested_count)


def is_execution_job_retryable(status: str | None) -> bool:
    """Return whether a provider attempt can be retried by the admin UI."""

    return (status or "").strip().casefold() in RETRYABLE_EXECUTION_JOB_STATUSES


def roll_up_execution_jobs(jobs: Iterable[object]) -> AIGenerationExecutionUsageRollup:
    """Return source-of-truth execution totals from provider-attempt rows.

    The function accepts ORM rows or compatible objects with the same field
    names. It keeps retry attempts in the totals on purpose: retries and failed
    provider calls can consume tokens/cost, so cost reporting must remain an
    all-attempt accounting view rather than only a successful-output view.
    """

    job_list = list(jobs)
    return AIGenerationExecutionUsageRollup(
        job_count=len(job_list),
        retry_job_count=sum(1 for job in job_list if getattr(job, "retry_of_job_id", None) is not None),
        completed_job_count=sum(1 for job in job_list if getattr(job, "status", None) == "completed"),
        failed_job_count=sum(1 for job in job_list if getattr(job, "status", None) == "failed"),
        running_job_count=sum(1 for job in job_list if getattr(job, "status", None) == "running"),
        requested_count=sum(int(getattr(job, "requested_count", 0) or 0) for job in job_list),
        generated_count=sum(int(getattr(job, "generated_count", 0) or 0) for job in job_list),
        actual_input_tokens=_sum_optional_int(getattr(job, "actual_input_tokens", None) for job in job_list),
        actual_output_tokens=_sum_optional_int(getattr(job, "actual_output_tokens", None) for job in job_list),
        actual_total_tokens=_sum_optional_int(getattr(job, "actual_total_tokens", None) for job in job_list),
        actual_cost_usd=_sum_optional_decimal(getattr(job, "actual_cost_usd", None) for job in job_list),
        model_used=_first_non_empty(getattr(job, "model_used", None) for job in job_list),
        pricing_snapshot_json=_first_non_empty(getattr(job, "pricing_snapshot_json", None) for job in job_list),
    )


def _sum_optional_int(values) -> int | None:
    cleaned_values = [value for value in values if value is not None]
    if not cleaned_values:
        return None

    return int(sum(cleaned_values))


def _sum_optional_decimal(values) -> Decimal | None:
    cleaned_values = [Decimal(str(value)) for value in values if value is not None]
    if not cleaned_values:
        return None

    return sum(cleaned_values).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)


def _first_non_empty(values) -> str | None:
    for value in values:
        if value:
            return str(value)

    return None
