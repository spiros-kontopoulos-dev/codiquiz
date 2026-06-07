# Codiquiz Production Checklist

Use this checklist before exposing Codiquiz publicly.

## Repository and release flow

- Deploy from the private Git repository.
- Do not edit production code manually on the VPS.
- Use `git pull` or a future CI/CD deployment flow.
- Keep `.env.production` on the VPS only.
- Confirm no real secrets are committed.

## Domains

- `codiquiz.com` points to the production VPS.
- `www.codiquiz.com` points to the production VPS.
- `admin.codiquiz.com` points to the production/admin VPS or to the protected production VPS path chosen for the first deploy.
- DNS records are stable before requesting HTTPS certificates.

## HTTPS and proxy

- Caddy or Nginx is the only public entrypoint.
- HTTP redirects to HTTPS.
- API traffic is routed under `/api/*`.
- Frontend routes fall back to `index.html`.
- Admin domain is protected by app auth and, if desired, an extra proxy layer later.

## Network exposure

Publicly exposed ports should be limited to:

```text
22/tcp from trusted admin IPs if possible
80/tcp
443/tcp
443/udp if using HTTP/3
```

Do not expose:

```text
5432/tcp PostgreSQL
6379/tcp Redis
8000/tcp quiz-api
8001/tcp question-service
5173/tcp Vite dev server
```

## Production environment

Required values:

```env
CODIQUIZ_ENV=production
CODIQUIZ_CORS_ALLOWED_ORIGINS=https://codiquiz.com,https://www.codiquiz.com,https://admin.codiquiz.com
CODIQUIZ_AUTH_COOKIE_SECURE=true
CODIQUIZ_AUTH_COOKIE_SAMESITE=lax
CODIQUIZ_ENABLE_ADMIN_TEST_LAB=false
PUBLIC_VISIT_TRUST_PROXY_HEADERS=true
PUBLIC_VISIT_STORE_RAW_IP=false
PUBLIC_VISIT_IP_HASH_SALT=<random-production-secret>
```

Keep `AI_GENERATION_PROVIDER=mock` as the default unless real provider generation should be available by explicit owner/admin action.

## Database and migrations

- Use a strong production database password.
- Keep PostgreSQL on an internal Docker network only.
- Run Alembic migrations after deploy.
- Confirm `/api/health` reports database connectivity.
- Add backup and restore testing before declaring production complete.

## Admin account

- Bootstrap the first owner only once.
- Confirm owner login.
- Remove `CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD` after bootstrap.
- Create restricted demo account.
- Confirm demo account cannot mutate data or submit provider jobs.

## Verification

- `https://codiquiz.com` loads.
- `https://www.codiquiz.com` loads or redirects as intended.
- `https://admin.codiquiz.com` loads the admin app.
- `https://codiquiz.com/api/health` returns API health JSON.
- Admin login works.
- `/admin/security` has no production failures.
- Public quick-practice path works.
- Public visit tracking does not store raw IPs by default.
- Worker heartbeat and Batch API automation status display in admin settings.
