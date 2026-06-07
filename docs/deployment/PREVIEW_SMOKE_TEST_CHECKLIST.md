# Codiquiz Preview Smoke-Test Checklist

Use this checklist after:

```text
new preview deployment
manual backup setup
manual restore
Docker rebuild/restart
DNS/HTTPS/Caddy changes
admin/auth changes
```

Preview URLs:

```text
Public: https://preview.codiquiz.com
Admin:  https://admin.preview.codiquiz.com
Health: https://preview.codiquiz.com/api/health
Health: https://admin.preview.codiquiz.com/api/health
```

---

## 1. Infrastructure health

```bash
cd <preview-vps-project-root>

docker compose --env-file .env.preview -f docker-compose.prod.yml ps
curl -i https://preview.codiquiz.com/api/health
curl -i https://admin.preview.codiquiz.com/api/health
```

Pass criteria:

```text
[ ] All expected containers are up.
[ ] Public health returns HTTP 200.
[ ] Admin health returns HTTP 200.
[ ] Health JSON says database=connected.
[ ] Health JSON says redis=connected.
```

Expected containers:

```text
codiquiz_caddy
codiquiz_frontend
codiquiz_postgres
codiquiz_redis
codiquiz_quiz_api
codiquiz_question_service
codiquiz_quiz_worker
codiquiz_quiz_beat
codiquiz_question_worker
```

---

## 2. HTTPS and routing

Browser checks:

```text
[ ] https://preview.codiquiz.com opens without certificate warnings.
[ ] https://admin.preview.codiquiz.com opens without certificate warnings.
[ ] https://admin.preview.codiquiz.com/login opens the clean admin login page.
[ ] /admin/login redirects or normalizes to /login on the admin subdomain.
[ ] Refreshing an admin route does not show a Caddy/404 error.
```

---

## 3. Public site smoke test

```text
[ ] Homepage loads.
[ ] Technology carousel/section renders.
[ ] Python technology page opens.
[ ] Taxonomy navigation opens at least one module/topic/subtopic route.
[ ] Browser console has no repeated API/network failures.
[ ] Public site does not expose admin-only controls.
```

---

## 4. Admin owner smoke test

```text
[ ] Open https://admin.preview.codiquiz.com/login.
[ ] Owner/admin login works.
[ ] Admin dashboard or default admin page loads.
[ ] Blueprint Coverage loads rows.
[ ] Blueprint Rules page shows the global base rule.
[ ] AI Generation Create page loads.
[ ] AI Generation Detail page loads for a recent batch if available.
[ ] AI Generation Settings page loads.
[ ] Concept/Taxonomy admin pages load.
[ ] Logout works.
```

Blueprint base rule expected:

```text
scope_level = global
scope_key = global
target_count = 2
priority = 0
is_active = true
```

---

## 5. Demo/restricted user permission verification

Use the real demo/restricted account once it exists.

```text
[ ] Demo user can log in only through the intended demo/admin route.
[ ] Demo user cannot access owner-only user management.
[ ] Demo user cannot create owner/admin users.
[ ] Demo user cannot edit production/preview secrets.
[ ] Demo user cannot change global system settings unless explicitly intended.
[ ] Demo user cannot delete core taxonomy/content unless explicitly intended.
[ ] Demo user cannot run destructive restore/maintenance actions.
[ ] Demo user sees only the showcase/admin-demo sections intended for public demonstration.
[ ] Direct URL attempts to restricted pages return blocked/unauthorized behavior.
```

Recommended direct URL checks:

```text
/admin/users or equivalent user-management route
/admin/settings or equivalent system-settings route
/admin/blueprint/rules if rules are owner-only
/admin/ai-generation/settings if provider settings are owner-only
```

Adjust the exact paths to the current frontend routes.

---

## 6. Visitor tracking verification

Browser flow:

```text
[ ] Open a private/incognito browser window.
[ ] Visit https://preview.codiquiz.com.
[ ] Visit one technology/taxonomy page.
[ ] Refresh once.
[ ] Confirm visitor tracking appears in the expected admin/reporting area or DB table.
```

Database discovery helper:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml exec -T postgres \
  psql -U quiz_user -d quiz_db -c "\\dt *visitor*"
```

If the tracking table name is not obvious, inspect likely analytics tables:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml exec -T postgres \
  psql -U quiz_user -d quiz_db -c "\\dt *analytics*"
```

Pass criteria:

```text
[ ] A preview visit can be observed.
[ ] Tracking does not create server errors.
[ ] Tracking does not require exposing private user data in logs.
```

---

## 7. OpenAI preview generation smoke test

Only run this when you intentionally want to spend preview OpenAI credits.

```text
[ ] question-service can read the OpenAI preview key.
[ ] question-worker can read the OpenAI preview key.
[ ] A tiny generation batch can be created.
[ ] Generated drafts enter pending_review or the expected review state.
[ ] No OpenAI key is visible in frontend/network responses/logs.
```

Keep the test small:

```text
1-2 questions only
preview/demo data only
no production key
```

---

## 8. Backup smoke test

```bash
cd <preview-vps-project-root>
./deploy/scripts/backup_postgres.sh
```

Validate newest backup:

```bash
BACKUP_FILE=$(ls -1t <preview-postgres-backup-dir>/*.sql.gz | head -n 1)
gzip -t "$BACKUP_FILE"
sha256sum -c "${BACKUP_FILE}.sha256"
ls -lh "$BACKUP_FILE" "${BACKUP_FILE}.sha256"
```

Pass criteria:

```text
[ ] Backup command exits successfully.
[ ] Backup file exists.
[ ] Checksum file exists.
[ ] gzip validation succeeds.
[ ] sha256 validation succeeds.
[ ] Backup file is not in the Git repo.
```

---

## 9. Log review

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 quiz-api | grep -i "error\|traceback\|exception" || echo "no recent quiz-api errors"
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 question-service | grep -i "error\|traceback\|exception" || echo "no recent question-service errors"
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 question-worker | grep -i "error\|traceback\|exception" || echo "no recent question-worker errors"
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 caddy | grep -i "error\|traceback\|exception" || echo "no recent caddy errors"
```

Pass criteria:

```text
[ ] No repeated app tracebacks.
[ ] No repeated database connection failures.
[ ] No repeated Redis connection failures.
[ ] No persistent Caddy 502 errors after rebuild has completed.
```

---

## 10. Final sign-off

```text
[ ] Infrastructure healthy.
[ ] Public site healthy.
[ ] Admin owner flow healthy.
[ ] Demo permissions verified or explicitly marked pending.
[ ] Visitor tracking verified or explicitly marked pending.
[ ] Backup verified.
[ ] Logs reviewed.
[ ] Safe update workflow understood.
```

Result:

```text
Codiquiz preview is live, usable, backed up, and showcase-ready.
```
