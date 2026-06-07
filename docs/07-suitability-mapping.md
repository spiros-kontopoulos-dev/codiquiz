# Suitability Mapping

Suitability mapping decides which question task types fit each taxonomy entity or concept.

This is important because not every concept should be tested with every question type.

## Problem it solves

Without suitability mapping, a generation planner might create unnatural combinations such as:

- algorithmic complexity questions for a simple method-return-value concept,
- predict-output questions for topics that are mostly configuration or tooling,
- definition checks where code behavior practice would be much better.

Suitability mapping helps Codiquiz generate better content and avoid low-quality question targets.

## Question task type vs answer format

A question task type is the cognitive task:

- predict output,
- bug finding,
- code understanding,
- conceptual reasoning,
- fill missing code,
- edge-case reasoning.

An answer format is how the user answers:

- single choice,
- multiple choice,
- true/false,
- text input,
- code input.

Codiquiz can use single-choice answer format while still supporting many question task types.

## Suitability tiers

Current planning tiers:

### Strong / recommended

The question task type strongly fits the concept and can be automatically recommended for generation.

Example:

```text
append returns None → predict_output, bug_finding
```

### Secondary / recommended with lower priority

The question task type is useful but not the strongest fit. It can still be recommended, usually with lower priority or lower target counts.

Example:

```text
append returns None → conceptual reasoning
```

### Weak / manual-only

The question task type can remain visible to admins, but should not be automatically recommended.

### Not suitable / excluded

The combination should be excluded from automatic generation.

Example:

```text
append returns None → algorithmic_complexity
```

Older notes may use the labels top/secondary/weak/not suitable. The current admin behavior maps those ideas to recommended, secondary recommended, manual-only, and excluded.

## Suitability score

A numeric `question_type_suitability_score` can represent how valuable a task type is for a content entity.

Example:

```text
Python / Lists / append returns None
- predict_output: 95
- bug_finding: 90
- conceptual: 60
- algorithmic_complexity: 0
```

## Difficulty-specific suitability

Suitability is not only concept/type based. It can also vary by difficulty.

A concept/type pair can be:

- strong for beginner,
- strong for intermediate,
- blocked for advanced,
- or any other sensible combination.

This powers the AI Generation Create difficulty guidance banner and blocked-difficulty warnings. It helps prevent generation requests that would produce forced or unnatural questions.

## Reviewed seed coverage

Recent taxonomy work added reviewed Python suitability seed coverage for Core Language, Advanced Python, and Object-Oriented Programming. These reviewed rules are used by Blueprint defaults and generation planning so that suitability is not only theoretical documentation; it actively shapes recommended targets.

## Suitability and Blueprint coverage

Blueprint rows should use suitability to avoid generating bad combinations.

Example:

```text
Blueprint target:
Python / Lists / append returns None / predict_output / beginner
```

This is a strong row because:

- concept is beginner-relevant,
- output prediction tests the behavior well,
- the misconception is common,
- the answer is clear.

## Suitability and generation planner

The generation planner uses suitability to recommend targets.

For automatic generation:

- strong suitability = recommended,
- secondary suitability = recommended with lower priority,
- weak fit = visible but not automatically selected,
- not suitable = excluded.

## Suitability and future practice selection

Suitability can later improve public practice selection too.

When a user selects broad practice, Codiquiz can prefer questions where the question task type strongly matches the concept.

This helps practice feel more meaningful and less random.

## Admin controls

The admin should be able to inspect and adjust:

- concept/entity,
- question task type,
- suitability tier,
- suitability score,
- difficulty-specific weights,
- enabled/disabled status,
- explanation/reason.

## Example mappings

```text
Lists
- predict_output: strong
- code_understanding: strong
- bug_finding: strong
- conceptual: secondary

Inheritance
- code_understanding: strong
- bug_finding: strong
- scenario_reasoning: strong
- definition_check: secondary

Packaging
- scenario_reasoning: secondary
- definition_check: secondary
- predict_output: weak/manual-only
```
