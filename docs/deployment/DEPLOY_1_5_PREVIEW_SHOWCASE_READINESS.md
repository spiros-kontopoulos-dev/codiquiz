# DEPLOY 1.5 — Preview Showcase Polish / Public-Demo Readiness

## Status

Planned patch for the live preview environment.

This phase happens after DEPLOY 1.4, where the preview VPS was verified as live, backed up, smoke-tested, and protected by restricted demo permissions.

## Goal

Make the preview environment comfortable to show to other people without accidentally exposing unfinished production assumptions, owner-only controls, or confusing demo limitations.

The preview environment is still not final production. It is an isolated public/demo deployment used for showcasing, testing, and controlled admin demonstrations.

## Preview URLs

Public preview:

```text
https://preview.codiquiz.com
```

Admin preview:

```text
https://admin.preview.codiquiz.com/login
```

## Readiness definition

DEPLOY 1.5 is complete when:

```text
Public site is presentable and does not look broken.
Admin demo account is safe and clearly bounded.
Owner account still has full access.
Preview data is backed up before showcase sessions.
OpenAI/key/provider safety remains clean.
Visitor tracking continues to work.
The user has a repeatable walkthrough for recruiters/employers.
No public-facing copy claims this is final production.
```

## Scope

Included:

1. Public preview content check.
2. Admin demo walkthrough.
3. Demo account boundary check.
4. Public/recruiter showcase flow.
5. Optional README/public-documentation wording.
6. Final pre-demo verification checklist.

Not included:

1. Final production deployment.
2. New production VPS setup.
3. Major UI redesign.
4. New AI generation features.
5. Payment, scoring, user accounts, or learner progress systems.

## Pre-showcase command checks

Run this before an important demo:

```bash
cd <preview-vps-project-root>

./deploy/scripts/backup_postgres.sh

curl -fsS https://preview.codiquiz.com/api/health && echo
curl -fsS https://admin.preview.codiquiz.com/api/health && echo

docker compose --env-file .env.preview -f docker-compose.prod.yml ps

df -h
docker system df
```

Expected:

```text
Backup succeeds.
Both health endpoints return status ok.
All application containers are Up.
Disk usage is comfortable.
```

## Provider/key safety check

Run:

```bash
cd <preview-vps-project-root>

for svc in quiz-api quiz-worker quiz-beat question-service question-worker; do
  echo "=== $svc ==="
  docker compose --env-file .env.preview -f docker-compose.prod.yml exec -T "$svc" sh -lc '
    echo "AI_GENERATION_PROVIDER=${AI_GENERATION_PROVIDER:-not set}"
    if [ -n "${OPENAI_API_KEY:-}" ]; then
      echo "OPENAI_API_KEY=loaded"
    else
      echo "OPENAI_API_KEY=not set"
    fi
  '
done
```

Expected preview result:

```text
quiz-api: provider mock, key not set
quiz-worker: provider mock, key not set
quiz-beat: provider mock, key not set
question-service: key loaded
question-worker: key loaded
```

Do not put the OpenAI key into `quiz-api` just to silence warnings. The key belongs only in the generation services.

## Public preview browser checklist

1. Open `https://preview.codiquiz.com`.
2. Confirm homepage loads quickly.
3. Confirm the hero section communicates what Codiquiz is.
4. Confirm there are no obvious placeholder/broken sections.
5. Open the Python technology page.
6. Confirm taxonomy navigation works.
7. Confirm shareable routes still work after refresh.
8. Confirm public pages do not ask for admin login.
9. Confirm no obvious console/network errors for normal public browsing.
10. Confirm visitor tracking still writes rows.

## Admin preview browser checklist

Owner account:

1. Open `https://admin.preview.codiquiz.com/login`.
2. Log in as owner.
3. Open Blueprint Coverage.
4. Open AI Generation Create.
5. Use Blueprint candidates and confirm rows load.
6. Open AI Generation Settings.
7. Confirm provider safety/readiness is clean.
8. Open Questions.
9. Open an AI Generation detail page if available.
10. Confirm owner-only features still work.

Demo viewer account:

1. Log out from owner.
2. Log in as the demo/restricted account.
3. Confirm admin/demo pages can be viewed where intended.
4. Try destructive/write actions.
5. Confirm the actions are blocked, disabled, or return permission denied.
6. Confirm no secrets are visible.
7. Confirm the demo user cannot create users, change provider settings, or trigger dangerous owner-only actions.

## Recommended showcase order

Use this order when showing Codiquiz to another person:

```text
1. Public homepage
2. Python technology/taxonomy page
3. Explain admin is separate and protected
4. Admin login as demo viewer
5. Show Blueprint Coverage
6. Show AI Generation Create planning flow
7. Show AI Generation Settings / Batch API readiness
8. Show Questions / generated question quality
9. Explain current alpha scope and next production steps
```

Use owner login only for trusted private demos where write actions are needed.

## Demo messaging

Recommended wording:

```text
Codiquiz is an early-alpha AI-powered coding quiz platform. This preview environment demonstrates the architecture, taxonomy, admin workflows, AI generation pipeline, Blueprint planning, quality systems, and public technology pages. It is isolated from the future production environment and uses separate preview data and secrets.
```

Avoid wording like:

```text
Final production site
Fully launched public product
Complete learner platform
```

## Final DEPLOY 1.5 completion checklist

```text
[ ] Fresh backup created before showcase.
[ ] Health endpoints pass.
[ ] Public homepage reviewed.
[ ] Python technology page reviewed.
[ ] Admin owner login works.
[ ] Demo viewer login works.
[ ] Demo viewer is restricted.
[ ] Provider safety remains clean.
[ ] Visitor tracking verified.
[ ] Public/recruiter showcase flow reviewed.
[ ] Public docs/README wording does not overclaim production readiness.
```
