# Roadmap

Codiquiz is in early alpha. The current foundation already demonstrates the public practice experience, admin AI generation workflows, quality controls, Blueprint planning, cost/model management, async automation, and preview deployment. The roadmap below separates what is already implemented from the next platform layers.

## Implemented foundation

- Public homepage and Python technology/taxonomy pages.
- Quick Practice, Custom Practice, Try Concept, and Concept Finder.
- Public quiz technology filtering, technology badges, promoted quiz cards, and coming-soon quiz states.
- Admin taxonomy and question-bank foundations.
- AI Generation Create and batch detail flows.
- OpenAI normal API generation.
- OpenAI Batch API prepare/submit/status/collect/reconcile lifecycle.
- AI draft review and approval workflow.
- Backend Quality Engine foundations.
- Duplicate/fingerprint system and avoid-list support.
- Concept importance system.
- Question-type suitability mapping.
- Difficulty suitability guidance.
- Blueprint default target generation.
- Blueprint coverage and generation candidate queues.
- Redis/Celery worker foundation.
- Celery Beat scheduler.
- Batch API lifecycle automation scanner.
- Worker task-run history in admin settings.
- AI model profile visibility.
- Editable profile-to-model mappings.
- OpenAI model pricing catalog and relative cost comparison.
- Cost & Quality dashboard for generation outcomes.
- `tiktoken`-based pre-generation cost estimates.
- Preview deployment foundation and smoke-test workflow.

## Near term

- Polish the live preview/demo showcase flow with screenshots and short demo notes.
- Deploy final production site to `codiquiz.com`.
- Keep preview/admin demo environment isolated from final production.
- Add project screenshots and additional diagrams.
- Keep public documentation synced with major product milestones.

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
