# DEPLOY 1.3a — Preview Domain Configuration

This patch makes the production Docker/Caddy foundation reusable for both the
isolated preview environment and the future production environment.

## Why this exists

The first internet-facing Codiquiz server is now the isolated preview/demo VPS:

```text
<preview-vps>
preview.codiquiz.com
admin.preview.codiquiz.com
```

The future production VPS remains separate:

```text
codiquiz-prod-01
codiquiz.com
www.codiquiz.com
admin.codiquiz.com
```

Subdomains alone are not isolation. The preview server is a separate VPS with
its own database, Redis, files, Docker volumes, secrets, and demo/admin users.
This prevents preview/demo mistakes from touching the future production system.

## Files added/updated

- `.env.preview.example` — safe template for the preview VPS.
- `.env.production.example` — now includes configurable Caddy site addresses.
- `docker-compose.prod.yml` — passes public/admin Caddy addresses from env.
- `deploy/caddy/Caddyfile` — uses Caddy environment placeholders instead of
  hardcoded `codiquiz.com` addresses.

## Preview env values

For the preview server, copy:

```bash
cp .env.preview.example .env.preview
```

Then set real values for at least:

```env
CADDY_ACME_EMAIL=<ops email>
CODIQUIZ_PUBLIC_SITE_ADDRESSES=preview.codiquiz.com
CODIQUIZ_ADMIN_SITE_ADDRESSES=admin.preview.codiquiz.com
VITE_API_URL=https://preview.codiquiz.com/api
CODIQUIZ_CORS_ALLOWED_ORIGINS=https://preview.codiquiz.com,https://admin.preview.codiquiz.com
POSTGRES_PASSWORD=<long random password>
DATABASE_URL=postgresql://codiquiz_preview_user:<same password>@postgres:5432/codiquiz_preview_db
PUBLIC_VISIT_IP_HASH_SALT=<long random secret>
CODIQUIZ_BOOTSTRAP_OWNER_EMAIL=<owner email>
CODIQUIZ_BOOTSTRAP_OWNER_USERNAME=<owner username>
CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD=<temporary bootstrap password>
```

Keep `AI_GENERATION_PROVIDER=mock` for the first preview deployment unless real
OpenAI generation is intentionally enabled later.

## DNS prerequisite

Before starting Caddy with HTTPS, point these DNS records to the preview VPS IP:

```text
preview.codiquiz.com        A     <preview VPS IPv4>
admin.preview.codiquiz.com  A     <preview VPS IPv4>
```

Add AAAA records only if IPv6 is configured and intended.

## Compose validation

Validate the selected env file before running containers:

```bash
docker compose --env-file .env.preview -f docker-compose.prod.yml config > /tmp/codiquiz-preview-compose.yml
```

No database, Redis, API, or frontend development ports should be published to
the host. Only Caddy should publish `80`, `443`, and `443/udp`.
