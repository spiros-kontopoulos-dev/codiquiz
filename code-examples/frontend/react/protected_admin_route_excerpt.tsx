// Selected sanitized excerpt from Codiquiz ProtectedAdminRoute.
// Shows how the admin UI protects routes and integrates role-aware access boundaries.
// This is a partial excerpt and is not intended to compile standalone.

import { type ReactNode, useEffect, useMemo, useState } from "react";
import { Navigate, useLocation } from "react-router-dom";

import { ADMIN_RESTRICTION_EVENT_NAME, type AdminRestrictionNotice, logoutAdmin, notifyAdminRestriction } from "../../api/auth";
import { sendAdminHeartbeat } from "../../api/adminActivity";
import { AdminForbiddenModal } from "./AdminForbiddenModal";
import { useAdminAuth } from "../../auth/AdminAuthContext";
import { adminPath, normalizeAdminPathname } from "../../utils/adminRoutes";

const DEMO_BLOCKED_ROUTE_PREFIXES = [
    "/access",
    "/activity",
    "/ai-generations/create",
    "/ai-generations/settings",
    "/security",
    "/question-bank/blueprint-rules",
    "/questions/create",
    "/test-lab",
];

function isDemoBlockedRoute(pathname: string): boolean {
    if (/^\/questions\/[^/]+\/edit$/.test(pathname)) {
        return true;
    }

    return DEMO_BLOCKED_ROUTE_PREFIXES.some((prefix) => (
        pathname === prefix || pathname.startsWith(`${prefix}/`)
    ));
}

function buildDemoRestrictionNotice(pathname?: string): AdminRestrictionNotice {
    return {
        title: "Read-only demo mode",
        message: pathname
            ? `Demo viewer accounts cannot open ${pathname} because it can change production data or settings.`
            : "Demo viewer accounts can inspect safe Codiquiz admin pages, but production-changing actions are disabled.",
        detail: "Demo access is restricted. Request a live walkthrough from the project owner for full mutation/provider flows.",
    };
}

function roleLabel(role: string): string {
    if (role === "demo_viewer") {
        return "Demo viewer";
    }

    return role.charAt(0).toUpperCase() + role.slice(1);
}

export default function ProtectedAdminRoute({children}: {children: ReactNode}) {
    const location = useLocation();
    const {user, isLoading} = useAdminAuth();
    const [isLoggingOut, setIsLoggingOut] = useState(false);
    const [restrictionNotice, setRestrictionNotice] = useState<AdminRestrictionNotice | null>(null);

    const normalizedPathname = useMemo(() => normalizeAdminPathname(location.pathname), [location.pathname]);

    const demoRouteIsBlocked = useMemo(
        () => user?.role === "demo_viewer" && isDemoBlockedRoute(normalizedPathname),
        [normalizedPathname, user?.role],
    );

    useEffect(() => {
        function handleRestrictionEvent(event: Event) {
            const customEvent = event as CustomEvent<AdminRestrictionNotice>;
            setRestrictionNotice({
                title: customEvent.detail?.title || "Read-only demo mode",
                message: customEvent.detail?.message,
                detail: customEvent.detail?.detail,
            });
        }

        window.addEventListener(ADMIN_RESTRICTION_EVENT_NAME, handleRestrictionEvent);

        return () => {
            window.removeEventListener(ADMIN_RESTRICTION_EVENT_NAME, handleRestrictionEvent);
        };
    }, []);


    useEffect(() => {
        if (!user) {
            return undefined;
        }

        const currentPage = `${normalizedPathname}${location.search}`;

        async function sendHeartbeat() {
            try {
                await sendAdminHeartbeat({
                    current_page: currentPage,
                    page_title: document.title || null,
                });
            } catch {
                // Activity tracking should never interrupt admin browsing.
                // The next protected API request will still refresh last_active_at.
            }
        }

        void sendHeartbeat();
        const intervalId = window.setInterval(() => {
            void sendHeartbeat();
        }, 45_000);

        return () => {
            window.clearInterval(intervalId);
        };
    }, [normalizedPathname, location.search, user]);

    useEffect(() => {
        if (user?.role !== "demo_viewer") {
            return undefined;
        }

        function interceptDemoBlockedLinks(event: MouseEvent) {
            if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
                return;
            }

            const target = event.target;
            if (!(target instanceof Element)) {
                return;
            }

            const link = target.closest<HTMLAnchorElement>("a[href]");
            if (!link) {
                return;
            }

            const url = new URL(link.href, window.location.origin);

            if (url.origin !== window.location.origin || !isDemoBlockedRoute(normalizeAdminPathname(url.pathname))) {
                return;
            }

            event.preventDefault();
            event.stopPropagation();
            notifyAdminRestriction(buildDemoRestrictionNotice(normalizeAdminPathname(url.pathname)));
        }

        document.addEventListener("click", interceptDemoBlockedLinks, true);

        return () => {
            document.removeEventListener("click", interceptDemoBlockedLinks, true);
        };
    }, [user?.role]);

    async function handleLogout() {
        setIsLoggingOut(true);

        try {
            await logoutAdmin();
        } finally {
            // Force a full reload so the auth provider clears any in-memory user
            // state even if it was not part of this small predeploy patch ZIP.
            window.location.assign(adminPath("/login"));
        }
    }

    if (isLoading) {
        return (
            <main className="admin-auth-shell">
                <section className="admin-auth-card">
                    <p className="admin-auth-eyebrow">Codiquiz Admin</p>
                    <h1>Checking access…</h1>
                    <p className="admin-auth-muted">Verifying your admin session before loading the workspace.</p>
                </section>
            </main>
        );
    }

    if (!user) {
        return <Navigate to={adminPath("/login")} replace state={{from: location}} />;
    }

    return (
        <>
            <div className="admin-session-toolbar" aria-label="Admin session">
                <div className="admin-session-toolbar-user">
                    <span className="admin-session-toolbar-label">Signed in</span>
                    <strong>{user.display_name || user.email}</strong>
                    <span className="admin-session-role-badge">{roleLabel(user.role)}</span>
                    {user.role === "demo_viewer" && (
                        <span className="admin-session-demo-badge">Read-only demo mode</span>
                    )}
                </div>

                <button
                    className="admin-session-logout-button"
                    type="button"
                    disabled={isLoggingOut}
                    onClick={handleLogout}
                >
                    {isLoggingOut ? "Logging out…" : "Log out"}
                </button>
            </div>

            {demoRouteIsBlocked ? (
                <main className="admin-demo-blocked-shell">
                    <section className="admin-management-card admin-demo-blocked-card">
                        <p className="eyebrow">Read-only demo mode</p>
                        <h1>Demo access is restricted</h1>
                        <p>
                            Demo viewer accounts can inspect safe Codiquiz admin pages, but destructive or
                            production-changing workspaces are blocked. This protects real taxonomy, Blueprint,
                            provider, and user-management data before deployment.
                        </p>
                        <a className="admin-secondary-link-button" href={adminPath("/")}>
                            Return to dashboard
                        </a>
                    </section>
                </main>
            ) : children}

            {restrictionNotice && (
                <AdminForbiddenModal
                    title={restrictionNotice.title}
                    message={restrictionNotice.message}
                    detail={restrictionNotice.detail}
                    onClose={() => setRestrictionNotice(null)}
                />
