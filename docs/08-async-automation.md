# Async Automation with Redis and Celery

Codiquiz uses Redis and Celery for background processing and scheduled automation.

This keeps slow or recurring work out of normal HTTP request/response flows.

## Current services

```text
redis
  broker/result backend

quiz-worker
  Celery worker for quiz-api-owned background jobs

quiz-beat
  Celery Beat scheduler for recurring quiz-api jobs

question-worker
  provider-side/background worker for question-service
```

## Why quiz-worker belongs to quiz-api

Batch API lifecycle automation depends on quiz-api domain state:

- AI generation batches,
- execution jobs,
- provider batch IDs,
- collected provider result lines,
- staged drafts,
- duplicate policies,
- admin settings,
- worker task-run history.

Therefore the first worker implementation runs as a separate container/process but shares the quiz-api codebase.

This gives the platform a dedicated background runtime without prematurely extracting a separate worker repository.

## Current automated workflow

The Batch API lifecycle scanner can run through Celery Beat.

Flow:

```text
Celery Beat
→ enqueue lifecycle scanner
→ scanner finds eligible Batch API batches
→ worker checks status / collects results / reconciles drafts when safe
→ task run is logged
→ admin can inspect recent worker runs
```

## Scanner safety rules

The scanner is bounded and conservative.

It skips:

- archived batches,
- normal API batches,
- unsubmitted batches,
- already reconciled batches,
- failed/expired/cancelled terminal provider states unless reporting only.

It processes only a configured number of eligible batches per pass.

## Dry-run vs live mode

### Dry-run mode

The scanner reports candidates without making changes.

Useful for:

- validating automation,
- checking what would be processed,
- safe staging/admin demo mode.

### Live mode

The scanner performs actual lifecycle actions:

- provider status check,
- result collection,
- draft reconciliation.

## Manual controls remain available

Admin lifecycle buttons still exist on the Batch API detail page.

They act as:

- manual override,
- debugging tools,
- recovery controls,
- visibility into individual lifecycle actions.

Scheduled automation does not remove manual control.

## Worker task-run history

Worker runs are logged so the admin can answer:

- when did the worker run?
- which task ran?
- did it succeed or fail?
- which batch did it touch?
- was it dry-run or live?
- how long did it take?
- what error happened?

This is the first observability layer for async automation.

## Future async jobs

The same worker foundation can later support:

- Blueprint auto-generation scanner,
- automatic batch creator,
- embedding generation,
- embedding backfills,
- semantic similarity maintenance,
- public question pool cache warming,
- question quality metric recalculation,
- analytics/report refreshes.
