# Codiquiz Code Examples

This folder contains selected sanitized excerpts from the private Codiquiz codebase.

The goal is to show implementation style and system design without publishing the complete application source. These examples are intentionally partial and are not expected to run as a standalone project.

## What is included

### Backend / FastAPI

- `backend/fastapi/public_traffic_router_excerpt.py` — anonymous public visitor/session tracking, source normalization, privacy-aware IP hashing, and admin traffic summaries.
- `backend/fastapi/security_readiness_excerpt.py` — deployment-readiness checks for CORS, cookies, provider defaults, bootstrap owner cleanup, test-lab exposure, and visitor privacy.

### Backend / Pydantic contracts

- `backend/pydantic/ai_generation_plan_schema_excerpt.py` — normalized AI generation planning request shape used by admin planning and backend validation.
- `backend/pydantic/question_service_generation_contract_excerpt.py` — question-service generation request/response contracts and strict multiple-choice validation.

### Backend / AI generation

- `backend/ai-generation/planner_allocation_excerpt.py` — generation-plan allocation and strategy validation logic.
- `backend/ai-generation/execution_chunking_and_cost_rollup_excerpt.py` — normal API vs Batch API chunking and token/cost rollups.
- `backend/question-service/openai_structured_generation_excerpt.py` — structured OpenAI response calls, Batch API JSONL construction, schema validation, and usage extraction.
- `backend/question-service/prompt_rules_excerpt.py` — prompt construction rules for model profile, difficulty, question type, generation mode, and avoid-list hints.

### Backend Intelligence Layer

- `backend/blueprint-intelligence/priority_service.py` — priority scoring for deciding which Blueprint gaps should be generated next.
- `backend/blueprint-intelligence/generation_candidate_service_excerpt.py` — conversion of ranked coverage rows into AI-generation plan items.
- `backend/blueprint-intelligence/default_targets_excerpt.py` — default target calculation from concept importance, suitability, difficulty fit, and coverage gaps.

### Backend Quality Engine

- `backend/quality-engine/signature_service.py` — deterministic prompt/code/answer/full-question signatures.
- `backend/quality-engine/avoid_list_service.py` — compact avoid-list hints for preventing repeated AI output patterns.
- `backend/quality-engine/duplicate_service_excerpt.py` — duplicate warning collection, source policy, warning formatting, and normalized similarity helpers.

### Async automation

- `backend/async-workers/batch_lifecycle_worker_excerpt.py` — Celery task wrapper for cautious Batch API lifecycle automation and task-run visibility.

### Data model / taxonomy seeds

- `backend/models/sqlalchemy_intelligence_models_excerpt.py` — SQLAlchemy model excerpts for concept importance, suitability, Blueprint rules, execution jobs, and AI drafts.
- `backend/taxonomy-seeding/concept_importance_seed_excerpt.py` — taxonomy seed example with inline concept importance scores.
- `backend/taxonomy-seeding/suitability_seed_excerpt.py` — reviewed concept-to-suitability profile mapping.

### Frontend / React + TypeScript

- `frontend/react/public_visit_tracker.tsx` — public visit/session source tracking that never blocks navigation.
- `frontend/react/blueprint_api_client_excerpt.ts` — typed Blueprint coverage/candidate client calls.

### Tests and infrastructure

- `tests/playwright/playwright_config_excerpt.ts` — representative Playwright config.
- `infrastructure/docker-compose.example.yml` — sanitized service topology example.
- `infrastructure/env.example` — safe example environment variables without secrets.

## What is intentionally excluded

- Complete private source tree.
- Real `.env` files and secrets.
- Real production Docker Compose configuration.
- Database dumps/backups.
- Full admin UI pages where a short excerpt is enough.
- Proprietary operational details that are not needed for portfolio review.
