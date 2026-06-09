# Codiquiz Recruiter Demo Presentation Flow

This document gives a focused 10-15 minute demo path for recruiters, engineering managers, and technical reviewers.

## One-sentence pitch

Codiquiz is an AI-powered coding quiz platform with a backend intelligence layer that plans, generates, reviews, de-duplicates, and prioritizes programming questions instead of simply wrapping an LLM.

## 30-second opening

Codiquiz is built as a portfolio-level engineering project. It combines a public coding-practice product with a protected admin platform for taxonomy management, AI question generation, draft review, duplicate control, Blueprint coverage planning, suitability scoring, model/cost management, async automation, and deployment operations.

The important point is that Codiquiz does not publish AI output directly. It uses a controlled backend workflow: plan, generate, validate, fingerprint, stage, review, approve, measure cost/quality, and only then serve questions.

## Recommended demo order

### 1. Public homepage

Open the public preview and show the product direction: coding practice, technology pages, Python focus, and early-alpha status.

Talking point:

> The public side is intentionally clean. The complexity is hidden in the admin/backend systems that build and protect the question bank.

### 2. Public practice and taxonomy flow

Show the Python technology/taxonomy page, then show how users can move into practice.

Recommended path:

1. Python technology page.
2. Taxonomy depth: domain → module → topic → subtopic → concept.
3. Quick Practice.
4. Custom Practice with taxonomy prefill.
5. Try Concept or Concept Finder.
6. Public quiz list with technology filtering.

Talking point:

> The public side is not just random quizzes. Practice can start broad or narrow down to one Python concept, while the admin system controls what content is approved and available.

### 3. Admin login and dashboard

Log into the protected admin preview.

Talking point:

> The admin side is the operational control center for taxonomy, generation, review, quality, Blueprint planning, and automation.

### 4. Blueprint Coverage

Show Blueprint Coverage and work queues.

Talking point:

> The Blueprint system answers: what should the question bank contain, where are the gaps, and what should AI generate next?

### 5. Backend Intelligence Layer

Show or explain concept importance, suitability mapping, difficulty weighting, and priority candidates.

Talking point:

> Codiquiz now has an intelligence layer that ranks missing coverage using educational importance, question-type suitability, difficulty fit, approved count, and pending drafts.

### 6. AI Generation Create

Show loading Blueprint candidates into a generation plan.

Talking point:

> Generation is not just a prompt box. The admin selects planned targets driven by coverage and suitability signals.

### 7. Draft review workflow

Show staged drafts, statuses, review/approve/reject flow, and generated question structure.

Talking point:

> Generated questions enter the system as drafts first. They are not automatically published.

### 8. Quality controls

Show duplicate warnings, fingerprints, avoid-list/repetition controls, or Similarity Review if available.

Talking point:

> The backend protects the approved bank from repeated or near-identical generated questions.

### 9. Batch/async automation and model/cost controls

Show Batch API readiness, lifecycle status, worker task history, automation settings, model profile settings, or Cost & Quality if available.

Talking point:

> Redis/Celery and scheduled workers support long-running generation and background lifecycle work. The admin can also inspect model profiles, edit profile-to-model mappings, compare model pricing, estimate generation cost before running, and review cost/quality outcomes after generation.

### 10. Deployment/security foundation

Mention the isolated preview environment, HTTPS, firewall, no public DB/Redis/API ports, backups, restore checklist, and demo-viewer restrictions.

Talking point:

> The project is not only local code. It has a live isolated preview with deployment, backup, and security foundations.

## Technical highlights to mention

- FastAPI backend with SQLAlchemy/Alembic.
- PostgreSQL as source of truth.
- React + TypeScript public/admin UI.
- Docker Compose deployment.
- Redis/Celery worker automation.
- OpenAI normal API and Batch API integration.
- AI draft staging and admin review.
- Deterministic duplicate/fingerprint system.
- Blueprint coverage planning.
- Concept importance and suitability scoring.
- Public Quick Practice, Custom Practice, Try Concept, and Concept Finder flows.
- Public quiz technology filtering and promoted/coming-soon quiz controls.
- Editable AI model profile mappings.
- OpenAI model pricing catalog and `tiktoken` pre-generation estimates.
- Cost & Quality dashboard for generation outcomes.
- Preview deployment with HTTPS, backups, smoke tests, and restricted demo user.

## What to avoid showing

Do not show:

- environment files,
- secret values,
- database passwords,
- OpenAI keys,
- destructive owner-only actions,
- raw server credentials,
- private source code files unless intentionally discussed.

## Short portfolio framing

Use this phrasing when explaining the project:

> Codiquiz demonstrates backend architecture, AI integration, data modeling, async automation, quality systems, and deployment ownership. The interesting part is not that it calls OpenAI, but that it wraps generation inside a controlled content-planning and review engine.

## Longer portfolio framing

Codiquiz is a service-oriented AI-assisted coding practice platform. It has a public learner-facing side and a protected admin system. The backend models a deep Python taxonomy, plans desired question coverage through Blueprint rules, scores concepts by importance, maps concepts to suitable question types, generates AI drafts through normal and batch provider workflows, validates and fingerprints generated content, flags duplicates and repetitive patterns, and exposes review/admin workflows before approval.

The project is designed to evolve toward semantic similarity, adaptive serving, learner accounts, scoring, mastery tracking, and production deployment.
