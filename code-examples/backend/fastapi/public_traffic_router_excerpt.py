# FastAPI public traffic privacy helpers
# Source: quiz-api/app/routers/public_traffic.py (excerpt lines 39-180)
# Public portfolio excerpt; not standalone application code.

def _clean_ip_candidate(value: str | None) -> str | None:
    if value is None:
        return None

    candidate = value.strip().strip('"').strip("'")
    if not candidate:
        return None

    # X-Forwarded-For can contain a chain. The first valid public client value
    # is what we want, but only when proxy headers are explicitly trusted.
    if "," in candidate:
        for part in candidate.split(","):
            cleaned_part = _clean_ip_candidate(part)
            if cleaned_part:
                return cleaned_part
        return None

    # Some proxies append a port to IPv4 values. IPv6 addresses are left alone.
    if candidate.count(":") == 1 and "." in candidate:
        candidate = candidate.rsplit(":", 1)[0]

    try:
        return str(ipaddress.ip_address(candidate))
    except ValueError:
        return None


def _hash_ip_address(ip_address: str | None) -> str | None:
    if not ip_address:
        return None

    # Use a deployment-specific salt so the same IP cannot be correlated across
    # environments. ADMIN_AUTH_SECRET is a reasonable fallback in the existing
    # app; PUBLIC_VISIT_IP_HASH_SALT can override it for a dedicated analytics salt.
    salt = (
        os.getenv("PUBLIC_VISIT_IP_HASH_SALT")
        or os.getenv("ADMIN_AUTH_SECRET")
        or "codiquiz-local-dev-public-visit-ip-salt"
    )
    return hashlib.sha256(f"{salt}:{ip_address}".encode("utf-8")).hexdigest()


def _extract_client_ip(request: Request) -> tuple[str | None, str | None]:
    if _env_flag("PUBLIC_VISIT_TRUST_PROXY_HEADERS"):
        trusted_header_candidates = [
            ("cf-connecting-ip", "cf_connecting_ip"),
            ("x-real-ip", "x_real_ip"),
            ("x-forwarded-for", "x_forwarded_for"),
        ]
        for header_name, capture_source in trusted_header_candidates:
            candidate = _clean_ip_candidate(request.headers.get(header_name))
            if candidate:
                return candidate, capture_source

    if request.client and request.client.host:
        return _clean_ip_candidate(request.client.host), "request_client"

    return None, None


def normalize_source_key(value: str | None) -> str:
    raw_value = (value or "").strip().lower()
    if not raw_value:
        return DIRECT_SOURCE_KEY

    normalized = re.sub(r"[^a-z0-9_-]+", "_", raw_value).strip("_")
    return (normalized or DIRECT_SOURCE_KEY)[:80]


def source_label_for_key(source_key: str) -> str:
    if source_key in DEFAULT_SOURCE_LABELS:
        return DEFAULT_SOURCE_LABELS[source_key]

    return source_key.replace("_", " ").replace("-", " ").title()


def detect_browser_family(user_agent: str | None) -> str | None:
    if not user_agent:
        return None

    lowered = user_agent.lower()
    if "edg/" in lowered or "edge/" in lowered:
        return "Edge"
    if "firefox/" in lowered:
        return "Firefox"
    if "chrome/" in lowered or "chromium/" in lowered:
        return "Chrome"
    if "safari/" in lowered:
        return "Safari"
    return "Other"


def get_or_create_source(db: Session, source_key: str, now: datetime) -> models.PublicTrafficSource:
    source = (
        db.query(models.PublicTrafficSource)
        .filter(models.PublicTrafficSource.source_key == source_key)
        .first()
    )

    if source is None:
        source = models.PublicTrafficSource(
            source_key=source_key,
            label=source_label_for_key(source_key),
            is_active=True,
            first_seen_at=now,
            last_seen_at=now,
        )
        db.add(source)
        db.flush()
        return source

    if source.first_seen_at is None:
        source.first_seen_at = now
    source.last_seen_at = now
    return source


def _upsert_visitor_session(
    db: Session,
    *,
    payload: schemas.PublicVisitTrackRequest,
    source_key: str,
    page_path: str,
    now: datetime,
    user_agent: str | None,
    browser_family: str | None,
    client_ip: str | None,
    ip_capture_source: str | None,
    geo_context: PublicVisitGeoContext,
) -> models.PublicVisitorSession:
    session = (
        db.query(models.PublicVisitorSession)
        .filter(models.PublicVisitorSession.session_id == payload.session_id)
        .first()
    )

    ip_hash = _hash_ip_address(client_ip)
    raw_ip_address = client_ip if _env_flag("PUBLIC_VISIT_STORE_RAW_IP") else None

    if session is None:
        session = models.PublicVisitorSession(
            visitor_id=payload.visitor_id,

# FastAPI public visit tracking endpoint
# Source: quiz-api/app/routers/public_traffic.py (excerpt lines 296-370)
# Public portfolio excerpt; not standalone application code.

@router.post("/public/visits", response_model=schemas.PublicVisitTrackResponse)
async def track_public_visit(
    payload: schemas.PublicVisitTrackRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    """Record one anonymous public page-view event and its parent session.

    The event table remains useful for behavior/page-path analysis. The session
    table is the safer source for visitor-count metrics so one recruiter who
    refreshes or browses many pages is counted as one session, not many visits.
    """
    now = auth.utcnow()
    source_key = normalize_source_key(payload.source)
    get_or_create_source(db, source_key, now)

    page_path = _truncate(payload.page_path, 500) or "/"
    user_agent = _truncate(request.headers.get("user-agent"), 500)
    browser_family = detect_browser_family(user_agent)
    client_ip, ip_capture_source = _extract_client_ip(request)
    geo_context = resolve_public_visit_location(request=request, client_ip=client_ip)
    ip_hash = _hash_ip_address(client_ip)
    raw_ip_address = client_ip if _env_flag("PUBLIC_VISIT_STORE_RAW_IP") else None

    _upsert_visitor_session(
        db,
        payload=payload,
        source_key=source_key,
        page_path=page_path,
        now=now,
        user_agent=user_agent,
        browser_family=browser_family,
        client_ip=client_ip,
        ip_capture_source=ip_capture_source,
        geo_context=geo_context,
    )

    page_view = models.PublicVisitEvent(
        visitor_id=payload.visitor_id,
        session_id=payload.session_id,
        source_key=source_key,
        page_path=page_path,
        page_title=_truncate(payload.page_title, 255),
        referrer=_truncate(payload.referrer, 500),
        user_agent=user_agent,
        browser_family=browser_family,
        ip_address_hash=ip_hash,
        raw_ip_address=raw_ip_address,
        ip_capture_source=ip_capture_source,
        country_code=geo_context.country_code,
        country_name=geo_context.country_name,
        region_name=geo_context.region_name,
        city_name=geo_context.city_name,
        location_source=geo_context.location_source,
        location_status=geo_context.location_status,
        is_returning_visitor=payload.is_returning_visitor,
    )
    db.add(page_view)
    db.commit()

    return schemas.PublicVisitTrackResponse(source_key=source_key)


@router.get("/admin/public-traffic/summary", response_model=schemas.AdminPublicTrafficSummaryRead)
async def get_public_traffic_summary(
    days: int = Query(default=30, ge=1, le=365),
    db: Session = Depends(get_db),
):
    since = auth.utcnow() - timedelta(days=days)
    today_start = auth.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

    scoped_page_views = db.query(models.PublicVisitEvent).filter(models.PublicVisitEvent.created_at >= since)
    scoped_sessions = db.query(models.PublicVisitorSession).filter(models.PublicVisitorSession.first_seen_at >= since)

    total_page_views = scoped_page_views.count()
