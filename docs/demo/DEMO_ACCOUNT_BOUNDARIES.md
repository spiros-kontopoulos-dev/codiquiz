# Preview Demo Account Boundaries

## Purpose

The preview environment can be shown to other people without giving them owner-level access.

The demo/restricted account is intended for safe exploration only.

## Current intended roles

```text
owner
  Full trusted owner/admin access.

demo_viewer
  Restricted demo access for preview walkthroughs.
```

## Demo viewer should be allowed to

1. Log in to the admin preview environment.
2. View safe admin/demo pages.
3. Inspect high-level workflows and dashboards.
4. Browse Blueprint/coverage/admin data where safe.
5. Understand the product without changing important state.

## Demo viewer should not be allowed to

1. Create, edit, or delete admin users.
2. View secrets, keys, env values, or sensitive config.
3. Change provider/model settings.
4. Trigger large or expensive OpenAI generation runs.
5. Approve/reject/archive important content unless explicitly designed as demo-safe.
6. Delete batches, questions, taxonomy, or blueprint rules.
7. Perform destructive maintenance actions.
8. Access owner-only security panels.

## Manual verification checklist

Run this after permission changes:

```text
[ ] Owner can log in.
[ ] Owner-only pages work for owner.
[ ] Demo viewer can log in.
[ ] Demo viewer cannot create/edit users.
[ ] Demo viewer cannot see secrets.
[ ] Demo viewer cannot change AI provider settings.
[ ] Demo viewer cannot run dangerous/destructive actions.
[ ] Demo viewer receives disabled controls, hidden controls, or permission denied responses.
[ ] Logging out protects admin routes.
```

## SQL baseline check

```bash
cd <preview-vps-project-root>

docker compose --env-file .env.preview -f docker-compose.prod.yml exec postgres sh -lc '
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "
select id, email, role, is_active, created_at
from admin_users
order by id;
"
'
```

Expected for preview:

```text
At least one active owner.
At least one active demo_viewer if demo access is enabled.
No unplanned active high-privilege accounts.
```

## Recommended handling

Use `demo_viewer` for public/recruiter demos.
Use `owner` only for private trusted demos or real maintenance.

Before any important demo, create a fresh backup:

```bash
cd <preview-vps-project-root>
./deploy/scripts/backup_postgres.sh
```
