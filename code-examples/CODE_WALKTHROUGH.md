# Codiquiz Code Walkthrough

The files in `code-examples/` are intentionally partial, but they are not random snippets. They are arranged to show how the main Codiquiz workflows connect across frontend, FastAPI, background workers, AI services, quality checks, and the Backend Intelligence Layer.

## 1. Public visit tracking workflow

A recruiter or visitor opens the live early-alpha public site.

Flow:

```text
React public layout
→ PublicVisitTracker
→ public traffic API client
→ FastAPI public traffic router
→ public_visitor_sessions / public_visit_events
→ admin public traffic page
```

Relevant excerpts:

- `frontend/react/public_visit_tracker.tsx`
- `frontend/react/admin_public_traffic_page_excerpt.tsx`
- `backend/fastapi/public_traffic_router_excerpt.py`

What this demonstrates:

- Non-blocking frontend analytics.
- Privacy-aware visitor tracking.
- Admin visibility into preview/demo visits.

## 2. Blueprint-driven AI generation workflow

An admin wants to generate useful questions, not random AI output. The UI requests Blueprint candidates, converts them into generation-plan rows, previews the plan, then starts a controlled generation batch.

Flow:

```text
Admin AI Generation Create page
→ Blueprint API client
→ /admin/blueprint/generation-candidates
→ Blueprint generation candidate service
→ priority service
→ AI generation plan preview
→ AI generation batch create/run endpoints
→ execution jobs / question-service calls
```

Relevant excerpts:

- `frontend/react/admin_ai_generation_blueprint_flow_excerpt.tsx`
- `frontend/react/blueprint_api_client_excerpt.ts`
- `backend/fastapi/blueprint_coverage_router_excerpt.py`
- `backend/blueprint-intelligence/generation_candidate_service_excerpt.py`
- `backend/blueprint-intelligence/priority_service.py`
- `backend/ai-generation/planner_allocation_excerpt.py`
- `backend/fastapi/ai_generation_router_workflow_excerpt.py`

What this demonstrates:

- The AI generator is guided by coverage gaps and educational priority.
- Blueprint metadata travels from backend ranking to UI plan rows.
- Manual plan edits can coexist with intelligent candidate suggestions.

## 3. Backend Intelligence Layer workflow

Codiquiz decides what the question bank should contain by combining concept importance, question-type suitability, difficulty fit, and existing coverage.

Flow:

```text
Taxonomy concept seeds
→ concept importance scores
→ suitability seed rules
→ default Blueprint target counts
→ priority-scored coverage rows
→ top generation candidates
```

Relevant excerpts:

- `backend/taxonomy-seeding/concept_importance_seed_excerpt.py`
- `backend/taxonomy-seeding/suitability_seed_excerpt.py`
- `backend/blueprint-intelligence/default_targets_excerpt.py`
- `backend/blueprint-intelligence/priority_service.py`
- `backend/blueprint-intelligence/generation_candidate_service_excerpt.py`
- `backend/models/sqlalchemy_intelligence_models_excerpt.py`

What this demonstrates:

- Codiquiz is not only an OpenAI wrapper.
- It has a backend planning layer that decides what should be generated and why.
- The content plan is explainable through importance, suitability, and coverage gaps.

## 4. AI execution + quality workflow

Generated questions are not immediately trusted. They are staged, validated, fingerprinted, checked for duplicates/repetition, and reviewed before approval.

Flow:

```text
AI generation batch
→ execution jobs and chunking
→ question-service structured OpenAI response
→ Pydantic validation contract
→ staged draft question
→ signature and duplicate checks
→ avoid-list / anti-repetition hints
→ admin draft review
```

Relevant excerpts:

- `backend/ai-generation/execution_chunking_and_cost_rollup_excerpt.py`
- `backend/question-service/openai_structured_generation_excerpt.py`
- `backend/pydantic/question_service_generation_contract_excerpt.py`
- `backend/quality-engine/signature_service.py`
- `backend/quality-engine/duplicate_service_excerpt.py`
- `backend/quality-engine/avoid_list_service.py`

What this demonstrates:

- Durable execution jobs for normal and Batch API generation.
- Structured AI output boundaries.
- Deterministic quality checks before content reaches the approved bank.

## 5. Admin/demo safety workflow

The public preview includes a restricted demo account. The account can view the admin surface but cannot perform destructive or owner-only actions.

Flow:

```text
Admin login
→ admin auth context
→ protected admin route
→ backend role checks
→ demo-viewer write restrictions
→ admin security readiness page
```

Relevant excerpts:

- `frontend/react/protected_admin_route_excerpt.tsx`
- `backend/security/demo_viewer_permissions_excerpt.py`
- `backend/fastapi/security_readiness_excerpt.py`

What this demonstrates:

- The preview is safe to show publicly.
- Demo permissions are enforced both in the UI and backend.
- Provider/key safety is visible through admin readiness checks.

## 6. Async automation workflow

Long-running or scheduled operations are handled by Redis/Celery workers instead of blocking admin requests.

Flow:

```text
Admin action or scheduled scanner
→ Celery task wrapper
→ batch lifecycle scan
→ provider status/collect/reconcile actions
→ task-run logging
→ admin visibility
```

Relevant excerpts:

- `backend/async-workers/batch_lifecycle_worker_excerpt.py`
- `backend/ai-generation/execution_chunking_and_cost_rollup_excerpt.py`
- `infrastructure/docker-compose.example.yml`

What this demonstrates:

- Separation between web requests and background lifecycle work.
- Production-style async architecture with task-run observability.
- A path toward larger generation automation without making the admin UI wait.
