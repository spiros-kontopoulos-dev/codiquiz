# Deployment Model

Codiquiz is planned for deployment on Hetzner with separate public and admin/staging environments.

## Repository model

The official source-code repository remains private.

The public repository is documentation-focused and contains:

- project overview,
- architecture notes,
- system design documents,
- roadmap,
- screenshots,
- diagrams,
- engineering highlights.

## VPS plan

Planned environments:

### Live VPS

Purpose:

- official public Codiquiz site,
- public practice experience,
- production-facing services.

Domain:

```text
codiquiz.com
```

### Admin/Staging VPS

Purpose:

- protected admin demo,
- staging environment,
- internal generation/review tools,
- testing new admin workflows before live exposure.

The public site and admin environment are separated so the public quiz experience can remain clean while admin tools stay protected.

## Deployment philosophy

Keep the first public deployment controlled and cost-aware.

Initial online stack:

- frontend,
- quiz-api,
- question-service,
- PostgreSQL,
- Redis,
- quiz-worker,
- quiz-beat,
- question-worker.

Later infrastructure can be added when needed:

- pgvector,
- OpenSearch/Elasticsearch,
- Kafka,
- Airflow,
- analytics-service,
- observability stack.

## Security notes

Admin/generation tools should not be publicly exposed without protection.

Important concerns:

- OpenAI API keys stay backend-only.
- Admin endpoints require authentication/protection.
- Staging/admin domain should be hidden or access-controlled.
- Database and Redis should not be open to the public internet.
- Batch API and worker actions should remain controlled.

## DEPLOY 1 production foundation

The first production foundation has been added as repository-level deployment templates and checklists. The local development Docker Compose file remains local-only, while production should use:

```bash
docker compose --env-file .env.production -f docker-compose.prod.yml up -d --build
```

Production entrypoint:

```text
Internet → Caddy/Nginx reverse proxy → frontend or quiz-api
```

Initial domain map:

```text
codiquiz.com       → public Codiquiz frontend
www.codiquiz.com   → public Codiquiz frontend
admin.codiquiz.com → same frontend app with admin routes protected by admin auth
/api/*             → quiz-api, with /api stripped by the proxy
```

Key production rules:

- Keep PostgreSQL and Redis off public ports.
- Keep `quiz-api` and `question-service` internal to Docker.
- Use exact HTTPS CORS origins.
- Store `.env.production` on the VPS only.
- Run Alembic migrations during deployment.
- Add database backups and restore testing before declaring production complete.

See:

- [DEPLOY 1.1 — Production Deployment Foundation](deployment/DEPLOY_1_1_PRODUCTION_FOUNDATION.md)
- [Codiquiz Production Checklist](deployment/PRODUCTION_CHECKLIST.md)

## Future deployment documentation

Future docs should include:

- VPS hardening details,
- SSH key-only access,
- firewall commands,
- backup and restore runbooks,
- monitoring/logging plan,
- rollback plan,
- staging-to-production release workflow.
