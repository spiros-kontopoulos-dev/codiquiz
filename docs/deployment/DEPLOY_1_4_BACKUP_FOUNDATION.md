# DEPLOY 1.4 — Preview Backup Foundation

Status: patch ready, VPS validation pending.

DEPLOY 1.4 protects the isolated Codiquiz preview/demo VPS before it becomes the normal showcase environment.

Preview environment:

```text
Public preview: https://preview.codiquiz.com
Admin preview:  https://admin.preview.codiquiz.com
VPS role:       preview/demo only
Future prod:    separate VPS, separate DB, separate secrets
```

---

## What this patch adds

```text
deploy/scripts/backup_postgres.sh
  Manual Postgres backup helper for the preview VPS.

deploy/scripts/restore_postgres_preview.md
  Manual restore checklist for preview backups.

docs/deployment/PREVIEW_OPERATIONS_RUNBOOK.md
  Day-to-day preview operations, logs, disk cleanup, and update workflow.

docs/deployment/PREVIEW_SMOKE_TEST_CHECKLIST.md
  Manual smoke-test checklist after deployment, backup, restore, or updates.

docs/deployment/DEPLOY_1_4_BACKUP_FOUNDATION.md
  DEPLOY 1.4 overview and acceptance checklist.
```

No application runtime code is changed.

---

## One-time VPS setup

Run this on the preview VPS if the backup directory does not already exist:

```bash
sudo mkdir -p <preview-postgres-backup-dir>
sudo chown deploy:deploy <preview-postgres-backup-dir>
sudo chmod 750 <preview-postgres-backup-dir>
```

After applying the patch, make sure the script is executable on the VPS:

```bash
cd <preview-vps-project-root>
chmod +x deploy/scripts/backup_postgres.sh
```

If applying from Windows and committing the script to Git, also preserve the executable bit:

```bash
git update-index --chmod=+x deploy/scripts/backup_postgres.sh
```

---

## Manual backup command

Run from the preview VPS project root:

```bash
cd <preview-vps-project-root>
./deploy/scripts/backup_postgres.sh
```

Default backup output:

```text
<preview-postgres-backup-dir>/codiquiz_preview_postgres_YYYYMMDDTHHMMSSZ.sql.gz
<preview-postgres-backup-dir>/codiquiz_preview_postgres_YYYYMMDDTHHMMSSZ.sql.gz.sha256
```

The script validates that:

```text
.env.preview exists
docker-compose.prod.yml exists
Postgres is ready
pg_dump completes
gzip output is valid
the backup file is non-empty
a SHA-256 checksum file is created
retention cleanup runs only against Codiquiz preview backup filenames
```

---

## Backup script defaults

```text
Env file:         .env.preview
Compose file:     docker-compose.prod.yml
Postgres service: postgres
Database:         quiz_db
DB user:          quiz_user
Backup dir:       <preview-postgres-backup-dir>
Retention:        14 days
```

Safe overrides:

```bash
CODIQUIZ_BACKUP_RETENTION_DAYS=30 ./deploy/scripts/backup_postgres.sh
CODIQUIZ_BACKUP_DIR=/some/other/dir ./deploy/scripts/backup_postgres.sh
CODIQUIZ_DB_NAME=quiz_db CODIQUIZ_DB_USER=quiz_user ./deploy/scripts/backup_postgres.sh
```

---

## Retention policy

Initial preview policy:

```text
Keep local compressed Postgres backups for 14 days.
Delete only files matching:
  codiquiz_preview_postgres_*.sql.gz
  codiquiz_preview_postgres_*.sql.gz.sha256
```

This is enough for the preview/demo VPS foundation.

Recommended next hardening after DEPLOY 1.4:

```text
1. Add off-server backup copy.
2. Add an automated daily cron/systemd timer after one manual restore is tested.
3. Add backup monitoring/alerting.
```

Do not commit backups to Git.

---

## Optional cron after manual verification

Only enable automation after at least one manual backup has succeeded and the restore checklist has been reviewed.

```bash
crontab -e
```

Example daily backup at 03:15 UTC:

```cron
15 3 * * * cd <preview-vps-project-root> && /bin/bash deploy/scripts/backup_postgres.sh >> <preview-postgres-backup-dir>/backup.log 2>&1
```

Check cron output:

```bash
tail -n 120 <preview-postgres-backup-dir>/backup.log
```

---

## Manual restore checklist

Use:

```text
deploy/scripts/restore_postgres_preview.md
```

The restore checklist intentionally remains manual. Restores are destructive and should not be hidden behind a casual one-line script yet.

---

## DEPLOY 1.4 acceptance checklist

Mark these on the VPS:

```text
[ ] Patch files applied.
[ ] backup_postgres.sh executable on the VPS.
[ ] Backup directory exists and is owned by deploy.
[ ] One manual backup completed successfully.
[ ] Backup .sql.gz file exists.
[ ] Backup .sha256 file exists.
[ ] gzip -t succeeds against the backup file.
[ ] sha256sum -c succeeds.
[ ] Recent backup list is visible.
[ ] Restore checklist reviewed.
[ ] Runbook reviewed.
[ ] Smoke-test checklist completed.
[ ] Admin/demo permissions verified.
[ ] Visitor tracking verified on preview.
[ ] Safe update workflow documented and understood.
```

After these are done, the preview environment can be treated as:

```text
live
usable
backed up
showcase-ready
```
