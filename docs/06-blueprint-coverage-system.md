# Blueprint Coverage System

The Blueprint system defines what the question bank should contain.

It is the planning layer for content generation and future practice selection. In the current alpha, Blueprint coverage, default target generation, work queues, and generation candidate selection are implemented in the admin flow. Deeper automation policies can still evolve, but the main planning signals now exist.

```text
Blueprint = content plan
Question bank = current content
Coverage gap = what should be generated next
```

## Problem it solves

A deep taxonomy creates a risk: if every topic gets the same number of questions, the bank may look balanced but be educationally weak.

Some concepts are foundational and high-value. Others are niche, advanced, or less suitable for quiz practice.

The Blueprint system prevents flat generation by considering:

- taxonomy priority,
- concept importance,
- difficulty relevance,
- question type suitability,
- approved question count,
- pending draft count,
- generation gap,
- generation reliability.

## Current implemented intelligence

Current Blueprint planning is driven by the Backend Intelligence Layer:

- concept importance scores and tiers,
- reviewed question-type suitability rules,
- difficulty-specific weights and blocked difficulties,
- approved and pending draft coverage counts,
- generated default target counts,
- generation priority scores for candidate rows.

The admin can inspect default target previews, focused coverage rows, top generation candidates, and work queues such as recommended targets, strong fit, secondary fit, weak manual-only, all eligible, and unrated.

## Blueprint row

A Blueprint row represents a desired target for a specific content combination.

Example:

```text
Technology: Python
Domain: Core Language
Module: Data Structures
Topic: Lists
Subtopic: List Methods
Concept: append returns None
Question task type: predict_output
Difficulty: beginner
Target count: 5
```

## Coverage counts

Each Blueprint row can track:

- target count,
- approved count,
- pending review count,
- generation gap,
- status.

Formula:

```text
generation_gap = target_question_count - approved_question_count - pending_review_count
```

If the gap is positive, the row is underfilled. If the gap is zero or negative, the row is healthy or overfilled.

## Blueprint rules

Blueprint rules define how target counts and priorities are created.

Possible rule dimensions:

- entity type,
- entity ID,
- difficulty,
- question task type,
- target count,
- enabled/disabled flag,
- priority tier,
- concept importance,
- suitability tier,
- difficulty weight.

Rules can be manual or computed.

Possible rule types:

- **Default rules** — broad defaults such as beginner concepts needing more predict-output and conceptual questions.
- **Entity rules** — overrides for one taxonomy entity or concept.
- **Question-type rules** — target changes based on how well a question task type fits the entity.
- **Difficulty rules** — beginner/intermediate/advanced weighting.
- **Disable rules** — prevent generation for weak or unsuitable combinations.
- **Manual override rules** — admin corrections when computed priorities are not enough.

A Blueprint rule should explain why a row exists and whether it is recommended, optional, disabled, or manually forced.

## Concept importance and content priority

Concept importance answers:

> How educationally important, useful, common, or strategically valuable is this concept?

The current taxonomy seed data can attach importance scores to concepts. These scores are grouped into tiers such as core, standard, niche, and excluded. Blueprint planning uses these tiers to avoid treating all concepts as equal.

Concept importance is not the only signal, but it is the base signal that decides whether a missing cell is worth generating at all and how large its target should be.

## Parent/child priority inheritance

Parent priority should influence children, but not dominate them.

Example idea:

```text
hierarchy_priority =
  0.65 * own_entity_priority
+ 0.20 * parent_module_priority
+ 0.10 * parent_domain_priority
+ 0.05 * technology_priority
```

This allows an important child concept in a lower-ranked domain to outrank a weak child concept in a higher-ranked domain.

## Difficulty weights

A concept can be more valuable at one difficulty than another.

Examples:

- Python basics are high-value for beginners but lower-value for advanced users.
- OOP inheritance is stronger for intermediate/advanced users.
- Cryptography internals may be low priority for beginner practice but valuable for advanced practice.

## Generation priority score

The generation priority score ranks what should be generated next.

Example formula:

```text
generation_priority_score =
  effective_content_priority
* question_type_suitability_score
* difficulty_weight
* generation_gap_ratio
* generation_reliability_score
```

The exact formula can evolve, but the goal stays the same: generate useful missing content, not random combinations.

## Blueprint row status

A Blueprint row can be classified as:

- **underfilled** — approved + pending count is below target, generation is useful;
- **healthy** — current coverage is close to target;
- **overfilled** — generation should normally stop for this row;
- **disabled** — row should not receive automatic generation;
- **manual only** — visible to admin but not recommended automatically.

This status is important because automatic generation should not simply choose random taxonomy paths. It should choose useful underfilled rows with enough suitability and priority.

## Blueprint candidate selection

The admin generation planner can load Blueprint candidates from ranked coverage gaps. A candidate should include:

- target Blueprint row,
- requested count,
- generation priority score,
- suitability tier,
- current approved/pending counts,
- avoid-list patterns,
- model profile/execution mode,
- budget and batch-size constraints.

## Blueprint admin page

The Blueprint admin page should feel like a planning cockpit, not a raw CRUD page. The current direction uses clickable work queues and focused result sections so admins can inspect one target group at a time.

Useful columns:

- taxonomy path,
- content priority,
- difficulty weights,
- best question task types,
- approved count,
- pending count,
- target count,
- generation gap,
- status,
- generate action.

Useful filters:

- technology,
- difficulty,
- status,
- priority tier,
- entity level,
- question task type,
- suitability tier.

## How Blueprint connects to AI generation

Current/future flow:

```text
Blueprint detects underfilled rows
→ generation candidates are ranked
→ AI generation plan or batch is created
→ OpenAI generates candidates
→ Quality Engine checks duplicates/repetition
→ drafts enter admin review
→ approved questions reduce the gap
```

## How Blueprint connects to practice selection

Later, the same Blueprint can influence broad practice selection.

When a user selects a broad target like “Python beginner practice”, the backend should not pick uniformly from every possible topic. It should prefer high-value areas while preserving variety and avoiding repetition.

Future selection weight:

```text
question_selection_weight =
  content_priority
* question_type_suitability
* difficulty_match
* user_scope_match
* variety_factor
* not_recently_seen_penalty
* user_weakness_boost
```
