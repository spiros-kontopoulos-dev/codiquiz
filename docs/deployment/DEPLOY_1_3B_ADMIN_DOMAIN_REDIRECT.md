# DEPLOY 1.3b — Admin Domain Redirect and Codiquiz Domain Correction

## Purpose

The preview environment uses a single React frontend image for both the public
site and admin UI. The admin UI is mounted under the `/admin` route inside the
SPA, so opening the admin hostname root previously rendered the public homepage.

This patch makes the behavior explicit:

```text
https://admin.preview.codiquiz.com/      -> /admin
https://admin.preview.codiquiz.com/admin -> admin SPA route
```

The patch also corrects preview/production deployment examples from
`codiquiz.com` to the real project domain, `codiquiz.com`.

## Files changed

- `deploy/caddy/Caddyfile`
  - Adds `redir / /admin 302` in the admin host block.
  - Keeps `/api/*` proxying to `quiz-api`.
  - Keeps all other paths served by the React frontend.

- `.env.preview.example`
  - Uses `preview.codiquiz.com` and `admin.preview.codiquiz.com`.

- `.env.production.example`
  - Uses `codiquiz.com`, `www.codiquiz.com`, and `admin.codiquiz.com`.

- `docs/deployment/DEPLOY_1_3A_PREVIEW_DOMAIN_CONFIG.md`
  - Corrects domain examples to `codiquiz.com`.

## Deployment commands

After pulling this patch on the VPS:

```bash
cd <preview-vps-project-root>

docker compose --env-file .env.preview -f docker-compose.prod.yml config > /tmp/codiquiz-preview-compose-check.yml && echo "preview compose config OK"

docker compose --env-file .env.preview -f docker-compose.prod.yml up -d caddy
```

Then verify:

```bash
curl -I https://admin.preview.codiquiz.com/
curl -I https://admin.preview.codiquiz.com/admin
```

Expected root behavior is a redirect to `/admin`.
