# Portfolio and Engineering Highlights

Codiquiz is designed to demonstrate serious backend, AI engineering, and full-stack product architecture.

## Backend engineering

- FastAPI service-oriented backend.
- SQLAlchemy data model.
- Alembic migrations.
- PostgreSQL source of truth.
- Admin APIs for taxonomy, generation, review, and automation.
- Clear service boundaries between product API and provider/prompt service.

## AI engineering

- OpenAI Normal API integration.
- OpenAI Batch API integration.
- Structured question generation.
- Prompt rules and output normalization.
- Draft staging before publication.
- Cost/execution metadata tracking.
- Avoid-list support for overused patterns.
- Future embeddings and pgvector semantic search.

## Content quality systems

- Deterministic duplicate signatures.
- Code/prompt normalization.
- Same-concept duplicate checks.
- Related-pattern notes.
- Anti-repetition inside generated batches.
- Approved question bank as source of truth.
- Archived content excluded from active blocking checks.

## Backend intelligence and content planning

- Deep taxonomy model.
- Concept-based question targets.
- Concept importance scoring and tiers.
- Reviewed question task type suitability.
- Difficulty-specific suitability weighting and blocking.
- Blueprint default target generation from importance + suitability.
- Blueprint coverage/gap detection.
- Generation priority scoring for recommended candidates.
- Future auto-generation from Blueprint gaps.

## Async/distributed systems

- Redis broker/result backend.
- Dedicated Celery worker container.
- Dedicated Celery Beat scheduler container.
- Scheduled Batch API lifecycle scanner.
- Dry-run/live automation modes.
- Worker task-run history.
- Future embedding/backfill jobs.

## Frontend/admin engineering

- React + TypeScript public/admin UI.
- Admin generation planner.
- AI draft review UI.
- Batch API lifecycle detail page.
- Settings/readiness pages.
- Worker history pagination.
- Practical admin queue-card/focused-content patterns.

## User and learning systems

- Future registered learner accounts.
- Anonymous and registered practice modes.
- Persistent attempt history.
- Seen-question tracking.
- Ranking score direction.
- Concept mastery profiles.
- Personalized/adaptive practice direction.

## Future learning/analytics systems

- Question serving and selection engine.
- Rolling pool / endless practice mode.
- User scoring and ranking.
- Concept mastery tracking.
- Question quality metrics.
- Analytics-service and data pipelines.

## Strong summary

Codiquiz demonstrates more than AI question generation. It combines structured taxonomy design, AI draft staging, duplicate/similarity evaluation, a Backend Intelligence Layer for deciding what should be generated next, Blueprint coverage planning, suitability scoring, Redis/Celery automation, future user progress, and adaptive serving/scoring systems into one coherent coding-practice platform.
