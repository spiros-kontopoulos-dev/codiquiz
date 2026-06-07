# Celery Batch API lifecycle worker excerpt
# Source: quiz-api/app/async_worker/tasks.py (excerpt lines 280-460)
# Public portfolio excerpt; not standalone application code.

    from app.routers.ai_generations import check_ai_generation_batch_api_status

    return _run_batch_api_endpoint_action(
        action="check_status",
        batch_id=batch_id,
        endpoint=check_ai_generation_batch_api_status,
    )


@celery_app.task(name="quiz_api.batch_api.collect_results")
def collect_batch_api_results(batch_id: int) -> dict[str, object]:
    """Worker wrapper for the manual Batch API collect action."""

    from app.routers.ai_generations import collect_ai_generation_batch_api_results

    return _run_batch_api_endpoint_action(
        action="collect_results",
        batch_id=batch_id,
        endpoint=collect_ai_generation_batch_api_results,
    )


@celery_app.task(name="quiz_api.batch_api.reconcile_drafts")
def reconcile_batch_api_drafts(batch_id: int) -> dict[str, object]:
    """Worker wrapper for the manual Batch API reconcile action."""

    from app.routers.ai_generations import reconcile_ai_generation_batch_api_results

    return _run_batch_api_endpoint_action(
        action="reconcile_drafts",
        batch_id=batch_id,
        endpoint=reconcile_ai_generation_batch_api_results,
    )


@celery_app.task(name="quiz_api.batch_api.run_lifecycle")
def run_batch_api_lifecycle(batch_id: int) -> dict[str, object]:
    """Run one cautious Batch API lifecycle pass for a single batch.

    The overall lifecycle pass now gets its own task-run row, and the nested
    check/collect/reconcile helpers still log their own specific rows. This
    makes the AI Generation Detail history useful both for direct manual worker
    calls and for scheduled scanner-driven runs.
    """

    task_run_id = _start_worker_task_visibility(
        task_name="quiz_api.batch_api.run_lifecycle",
        action="run_lifecycle",
        batch_id=batch_id,
        target_type="ai_generation_batch",
        target_id=batch_id,
    )

    def finish(result: dict[str, object]) -> dict[str, object]:
        _finish_worker_task_visibility(task_run_id, result=result)
        return result

    try:
        steps: list[dict[str, object]] = []
        initial_state = _read_batch_api_worker_state(batch_id)

        if not initial_state.get("exists"):
            return finish(
                _batch_api_task_result(
                    action="run_lifecycle",
                    batch_id=batch_id,
                    status="blocked",
                    message="Batch not found.",
                )
            )
        if initial_state.get("is_archived"):
            return finish(
                _batch_api_task_result(
                    action="run_lifecycle",
                    batch_id=batch_id,
                    status="blocked",
                    message="Archived batches are skipped by Batch API worker tasks.",
                )
            )
        if not initial_state.get("is_batch_api"):
            return finish(
                _batch_api_task_result(
                    action="run_lifecycle",
                    batch_id=batch_id,
                    status="blocked",
                    message="Only Batch API execution-mode batches can be advanced by this worker task.",
                )
            )
        if not initial_state.get("provider_batch_id"):
            return finish(
                _batch_api_task_result(
                    action="run_lifecycle",
                    batch_id=batch_id,
                    status="blocked",
                    message="Batch has not been submitted to OpenAI Batch API yet; submit remains a manual admin action.",
                )
            )
        if initial_state.get("results_reconciled"):
            return finish(
                _batch_api_task_result(
                    action="run_lifecycle",
                    batch_id=batch_id,
                    status="ok",
                    message="Batch API lifecycle already appears reconciled.",
                    batch=initial_state,
                )
            )

        state = initial_state
        if not state.get("results_collected"):
            status_result = check_batch_api_status(batch_id)
            steps.append(status_result)
            if status_result.get("status") == "error":
                return finish(
                    {
                        "status": "error",
                        "action": "run_lifecycle",
                        "batch_id": batch_id,
                        "message": "Batch API lifecycle stopped after status check error.",
                        "steps": steps,
                        "checked_at": _batch_lifecycle_timestamp(),
                    }
                )
            state = _read_batch_api_worker_state(batch_id)

        can_collect = bool(
            not state.get("results_collected")
            and (state.get("provider_output_file_id") or state.get("provider_error_file_id"))
        )
        if can_collect:
            collect_result = collect_batch_api_results(batch_id)
            steps.append(collect_result)
            if collect_result.get("status") == "error":
                return finish(
                    {
                        "status": "error",
                        "action": "run_lifecycle",
                        "batch_id": batch_id,
                        "message": "Batch API lifecycle stopped after collection error.",
                        "steps": steps,
                        "checked_at": _batch_lifecycle_timestamp(),
                    }
                )
            state = _read_batch_api_worker_state(batch_id)

        if state.get("results_collected") and not state.get("results_reconciled"):
            reconcile_result = reconcile_batch_api_drafts(batch_id)
            steps.append(reconcile_result)
            if reconcile_result.get("status") == "error":
                return finish(
                    {
                        "status": "error",
                        "action": "run_lifecycle",
                        "batch_id": batch_id,
                        "message": "Batch API lifecycle stopped after reconciliation error.",
                        "steps": steps,
                        "checked_at": _batch_lifecycle_timestamp(),
                    }
                )
            state = _read_batch_api_worker_state(batch_id)

        final_status = "ok" if steps else "blocked"
        final_message = (
            "Batch API lifecycle worker pass completed."
            if steps
            else "No lifecycle action was ready for this batch."
        )
        return finish(
            {
                "status": final_status,
                "action": "run_lifecycle",
                "batch_id": batch_id,
                "message": final_message,
                "initial_state": initial_state,
                "final_state": state,
                "steps": steps,
                "checked_at": _batch_lifecycle_timestamp(),
            }
        )
    except Exception as exc:  # noqa: BLE001 - worker visibility should capture lifecycle failures.
        result = _batch_api_task_result(
