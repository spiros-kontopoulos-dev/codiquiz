# Product Overview

Codiquiz is an AI-powered coding quiz platform focused on deep, taxonomy-based programming practice. The project is currently in early alpha: the core admin, generation, quality, Blueprint, and automation systems are being built before the first public deployment.

The product goal is not simply to display random multiple-choice questions. Codiquiz aims to build a high-quality, planned, reviewable, and scalable question bank for programming technologies such as Python.

## Core product idea

Codiquiz combines three major areas:

1. **Public coding practice** — users practice programming concepts through structured coding questions.
2. **User progress systems** — registered learners will later receive persistent attempts, scores, mastery profiles, and adaptive recommendations.
3. **Admin content operations** — admins manage taxonomy, question banks, AI drafts, generation batches, and coverage gaps.
4. **Backend intelligence layer** — concept importance, suitability, difficulty weights, and Blueprint gaps decide what should be generated next.
5. **AI-assisted content platform** — OpenAI generates candidate questions, while Codiquiz validates, fingerprints, reviews, and decides what becomes approved content.

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

Current and planned features:

- homepage,
- technology pages,
- quick practice flow,
- taxonomy-based selection,
- single-choice coding questions,
- future custom practice builder,
- future adaptive practice based on weak concepts.

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
- question type mapping,
- suitability rule management,
- AI generation planning,
- AI draft review,
- Batch API lifecycle management,
- concept importance audit views,
- Blueprint coverage analysis and candidate queues,
- Redis/Celery automation visibility,
- worker task-run history.

### Content platform

The content system is built around a simple rule:

> OpenAI generates candidates. Codiquiz decides what gets accepted.

Generated questions are not published automatically. They are stored as drafts, validated, checked for duplication and repetition, reviewed by an admin, and only then promoted to the approved question bank.

## Product positioning

Codiquiz is best described as:

> A service-oriented AI-assisted coding practice platform with a controlled question-generation pipeline, quality engine, Backend Intelligence Layer, Blueprint coverage system, and async automation.

It is not only:

- a quiz UI,
- an AI prompt wrapper,
- a CRUD admin panel,
- a random question generator.

The strongest value is the platform architecture around the question lifecycle: plan → generate → validate → review → approve → serve → score → improve.
