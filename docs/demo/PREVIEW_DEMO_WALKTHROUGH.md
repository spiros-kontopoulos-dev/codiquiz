# Codiquiz Preview Demo Walkthrough

## Purpose

This walkthrough is the repeatable path for showing the Codiquiz preview environment to recruiters, employers, collaborators, or trusted testers.

Use the preview environment only:

- Public preview: [preview.codiquiz.com](https://preview.codiquiz.com)
- Admin demo access: [admin.preview.codiquiz.com/admin/demo-access](https://admin.preview.codiquiz.com/admin/demo-access)

## 1. Public product overview

Open: [preview.codiquiz.com](https://preview.codiquiz.com)

Explain:

```text
Codiquiz is an AI-powered coding quiz platform. The public site shows the learner-facing direction, while the admin system contains the deeper AI generation, taxonomy, quality, and planning workflows.
```

Show:

1. Homepage hero.
2. Technology carousel or technology entry points.
3. Python technology page.
4. Taxonomy navigation: domain → module → topic → subtopic → concept.
5. Public routing refresh/share behavior.
6. Practice landing page.
7. Quick Practice.
8. Custom Practice from a taxonomy path.
9. Try Concept or Concept Finder.
10. Public quiz list with technology filtering.

Mention:

```text
The current preview focuses on the public practice experience, taxonomy depth, admin workflows, and AI generation pipeline. Full learner accounts, scoring, and final production launch are later milestones.
```

## 2. Admin separation

Open: [admin.preview.codiquiz.com/admin/demo-access](https://admin.preview.codiquiz.com/admin/demo-access)

Explain:

```text
The admin app is separated onto its own preview admin subdomain. The demo access page provides a controlled entry point for recruiter/visitor previews, while owner-only actions remain protected.
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
2. Editable profile-to-model settings.
3. Model pricing catalog and relative cost comparison.
4. Cost estimate before generation.
5. Batch API readiness.
6. Worker/task history.
7. Scheduler/automation status.
8. Provider safety check.

Explain:

```text
The platform supports normal API generation, Batch API workflows, retry/chunk tracking, worker automation, and provider safety checks. Model choices are managed through admin-readable profiles, and the system can estimate costs before generation while tracking actual usage after generation.
```

If useful, show the Cost & Quality dashboard:

```text
This dashboard summarizes generated drafts, approvals, rejections, pending review, duplicate warnings, cost per generated question, cost per approved question, and performance by model/profile.
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
This is an early-alpha preview. The public practice flows, taxonomy-driven question experience, admin AI-generation systems, cost/model controls, and preview deployment foundation are live, but full learner accounts, scoring, final production deployment, and long-term learning features are future work.
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
