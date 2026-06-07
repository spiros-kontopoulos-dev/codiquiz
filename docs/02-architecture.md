# Architecture Overview

Codiquiz is currently a Dockerized service-oriented modular platform. It uses separate runtime services for the frontend, quiz API, question service, PostgreSQL, Redis, Celery workers, and scheduled automation.

The architecture is intentionally practical: clear service boundaries where they help, without over-splitting the system into premature microservices.

## Current runtime services

```text
frontend-web
  React + TypeScript public/admin UI

quiz-api
  FastAPI product/admin API
  owns database models, quiz flow, user/session logic, admin workflows, AI generation batches

question-service
  FastAPI provider/prompt boundary
  owns OpenAI request formatting and provider-facing generation logic

quiz-worker
  Celery worker for quiz-api-owned background jobs

quiz-beat
  Celery Beat scheduler for recurring quiz-api jobs

question-worker
  provider-side/background worker for question-service

postgres
  source of truth

redis
  Celery broker/result backend
```

## Service boundary philosophy

Codiquiz is not trying to split every file into a separate service. The current rule is:

- keep product/domain ownership in `quiz-api`,
- keep prompt/provider boundary in `question-service`,
- run long-running or scheduled work through workers,
- use PostgreSQL as the source of truth,
- use Redis as broker/result backend,
- add future services only when a clear reason exists.


## User/account layer

The user system should start inside `quiz-api`, not as a separate service. It depends on the product database and needs direct access to:

- users and roles,
- practice sessions,
- question attempts,
- answer correctness,
- seen-question history,
- taxonomy/concept metadata,
- scoring and mastery tables.

Later, aggregate reporting can move to workers or an analytics-service, but the core user/session domain belongs in `quiz-api`.

## Worker service explanation

The project has dedicated worker containers:

- `quiz-worker`,
- `quiz-beat`,
- `question-worker`.

The `quiz-worker` is independent as a runtime service/container, but it currently shares the `quiz-api` codebase because it processes `quiz-api` owned domain tasks, such as:

- Batch API lifecycle scanning,
- provider status polling,
- provider result collection,
- draft reconciliation,
- worker task-run logging,
- future embedding/backfill jobs.

This is intentional. A fully separate worker repository would add complexity too early and would either duplicate domain logic or force awkward service calls.

## Infrastructure vs application services

Codiquiz separates application services from infrastructure systems.

Application/runtime services:

- frontend-web,
- quiz-api,
- question-service,
- quiz-worker,
- quiz-beat,
- question-worker,
- future analytics-service,
- future search-indexer,
- future event-consumer.

Infrastructure systems:

- PostgreSQL,
- Redis,
- future pgvector extension,
- future OpenSearch/Elasticsearch,
- future Kafka,
- future Airflow,
- future monitoring stack.

Implementation tools/frameworks:

- FastAPI,
- SQLAlchemy,
- Alembic,
- Pydantic,
- React,
- TypeScript,
- Celery,
- Celery Beat,
- Playwright.

## Current architecture diagram

```text
React Frontend
   |
   v
quiz-api ---------------> question-service -----> OpenAI API
   |
   +---- PostgreSQL
   |
   +---- Redis <---- quiz-worker
   |             \
   |              +---- quiz-beat
   |
   +---- admin review / approval / automation visibility
```

## Future architecture layers

Future layers are planned as the product grows:

- pgvector semantic similarity,
- OpenSearch/Elasticsearch search projection,
- Kafka event stream,
- event-consumer,
- analytics-service,
- Airflow data pipelines,
- observability stack.

These should be added as separate layers only when they solve a clear product or portfolio problem.
