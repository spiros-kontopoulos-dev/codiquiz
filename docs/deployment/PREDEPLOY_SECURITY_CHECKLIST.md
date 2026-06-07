# Codiquiz Pre-Deployment Security Checklist

This checklist is the handoff point between `PREDEPLOY 1` and `DEPLOY 1`.
It does not replace production infrastructure work, but it defines the safety
baseline that must be true before `codiquiz.com` and `admin.codiquiz.com` are
opened publicly.

## Required production environment values

Use explicit production settings on the VPS:

```env
CODIQUIZ_ENV=production
CODIQUIZ_CORS_ALLOWED_ORIGINS=https://codiquiz.com,https://www.codiquiz.com,https://admin.codiquiz.com
CODIQUIZ_AUTH_COOKIE_SECURE=true
CODIQUIZ_AUTH_COOKIE_SAMESITE=lax
CODIQUIZ_ENABLE_ADMIN_TEST_LAB=false
PUBLIC_VISIT_TRUST_PROXY_HEADERS=true
PUBLIC_VISIT_STORE_RAW_IP=false
PUBLIC_VISIT_IP_HASH_SALT=<deployment-specific-random-secret>
```

Keep the default AI provider safe unless a real provider action is explicitly
chosen by an owner/admin:

```env
AI_GENERATION_PROVIDER=mock
```

## First-owner bootstrap

The bootstrap password is only for initial owner creation.

1. Set `CODIQUIZ_BOOTSTRAP_OWNER_EMAIL`, optional `CODIQUIZ_BOOTSTRAP_OWNER_USERNAME`, and `CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD`.
2. Run migrations and start the API once.
3. Confirm the owner user exists and can log in.
4. Remove `CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD` from the production environment.

Do not leave bootstrap credentials active permanently.

## Admin/demo access baseline

Before deployment, verify:

- Admin APIs require authentication.
- `/admin` routes redirect unauthenticated users to login.
- `owner` can manage users.
- `admin` can access operational admin workspaces but cannot manage users.
- `demo_viewer` can browse safe pages only.
- `demo_viewer` cannot mutate production data.
- `demo_viewer` cannot submit real provider/OpenAI jobs.
- `demo_viewer` cannot approve/reject drafts.
- `demo_viewer` cannot edit taxonomy, Blueprint policy, users, or settings.
- Blocked demo clicks show the read-only modal.
- Direct/manual blocked URLs show the full restricted page.

## Developer/Test Lab

`/admin/test-lab` is a developer-support workspace. It is useful locally and in
staging, but it should not be available in production.

Production requirement:

```env
CODIQUIZ_ENABLE_ADMIN_TEST_LAB=false
```

## CORS and cookies

Production CORS should use exact HTTPS origins only. Do not use wildcard CORS.

Recommended origins:

```text
https://codiquiz.com
https://www.codiquiz.com
https://admin.codiquiz.com
```

Admin auth cookies should use:

```env
CODIQUIZ_AUTH_COOKIE_SECURE=true
CODIQUIZ_AUTH_COOKIE_SAMESITE=lax
```

## Public tracking privacy

Public tracking should count visitors/sessions/page views without storing raw
personal data by default.

Recommended production values:

```env
PUBLIC_VISIT_STORE_RAW_IP=false
PUBLIC_VISIT_IP_HASH_SALT=<deployment-specific-random-secret>
```

Location detection should come from trusted proxy/CDN headers or a local GeoIP
DB. Do not trust arbitrary client-supplied headers unless the request comes
through your controlled proxy layer.

## Admin readiness page

Owners/admins can review current runtime readiness in:

```text
/admin/security
```

The page reports pass/warning/fail/info checks without exposing secret values.
Use it after setting production environment variables and after every deployment
configuration change.

## DEPLOY 1 handoff

See also: [DEPLOY 1.1 — Production Deployment Foundation](deployment/DEPLOY_1_1_PRODUCTION_FOUNDATION.md) and [Codiquiz Production Checklist](deployment/PRODUCTION_CHECKLIST.md).
