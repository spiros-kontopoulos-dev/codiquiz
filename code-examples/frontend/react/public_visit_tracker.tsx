// React public visitor/session tracker
// Source: frontend/src/components/public/PublicVisitTracker.tsx (excerpt lines 1-102)
// Public portfolio excerpt; not standalone application code.
// Frontend source excerpt; analytics errors are deliberately swallowed so tracking never
// breaks public navigation.

import { type ReactNode, useEffect } from "react";
import { useLocation } from "react-router-dom";

import { trackPublicVisit } from "../../api/publicTraffic";

const VISITOR_ID_KEY = "codiquiz_public_visitor_id";
const SESSION_ID_KEY = "codiquiz_public_session_id";
const SESSION_SOURCE_KEY = "codiquiz_public_session_source";
const SESSION_LAST_ACTIVITY_KEY = "codiquiz_public_session_last_activity_at";
const SESSION_TIMEOUT_MS = 30 * 60 * 1000;
const DIRECT_SOURCE = "direct";

type StoredTrackingId = {
    id: string;
    existed: boolean;
};

type PublicTrackingSession = {
    id: string;
    source: string;
};

function randomTrackingId(prefix: string): string {
    if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
        return `${prefix}_${crypto.randomUUID()}`;
    }

    return `${prefix}_${Date.now()}_${Math.random().toString(16).slice(2)}`;
}

function getOrCreateStoredId(storage: Storage, key: string, prefix: string): StoredTrackingId {
    const existingId = storage.getItem(key);
    if (existingId) {
        return {id: existingId, existed: true};
    }

    const nextId = randomTrackingId(prefix);
    storage.setItem(key, nextId);
    return {id: nextId, existed: false};
}

function readExplicitSource(search: string): string | null {
    const params = new URLSearchParams(search);
    const explicitSource = params.get("src")?.trim();
    return explicitSource || null;
}

function getOrCreateSession(storage: Storage, search: string, now: number): PublicTrackingSession {
    const explicitSource = readExplicitSource(search);
    const existingSessionId = storage.getItem(SESSION_ID_KEY);
    const lastActivityRaw = storage.getItem(SESSION_LAST_ACTIVITY_KEY);
    const lastActivity = lastActivityRaw ? Number(lastActivityRaw) : 0;
    const isExpired = !lastActivity || Number.isNaN(lastActivity) || now - lastActivity > SESSION_TIMEOUT_MS;

    if (!existingSessionId || isExpired) {
        const nextSource = explicitSource || DIRECT_SOURCE;
        const nextSessionId = randomTrackingId("session");
        storage.setItem(SESSION_ID_KEY, nextSessionId);
        storage.setItem(SESSION_SOURCE_KEY, nextSource);
        storage.setItem(SESSION_LAST_ACTIVITY_KEY, String(now));
        return {id: nextSessionId, source: nextSource};
    }

    // Keep the original source for the active session unless the visitor lands
    // with a new explicit source after timeout. That makes one CV browsing
    // session stay one CV session across route changes and refreshes.
    const sessionSource = storage.getItem(SESSION_SOURCE_KEY) || explicitSource || DIRECT_SOURCE;
    storage.setItem(SESSION_SOURCE_KEY, sessionSource);
    storage.setItem(SESSION_LAST_ACTIVITY_KEY, String(now));
    return {id: existingSessionId, source: sessionSource};
}

export function PublicVisitTracker({children}: {children: ReactNode}) {
    const location = useLocation();

    useEffect(() => {
        if (typeof window === "undefined") {
            return;
        }

        try {
            const visitor = getOrCreateStoredId(localStorage, VISITOR_ID_KEY, "visitor");
            const session = getOrCreateSession(localStorage, location.search, Date.now());
            const pagePath = `${location.pathname}${location.search}${location.hash}` || "/";

            trackPublicVisit({
                visitor_id: visitor.id,
                session_id: session.id,
                page_path: pagePath,
                page_title: document.title || null,
                source: session.source,
                referrer: document.referrer || null,
                is_returning_visitor: visitor.existed,
            });
        } catch {
            // Analytics should never break public navigation, including in
            // private browsing modes where storage APIs can be unavailable.
        }
    }, [location.hash, location.pathname, location.search]);

    return <>{children}</>;
}
