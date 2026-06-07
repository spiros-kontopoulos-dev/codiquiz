# Compact avoid-list generation
# Source: quiz-api/app/question_similarity/avoid_list_service.py (excerpt lines 1-163)
# Public portfolio excerpt; not standalone application code.

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

MAX_COMPACT_AVOID_LIST_ENTRIES = 15
COMPACT_AVOID_LIST_ENTRY_MAX_LENGTH = 180
_AVOID_LIST_SOURCE_ROW_LIMIT = 50


@dataclass(frozen=True)
class CompactAvoidListEntry:
    """One short negative-pattern hint for a future provider call.

    The entry intentionally carries only compact pattern/signature metadata. It
    must not include full question prompts, full code snippets, answer options,
    or explanations from previous generated drafts.
    """

    source_generated_question_id: int | None
    text: str
    pattern_key: str | None = None
    prompt_signature: str | None = None
    code_signature: str | None = None


def build_compact_avoid_list(
    generated_questions: Iterable[Any],
    *,
    max_entries: int = MAX_COMPACT_AVOID_LIST_ENTRIES,
) -> list[str]:
    """Return capped avoid-list text lines for prompt/provider context."""

    return [
        entry.text
        for entry in build_compact_avoid_list_entries(
            generated_questions,
            max_entries=max_entries,
        )
    ]


def build_compact_avoid_list_entries(
    generated_questions: Iterable[Any],
    *,
    max_entries: int = MAX_COMPACT_AVOID_LIST_ENTRIES,
) -> list[CompactAvoidListEntry]:
    """Build compact, deduplicated avoid-list entries from prior drafts.

    BQE 1.48 deliberately avoids sending full prior questions back to the model.
    The provider receives only bounded pattern summaries and short signature
    families from earlier generated drafts, usually previous normal-API chunks
    for the same plan item.
    """

    safe_limit = max(0, min(max_entries, MAX_COMPACT_AVOID_LIST_ENTRIES))
    if safe_limit <= 0:
        return []

    entries: list[CompactAvoidListEntry] = []
    seen_identity_keys: set[tuple[str, str]] = set()

    for draft in list(generated_questions)[:_AVOID_LIST_SOURCE_ROW_LIMIT]:
        identity_key = _avoid_identity_key(draft)
        if identity_key is None or identity_key in seen_identity_keys:
            continue

        entry_text = _build_entry_text(draft)
        if not entry_text:
            continue

        seen_identity_keys.add(identity_key)
        entries.append(
            CompactAvoidListEntry(
                source_generated_question_id=getattr(draft, "id", None),
                text=entry_text,
                pattern_key=getattr(draft, "pattern_key", None),
                prompt_signature=getattr(draft, "prompt_signature", None),
                code_signature=getattr(draft, "code_signature", None),
            )
        )

        if len(entries) >= safe_limit:
            break

    return entries


def _avoid_identity_key(draft: Any) -> tuple[str, str] | None:
    pattern_key = _clean_text(getattr(draft, "pattern_key", None))
    if pattern_key:
        return ("pattern", pattern_key)

    prompt_signature = _clean_text(getattr(draft, "prompt_signature", None))
    code_signature = _clean_text(getattr(draft, "code_signature", None))
    if prompt_signature and code_signature:
        return ("prompt_code", f"{prompt_signature}:{code_signature}")

    concept_target_key = _clean_text(getattr(draft, "concept_question_type_difficulty_key", None))
    if concept_target_key and code_signature:
        return ("target_code", f"{concept_target_key}:{code_signature}")

    full_signature = _clean_text(getattr(draft, "full_question_signature", None))
    if full_signature:
        return ("full", full_signature)

    if prompt_signature:
        return ("prompt", prompt_signature)

    return None


def _build_entry_text(draft: Any) -> str | None:
    summary = _clean_text(getattr(draft, "pattern_summary", None))
    signature_hint = _signature_hint(draft)

    if summary:
        if signature_hint:
            return _clip_entry(f"Avoid prior pattern: {summary}. {signature_hint}")
        return _clip_entry(f"Avoid prior pattern: {summary}.")

    if signature_hint:
        return _clip_entry(f"Avoid prior signature family: {signature_hint}")

    return None


def _signature_hint(draft: Any) -> str | None:
    prompt_signature = _short_signature(getattr(draft, "prompt_signature", None))
    code_signature = _short_signature(getattr(draft, "code_signature", None))
    pattern_key = _short_signature(getattr(draft, "pattern_key", None))

    if prompt_signature and code_signature:
        return f"Signature family prompt+code {prompt_signature}/{code_signature}."
    if pattern_key:
        return f"Pattern key {pattern_key}."
    if prompt_signature:
        return f"Prompt signature {prompt_signature}."
    if code_signature:
        return f"Code signature {code_signature}."

    return None


def _short_signature(value: Any) -> str | None:
    cleaned = _clean_text(value)
    if not cleaned:
        return None
    return cleaned[:12]


def _clean_text(value: Any) -> str | None:
    if value is None:
        return None

    cleaned = " ".join(str(value).split())
    return cleaned or None


def _clip_entry(value: str) -> str:
    cleaned = " ".join(value.split())
    if len(cleaned) <= COMPACT_AVOID_LIST_ENTRY_MAX_LENGTH:
        return cleaned
    return f"{cleaned[: COMPACT_AVOID_LIST_ENTRY_MAX_LENGTH - 1].rstrip()}…"
