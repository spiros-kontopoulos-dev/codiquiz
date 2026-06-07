// Selected sanitized excerpt from Codiquiz AdminPublicTrafficPage.
// Shows how preview/demo visitor tracking is surfaced to the admin UI.
// This is a partial excerpt and is not intended to compile standalone.

import { useCallback, useEffect, useMemo, useState } from "react";

import {
    fetchAdminPublicTrafficSources,
    fetchAdminPublicTrafficSummary,
    fetchAdminPublicVisitorSessions,
    fetchAdminPublicVisitEvents,
    updateAdminPublicTrafficSource,
    type AdminPublicTrafficSource,
    type AdminPublicTrafficSummary,
    type AdminPublicVisitorSession,
    type AdminPublicVisitEvent,
} from "../../api/publicTraffic";
import { AdminPagination } from "../../components/admin/AdminPagination";
import { useAdminAuth } from "../../auth/AdminAuthContext";
import "../../styles/admin/pages/admin-public-traffic.css";

type SourceDraft = {
    label: string;
    description: string;
    isActive: boolean;
};

function formatNumber(value: number): string {
    return new Intl.NumberFormat().format(value);
}

function formatDateTime(value: string | null | undefined): string {
    if (!value) {
        return "—";
    }

    const parsedDate = new Date(value);
    if (Number.isNaN(parsedDate.getTime())) {
        return value;
    }

    return parsedDate.toLocaleString();
}

function maskTrackingId(value: string): string {
    if (value.length <= 12) {
        return value;
    }

    return `${value.slice(0, 8)}…${value.slice(-4)}`;
}

function maskIpHash(value: string | null): string {
    if (!value) {
        return "—";
    }

    return `${value.slice(0, 10)}…`;
}

type LocationRecord = Pick<
    AdminPublicVisitorSession | AdminPublicVisitEvent,
    "country_code" | "country_name" | "region_name" | "city_name" | "location_source" | "location_status"
>;

function formatLocation(record: LocationRecord): string {
    if (record.location_status === "private_network") {
        return "Local/private network";
    }

    const country = record.country_name || record.country_code;
    const region = record.region_name;
    const city = record.city_name;
    const parts = [city, region, country].filter(Boolean);

    if (parts.length > 0) {
        return parts.join(", ");
    }

    if (record.location_status === "not_configured") {
        return "Geo lookup not configured";
    }
    if (record.location_status === "unavailable") {
        return "Geo lookup unavailable";
    }

    return "Unknown location";
}

function formatLocationSource(record: LocationRecord): string {
    if (record.location_status === "private_network") {
        return "Local/dev request";
    }
    if (record.location_source === "trusted_proxy_headers") {
        return "Trusted proxy/CDN headers";
    }
    if (record.location_source === "maxmind_geoip2") {
        return "MaxMind GeoIP2";
    }
    if (record.location_status === "not_configured") {
        return "Configure proxy headers or GeoIP DB";
    }

    return record.location_source || "No location source";
}

function formatLocationStatus(record: LocationRecord): string {
    if (!record.location_status) {
        return "unknown";
    }

    return record.location_status.replace(/_/g, " ");
}

function buildDrafts(sources: AdminPublicTrafficSource[]): Record<string, SourceDraft> {
    return Object.fromEntries(
        sources.map((source) => [
            source.source_key,
            {
                label: source.label,
                description: source.description ?? "",
                isActive: source.is_active,
            },
        ]),
    );
}

function AdminPublicTrafficPage() {
    const {user: currentUser} = useAdminAuth();
    const canManageSources = currentUser?.role === "owner" || currentUser?.role === "admin";
    const [summary, setSummary] = useState<AdminPublicTrafficSummary | null>(null);
    const [sources, setSources] = useState<AdminPublicTrafficSource[]>([]);
    const [sessions, setSessions] = useState<AdminPublicVisitorSession[]>([]);
    const [events, setEvents] = useState<AdminPublicVisitEvent[]>([]);
    const [totalSessions, setTotalSessions] = useState(0);
    const [totalEvents, setTotalEvents] = useState(0);
    const [sourceFilter, setSourceFilter] = useState("all");
    const [days, setDays] = useState(30);
    const [sessionPage, setSessionPage] = useState(1);
    const [sessionRowsPerPage, setSessionRowsPerPage] = useState(10);
    const [eventPage, setEventPage] = useState(1);
    const [eventRowsPerPage, setEventRowsPerPage] = useState(25);
    const [draftsBySource, setDraftsBySource] = useState<Record<string, SourceDraft>>({});
    const [isLoading, setIsLoading] = useState(true);
    const [isSaving, setIsSaving] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [successMessage, setSuccessMessage] = useState<string | null>(null);

    const sessionOffset = useMemo(() => (sessionPage - 1) * sessionRowsPerPage, [sessionPage, sessionRowsPerPage]);
    const eventOffset = useMemo(() => (eventPage - 1) * eventRowsPerPage, [eventPage, eventRowsPerPage]);

    const loadTraffic = useCallback(async () => {
        setIsLoading(true);
        setErrorMessage(null);

        try {
            const [nextSummary, nextSources, nextSessions, nextEvents] = await Promise.all([
                fetchAdminPublicTrafficSummary(days),
                fetchAdminPublicTrafficSources(),
                fetchAdminPublicVisitorSessions({
                    source: sourceFilter,
                    limit: sessionRowsPerPage,
                    offset: sessionOffset,
                }),
                fetchAdminPublicVisitEvents({
                    source: sourceFilter,
                    limit: eventRowsPerPage,
                    offset: eventOffset,
                }),
            ]);

            setSummary(nextSummary);
            setSources(nextSources.sources);
            setDraftsBySource(buildDrafts(nextSources.sources));
            setSessions(nextSessions.sessions);
            setTotalSessions(nextSessions.total);
            setEvents(nextEvents.events);
            setTotalEvents(nextEvents.total);
        } catch (error) {
            setErrorMessage(error instanceof Error ? error.message : "Failed to load public traffic");
        } finally {
            setIsLoading(false);
        }
    }, [days, eventOffset, eventRowsPerPage, sessionOffset, sessionRowsPerPage, sourceFilter]);

    useEffect(() => {
        void loadTraffic();
    }, [loadTraffic]);

    useEffect(() => {
        setSessionPage(1);
        setEventPage(1);
    }, [eventRowsPerPage, sessionRowsPerPage, sourceFilter]);

    function updateSourceDraft(sourceKey: string, patch: Partial<SourceDraft>) {
        setDraftsBySource((currentDrafts) => ({
            ...currentDrafts,
            [sourceKey]: {
                ...currentDrafts[sourceKey],
                ...patch,
            },
        }));
    }

    async function handleSaveSource(source: AdminPublicTrafficSource) {
        const draft = draftsBySource[source.source_key];
        if (!draft) {
            return;
        }

        setIsSaving(true);
        setErrorMessage(null);
        setSuccessMessage(null);

        try {
            await updateAdminPublicTrafficSource(source.source_key, {
                label: draft.label.trim(),
                description: draft.description.trim() || null,
                is_active: draft.isActive,
            });
            setSuccessMessage(`Updated source ${source.source_key}.`);
            await loadTraffic();
        } catch (error) {
            setErrorMessage(error instanceof Error ? error.message : "Failed to update tracking source");
        } finally {
            setIsSaving(false);
        }
    }

    return (
        <section className="admin-public-traffic-page">
            <div className="admin-page-heading admin-page-heading-with-action">
                <div>
                    <p className="eyebrow">Public tracking</p>
                    <h1>Public visitor tracking</h1>
                    <p>
                        Track anonymous visitors, sessions, and page views from CV, LinkedIn, and other campaign links before deployment.
                    </p>
                </div>

                <div className="admin-heading-actions">
                    <a className="admin-secondary-link-button" href="/?src=cv" target="_blank" rel="noreferrer">
                        Test CV source
                    </a>
