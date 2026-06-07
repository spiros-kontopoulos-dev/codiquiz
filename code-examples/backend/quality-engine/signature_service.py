# Backend Quality Engine deterministic signatures
# Source: quiz-api/app/question_similarity/signature_service.py (excerpt lines 1-133)
# Public portfolio excerpt; not standalone application code.

from collections.abc import Iterable
from dataclasses import dataclass
from hashlib import sha256
from typing import Any

from app.question_similarity.normalization_service import (
    normalize_answer_options_for_signature,
    normalize_code_for_signature,
    normalize_text_for_signature,
)

QUESTION_SIGNATURE_VERSION = "question_similarity.v1.1"


@dataclass(frozen=True)
class QuestionSignatureSet:
    fingerprint_version: str
    normalized_prompt: str
    normalized_code: str
    normalized_answer: str
    normalized_full_question: str
    prompt_signature: str | None
    code_signature: str | None
    answer_signature: str | None
    full_question_signature: str | None


def build_question_signatures(
    *,
    prompt: str | None,
    code_snippet: str | None,
    answer_options: Iterable[Any] | None = None,
) -> QuestionSignatureSet:
    """Build deterministic signatures for a question-like object.

    BQE 1.46 policy: answer-option order is not part of question
    identity. Public serving can shuffle options, so two questions whose only
    difference is answer option order must produce the same answer/full
    signatures and be treated as duplicate variants.
    """
    normalized_prompt = normalize_text_for_signature(prompt)
    normalized_code = normalize_code_for_signature(code_snippet)
    normalized_answer = normalize_answer_options_for_signature(answer_options)
    normalized_full_question = _join_signature_parts(
        (
            ("prompt", normalized_prompt),
            ("code", normalized_code),
            ("answers", normalized_answer),
        )
    )

    return QuestionSignatureSet(
        fingerprint_version=QUESTION_SIGNATURE_VERSION,
        normalized_prompt=normalized_prompt,
        normalized_code=normalized_code,
        normalized_answer=normalized_answer,
        normalized_full_question=normalized_full_question,
        prompt_signature=_hash_or_none(normalized_prompt),
        code_signature=_hash_or_none(normalized_code),
        answer_signature=_hash_or_none(normalized_answer),
        full_question_signature=_hash_or_none(normalized_full_question),
    )


def apply_question_signatures(question: Any) -> QuestionSignatureSet:
    """Apply deterministic signatures to a Question or AIGeneratedQuestion model."""
    signatures = build_question_signatures(
        prompt=getattr(question, "prompt", None),
        code_snippet=getattr(question, "code_snippet", None),
        answer_options=getattr(question, "answer_options", None),
    )

    question.fingerprint_version = signatures.fingerprint_version
    question.prompt_signature = signatures.prompt_signature
    question.code_signature = signatures.code_signature
    question.answer_signature = signatures.answer_signature
    question.full_question_signature = signatures.full_question_signature

    return signatures


def apply_question_signatures_from_parts(
    question: Any,
    *,
    prompt: str | None,
    code_snippet: str | None,
    answer_options: Iterable[Any] | None = None,
) -> QuestionSignatureSet:
    """Apply signatures from explicit parts before ORM relationships refresh."""
    signatures = build_question_signatures(
        prompt=prompt,
        code_snippet=code_snippet,
        answer_options=answer_options,
    )

    question.fingerprint_version = signatures.fingerprint_version
    question.prompt_signature = signatures.prompt_signature
    question.code_signature = signatures.code_signature
    question.answer_signature = signatures.answer_signature
    question.full_question_signature = signatures.full_question_signature

    return signatures


def copy_question_signatures(source: Any, target: Any) -> None:
    """Copy persisted signatures between question-like models when content matches."""
    target.fingerprint_version = getattr(source, "fingerprint_version", None)
    target.prompt_signature = getattr(source, "prompt_signature", None)
    target.code_signature = getattr(source, "code_signature", None)
    target.answer_signature = getattr(source, "answer_signature", None)
    target.full_question_signature = getattr(source, "full_question_signature", None)


def duplicate_signature_text(prompt: str | None, code_snippet: str | None) -> str:
    """Compatibility helper for the existing prompt/code duplicate warnings."""
    normalized_prompt = normalize_text_for_signature(prompt)
    normalized_code = normalize_code_for_signature(code_snippet)

    if normalized_code:
        return f"{normalized_prompt} {normalized_code}".strip()

    return normalized_prompt


def _hash_or_none(value: str) -> str | None:
    if not value:
        return None

    return sha256(value.encode("utf-8")).hexdigest()


def _join_signature_parts(parts: Iterable[tuple[str, str]]) -> str:
    return "\n".join(f"{label}:{value}" for label, value in parts if value)
