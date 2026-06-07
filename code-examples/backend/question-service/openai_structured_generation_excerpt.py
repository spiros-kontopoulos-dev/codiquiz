# Question-service structured OpenAI and Batch API boundary
# Source: question-service/app/main.py (excerpt lines 795-1077)
# Public portfolio excerpt; not standalone application code.

def generate_questions_openai(payload: GenerationRequest):
    # Normal OpenAI mode is intentionally synchronous for small admin test runs.
    # Large offline generation will use a separate Batch API path later.
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not configured for question-service.",
        )

    try:
        response = _call_openai_structured_generation(payload)
    except OpenAIError as exc:
        raise HTTPException(status_code=502, detail=f"OpenAI request failed: {exc}") from exc
    except (json.JSONDecodeError, ValidationError, ValueError) as exc:
        raise HTTPException(status_code=502, detail=f"OpenAI response validation failed: {exc}") from exc

    if len(response.questions) != payload.count:
        raise HTTPException(
            status_code=502,
            detail=(
                "OpenAI returned an unexpected question count: "
                f"expected {payload.count}, got {len(response.questions)}."
            ),
        )

    return response



def _build_openai_batch_jsonl_lines(
    request_items: list[BatchGenerationRequestItem],
) -> tuple[list[str], str, str]:
    seen_custom_ids: set[str] = set()
    jsonl_lines: list[str] = []
    resolved_model_profile: str | None = None
    resolved_model: str | None = None

    for item in request_items:
        if item.custom_id in seen_custom_ids:
            raise ValueError(f"Duplicate Batch API custom_id: {item.custom_id}")
        seen_custom_ids.add(item.custom_id)

        model_profile, model = _resolve_openai_model(item.request)
        if resolved_model is None:
            resolved_model_profile = model_profile
            resolved_model = model
        elif model != resolved_model:
            raise ValueError(
                "OpenAI Batch API input files can only target one model. "
                f"Found both '{resolved_model}' and '{model}'."
            )

        jsonl_lines.append(
            json.dumps(
                {
                    "custom_id": item.custom_id,
                    "method": "POST",
                    "url": "/v1/responses",
                    "body": _build_openai_responses_body(item.request, model),
                },
                ensure_ascii=False,
            )
        )

    if resolved_model is None or resolved_model_profile is None:
        raise ValueError("At least one batch request is required.")

    return jsonl_lines, resolved_model_profile, resolved_model


def _build_openai_responses_body(
    payload: GenerationRequest,
    model: str,
    validation_retry_note: str | None = None,
) -> dict[str, object]:
    user_prompt = build_generation_user_prompt(payload)
    if validation_retry_note:
        # Keep retries explicit but still schema-compatible. The first response
        # may have been valid JSON but failed Codiquiz quality validation, such
        # as duplicate answer option text values. A single focused retry usually
        # fixes provider-output mistakes without hiding persistent prompt issues.
        user_prompt = f"{user_prompt}\n\nVALIDATION RETRY NOTE:\n{validation_retry_note}"

    return {
        "model": model,
        "input": [
            {"role": "system", "content": build_generation_system_prompt(payload)},
            {"role": "user", "content": user_prompt},
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "codiquiz_question_generation_response",
                "schema": OPENAI_GENERATION_RESPONSE_SCHEMA,
                "strict": True,
            }
        },
    }


def _download_openai_jsonl_file(client: OpenAI, file_id: str) -> list[dict[str, Any]]:
    content_response = client.files.content(file_id)
    if hasattr(content_response, "text"):
        raw_content = content_response.text
    elif hasattr(content_response, "read"):
        raw_bytes = content_response.read()
        raw_content = raw_bytes.decode("utf-8") if isinstance(raw_bytes, bytes) else str(raw_bytes)
    elif isinstance(content_response, bytes):
        raw_content = content_response.decode("utf-8")
    elif hasattr(content_response, "content"):
        raw_bytes = content_response.content
        raw_content = raw_bytes.decode("utf-8") if isinstance(raw_bytes, bytes) else str(raw_bytes)
    else:
        raw_content = str(content_response)

    parsed_lines: list[dict[str, Any]] = []
    for line_number, raw_line in enumerate(raw_content.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            parsed_line = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Could not parse OpenAI Batch API JSONL line {line_number} from file {file_id}: {exc}") from exc
        if not isinstance(parsed_line, dict):
            raise ValueError(f"OpenAI Batch API JSONL line {line_number} from file {file_id} is not an object.")
        parsed_lines.append(parsed_line)

    return parsed_lines


def _serialize_openai_batch(batch: Any) -> dict[str, Any]:
    if hasattr(batch, "model_dump"):
        data = batch.model_dump(mode="json")
    elif isinstance(batch, dict):
        data = dict(batch)
    else:
        data = {
            "id": getattr(batch, "id", None),
            "endpoint": getattr(batch, "endpoint", None),
            "input_file_id": getattr(batch, "input_file_id", None),
            "output_file_id": getattr(batch, "output_file_id", None),
            "error_file_id": getattr(batch, "error_file_id", None),
            "completion_window": getattr(batch, "completion_window", None),
            "status": getattr(batch, "status", None),
            "request_counts": getattr(batch, "request_counts", None),
            "errors": getattr(batch, "errors", None),
        }

    request_counts = data.get("request_counts")
    if hasattr(request_counts, "model_dump"):
        request_counts = request_counts.model_dump(mode="json")
    elif request_counts is not None and not isinstance(request_counts, dict):
        request_counts = {
            "total": getattr(request_counts, "total", None),
            "completed": getattr(request_counts, "completed", None),
            "failed": getattr(request_counts, "failed", None),
        }
    data["request_counts"] = request_counts

    if not data.get("id"):
        raise ValueError("OpenAI Batch API response did not include a batch id.")

    return data


def _call_openai_structured_generation(payload: GenerationRequest) -> GenerationResponse:
    model_profile, model = _resolve_openai_model(payload)
    timeout_seconds = float(os.getenv("OPENAI_GENERATION_TIMEOUT_SECONDS", "60"))

    client = OpenAI(timeout=timeout_seconds)
    validation_retry_note: str | None = None
    last_validation_error: ValidationError | None = None

    for attempt_number in range(2):
        openai_response = client.responses.create(
            **_build_openai_responses_body(
                payload,
                model,
                validation_retry_note=validation_retry_note,
            )
        )

        raw_output = openai_response.output_text
        if not raw_output:
            raise ValueError("OpenAI returned no output_text.")

        try:
            response = GenerationResponse.model_validate_json(raw_output)
        except ValidationError as exc:
            last_validation_error = exc
            if attempt_number == 0:
                validation_retry_note = _build_openai_validation_retry_note(exc)
                continue
            raise

        input_tokens, output_tokens, total_tokens = _extract_openai_usage(openai_response)

        response.provider = "openai"
        response.model_profile = model_profile
        response.model_used = model
        response.input_tokens = input_tokens
        response.output_tokens = output_tokens
        response.total_tokens = total_tokens
        response.prompt_version = PROMPT_RULESET_VERSION

        return response

    # The loop either returns or raises on the second failed validation attempt.
    # This fallback keeps type-checkers honest and preserves the original error.
    if last_validation_error is not None:
        raise last_validation_error
    raise ValueError("OpenAI generation failed before returning a valid response.")


def _build_openai_validation_retry_note(exc: ValidationError) -> str:
    # Convert verbose Pydantic errors into a focused provider-facing retry note.
    # The most common failure is duplicate multiple-choice option text, but the
    # note also covers the other Codiquiz service-side gates.
    messages: list[str] = []
    for error in exc.errors():
        message = str(error.get("msg") or "").strip()
        if message and message not in messages:
            messages.append(message)

    short_messages = "; ".join(messages[:4])
    if short_messages:
        short_messages = f" Previous validation errors: {short_messages}."

    return (
        "Regenerate the entire JSON response. Do not repeat the invalid output."
        " For every question, return exactly four answer options, exactly one correct answer,"
        " positions 1, 2, 3, and 4, and four unique answer option text values after"
        " trimming whitespace and ignoring case. If two distractors would have the same"
        " text, rewrite one of them to a different plausible wrong answer."
        f"{short_messages}"
    )


def _resolve_openai_model(payload: GenerationRequest) -> tuple[str, str]:
    # Admins choose stable Codiquiz model profiles. Environment variables map
    # those profiles to provider-specific model names so the UI does not depend
    # on raw OpenAI model identifiers.
    model_profile = (
        payload.model_profile
        or os.getenv("OPENAI_GENERATION_MODEL_PROFILE")
        or "budget_draft"
    )

    profile_to_env_name = {
        "budget_draft": "OPENAI_BUDGET_DRAFT_MODEL",
        "balanced_draft": "OPENAI_BALANCED_DRAFT_MODEL",
        "premium_advanced": "OPENAI_PREMIUM_ADVANCED_MODEL",
        "validation_only": "OPENAI_VALIDATION_MODEL",
    }

    model_env_name = profile_to_env_name.get(model_profile, "OPENAI_GENERATION_MODEL")
    model = (
        os.getenv(model_env_name)
        or os.getenv("OPENAI_GENERATION_MODEL")
        or "gpt-4.1-mini"
    )

    return model_profile, model


def _extract_openai_usage(openai_response) -> tuple[int | None, int | None, int | None]:
    usage = getattr(openai_response, "usage", None)
    if usage is None:
        return None, None, None

    input_tokens = _read_usage_int(usage, "input_tokens")
    output_tokens = _read_usage_int(usage, "output_tokens")
    total_tokens = _read_usage_int(usage, "total_tokens")

    if total_tokens is None and input_tokens is not None and output_tokens is not None:
        total_tokens = input_tokens + output_tokens

    return input_tokens, output_tokens, total_tokens


def _read_usage_int(usage, field_name: str) -> int | None:
    if isinstance(usage, dict):
