# Prompt rules for generation mode, profile, difficulty, type, taxonomy, and avoid-list
# Source: question-service/app/prompt_rules.py (excerpt lines 359-554)
# Public portfolio excerpt; not standalone application code.

def build_generation_system_prompt(payload: Any) -> str:
    profile_key = _normalize_key(getattr(payload, "model_profile", None) or "budget_draft")
    difficulty_key = _normalize_key(getattr(payload, "difficulty", None))
    question_type_code = resolve_question_type_code(
        getattr(payload, "question_type_code", None),
        getattr(payload, "question_type_name", None),
    )

    sections = [
        _format_section("Role", ["You generate original multiple-choice coding quiz questions for Codiquiz."]),
        _format_section("Base Codiquiz rules", BASE_GENERATION_RULES),
        _format_section(
            f"Model/profile rules: {profile_key}",
            MODEL_PROFILE_RULES.get(profile_key, MODEL_PROFILE_RULES["budget_draft"]),
        ),
    ]

    if difficulty_key and difficulty_key in DIFFICULTY_RULES:
        sections.append(_format_section(f"Difficulty rules: {difficulty_key}", DIFFICULTY_RULES[difficulty_key]))
    else:
        sections.append(_format_section("Difficulty rules", ["Use the requested difficulty label from the user message and keep the question fair for that level."]))

    if question_type_code and question_type_code in QUESTION_TYPE_RULES:
        sections.append(_format_section(f"Question-type rules: {question_type_code}", QUESTION_TYPE_RULES[question_type_code]))
    else:
        sections.append(_format_section("Question-type rules", ["Use the requested question type from the user message. If code is useful for that type, include a code_snippet; otherwise set code_snippet to null."]))

    generation_mode = getattr(payload, "generation_mode", "normal") or "normal"
    sections.append(_format_section(f"Generation mode: {generation_mode}", _classification_rules_for_mode(generation_mode)))

    sections.append(
        _format_section(
            "Future concept/category note",
            [
                "Use the supplied technology/domain/module/topic/subtopic/concept path as the content target.",
                "If a subtopic is supplied, keep questions focused on that subtopic instead of the whole topic.",
                "If no subtopic is supplied, treat the selected topic as a broad topic-level target.",
                "Legacy language/category/topic fields may appear only as compatibility context.",
                "Normal mode must not invent taxonomy labels. Reverse mode may suggest a new concept only inside classification.suggested_new_concept_name, never by changing the generated question target path.",
                "If prompt_context is provided, treat it as admin guidance while still respecting the requested target metadata.",
            ],
        )
    )

    if getattr(payload, "avoid_patterns", None):
        sections.append(
            _format_section(
                "Compact avoid-list rules",
                [
                    "avoid_patterns contains short summaries/signature families from earlier drafts for this same plan item.",
                    "Treat avoid_patterns as negative examples: do not repeat the same idea, code shape, edge case, prompt shape, or answer pattern.",
                    "Do not copy avoid_patterns into generated prompts, explanations, code, or answers.",
                    "Use the avoid-list only to create meaningfully different questions while still respecting the requested target metadata.",
                ],
            )
        )

    sections.append(f"Prompt ruleset version: {PROMPT_RULESET_VERSION}")
    return "\n\n".join(sections).strip()


def _jsonable(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    return value


def build_generation_user_prompt(payload: Any) -> str:
    target = {
        "language_id": getattr(payload, "language_id", None),
        "language_name": getattr(payload, "language_name", None),
        "category_id": getattr(payload, "category_id", None),
        "category_name": getattr(payload, "category_name", None),
        "topic_id": getattr(payload, "topic_id", None),
        "topic_name": getattr(payload, "topic_name", None),
        "technology_id": getattr(payload, "technology_id", None),
        "technology_name": getattr(payload, "technology_name", None),
        "technology_domain_id": getattr(payload, "technology_domain_id", None),
        "technology_domain_name": getattr(payload, "technology_domain_name", None),
        "technology_module_id": getattr(payload, "technology_module_id", None),
        "technology_module_name": getattr(payload, "technology_module_name", None),
        "technology_topic_id": getattr(payload, "technology_topic_id", None),
        "technology_topic_name": getattr(payload, "technology_topic_name", None),
        "technology_subtopic_id": getattr(payload, "technology_subtopic_id", None),
        "technology_subtopic_name": getattr(payload, "technology_subtopic_name", None),
        "primary_concept_id": getattr(payload, "primary_concept_id", None),
        "primary_concept_name": getattr(payload, "primary_concept_name", None),
        "question_type_id": getattr(payload, "question_type_id", None),
        "question_type_code": getattr(payload, "question_type_code", None),
        "question_type_name": getattr(payload, "question_type_name", None),
        "difficulty": getattr(payload, "difficulty", None),
        "count": getattr(payload, "count", None),
        "prompt_context": getattr(payload, "prompt_context", None),
        "model_profile": getattr(payload, "model_profile", None),
        "generation_mode": getattr(payload, "generation_mode", "normal"),
        "taxonomy_slice": _jsonable(getattr(payload, "taxonomy_slice", None)),
        "avoid_patterns": list(getattr(payload, "avoid_patterns", None) or [])[:15],
        "prompt_ruleset_version": PROMPT_RULESET_VERSION,
    }

    target_path = " → ".join(
        part
        for part in [
            target.get("technology_name") or target.get("language_name"),
            target.get("technology_domain_name") or target.get("category_name"),
            target.get("technology_module_name"),
            target.get("technology_topic_name") or target.get("topic_name"),
            target.get("technology_subtopic_name"),
            target.get("primary_concept_name"),
        ]
        if part
    )
    target_specificity = (
        "concept"
        if target.get("primary_concept_id") is not None
        else "subtopic"
        if target.get("technology_subtopic_id") is not None
        else "topic"
        if target.get("technology_topic_id") is not None
        else "module"
        if target.get("technology_module_id") is not None
        else "technology"
    )

    return (
        "Generate exactly {count} Codiquiz draft questions for this normalized plan item.\n"
        "The returned data will be staged for admin review, so be precise, internally consistent, and ready for a human editor.\n"
        "Generation mode: {generation_mode}\n"
        "For normal mode, do not create or rename taxonomy; use the supplied target metadata exactly and return classification as null.\n"
        "For reverse mode, generate inside the broad target and return classification metadata for each question.\n"
        "If taxonomy_slice is supplied, choose suggested subtopic, concept, and question type from that slice whenever possible.\n"
        "If avoid_patterns is non-empty, avoid those compact prior patterns without copying their wording.\n"
        "Resolved target path: {target_path}\n"
        "Target specificity: {target_specificity}\n"
        "If the target specificity is subtopic, generate questions specifically for that subtopic, not the broader topic.\n\n"
        "Plan item JSON:\n{target_json}"
    ).format(
        count=getattr(payload, "count", None),
        generation_mode=getattr(payload, "generation_mode", "normal"),
        target_path=target_path or "unspecified",
        target_specificity=target_specificity,
        target_json=json.dumps(target, ensure_ascii=False, indent=2),
    )


def _classification_rules_for_mode(generation_mode: str) -> list[str]:
    if generation_mode == "reverse":
        return CLASSIFICATION_CONTRACT_RULES + [
            "Generate inside the selected broad scope, then classify each question as narrowly as possible.",
            "Use the supplied taxonomy_slice as the authoritative local menu for existing subtopics, concepts, and question types.",
            "Only set matched IDs that appear in taxonomy_slice or in the plan-item target fields.",
            "If question type is not supplied, choose the most suitable task type and explain that choice in classification_reason.",
            "If difficulty is supplied, keep suggested_difficulty aligned with it unless the generated question clearly belongs elsewhere.",
            "For suggested_new_concept_name cases, include suitability suggestions with suitability_score from 0 to 100, difficulty weights near 1.0 for good matches, lower weights for weaker difficulty fit, and concise admin-facing notes.",
        ]

    return [
        "Return classification as null for every question.",
        "Do not suggest new subtopics, concepts, or question types in normal mode.",
    ]


def resolve_question_type_code(question_type_code: str | None, question_type_name: str | None) -> str | None:
    if question_type_code:
        return _normalize_key(question_type_code)

    if not question_type_name:
        return None

    normalized_name = question_type_name.strip().casefold()
    if normalized_name in NAME_TO_CODE_OVERRIDES:
        return NAME_TO_CODE_OVERRIDES[normalized_name]

    return _normalize_key(question_type_name)


def _normalize_key(value: str | None) -> str | None:
    if value is None:
        return None

    cleaned = value.strip().casefold()
    if not cleaned:
        return None

    return (
        cleaned.replace("/", "_")
        .replace("-", "_")
        .replace(" ", "_")
        .replace("__", "_")
    )


def _format_section(title: str, rules: list[str]) -> str:
    lines = [f"{title}:"]
    lines.extend(f"- {rule}" for rule in rules)
    return "\n".join(lines)
