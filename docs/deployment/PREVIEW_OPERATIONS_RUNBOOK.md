# Public-Safe Preview Operations Overview

This document is a public-safe version of the preview operations notes. It keeps the operational model visible for portfolio/review purposes, but exact private secrets, passwords, personal accounts, and machine-specific values are not included.

# Codiquiz Preview Operations Runbook

This runbook is for the isolated preview/demo VPS.

```text
Preview public: https://preview.codiquiz.com
Preview admin:  https://admin.preview.codiquiz.com
Project path:   <preview-vps-project-root>
Env file:       .env.preview
Compose file:   docker-compose.prod.yml
```

The preview VPS is not the future production VPS. Do not reuse preview data, preview secrets, or preview OpenAI keys for production.

---

## Compose command prefix

Most commands start from the project root:

```bash
cd <preview-vps-project-root>
```

Compose command:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml
```

---

## Daily quick health check

```bash
cd <preview-vps-project-root>

docker compose --env-file .env.preview -f docker-compose.prod.yml ps

curl -i https://preview.codiquiz.com/api/health
curl -i https://admin.preview.codiquiz.com/api/health
```

Expected health shape:

```json
{"status":"ok","service":"quiz-api","database":"connected","redis":"connected"}
```

---

## Manual Postgres backup

```bash
cd <preview-vps-project-root>
./deploy/scripts/backup_postgres.sh
```

Backups are stored outside the repo:

```text
<preview-postgres-backup-dir>
```

List backups:

```bash
ls -lh <preview-postgres-backup-dir>/*.sql.gz
```

Validate the newest backup:

```bash
BACKUP_FILE=$(ls -1t <preview-postgres-backup-dir>/*.sql.gz | head -n 1)
gzip -t "$BACKUP_FILE"
sha256sum -c "${BACKUP_FILE}.sha256"
```

---

## Safe update workflow

Use this when applying a new committed patch to the preview VPS.

### 1. Confirm local work is committed and pushed

Local Windows:

```powershell
git status
git push origin main
```

### 2. SSH to preview and enter project

```bash
cd <preview-vps-project-root>
```

### 3. Capture current commit

```bash
git rev-parse --short HEAD
```

Copy the output somewhere safe. It is the quick rollback commit.

### 4. Take a backup before update

```bash
./deploy/scripts/backup_postgres.sh
```

### 5. Pull exact GitHub main state

```bash
git fetch origin
git reset --hard origin/main
```

### 6. Rebuild/restart containers

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml up -d --build
```

### 7. Verify

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml ps
curl -i https://preview.codiquiz.com/api/health
curl -i https://admin.preview.codiquiz.com/api/health
```

Then run:

```text
docs/deployment/PREVIEW_SMOKE_TEST_CHECKLIST.md
```

---

## Rollback workflow

Use this only if the new deployment is clearly broken.

```bash
cd <preview-vps-project-root>

git reset --hard <previous-good-commit>
docker compose --env-file .env.preview -f docker-compose.prod.yml up -d --build
```

Then verify:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml ps
curl -i https://preview.codiquiz.com/api/health
curl -i https://admin.preview.codiquiz.com/api/health
```

If the issue came from a destructive database migration or bad data change, code rollback may not be enough. Use the restore checklist:

```text
deploy/scripts/restore_postgres_preview.md
```

---

## Logs

All services:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120
```

Service logs:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 caddy
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 frontend
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 quiz-api
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 question-service
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 postgres
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 redis
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 quiz-worker
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 quiz-beat
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=120 question-worker
```

Follow one service:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml logs -f quiz-api
```

Search recent errors:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 quiz-api | grep -i "error\|traceback\|exception" || echo "no recent quiz-api errors"
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 question-service | grep -i "error\|traceback\|exception" || echo "no recent question-service errors"
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 question-worker | grep -i "error\|traceback\|exception" || echo "no recent question-worker errors"
docker compose --env-file .env.preview -f docker-compose.prod.yml logs --tail=300 caddy | grep -i "error\|traceback\|exception" || echo "no recent caddy errors"
```

Expected harmless case:

```text
Caddy may show temporary 502/connect refused lines during app rebuilds or container restarts.
```

These are only a problem if they continue after all app containers are healthy.

---

## Docker disk checks

Check disk:

```bash
df -h
sudo du -sh /var/lib/docker || true
sudo du -sh <preview-postgres-backup-dir> || true
```

Docker usage:

```bash
docker system df
```

Low-risk cleanup:

```bash
docker builder prune -f --filter "until=168h"
docker image prune -f
```

More aggressive cleanup after verification:

```bash
docker container prune -f
docker network prune -f
```

Avoid on preview unless you are intentionally deleting data:

```bash
docker volume prune
```

Do not run prune commands with `--volumes` on the preview VPS unless you have verified backups and you intentionally want to remove unused Docker volumes.

---

## Caddy reload

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml exec caddy \
  caddy reload --config /etc/caddy/Caddyfile
```

---

## Database inspection helpers

Open psql:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml exec postgres \
  psql -U quiz_user -d quiz_db
```

Quick counts:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml exec -T postgres \
  psql -U quiz_user -d quiz_db -c "select count(*) as concepts from concepts;"
```

Discover visitor-related tables if needed:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml exec -T postgres \
  psql -U quiz_user -d quiz_db -c "\\dt *visitor*"
```

---

## Preview protection rules

```text
Do not expose Postgres, Redis, quiz-api, question-service, or frontend container ports publicly.
Do not commit .env.preview.
Do not commit backups.
Do not reuse preview secrets in production.
Do not run destructive restore commands without first creating a safety backup.
Do not use demo accounts with owner/admin-destructive permissions.
```
