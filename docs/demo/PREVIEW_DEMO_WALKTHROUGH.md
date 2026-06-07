# Codiquiz Preview Demo Walkthrough

## Purpose

This walkthrough is the repeatable path for showing the Codiquiz preview environment to recruiters, employers, collaborators, or trusted testers.

Use the preview environment only:

```text
https://preview.codiquiz.com
https://admin.preview.codiquiz.com/login
```

## 1. Public product overview

Open:

```text
https://preview.codiquiz.com
```

Explain:

```text
Codiquiz is an AI-powered coding quiz platform. The public site shows the learner-facing direction, while the admin system contains the deeper AI generation, taxonomy, quality, and planning workflows.
```

Show:

1. Homepage hero.
2. Technology carousel or technology entry points.
3. Python technology page.
4. Taxonomy navigation: domain → module → topic → subtopic.
5. Public routing refresh/share behavior.

Mention:

```text
The current preview focuses on the platform foundation, taxonomy depth, admin workflows, and AI generation pipeline. Full learner accounts, scoring, and production launch are later milestones.
```

## 2. Admin separation

Open:

```text
https://admin.preview.codiquiz.com/login
```

Explain:

```text
The admin app is separated onto its own preview admin subdomain. Demo access is restricted, and owner-only actions remain protected.
```

For public/recruiter demos, prefer the demo viewer account unless you intentionally need owner-only actions.

## 3. Blueprint Coverage

Show:

1. Summary/work-queue blocks.
2. Recommended targets.
3. Strong/secondary suitability filters.
4. Coverage gaps.
5. Priority/generation candidate concepts.

Explain:

```text
The Blueprint system decides what the question bank should contain. It combines concept importance, question-type suitability, difficulty guidance, existing approved questions, and pending drafts to prioritize what to generate next.
```

Good points to mention:

1. This avoids random AI generation.
2. The platform knows where coverage is missing.
3. Admins can review and adjust targets.
4. Weak-fit combinations remain visible but are not automatically recommended.

## 4. AI Generation Create

Show:

1. Technology/domain/module/topic/subtopic/concept selection.
2. Suitability-aware question type selector.
3. Difficulty guidance.
4. Use Blueprint candidates.
5. Plan preview rows.

Explain:

```text
Generation is controlled by taxonomy and Blueprint planning. The admin does not simply ask AI for random questions; it creates structured generation plans with target paths, question types, difficulty, and validation.
```

Avoid triggering expensive or unnecessary real OpenAI runs during casual demos unless the owner intentionally wants to show a live generation.

## 5. AI Generation Settings / Batch API readiness

Show:

1. Provider/model profile mapping.
2. Batch API readiness.
3. Worker/task history.
4. Scheduler/automation status.
5. Provider safety check.

Explain:

```text
The platform supports normal API generation, Batch API workflows, retry/chunk tracking, worker automation, and provider safety checks. OpenAI keys are isolated to the generation services.
```

## 6. Generated questions / review quality

Show:

1. Questions page.
2. AI Generation detail page if available.
3. Draft/review flow if safe to show.
4. Duplicate/fingerprint/similarity warnings if available.

Explain:

```text
Generated content is staged and reviewed before entering the approved question bank. The quality pipeline includes normalization, duplicate detection, taxonomy mapping, and admin approval.
```

## 7. Current alpha honesty

Say clearly:

```text
This is an early-alpha preview. The core architecture and admin AI-generation systems are live, but full public learner accounts, scoring, production deployment, and long-term learning features are future work.
```

## Demo do-not-do list

Avoid during normal public demos:

1. Showing raw `.env` values or secrets.
2. Showing OpenAI API keys.
3. Triggering many real OpenAI generations.
4. Using owner account for untrusted viewers.
5. Editing/deleting production-like data without a fresh backup.
6. Claiming the preview is the final production launch.

## Quick final line

Use this as the closing summary:

```text
Codiquiz shows that I can build a full-stack AI product with real deployment, admin workflows, taxonomy modeling, background workers, provider integration, validation systems, and production-style operations.
```
