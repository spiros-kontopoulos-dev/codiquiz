# Roadmap

Codiquiz is in early alpha. This roadmap separates what is implemented, what is near-term, and what belongs to later platform expansion.

## Implemented foundation

- Public homepage / technology page / quick practice foundation.
- Admin taxonomy and question-bank pages.
- AI generation planner.
- Normal OpenAI generation.
- OpenAI Batch API lifecycle.
- Draft staging and review workflow.
- Backend Quality Engine foundations.
- Concept importance scoring and admin audit views.
- Reviewed suitability-aware generation planning foundation.
- Blueprint default target generation from importance + suitability.
- Blueprint coverage/admin foundation with work queues and candidates.
- Redis/Celery worker foundation.
- Celery Beat scheduler.
- Batch API lifecycle automation scanner.
- Worker task-run history in admin settings.

## Near term

- Polish the live preview/demo showcase flow.
- Deploy final production site to `codiquiz.com`.
- Keep preview/admin demo environment isolated from final production.
- Add project screenshots.
- Add architecture diagrams.
- Improve public documentation repository and keep the Backend Intelligence Layer visible.

## Next product/AI milestones

- pgvector embeddings and semantic similarity warnings.
- Blueprint auto-generation scheduler.
- Automatic generation batch creation from Blueprint gaps.
- Better Similarity Review UI.
- More robust question serving/selection engine.
- Registered learner accounts, attempt history, ranking score, and mastery foundation.

## Future platform engines

- User accounts and persistent progress.
- Adaptive practice and rolling pools.
- Scoring, ranking, and mastery engine.
- Question quality scoring from real usage data.
- Focused GraphQL read model.
- Standalone GraphQL gateway service.
- Search projection with OpenSearch/Elasticsearch.
- Kafka event stream.
- Analytics-service.
- Airflow data pipelines.
- Observability with metrics, dashboards, and error tracking.

## Long-term platform vision

Codiquiz should become a controlled AI-assisted content platform for coding education.

The long-term system should be able to:

```text
plan coverage
→ generate candidates
→ detect duplicates/similarity
→ review/approve content
→ serve questions intelligently
→ score users fairly
→ measure mastery
→ improve question quality from real usage
```
