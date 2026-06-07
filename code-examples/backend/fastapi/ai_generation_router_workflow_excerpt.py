"""Selected sanitized excerpt from Codiquiz AI generation FastAPI router.

Shows the backend workflow around plan preview, batch creation, immediate normal execution,
and Batch API preparation. This is partial and is not intended to run standalone.
"""

@router.post("/preview-plan", response_model=AIGenerationPlanPreview)
@router.post("/plan-preview", response_model=AIGenerationPlanPreview)
def preview_ai_generation_plan(
    payload: AIGenerationPlanCreate,
    db: Session = Depends(get_db),
):
    # The preview endpoint lets the admin UI build/adjust the allocation plan
    # before any batch is saved or any future OpenAI call is made.
    try:
        plan = build_ai_generation_plan(db, payload)
        _ensure_normal_plan_preview_has_strict_taxonomy_identity(
            db,
            plan,
            _payload_generation_mode(payload),
        )
        return plan
    except PlanValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("", response_model=AIGenerationBatchDetail, status_code=201)
def create_ai_generation_batch(
    payload: AIGenerationPlanCreate,
    db: Session = Depends(get_db),
):
    # This creates only the planned batch and plan items. Actual AI generation
    # will be added later, so we can test allocation, validation, and review
    # foundations without mixing in OpenAI/network behavior yet.
    try:
        plan = build_ai_generation_plan(db, payload)
        _ensure_normal_plan_preview_has_strict_taxonomy_identity(
            db,
            plan,
            _payload_generation_mode(payload),
        )
    except PlanValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    batch = models.AIGenerationBatch(
        status="planned",
        allocation_strategy=payload.allocation_strategy,
        requested_count=payload.requested_count,
        planned_count=plan.planned_count,
        generated_count=0,
        approved_count=0,
        rejected_count=0,
        source_model=payload.source_model,
        prompt_version=payload.prompt_version,
        prompt_instructions=payload.prompt_instructions,
        execution_mode=NORMAL_API_EXECUTION_MODE,
        raw_request_json=json.dumps(payload.model_dump(mode="json"), ensure_ascii=False),
    )
    db.add(batch)
    db.flush()

    for item in plan.plan_items:
        db.add(
            models.AIGenerationPlanItem(
                batch_id=batch.id,
                position=item.position,
                requested_count=item.requested_count,
                generated_count=0,
                status="pending",
                language_id=item.language_id,
                category_id=item.category_id,
                topic_id=item.topic_id,
                technology_id=item.technology_id,
                technology_domain_id=item.technology_domain_id,
                technology_module_id=item.technology_module_id,
                technology_topic_id=item.technology_topic_id,
                technology_subtopic_id=item.technology_subtopic_id,
                primary_concept_id=item.primary_concept_id,
                question_type_id=item.question_type_id,
                difficulty=item.difficulty,
                prompt_context=item.prompt_context,
            )
        )

    db.commit()
    db.refresh(batch)

    return _batch_detail(batch)


@router.post("/{batch_id}/run", response_model=AIGenerationRunResult)
def run_ai_generation_batch(
    batch_id: int,
    provider: Literal["mock", "openai"] | None = Query(default=None),
    model_profile: str | None = Query(default=None),
    execution_mode: Literal["normal", "normal_api", "batch_api"] | None = Query(default=None),
    mock_classification_case: Literal["missing", "invalid_ids", "low_confidence", "new_concept"] | None = Query(default=None),
    db: Session = Depends(get_db),
):
    # Normal API remains the immediate execution path. Batch API mode creates
    # durable execution jobs first; separate admin actions then submit the
    # provider batch, check status, collect results, and reconcile staged drafts.
    selected_provider = _resolve_ai_generation_provider(provider)
    selected_model_profile = _resolve_ai_generation_model_profile(selected_provider, model_profile)
    selected_execution_mode = _resolve_ai_generation_execution_mode(execution_mode)
    _validate_execution_mode_provider_pair(selected_provider, selected_execution_mode)

    if mock_classification_case is not None and selected_provider != "mock":
        raise HTTPException(
            status_code=400,
            detail="mock_classification_case is only available when provider=mock.",
        )
    if mock_classification_case is not None and is_batch_api_execution_mode(selected_execution_mode):
        raise HTTPException(
            status_code=400,
            detail="mock_classification_case is not available for Batch API preparation.",
        )

    batch = _get_batch_or_404(db, batch_id)
    batch_generation_mode = _batch_generation_mode(batch)

    pending_items = (
        db.query(models.AIGenerationPlanItem)
        .filter(
            models.AIGenerationPlanItem.batch_id == batch_id,
            models.AIGenerationPlanItem.status.in_(["pending", "failed"]),
        )
        .order_by(models.AIGenerationPlanItem.position.asc())
        .all()
    )

    if not pending_items:
        return AIGenerationRunResult(
            batch_id=batch.id,
            status=batch.status,
            processed_plan_item_count=0,
            generated_question_count=0,
            failed_plan_item_count=0,
            provider=selected_provider,
            model_profile=selected_model_profile,
            model_used=batch.model_used,
            actual_input_tokens=batch.actual_input_tokens,
            actual_output_tokens=batch.actual_output_tokens,
            actual_total_tokens=batch.actual_total_tokens,
            actual_cost_usd=_decimal_to_float(batch.actual_cost_usd),
            message=(
                f"No pending plan items to run for provider '{selected_provider}' "
                f"using execution mode '{selected_execution_mode}'."
            ),
        )

    if batch_generation_mode != "reverse":
        _ensure_normal_plan_items_have_strict_taxonomy_identity(db, pending_items)

    if is_batch_api_execution_mode(selected_execution_mode):
        return _prepare_batch_api_generation_jobs(
            db=db,
            batch=batch,
            pending_items=pending_items,
            selected_provider=selected_provider,
            selected_model_profile=selected_model_profile,
        )

    batch.status = "running"
    batch.started_at = batch.started_at or datetime.utcnow()
    batch.execution_provider = selected_provider
    batch.execution_mode = NORMAL_API_EXECUTION_MODE
    batch.model_profile = selected_model_profile
    batch.error_message = None
    db.commit()

    processed_plan_item_count = 0
    generated_question_count = 0
    failed_plan_item_count = 0

    for item in pending_items:
        item.status = "running"
        item.execution_provider = selected_provider
        item.execution_mode = NORMAL_API_EXECUTION_MODE
        item.model_profile = selected_model_profile
        item.error_message = None
        db.commit()

        chunks = split_normal_api_chunks(item.requested_count)
        item_generated_count = 0
        item_failed_chunk_count = 0

        for chunk in chunks:
            execution_job = _create_execution_job_for_plan_item(
                db=db,
                item=item,
                provider=selected_provider,
                model_profile=selected_model_profile,
                chunk=chunk,
                execution_mode=NORMAL_API_EXECUTION_MODE,
            )

            try:
                avoid_patterns = _build_plan_item_avoid_patterns(db, item)
                service_response = _call_question_service(
                    db=db,
                    item=item,
                    provider=selected_provider,
                    model_profile=selected_model_profile,
                    generation_mode=batch_generation_mode,
                    requested_count=chunk.requested_count,
                    avoid_patterns=avoid_patterns,
                    mock_classification_case=mock_classification_case,
                )
                if service_response.prompt_version and not batch.prompt_version:
                    batch.prompt_version = service_response.prompt_version

                usage_summary = _apply_plan_item_usage_metadata(
                    item=item,
                    service_response=service_response,
                    selected_provider=selected_provider,
                    selected_model_profile=selected_model_profile,
                    execution_mode=NORMAL_API_EXECUTION_MODE,
                )
                _copy_plan_item_execution_metadata_to_job(execution_job, item)
                created_count = _store_generated_questions(
                    db=db,
                    batch=batch,
                    item=item,
                    service_response=service_response,
                    usage_summary=usage_summary,
                )
                execution_job.generated_count = created_count
                execution_job.status = "completed"
                execution_job.completed_at = datetime.utcnow()
                item_generated_count += created_count
                generated_question_count += created_count
            except Exception as exc:  # noqa: BLE001 - convert service failures into execution-job state.
                execution_job.status = "failed"
                execution_job.error_category = _categorize_generation_error(exc)
                execution_job.error_message = str(exc)
                execution_job.completed_at = datetime.utcnow()
                item_failed_chunk_count += 1

            db.commit()

        _refresh_plan_item_execution_totals(db, item.id)

        if item_failed_chunk_count == 0:
            item.status = "completed"
            item.error_message = None
        elif item_generated_count > 0:
            item.status = "partial_failed"
            item.error_message = (
                f"{item_failed_chunk_count} of {len(chunks)} normal-API chunk(s) failed during generation."
            )
            failed_plan_item_count += 1
        else:
            item.status = "failed"
            item.error_message = "All normal-API chunks failed during generation."
            failed_plan_item_count += 1

        processed_plan_item_count += 1
        db.commit()

    batch.generated_count = (
        db.query(models.AIGeneratedQuestion)
        .filter(models.AIGeneratedQuestion.batch_id == batch.id)
        .count()
    )
    _refresh_batch_execution_totals(db, batch.id)
    batch.completed_at = datetime.utcnow()
    batch.status = "completed" if failed_plan_item_count == 0 else "partial_failed"
    if failed_plan_item_count:
        batch.error_message = f"{failed_plan_item_count} plan item(s) failed during generation."

    db.commit()
    db.refresh(batch)

    return AIGenerationRunResult(
        batch_id=batch.id,
        status=batch.status,
        processed_plan_item_count=processed_plan_item_count,
        generated_question_count=generated_question_count,
        failed_plan_item_count=failed_plan_item_count,
        provider=selected_provider,
        model_profile=batch.model_profile,
        model_used=batch.model_used,
        actual_input_tokens=batch.actual_input_tokens,
        actual_output_tokens=batch.actual_output_tokens,
        actual_total_tokens=batch.actual_total_tokens,
        actual_cost_usd=_decimal_to_float(batch.actual_cost_usd),
        message=(
            f"AI generation batch run finished using provider '{selected_provider}' "
            f"with normal API chunks capped at {NORMAL_API_MAX_QUESTIONS_PER_REQUEST} question(s)."
        ),
    )


def _prepare_batch_api_generation_jobs(
    db: Session,
    batch: models.AIGenerationBatch,
    pending_items: list[models.AIGenerationPlanItem],
    selected_provider: Literal["openai"],
    selected_model_profile: str,
) -> AIGenerationRunResult:
    # Batch API starts by creating durable execution jobs that represent JSONL
    # request lines. The admin can then submit, poll, collect, and reconcile the
    # provider batch using explicit lifecycle actions.
    batch.status = BATCH_API_BATCH_STATUS
    batch.started_at = batch.started_at or datetime.utcnow()
    batch.completed_at = None
    batch.execution_provider = selected_provider
    batch.execution_mode = BATCH_API_EXECUTION_MODE
    batch.model_profile = selected_model_profile
    batch.model_used = _resolve_ai_generation_model_used(
        provider=selected_provider,
        model_profile=selected_model_profile,
    )
    batch.provider_batch_id = None
    batch.provider_batch_status = None
    batch.provider_input_file_id = None
    batch.provider_output_file_id = None
    batch.provider_error_file_id = None
    batch.provider_batch_request_counts_json = None
    batch.provider_batch_submitted_at = None
    batch.provider_batch_status_checked_at = None
    batch.error_message = (
        "Batch API execution jobs are prepared but not submitted yet. "
        "Submit them to OpenAI Batch API, then check status until output is ready."
    )

    prepared_job_count = 0
    prepared_question_count = 0

    for item in pending_items:
        item.status = BATCH_API_PENDING_SUBMISSION_STATUS
        item.execution_provider = selected_provider
        item.execution_mode = BATCH_API_EXECUTION_MODE
        item.model_profile = selected_model_profile
        item.model_used = batch.model_used
        item.error_message = "Prepared for Batch API submission; not submitted to OpenAI yet."

        for chunk in split_execution_chunks(item.requested_count, BATCH_API_EXECUTION_MODE):
            execution_job = _create_execution_job_for_plan_item(
                db=db,
                item=item,
                provider=selected_provider,
                model_profile=selected_model_profile,
                chunk=chunk,
                execution_mode=BATCH_API_EXECUTION_MODE,
                status=BATCH_API_PENDING_SUBMISSION_STATUS,
            )
            execution_job.model_used = batch.model_used
            execution_job.provider_batch_id = None
            execution_job.provider_request_custom_id = None
            execution_job.error_category = None
            execution_job.error_message = "Prepared for OpenAI Batch API submission."
            execution_job.started_at = None
            prepared_job_count += 1
            prepared_question_count += chunk.requested_count

    db.commit()
    db.refresh(batch)

    return AIGenerationRunResult(
        batch_id=batch.id,
        status=batch.status,
        processed_plan_item_count=len(pending_items),
        generated_question_count=0,
        failed_plan_item_count=0,
        provider=selected_provider,
        model_profile=batch.model_profile,
        model_used=batch.model_used,
        actual_input_tokens=batch.actual_input_tokens,
        actual_output_tokens=batch.actual_output_tokens,
        actual_total_tokens=batch.actual_total_tokens,
        actual_cost_usd=_decimal_to_float(batch.actual_cost_usd),
        provider_batch_id=batch.provider_batch_id,
        provider_batch_status=batch.provider_batch_status,
        provider_input_file_id=batch.provider_input_file_id,
        provider_output_file_id=batch.provider_output_file_id,
        provider_error_file_id=batch.provider_error_file_id,
        provider_batch_request_counts_json=batch.provider_batch_request_counts_json,
        message=(
            f"Prepared {prepared_job_count} Batch API execution job(s) covering "
            f"{prepared_question_count} requested question(s). Submit them to OpenAI Batch API from the batch detail page."
        ),
    )



@router.post("/{batch_id}/batch-api/submit", response_model=AIGenerationBatchDetail)
def submit_ai_generation_batch_api(
    batch_id: int,
    db: Session = Depends(get_db),
