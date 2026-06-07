# Deployment security readiness checks
# Source: quiz-api/app/security.py (excerpt lines 1-240)
# Public portfolio excerpt; not standalone application code.

"""Deployment security helpers for Codiquiz.

The goal is to keep local development convenient while making production
configuration explicit and reviewable before Codiquiz is exposed publicly.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Iterable, Literal

from fastapi import HTTPException, status

LOCAL_CORS_ORIGINS = (
    "http://localhost:5173",
    "http://127.0.0.1:5173",
)

SecurityCheckStatus = Literal["pass", "warning", "fail", "info"]


def _env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_text(name: str, default: str = "") -> str:
    value = os.getenv(name)
    return value.strip() if value is not None else default


def get_runtime_environment() -> str:
    return _env_text("CODIQUIZ_ENV", "local").lower() or "local"


def is_production_environment() -> bool:
    return get_runtime_environment() in {"production", "prod", "live"}


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def get_allowed_cors_origins() -> tuple[str, ...]:
    """Return exact origins allowed to call the API from browsers.

    Production should set CODIQUIZ_CORS_ALLOWED_ORIGINS explicitly, e.g.
    https://codiquiz.com,https://www.codiquiz.com,https://admin.codiquiz.com. Local development keeps
    localhost defaults so existing Docker/Playwright flows continue to work.
    """
    configured_origins = parse_csv(os.getenv("CODIQUIZ_CORS_ALLOWED_ORIGINS"))
    if configured_origins:
        return tuple(dict.fromkeys(configured_origins))
    return LOCAL_CORS_ORIGINS


def should_enable_admin_test_lab() -> bool:
    """Keep Developer/Test Lab available locally but off by default in production."""
    explicit_value = os.getenv("CODIQUIZ_ENABLE_ADMIN_TEST_LAB")
    if explicit_value is not None:
        return _env_flag("CODIQUIZ_ENABLE_ADMIN_TEST_LAB", default=False)
    return not is_production_environment()


def require_admin_test_lab_enabled() -> None:
    if not should_enable_admin_test_lab():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admin Test Lab is disabled in this environment",
        )


@dataclass(frozen=True)
class SecurityCheck:
    key: str
    label: str
    status: SecurityCheckStatus
    category: str
    detail: str
    recommendation: str | None = None


def _status_rank(status_value: SecurityCheckStatus) -> int:
    order = {"fail": 4, "warning": 3, "info": 2, "pass": 1}
    return order[status_value]


def _check(
    *,
    key: str,
    label: str,
    status_value: SecurityCheckStatus,
    category: str,
    detail: str,
    recommendation: str | None = None,
) -> SecurityCheck:
    return SecurityCheck(
        key=key,
        label=label,
        status=status_value,
        category=category,
        detail=detail,
        recommendation=recommendation,
    )


def get_deployment_security_checks() -> list[SecurityCheck]:
    environment = get_runtime_environment()
    production = is_production_environment()
    origins = get_allowed_cors_origins()
    origin_text = ", ".join(origins) if origins else "none"
    has_wildcard_origin = any(origin == "*" for origin in origins)
    has_local_origin = any("localhost" in origin or "127.0.0.1" in origin for origin in origins)
    secure_cookie = _env_flag("CODIQUIZ_AUTH_COOKIE_SECURE", default=production)
    cookie_samesite = _env_text("CODIQUIZ_AUTH_COOKIE_SAMESITE", "lax").lower()
    bootstrap_password_is_set = bool(_env_text("CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD"))
    raw_ip_storage = _env_flag("PUBLIC_VISIT_STORE_RAW_IP", default=False)
    trust_proxy_headers = _env_flag("PUBLIC_VISIT_TRUST_PROXY_HEADERS", default=False)
    geoip_db_path = _env_text("PUBLIC_VISIT_GEOIP_DB_PATH")
    ip_hash_salt = _env_text("PUBLIC_VISIT_IP_HASH_SALT")
    openai_key_is_set = bool(_env_text("OPENAI_API_KEY"))
    default_provider = _env_text("AI_GENERATION_PROVIDER", "mock")
    test_lab_enabled = should_enable_admin_test_lab()

    checks: list[SecurityCheck] = [
        _check(
            key="runtime-environment",
            label="Runtime environment is explicit",
            status_value="pass" if environment else "warning",
            category="Environment",
            detail=f"CODIQUIZ_ENV={environment}",
            recommendation="Use CODIQUIZ_ENV=production on the live VPS.",
        ),
        _check(
            key="cors-origins",
            label="CORS uses explicit origins",
            status_value=(
                "fail" if has_wildcard_origin else
                "warning" if production and (not origins or has_local_origin) else
                "pass"
            ),
            category="CORS",
            detail=f"Allowed browser origins: {origin_text}",
            recommendation="Production should use only https://codiquiz.com, https://www.codiquiz.com, and https://admin.codiquiz.com.",
        ),
        _check(
            key="secure-auth-cookie",
            label="Admin auth cookie uses Secure in production",
            status_value="pass" if secure_cookie else ("fail" if production else "info"),
            category="Authentication",
            detail=f"CODIQUIZ_AUTH_COOKIE_SECURE={str(secure_cookie).lower()}",
            recommendation="Set CODIQUIZ_AUTH_COOKIE_SECURE=true behind HTTPS.",
        ),
        _check(
            key="cookie-samesite",
            label="Admin auth cookie SameSite policy is safe",
            status_value="warning" if cookie_samesite == "none" and not secure_cookie else "pass",
            category="Authentication",
            detail=f"CODIQUIZ_AUTH_COOKIE_SAMESITE={cookie_samesite}",
            recommendation="Use SameSite=lax unless cross-site cookie behavior is intentionally required.",
        ),
        _check(
            key="bootstrap-owner-password",
            label="Bootstrap owner password is not left configured",
            status_value="warning" if bootstrap_password_is_set and production else "pass",
            category="Secrets",
            detail="Bootstrap owner password env var is set." if bootstrap_password_is_set else "Bootstrap owner password env var is not set.",
            recommendation="After creating the first owner, remove CODIQUIZ_BOOTSTRAP_OWNER_PASSWORD from production env.",
        ),
        _check(
            key="openai-provider-default",
            label="AI provider default is controlled",
            status_value="warning" if production and default_provider != "mock" else "pass",
            category="Provider safety",
            detail=f"AI_GENERATION_PROVIDER={default_provider}; OPENAI_API_KEY={'set' if openai_key_is_set else 'not set'}",
            recommendation="Keep default provider as mock; require explicit owner/admin actions for real OpenAI runs.",
        ),
        _check(
            key="admin-test-lab",
            label="Developer/Test Lab is disabled in production",
            status_value="fail" if production and test_lab_enabled else ("info" if test_lab_enabled else "pass"),
            category="Dangerous tools",
            detail=f"Admin Test Lab is {'enabled' if test_lab_enabled else 'disabled'} for this environment.",
            recommendation="Set CODIQUIZ_ENABLE_ADMIN_TEST_LAB=false in production.",
        ),
        _check(
            key="visitor-raw-ip",
            label="Raw visitor IP storage is disabled by default",
            status_value="warning" if raw_ip_storage else "pass",
            category="Privacy",
            detail=f"PUBLIC_VISIT_STORE_RAW_IP={str(raw_ip_storage).lower()}",
            recommendation="Prefer salted IP hashes. Store raw IP only with a clear retention/privacy reason.",
        ),
        _check(
            key="visitor-ip-salt",
            label="Visitor IP hash salt is deployment-specific",
            status_value="warning" if production and not ip_hash_salt else "pass",
            category="Privacy",
            detail="PUBLIC_VISIT_IP_HASH_SALT is set." if ip_hash_salt else "PUBLIC_VISIT_IP_HASH_SALT is not set; default local salt will be used.",
            recommendation="Set a production-only random salt before public launch.",
        ),
        _check(
            key="trusted-proxy-geo",
            label="Location tracking source is explicit",
            status_value="info" if not trust_proxy_headers and not geoip_db_path else "pass",
            category="Traffic tracking",
            detail=(
                "Trusted proxy headers enabled." if trust_proxy_headers else
                "MaxMind GeoIP database configured." if geoip_db_path else
                "No production geo source configured yet; local/private visits will not resolve to city/country."
            ),
            recommendation="Enable trusted proxy headers behind Nginx/Cloudflare or configure PUBLIC_VISIT_GEOIP_DB_PATH.",
        ),
    ]

    return checks


def summarize_deployment_security_checks(checks: Iterable[SecurityCheck]) -> dict[str, int | str]:
    counts = {"pass": 0, "warning": 0, "fail": 0, "info": 0}
    highest_status: SecurityCheckStatus = "pass"

    for check in checks:
        counts[check.status] += 1
        if _status_rank(check.status) > _status_rank(highest_status):
            highest_status = check.status

    return {
        "status": highest_status,
        "pass_count": counts["pass"],
        "warning_count": counts["warning"],
        "fail_count": counts["fail"],
        "info_count": counts["info"],
    }
