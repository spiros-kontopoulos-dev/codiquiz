# Portfolio and Engineering Highlights

Codiquiz is designed to demonstrate serious backend, AI engineering, full-stack product architecture, and operational ownership.

## Backend engineering

- FastAPI service-oriented backend.
- SQLAlchemy data model.
- Alembic migrations.
- PostgreSQL source of truth.
- Admin APIs for taxonomy, quizzes, generation, review, cost/quality, and automation.
- Clear service boundaries between product API and provider/prompt service.

## AI engineering

- OpenAI Normal API integration.
- OpenAI Batch API integration.
- Structured question generation.
- Prompt rules and output normalization.
- Draft staging before publication.
- Editable model profile mapping from admin settings.
- OpenAI model pricing catalog and relative cost comparison.
- `tiktoken`-based pre-generation cost estimates.
- Actual cost tracking from provider usage metadata.
- Cost & Quality dashboard for generation outcomes.
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

## Frontend/public engineering

- React + TypeScript public UI.
- Practice landing page.
- Quick Practice flow.
- Custom Practice with taxonomy targeting.
- Try Concept mode and Concept Finder.
- Public quiz technology filtering.
- Promoted and coming-soon quiz cards.
- Practice session UI with feedback, navigation protection, and review.

## Frontend/admin engineering

- React + TypeScript admin UI.
- Admin generation planner.
- AI draft review UI.
- Batch API lifecycle detail page.
- AI Generation Settings with model profiles, pricing, and automation status.
- Cost & Quality dashboard.
- Worker history pagination.
- Practical admin queue-card/focused-content patterns.

## User and learning systems

- Anonymous practice modes.
- Future registered learner accounts.
- Persistent attempt history direction.
- Seen-question tracking direction.
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

Codiquiz demonstrates more than AI question generation. It combines structured taxonomy design, public practice flows, AI draft staging, duplicate/similarity evaluation, a Backend Intelligence Layer for deciding what should be generated next, Blueprint coverage planning, suitability scoring, editable model/cost management, Redis/Celery automation, preview deployment, and future adaptive serving/scoring systems into one coherent coding-practice platform.
