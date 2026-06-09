# Product Overview

Codiquiz is an AI-powered coding quiz platform focused on deep, taxonomy-based programming practice. The project is currently in early alpha: the public practice flows, core admin workflows, AI generation pipeline, quality systems, Blueprint planning, model/cost management, and preview deployment foundation are live enough to demonstrate the product direction, while production rollout, learner accounts, scoring, semantic similarity, and advanced learning features are still evolving.

## Core product idea

Codiquiz combines five major areas:

1. **Public coding practice** — users practice programming concepts through Quick Practice, Custom Practice, Try Concept, public quizzes, and taxonomy-driven entry points.
2. **User progress systems** — registered learners will later receive persistent attempts, scores, mastery profiles, and adaptive recommendations.
3. **Admin content operations** — admins manage taxonomy, quizzes, question banks, AI drafts, generation batches, and coverage gaps.
4. **Backend intelligence layer** — concept importance, suitability, difficulty weights, and Blueprint gaps decide what should be generated next.
5. **AI-assisted content platform** — OpenAI generates candidate questions, while Codiquiz validates, fingerprints, reviews, measures cost/quality, and decides what becomes approved content.

## Why this matters

AI can generate many questions quickly, but raw AI output is not enough for a serious learning platform. Codiquiz adds the missing systems around generation:

- taxonomy targeting,
- prompt rules,
- draft staging,
- duplicate detection,
- concept importance scoring,
- suitability scoring,
- Blueprint default targets and coverage,
- review workflow,
- async automation,
- future semantic similarity,
- future scoring/mastery analytics.

## Product areas

### Public practice

The public side is designed for learners and developers who want focused coding practice.

Current public features:

- Practice landing page.
- Quick Practice for fast sessions.
- Custom Practice for taxonomy-targeted sessions.
- Try Concept mode for concept-level practice.
- Concept Finder with search, taxonomy paths, pagination, and approved-question counts.
- Python technology pages with taxonomy navigation and practice entry points.
- Public quiz list with technology filtering, promoted cards, coming-soon states, and technology badges/icons.
- Practice sessions with answer labels, feedback, result review, stop-session confirmation, and navigation protection.

Future public features will add registered progress, adaptive practice, mastery tracking, and stronger question selection based on user history.

### User accounts and progress

Codiquiz is designed to support both anonymous visitors and registered learners.

Planned user-system features:

- anonymous quick practice,
- registered learner accounts,
- persistent attempt history,
- seen-question tracking,
- difficulty-weighted scoring,
- ranking score,
- concept mastery,
- adaptive practice based on weak concepts.

### Admin platform

The admin side is the platform control center.

It supports:

- taxonomy management,
- question bank management,
- quiz technology/promoted/coming-soon configuration,
- question type mapping,
- suitability rule management,
- AI generation planning,
- AI draft review,
- Batch API lifecycle management,
- concept importance audit views,
- Blueprint coverage analysis and candidate queues,
- AI model profile visibility and editable profile-to-model mappings,
- model pricing catalog and cost comparison,
- Cost & Quality dashboard for generation results,
- `tiktoken`-based pre-generation estimates,
- Redis/Celery automation visibility,
- worker task-run history.

### Content platform

The content system is built around a simple rule:

> OpenAI generates candidates. Codiquiz decides what gets accepted.

Generated questions are not published automatically. They are stored as drafts, validated, checked for duplication and repetition, reviewed by an admin, and only then promoted to the approved question bank.

The newer model/cost layer makes this process measurable as well as controllable. Codiquiz can show which profile/model was used, estimate cost before a run, track actual provider usage after a run, and summarize cost per generated or approved question.

## Product positioning

Codiquiz is best described as:

> A service-oriented AI-assisted coding practice platform with a controlled question-generation pipeline, quality engine, Backend Intelligence Layer, Blueprint coverage system, and async automation.

It is not only:

- a quiz UI,
- an AI prompt wrapper,
- a CRUD admin panel,
- a random question generator.

The strongest value is the platform architecture around the question lifecycle: plan → generate → validate → review → approve → serve → score → improve.
