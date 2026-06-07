# DEPLOY 1.1 — Production Deployment Foundation

This chapter prepares the repository for a careful production deployment. It does not assume that the VPS has already been configured and it does not require editing production code directly on the server.

## What this patch adds

- `docker-compose.prod.yml` — production-oriented Docker Compose template.
- `.env.production.example` — production environment checklist/template.
- `frontend/Dockerfile.prod` and `frontend/nginx-spa.conf` — static production frontend build with SPA fallback.
- `deploy/caddy/Caddyfile` — Caddy reverse proxy template for `codiquiz.com`, `www.codiquiz.com`, and `admin.codiquiz.com`.
- This deployment guide and runbook notes.

The local development compose file remains unchanged.

## Production assumptions

Initial domains:

```text
codiquiz.com
www.codiquiz.com
admin.codiquiz.com
```

Traffic model:

```text
Internet → Caddy on 80/443 → frontend or quiz-api
```

API routing:

```text
https://codiquiz.com/api/* → quiz-api:8000/*
https://admin.codiquiz.com/api/* → quiz-api:8000/*
```

The Caddy `handle_path /api/*` rule strips the `/api` prefix before forwarding to FastAPI.

## Important security defaults

The production compose file publishes only Caddy ports:

```text
80/tcp
443/tcp
443/udp
```

It does not publish these internal services to the host:

```text
PostgreSQL
Redis
quiz-api
question-service
workers
```

The VPS firewall should still deny direct public access to database/cache ports. Compose isolation is not a substitute for firewall rules.

## Required production CORS value

Use exact HTTPS origins only:

```env
CODIQUIZ_CORS_ALLOWED_ORIGINS=https://codiquiz.com,https://www.codiquiz.com,https://admin.codiquiz.com
```

Do not use wildcard CORS in production.

## Environment file workflow

On the VPS, copy the example file:

```bash
cp .env.production.example .env.production
```

Then fill real values for:

```text
CADDY_ACME_EMAIL
POSTGRES_PASSWORD
DATABASE_URL
PUBLIC_VISIT_IP_HASH_SALT
OPENAI_API_KEY, if real provider use is needed
CODIQUIZ_BOOTSTRAP_OWNER_* for the first owner only
```

After the first owner account is confirmed, remove `CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD` from `.env.production` and redeploy.

## Manual deployment workflow

The first deployment can be manual and repo-driven:

```bash
git pull

docker compose --env-file .env.production -f docker-compose.prod.yml build

docker compose --env-file .env.production -f docker-compose.prod.yml up -d postgres redis

docker compose --env-file .env.production -f docker-compose.prod.yml up -d quiz-api question-service

docker compose --env-file .env.production -f docker-compose.prod.yml exec quiz-api alembic upgrade head

docker compose --env-file .env.production -f docker-compose.prod.yml up -d
```

Then verify:

```bash
curl -I https://codiquiz.com
curl https://codiquiz.com/api/health
curl https://admin.codiquiz.com/api/health
```

Also verify `/admin/security` from the admin UI after login.

## Migration rule

Schema changes must go through Alembic migrations:

```bash
docker compose --env-file .env.production -f docker-compose.prod.yml exec quiz-api alembic upgrade head
```

Do not let production startup silently create or mutate schema outside migrations.

## Logs

Start with Docker logs:

```bash
docker compose --env-file .env.production -f docker-compose.prod.yml logs -f caddy

docker compose --env-file .env.production -f docker-compose.prod.yml logs -f quiz-api

docker compose --env-file .env.production -f docker-compose.prod.yml logs -f quiz-worker quiz-beat question-worker
```

Future deployment chapters can add external log rotation, monitoring, and alerting.

## Backups

Before going live, add database backups and test restore. The minimum acceptable next step is a daily PostgreSQL dump stored outside the container volume, plus a manual restore test on staging or a disposable database.

Backup work belongs in DEPLOY 1.6, but production deployment should not be considered complete until restore has been tested.

## Next deployment tasks

- DEPLOY 1.2 — VPS base setup, SSH key-only access, firewall, Docker.
- DEPLOY 1.3 — Production env/secrets finalization.
- DEPLOY 1.4 — Reverse proxy/domain routing verification.
- DEPLOY 1.5 — HTTPS certificate verification.
- DEPLOY 1.6 — Database backups and restore test.
- DEPLOY 1.7 — First staging/production deployment.
- DEPLOY 1.8 — Production verification checklist.
