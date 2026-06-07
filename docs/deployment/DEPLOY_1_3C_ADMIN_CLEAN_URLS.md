# DEPLOY 1.3c — Admin Subdomain Clean URLs

## Goal

The preview admin environment should use the admin subdomain as the admin root:

```text
https://admin.preview.codiquiz.com/
https://admin.preview.codiquiz.com/login
https://admin.preview.codiquiz.com/ai-generations
```

The admin subdomain should not require redundant `/admin/...` URLs such as:

```text
https://admin.preview.codiquiz.com/admin/login
```

## Implementation

The frontend now detects whether it is running on an `admin.*` hostname.

- On normal/local/public hosts, admin routes continue to live under `/admin/...`.
- On admin subdomains, admin routes live at the domain root.
- Legacy `/admin/...` paths on the admin subdomain are redirected to the clean equivalent.

This keeps local development unchanged while making the deployed admin preview URL cleaner.

## Expected preview URLs

```text
Public preview: https://preview.codiquiz.com/
Admin preview:  https://admin.preview.codiquiz.com/
Admin login:    https://admin.preview.codiquiz.com/login
```

## Compatibility

The legacy admin paths remain safe:

```text
https://admin.preview.codiquiz.com/admin/login -> /login
https://admin.preview.codiquiz.com/admin       -> /
```

The production public/admin separation should follow the same pattern later:

```text
https://codiquiz.com/
https://www.codiquiz.com/
https://admin.codiquiz.com/
```
