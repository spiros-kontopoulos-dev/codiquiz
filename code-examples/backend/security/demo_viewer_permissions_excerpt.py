"""Selected sanitized excerpt from Codiquiz admin auth/permission logic.

Shows role requirements and demo-viewer write restrictions used by the public preview admin.
This is partial and is not intended to run standalone.
"""

            detail="Authentication required",
        )
    return user


def require_roles(*allowed_roles: str):
    allowed = set(allowed_roles)

    async def dependency(user: models.AdminUser = Depends(get_current_admin_user)) -> models.AdminUser:
        if user.role not in allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )
        return user

    return dependency


def is_public_quiz_attempt_path(path: str) -> bool:
    # Public quiz taking uses nested attempt routes, while quiz creation/editing
    # is admin work. Keep learner attempt APIs open but protect quiz-management
    # mutations before deployment.
    parts = [part for part in path.split("/") if part]

    if len(parts) >= 3 and parts[0] == "quizzes" and parts[2] == "attempts":
        return True

    return len(parts) >= 2 and parts[0] == "quizzes" and parts[1] == "attempts"


def should_protect_path(path: str, method: str, prefixes: Iterable[str] = PROTECTED_API_PREFIXES) -> bool:
    normalized_method = method.upper()
    if normalized_method == "OPTIONS":
        return False

    if path in PUBLIC_AUTH_PATHS:
        return False

    if any(path == prefix or path.startswith(f"{prefix}/") for prefix in prefixes):
        return True

    if normalized_method in UNSAFE_METHODS and (path == "/quizzes" or path.startswith("/quizzes/")):
        return not is_public_quiz_attempt_path(path)

    if normalized_method in UNSAFE_METHODS:
        return any(
            path == prefix or path.startswith(f"{prefix}/")
            for prefix in PROTECTED_MUTATION_PREFIXES
        )

    return False


def should_block_demo_viewer_request(user: models.AdminUser, path: str, method: str) -> bool:
    """Keep recruiter/demo access read-only at the API edge.

    Demo users should be able to explore safe admin screens, but they must not
    mutate real production data, launch provider jobs, edit taxonomy/blueprint
    policy, manage users, or run developer cleanup tools. Centralizing this in
    middleware protects current and future routers even when a page accidentally
    leaves a dangerous button visible.
    """
    normalized_method = method.upper()

    if user.role != DEMO_VIEWER_ROLE:
        return False

    if normalized_method == "OPTIONS":
        return False

    if normalized_method not in UNSAFE_METHODS:
        return False

    return path not in DEMO_ALLOWED_UNSAFE_PATHS


def revoke_current_session(db: Session, request: Request) -> None:
    token = get_token_from_request(request)
    if not token:
        return

    session = (
        db.query(models.AdminAuthSession)
        .filter(models.AdminAuthSession.token_hash == hash_session_token(token))
        .first()
    )
    if session and session.revoked_at is None:
        now = utcnow()
        session.revoked_at = now
        session.last_seen_at = now
        if session.user:
            session.user.last_active_at = now
            db.add(models.AdminActivityEvent(
                user_id=session.user_id,
                session_id=session.id,
                event_type="logout",
                page_path=session.current_page,
                page_title=session.current_page_title,
                details="Admin user logged out",
                created_at=now,
