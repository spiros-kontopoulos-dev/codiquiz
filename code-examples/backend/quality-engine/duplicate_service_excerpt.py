# Duplicate warning collection excerpt
# Source: quiz-api/app/question_similarity/duplicate_service.py (excerpt lines 38-180)
# Public portfolio excerpt; not standalone application code.

def is_live_draft_duplicate_source(generated_draft: Any) -> bool:
    """Return whether a draft is allowed to block future generation.

    Drafts are duplicate sources only while they are active review candidates.
    Once a draft is approved, the approved question-bank row becomes the source
    of truth. Once a batch is archived, its drafts are treated as retired test or
    historical data and should not poison future duplicate warnings.
    """
    if getattr(generated_draft, "status", None) != ACTIVE_DRAFT_DUPLICATE_SOURCE_STATUS:
        return False
    if getattr(generated_draft, "approved_question_id", None) is not None:
        return False

    batch = getattr(generated_draft, "batch", None)
    if batch is not None and bool(getattr(batch, "is_archived", False)):
        return False

    return True


def _active_draft_duplicate_source_query(db: Session) -> Any:
    # Centralized DB policy for draft duplicate sources. Keep this aligned with
    # is_live_draft_duplicate_source() so self-checks and queries describe the
    # same business rule.
    return (
        db.query(models.AIGeneratedQuestion)
        .join(
            models.AIGenerationBatch,
            models.AIGeneratedQuestion.batch_id == models.AIGenerationBatch.id,
        )
        .filter(
            models.AIGeneratedQuestion.status == ACTIVE_DRAFT_DUPLICATE_SOURCE_STATUS,
            models.AIGeneratedQuestion.approved_question_id.is_(None),
            models.AIGenerationBatch.is_archived.is_(False),
        )
    )


def collect_duplicate_quality_warnings(
    db: Session,
    batch_id: int,
    language_id: int | None,
    category_id: int | None,
    topic_id: int | None,
    technology_id: int | None,
    technology_domain_id: int | None,
    technology_module_id: int | None,
    technology_topic_id: int | None,
    technology_subtopic_id: int | None,
    primary_concept_id: int | None,
    question_type_id: int | None,
    prompt: str,
    code_snippet: str | None,
    answer_options: Iterable[Any] | None = None,
    difficulty: str | None = None,
    exclude_generated_question_id: int | None = None,
) -> list[str]:
    """Collect deterministic duplicate warnings for an AI draft.

    BQE 1.43 keeps the existing review behavior but upgrades the comparison
    source. In addition to the legacy prompt/code checks, new drafts are now
    compared against persisted prompt/code/answer/full signatures and compact
    pattern keys from approved questions and older AI drafts across batches.
    BQE 1.46 explicitly treats answer-order-only variants as duplicates because
    public serving shuffles answer options without changing question identity.

    The warnings stay review-time metadata. They are stored in the existing
    validation_errors field so the current duplicate warning queues continue to
    work without introducing a new UI or vector database layer.
    """
    candidate_signatures = build_question_signatures(
        prompt=prompt,
        code_snippet=code_snippet,
        answer_options=answer_options,
    )
    candidate_patterns = build_question_pattern_metadata(
        prompt=prompt,
        code_snippet=code_snippet,
        answer_options=answer_options,
        difficulty=difficulty,
        language_id=language_id,
        category_id=category_id,
        topic_id=topic_id,
        technology_id=technology_id,
        technology_domain_id=technology_domain_id,
        technology_module_id=technology_module_id,
        technology_topic_id=technology_topic_id,
        technology_subtopic_id=technology_subtopic_id,
        primary_concept_id=primary_concept_id,
        question_type_id=question_type_id,
    )
    candidate_signature_text = duplicate_signature_text(prompt, code_snippet)
    candidate_code = candidate_signatures.normalized_code or normalize_code_for_signature(code_snippet)

    if not any(
        (
            candidate_signatures.full_question_signature,
            candidate_signatures.prompt_signature,
            candidate_signatures.code_signature,
            candidate_patterns.pattern_key,
            candidate_signature_text,
        )
    ):
        return []

    grouped_warnings: dict[tuple[str, str], list[str]] = {}

    def add_grouped_warning(warning_type: str, scope: str, reference_label: str) -> None:
        key = (warning_type, scope)
        grouped_warnings.setdefault(key, [])
        if reference_label not in grouped_warnings[key]:
            grouped_warnings[key].append(reference_label)

    approved_questions = _unique_candidates(
        [
            *_duplicate_candidate_approved_questions(
                db=db,
                language_id=language_id,
                category_id=category_id,
                topic_id=topic_id,
                technology_id=technology_id,
                technology_domain_id=technology_domain_id,
                technology_module_id=technology_module_id,
                technology_topic_id=technology_topic_id,
                technology_subtopic_id=technology_subtopic_id,
                primary_concept_id=primary_concept_id,
                question_type_id=question_type_id,
            ),
            *_signature_candidate_approved_questions(
                db=db,
                candidate_signatures=candidate_signatures,
                candidate_pattern_key=candidate_patterns.pattern_key,
                candidate_target_key=candidate_patterns.concept_question_type_difficulty_key,
            ),
        ]
    )
    for approved_question in approved_questions:
        for warning_type in _duplicate_warning_types_for_existing(
            existing_question=approved_question,
            candidate_signatures=candidate_signatures,
            candidate_signature_text=candidate_signature_text,
            candidate_code=candidate_code,
            candidate_pattern_key=candidate_patterns.pattern_key,

# Duplicate warning type policy excerpt
# Source: quiz-api/app/question_similarity/duplicate_service.py (excerpt lines 561-633)
# Public portfolio excerpt; not standalone application code.

def _duplicate_warning_types_for_existing(
    *,
    existing_question: Any,
    candidate_signatures: Any,
    candidate_signature_text: str,
    candidate_code: str,
    candidate_pattern_key: str | None,
    candidate_target_key: str | None,
    candidate_primary_concept_id: int | None,
    candidate_question_type_id: int | None,
    candidate_difficulty: str | None,
) -> list[str]:
    warning_types: list[str] = []
    target_relation = _target_relation_for_existing(
        existing_question=existing_question,
        candidate_target_key=candidate_target_key,
        candidate_primary_concept_id=candidate_primary_concept_id,
        candidate_question_type_id=candidate_question_type_id,
        candidate_difficulty=candidate_difficulty,
    )

    if (
        candidate_signatures.full_question_signature
        and getattr(existing_question, "full_question_signature", None)
        == candidate_signatures.full_question_signature
    ):
        # The full signature is answer-order neutral. This is the strongest
        # duplicate signal and intentionally catches drafts whose only
        # difference is stored answer-option order. Exact content identity stays
        # a duplicate even if taxonomy metadata differs.
        return ["exact_full_signature"]

    if candidate_pattern_key and getattr(existing_question, "pattern_key", None) == candidate_pattern_key:
        # pattern_key is target-aware, so an exact pattern-key match means same
        # concept/type/difficulty as well as the same compact pattern identity.
        warning_types.append("same_pattern")

    if (
        candidate_signatures.code_signature
        and getattr(existing_question, "code_signature", None) == candidate_signatures.code_signature
    ):
        # Same normalized code remains a hard duplicate. The exact same snippet
        # under a different concept is usually taxonomy drift, not useful variety.
        warning_types.append("same_code")

    if (
        not candidate_signatures.code_signature
        and candidate_signatures.prompt_signature
        and getattr(existing_question, "prompt_signature", None) == candidate_signatures.prompt_signature
    ):
        warning_types.append("exact_signature")

    for warning_type in _duplicate_warning_types_for_candidate(
        candidate_prompt=getattr(existing_question, "prompt", ""),
        candidate_code_snippet=getattr(existing_question, "code_snippet", None),
        candidate_signature=candidate_signature_text,
        candidate_code=candidate_code,
    ):
        if warning_type == "similar_signature" and target_relation == "different_concept":
            # Cross-concept questions can legitimately share a broad teaching
            # pattern, such as append()/reverse()/sort() returning None. Keep a
            # light informational note, but do not block approval as a duplicate.
            # Same-concept matches stay blocking even if the question type or
            # difficulty differs, because the approved question-bank row should
            # remain the canonical source after a canonical AI draft is approved.
            warning_type = RELATED_PATTERN_NOTE_WARNING_TYPE
        if warning_type not in warning_types:
            warning_types.append(warning_type)

    return warning_types


def _target_relation_for_existing(

# Duplicate warning formatting and similarity helpers
# Source: quiz-api/app/question_similarity/duplicate_service.py (excerpt lines 744-858)
# Public portfolio excerpt; not standalone application code.

def _format_duplicate_warning_groups(grouped_warnings: dict[tuple[str, str], list[str]]) -> list[str]:
    messages: list[str] = []
    ordered_warning_types = [
        "exact_full_signature",
        "exact_signature",
        "same_pattern",
        "same_code",
        "similar_signature",
        RELATED_PATTERN_NOTE_WARNING_TYPE,
    ]
    ordered_scopes = ["approved_question", "historical_draft", "batch_draft"]

    for warning_type in ordered_warning_types:
        for scope in ordered_scopes:
            reference_ids = grouped_warnings.get((warning_type, scope), [])
            if not reference_ids:
                continue

            messages.append(
                _format_duplicate_warning_message(
                    warning_type=warning_type,
                    scope=scope,
                    reference_ids=reference_ids,
                )
            )

            if len(messages) >= MAX_DUPLICATE_WARNINGS_PER_DRAFT:
                return messages

    return messages


def _format_duplicate_warning_message(
    warning_type: str,
    scope: str,
    reference_ids: list[str],
) -> str:
    visible_reference_ids = reference_ids[:12]
    reference_list = ", ".join(visible_reference_ids)
    remaining_count = len(reference_ids) - len(visible_reference_ids)
    if remaining_count > 0:
        reference_list = f"{reference_list}, and {remaining_count} more"

    reference_label = _duplicate_reference_label(scope, len(reference_ids))

    if warning_type == "exact_full_signature":
        return f"Duplicate warning: exact normalized full-question match with {reference_label} {reference_list}."

    if warning_type == "exact_signature":
        return f"Duplicate warning: exact normalized prompt/code match with {reference_label} {reference_list}."

    if warning_type == "same_pattern":
        return f"Duplicate warning: same stored question pattern as {reference_label} {reference_list}."

    if warning_type == "same_code":
        return f"Duplicate warning: same normalized code snippet as {reference_label} {reference_list}."

    if warning_type == RELATED_PATTERN_NOTE_WARNING_TYPE:
        return (
            f"Related pattern note: similar prompt/code pattern as {reference_label} {reference_list}. "
            "Informational only; different concept targets are not treated as blocking duplicates."
        )

    return f"Duplicate warning: prompt/code signature is highly similar to {reference_label} {reference_list}."


def _question_reference_label(question: Any) -> str:
    return f"#{question.id}"


def _draft_reference_label(draft: Any, *, include_batch: bool) -> str:
    if include_batch and getattr(draft, "batch_id", None) is not None:
        return f"#{draft.id} (batch #{draft.batch_id})"
    return f"#{draft.id}"


def _duplicate_reference_label(scope: str, count: int) -> str:
    plural = count != 1
    if scope == "approved_question":
        return "approved questions" if plural else "approved question"
    if scope == "historical_draft":
        return "older AI drafts" if plural else "older AI draft"

    return "drafts in this batch" if plural else "draft in this batch"


def _duplicate_text_similarity(left: str, right: str) -> float:
    if not left or not right:
        return 0.0

    sequence_similarity = SequenceMatcher(None, left, right).ratio()
    token_similarity = _duplicate_token_overlap(left, right)
    return max(sequence_similarity, token_similarity)


def _duplicate_token_overlap(left: str, right: str) -> float:
    left_tokens = set(left.split())
    right_tokens = set(right.split())

    if len(left_tokens) < 6 or len(right_tokens) < 6:
        return 0.0

    return len(left_tokens & right_tokens) / max(len(left_tokens), len(right_tokens))


def _unique_candidates(candidates: list[Any]) -> list[Any]:
    unique: list[Any] = []
    seen_ids: set[int] = set()
    for candidate in candidates:
        candidate_id = getattr(candidate, "id", None)
        if candidate_id is None or candidate_id in seen_ids:
            continue
        seen_ids.add(candidate_id)
        unique.append(candidate)
    return unique
