# Codiquiz: AI-Powered Coding Quiz Platform

> **Status:** Early alpha.
> Codiquiz is actively being built. The current version demonstrates the core architecture, admin workflows, AI generation pipeline, Batch API automation, Backend Quality Engine, Backend Intelligence Layer, Blueprint planning, and preview deployment foundation, while final production rollout, learner accounts, scoring, semantic similarity, and advanced learning features are still evolving.

Codiquiz is an AI-assisted coding quiz platform for building deep, taxonomy-based question banks. It combines a public coding-practice experience with an admin platform for taxonomy management, AI question generation, draft review, duplicate/similarity control, concept-importance scoring, suitability-aware Blueprint planning, and Redis/Celery automation.

This is the public documentation, architecture, and code-examples repository for Codiquiz. The complete application source remains private because Codiquiz is an active online platform, while this repository provides public documentation, diagrams, demo/recruiter walkthroughs, and selected sanitized code excerpts for portfolio review.


---

## Live early alpha preview

- Public preview: `https://preview.codiquiz.com`
- Admin preview: `https://admin.preview.codiquiz.com/login`

The preview environment is an isolated early-alpha deployment used for demonstration, testing, and portfolio review. It has its own database, Redis instance, secrets, OpenAI preview key, backup workflow, and restricted demo/admin access.

## Demo documentation

- Public preview: `https://preview.codiquiz.com`
- Admin preview: `https://admin.preview.codiquiz.com/login`
- Demo/recruiter walkthrough: [Recruiter Demo Presentation Flow](docs/demo/RECRUITER_DEMO_PRESENTATION_FLOW.md)
- Preview demo walkthrough: [Preview Demo Walkthrough](docs/demo/PREVIEW_DEMO_WALKTHROUGH.md)
- Demo account boundaries: [Demo Account Boundaries](docs/demo/DEMO_ACCOUNT_BOUNDARIES.md)

This public repository is not the full Codiquiz application source and is not intended to run as a standalone app. It contains public documentation plus selected code excerpts that demonstrate the backend, AI, quality, automation, frontend, testing, and deployment architecture.

---

## Documentation map

- [Product Overview](docs/01-product-overview.md)
- [Architecture](docs/02-architecture.md)
- [Taxonomy and Vocabulary](docs/03-taxonomy-vocabulary.md)
- [AI Generation Workflow](docs/04-ai-generation-workflow.md)
- [Backend Quality Engine](docs/05-backend-quality-engine.md)
- [Blueprint Coverage System](docs/06-blueprint-coverage-system.md)
- [Suitability Mapping](docs/07-suitability-mapping.md)
- [Backend Intelligence Layer](docs/17-backend-intelligence-layer.md)
- [Async Automation](docs/08-async-automation.md)
- [Deployment Model](docs/13-deployment-model.md)
- [Roadmap](docs/14-roadmap.md)
- [Portfolio Engineering Highlights](docs/15-portfolio-engineering-highlights.md)
- [Architecture Diagrams](docs/diagrams/README.md)


## Code examples

This repository includes selected sanitized code excerpts from the private Codiquiz codebase.

The examples show the engineering approach behind the platform, including FastAPI routers, Pydantic contracts, SQLAlchemy model excerpts, AI generation planning, Blueprint intelligence, quality and duplicate checks, async workers, public traffic tracking, React/TypeScript admin/public code, Playwright configuration, and sanitized infrastructure examples.

They are **not** the full application source code and are **not intended to run as a standalone application**.

See: [Code Examples](code-examples/README.md)

## Why Codiquiz is different

Codiquiz is not only a quiz UI and not only an AI wrapper. The core idea is to build a controlled question-bank platform where generated content is planned, validated, reviewed, and served intelligently.

Key ideas:

- Deep taxonomy model: technology → domain → module → topic → subtopic → concept.
- Concepts are testable behaviors, rules, traps, misconceptions, or comparisons, not just API reference items.
- AI-generated questions are staged as drafts first, then checked and reviewed before approval.
- The Backend Quality Engine protects the bank from duplicates, near-duplicates, repetitive patterns, and weak generation output.
- The Blueprint system defines what the question bank should contain and where generation gaps exist.
- The Backend Intelligence Layer combines concept importance, question-type suitability, difficulty weighting, and coverage gaps to decide what should be generated next.
- Suitability mapping decides which question task types fit each concept or taxonomy entity.
- Redis/Celery workers and Celery Beat automate background lifecycle work.
- Future engines will add semantic embeddings, adaptive serving, scoring, ranking, mastery, and analytics.

---

## Current implementation status

### Implemented

- Public homepage, technology page, and quick-practice foundation.
- Quiz/session-oriented practice foundation.
- Admin taxonomy and question-bank management.
- AI generation planner and draft review workflow.
- Normal OpenAI generation mode.
- OpenAI Batch API lifecycle: prepare → submit → status → collect → reconcile.
- Draft staging, review, edit, rejection, and approval flow.
- Backend Quality Engine foundations:
  - deterministic signatures,
  - duplicate detection,
  - anti-repetition checks,
  - avoid-list support,
  - related-pattern notes,
  - active duplicate-source policy.
- Concept importance scoring and admin audit views.
- Reviewed question-type suitability mapping with strong, secondary, weak/manual-only, and unsuitable tiers.
- Suitability-aware generation planning foundation.
- Blueprint default target generation from importance + suitability.
- Blueprint coverage, work queues, and generation candidate admin views.
- Redis/Celery worker foundation.
- Celery Beat scheduled automation.
- Batch API lifecycle scanner automation.
- Worker task-run history in admin settings.

### In progress / near term

- Polish the live preview/demo showcase flow.
- Deploy the final production site to `codiquiz.com` on a separate VPS.
- Keep the protected admin preview/demo environment isolated from final production.
- Add pgvector embeddings and semantic similarity warnings.
- Add Blueprint-driven automatic generation batches.
- Add registered learner accounts, persistent attempt history, scoring, and mastery tracking.

---

## Product areas

### Public practice experience

Codiquiz is designed around deep coding-practice question banks. The public side focuses on helping users practice technologies such as Python through structured multiple-choice coding questions.

Planned and current public features:

- Public homepage.
- Technology pages such as Python.
- Quick practice flow.
- Taxonomy-based question filtering.
- Multiple-choice coding questions.
- Future custom practice builder.
- Future adaptive practice based on weak concepts and user history.


### User accounts and progress system

Codiquiz is designed to support both anonymous practice and registered learner accounts. The early alpha can support quick practice without forcing sign-up, while the future learner account layer will add persistent progress and personalization.

Planned user-facing capabilities:

- Anonymous practice sessions for quick access.
- Registered learner accounts with saved progress.
- Attempt history by question, topic, concept, difficulty, and question task type.
- Seen-question tracking to avoid repetition.
- Concept mastery profiles such as strong, weak, or needs practice.
- Difficulty-weighted scoring and ranking score.
- Future leaderboards, streaks, accuracy metrics, and adaptive practice.

See: [User Accounts and Progress](docs/16-user-accounts-progress.md)

### Admin platform

The admin side is the operational control center for building and maintaining the question bank.

Admin capabilities include:

- Taxonomy management.
- Question-bank management.
- Question type mapping.
- Suitability rule management.
- Blueprint coverage and audit pages.
- AI generation planner.
- AI draft review inbox.
- Batch API lifecycle detail pages.
- Redis/Celery readiness display.
- Worker task-run history.

---

## Core architecture

Codiquiz is currently a Dockerized service-oriented modular platform. It uses separate runtime services for the frontend, quiz API, question service, PostgreSQL, Redis, Celery workers, and scheduled automation.

Current service boundaries:

- **frontend-web** — React/TypeScript public and admin UI.
- **quiz-api** — FastAPI product/admin API and database-domain owner.
- **question-service** — AI/provider/prompt boundary.
- **quiz-worker** — Celery worker for quiz-api-owned background jobs.
- **quiz-beat** — Celery Beat scheduler for recurring quiz-api automation.
- **question-worker** — provider-side/background worker for question-service.
- **PostgreSQL** — source of truth.
- **Redis** — Celery broker and result backend.

The workers are independent runtime services/containers. The quiz-worker currently shares the quiz-api codebase because it processes quiz-api-owned domain tasks such as Batch API lifecycle automation and future embedding/backfill jobs.

See: [Architecture Overview](docs/02-architecture.md)

---

## Core vocabulary

A few terms are central to the project:

- **Technology** — a programming ecosystem, such as Python.
- **Domain** — a broad area inside a technology, such as Core Language.
- **Module** — a major learning area, such as Data Structures.
- **Topic** — a focused area, such as Lists.
- **Subtopic** — a smaller grouping inside a topic, such as List Methods.
- **Concept** — a testable behavior, rule, trap, misconception, or comparison.
- **Concept importance** — an educational value score/tier used to prioritize coverage and generation.
- **Question task type** — the cognitive task, such as predict output, bug finding, code understanding, or conceptual reasoning.
- **Answer format** — how the user answers, such as single choice or multiple choice.
- **Draft** — generated candidate question waiting for admin review.
- **Approved question** — canonical question-bank item available for serving.
- **Blueprint** — the content plan describing what the question bank should contain.
- **Blueprint row** — one target combination such as concept + difficulty + question task type + target count.
- **Coverage gap** — missing amount between target count and current approved/pending coverage.
- **Suitability** — how well a question task type fits a concept or taxonomy entity.
- **Fingerprint** — the identity/signature of one question used for duplicate and similarity checks.
- **Avoid-list** — compact prompt guidance describing overused patterns that generation should avoid.
- **Embedding** — a vector representation of question meaning used for future semantic similarity search.
- **Attempt** — one user answer to one question.
- **Mastery profile** — future per-topic or per-concept estimate of user strength and weakness.

See: [Taxonomy and Vocabulary](docs/03-taxonomy-vocabulary.md)

---

## AI generation workflow

Codiquiz supports two OpenAI execution modes:

- **Normal API mode** for immediate generation.
- **Batch API mode** for asynchronous larger generation runs.

Batch API lifecycle:

```text
Prepare request jobs
→ Submit to OpenAI Batch API
→ Check provider status
→ Collect provider output/error files
→ Reconcile results into staged drafts
→ Admin review and approval
```

Generated questions are not published directly. They become staged drafts first. The backend parses and normalizes the provider output, separates question text from code snippets, applies prompt rules and format normalization, computes signatures/fingerprints, checks duplicate and repetition policies, and only then exposes drafts for admin review.

See: [AI Generation Workflow](docs/04-ai-generation-workflow.md)

---

## Backend Quality Engine

The Backend Quality Engine protects the approved question bank from duplicate, repetitive, or low-value generated content.

It includes:

- Deterministic question/code signatures.
- Normalized prompt/code signatures.
- Duplicate checks across approved questions and live AI drafts.
- Same-concept strong duplicate blocking.
- Cross-question-type duplicate detection.
- Related-pattern notes for non-blocking similarity.
- Compact avoid-list guidance for overused patterns.
- Anti-repetition checks inside generated batches.
- Archived batches/questions excluded from active duplicate checks.
- Approved question bank as the source of truth.

See: [Backend Quality Engine](docs/05-backend-quality-engine.md)


---

## Backend Intelligence Layer

Codiquiz is not only generating questions; it now has a backend intelligence layer that decides which content should exist, which gaps matter most, and which AI generation targets are worth spending tokens on.

Current intelligence signals include:

- **Concept importance** — scores Python concepts by educational value and groups them into core, standard, niche, or excluded tiers.
- **Question-type suitability** — maps concepts to task types using strong, secondary, weak/manual-only, and unsuitable tiers.
- **Difficulty weighting** — blocks or downranks concept/type/difficulty combinations that do not make educational sense.
- **Blueprint defaults** — converts importance + suitability into target counts for concept/type/difficulty coverage cells.
- **Generation priority** — ranks missing coverage using importance, suitability, approved count, pending drafts, and coverage gap.

This layer powers the admin coverage queues and the Blueprint candidate flow used by AI Generation Create.

See: [Backend Intelligence Layer](docs/17-backend-intelligence-layer.md)

---

## Blueprint coverage system

The Blueprint system defines what the question bank should contain.

```text
Blueprint = content plan
Question bank = current content
Coverage gap = what should be generated next
```

The system compares desired coverage against approved questions and pending drafts, then identifies generation gaps by taxonomy path, difficulty, question task type, suitability tier, and concept importance. Default target counts can be derived from the intelligence layer, while Blueprint rules and admin overrides keep the plan controllable.

See: [Blueprint Coverage System](docs/06-blueprint-coverage-system.md)

---

## Suitability mapping and scoring

Suitability mapping decides which question task types are appropriate for a taxonomy entity or concept.

It helps answer:

- Which question types fit this concept best?
- Which are secondary but still useful?
- Which are weak-fit and should only be manually selectable?
- Which are not suitable and should be excluded from automatic generation?

See: [Suitability Mapping](docs/07-suitability-mapping.md)

---

## Async automation with Redis/Celery

Codiquiz uses Redis and Celery for background processing and scheduled automation.

Current async capabilities:

- quiz-worker processes quiz-api-owned background jobs.
- quiz-beat schedules recurring automation.
- Redis acts as broker/result backend.
- Scheduled scanner can manage Batch API lifecycle steps.
- Worker task-run history is visible in admin settings.
- Dry-run/live scanner configuration and per-pass limits are available.

See: [Async Automation](docs/08-async-automation.md)

---

## Future engines

Codiquiz is designed to grow beyond generation and review.

Future platform engines include:

- **Question Serving & Selection Engine** — fixed sessions, rolling pools, endless practice, adaptive serving, and anti-repetition.
- **User Accounts & Progress System** — persistent attempts, seen-question history, saved progress, and future personalization.
- **Scoring, Ranking & Mastery Engine** — fair scoring, leaderboards, concept mastery, and question quality metrics.
- **Embeddings and Semantic Similarity** — pgvector-based semantic duplicate detection and similarity warnings.
- **GraphQL Read Model / Gateway** — focused future GraphQL exposure for nested read-heavy data.

See:

- [Question Serving & Selection](docs/09-question-serving-selection.md)
- [User Accounts and Progress](docs/16-user-accounts-progress.md)
- [Scoring, Ranking & Mastery](docs/10-scoring-ranking-mastery.md)
- [GraphQL Roadmap](docs/11-graphql-roadmap.md)
- [Embeddings and Semantic Similarity](docs/12-embeddings-semantic-similarity.md)

---

## Deployment model

Codiquiz uses an isolated deployment model. The current preview/demo environment is live separately from the future final production environment.

- **Preview VPS** — public preview at `preview.codiquiz.com` and clean admin preview at `admin.preview.codiquiz.com`.
- **Future production VPS** — official public site at `codiquiz.com` / `www.codiquiz.com` and protected admin at `admin.codiquiz.com`.

Preview and production must not share the same database, Redis instance, secrets, or OpenAI key. The public site and admin system are separated so the public quiz experience can remain clean while generation, review, automation, and admin tools stay protected.

See: [Deployment Model](docs/13-deployment-model.md)

---

## Roadmap

Near term:

- Polish the live preview/demo showcase flow.
- Update public README/docs with the Backend Intelligence Layer.
- Deploy final production to `codiquiz.com` on a separate VPS.
- Add screenshots and architecture diagrams.

Next:

- pgvector embeddings and semantic similarity warnings.
- Blueprint auto-generation scheduler.
- Optional off-server backup copy for preview/production.
- Better question serving/selection engine.
- User accounts, attempt history, ranking score, and mastery foundation.

Later:

- Focused GraphQL read model or standalone GraphQL gateway.
- OpenSearch/Elasticsearch search projection.
- Kafka event stream.
- Airflow/data pipelines.
- Analytics service.
- Observability stack.

See: [Roadmap](docs/14-roadmap.md)

---

## Engineering highlights

Codiquiz demonstrates more than AI question generation. It combines structured taxonomy design, AI draft staging, duplicate/similarity evaluation, a Backend Intelligence Layer for content planning, Blueprint coverage, suitability scoring, Redis/Celery automation, and future adaptive serving/scoring systems into one coherent coding-practice platform.

See: [Portfolio and Engineering Highlights](docs/15-portfolio-engineering-highlights.md)

## Pre-deployment security

Codiquiz includes a pre-deployment security readiness page at `/admin/security` for owner/admin users. It checks runtime environment, CORS origins, secure admin cookies, demo restrictions, Developer/Test Lab availability, provider defaults, and public tracking privacy settings without exposing secret values.

See `docs/deployment/PREDEPLOY_SECURITY_CHECKLIST.md` before opening `codiquiz.com` and `admin.codiquiz.com` publicly.
