# Blueprint generation priority scoring
# Source: quiz-api/app/blueprint/priority_service.py (excerpt lines 1-121)
# Public portfolio excerpt; not standalone application code.

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class GenerationPriority:
    score: float
    bucket: str
    reasons: list[str] = field(default_factory=list)


TIER_BONUS = {
    "strong": 35.0,
    "secondary": 20.0,
    "weak": 5.0,
    "unrated": 0.0,
    "excluded": 0.0,
}


def _round_score(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _clamp_rule_priority(priority: int) -> int:
    # Blueprint rule priority is an admin-controlled nudge. Clamp it so a single
    # rule cannot completely dominate real coverage gaps and suitability fit.
    return max(min(priority, 100), -100)


def _bucket_for_score(score: float) -> str:
    if score <= 0:
        return "none"
    if score >= 300:
        return "top"
    if score >= 220:
        return "high"
    if score >= 140:
        return "medium"
    return "low"


def calculate_generation_priority(
        *,
        target_count: int,
        approved_count: int,
        pending_review_count: int,
        hard_gap_count: int,
        effective_gap_count: int,
        suitability_score: float | None,
        suitability_tier: str,
        rule_priority: int,
) -> GenerationPriority:
    """Rank how useful it is to generate this Blueprint cell next.

    The priority score intentionally focuses on *actionable generation work*.
    Cells with no automatic target, no hard gap, or pending drafts that already
    cover the gap should remain visible in coverage, but should not compete with
    real generation targets in the planner queue.
    """
    if target_count <= 0:
        return GenerationPriority(
            score=0.0,
            bucket="none",
            reasons=["No automatic Blueprint target"],
        )

    if hard_gap_count <= 0:
        return GenerationPriority(
            score=0.0,
            bucket="none",
            reasons=["Target already covered by approved questions"],
        )

    if effective_gap_count <= 0:
        return GenerationPriority(
            score=0.0,
            bucket="none",
            reasons=["Pending review drafts already cover the hard gap"],
        )

    effective_coverage_pct = 0.0
    if target_count > 0:
        effective_coverage_pct = min(
            ((approved_count + pending_review_count) / target_count) * 100,
            100.0,
        )

    gap_component = effective_gap_count * 100.0
    coverage_pressure_component = max(100.0 - effective_coverage_pct, 0.0) * 0.35
    suitability_component = (suitability_score or 0.0) * 0.75
    tier_component = TIER_BONUS.get(suitability_tier, 0.0)
    rule_priority_component = _clamp_rule_priority(rule_priority) * 5.0
    pending_penalty = pending_review_count * 10.0

    score = _round_score(
        gap_component
        + coverage_pressure_component
        + suitability_component
        + tier_component
        + rule_priority_component
        - pending_penalty
    )
    score = max(score, 0.0)

    reasons = [
        f"{effective_gap_count} effective gap{'s' if effective_gap_count != 1 else ''}",
        f"{suitability_tier.replace('_', ' ')} suitability",
    ]
    if suitability_score is not None:
        reasons.append(f"score {suitability_score:g}")
    if pending_review_count > 0:
        reasons.append(f"{pending_review_count} pending draft{'s' if pending_review_count != 1 else ''} lowers urgency")
    if rule_priority != 0:
        reasons.append(f"rule priority {rule_priority:+d}")

    return GenerationPriority(
        score=score,
        bucket=_bucket_for_score(score),
        reasons=reasons,
    )
