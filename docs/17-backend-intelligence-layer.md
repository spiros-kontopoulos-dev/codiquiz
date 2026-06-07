# Backend Intelligence Layer

The Backend Intelligence Layer is the part of Codiquiz that decides what content should exist and what the AI should generate next.

It is different from the Backend Quality Engine:

```text
Backend Quality Engine = protects quality after/generated content exists
Backend Intelligence Layer = plans useful content before generation happens
```

Codiquiz should not spend tokens generating random combinations. It should generate the most useful missing questions for the question bank.

## Why this layer exists

A large taxonomy creates many possible generation targets:

```text
concept × question task type × difficulty
```

Most combinations are not equally valuable. Some concepts are foundational, some are advanced but important, some are niche, and some should not be tested with certain question types at all.

The intelligence layer answers questions such as:

- Which Python concepts matter most?
- Which question task types fit each concept?
- Which difficulties make sense for that concept/type pair?
- How many questions should exist for this cell?
- Is the cell already covered by approved or pending content?
- Which missing cells should be generated first?

## Current implemented signals

### Concept importance

Concept importance scores the educational value of concepts. It helps distinguish core concepts from standard, niche, or excluded content.

Typical tiers:

```text
core
standard
niche
excluded
```

Importance is used by coverage and generation planning so Codiquiz does not treat every concept as equally valuable.

### Question-type suitability

Suitability rules describe how well a question task type fits a concept.

Current planning categories:

```text
strong / recommended
secondary / recommended with lower priority
weak / manual-only
not suitable / excluded from automatic generation
```

This prevents low-value targets, such as generating algorithmic-complexity questions for simple API-return behavior concepts.

### Difficulty weighting and blocking

Some concept/type combinations are strong at one difficulty and weak or invalid at another.

Examples:

- Beginner should focus on core behavior and common misconceptions.
- Intermediate can handle more trace/debug/design reasoning.
- Advanced should be used only when the concept truly supports advanced reasoning.

Difficulty-specific weights allow the generation planner to recommend good difficulties and block unsuitable ones.

### Blueprint default targets

The Blueprint system uses importance + suitability to create default target counts.

Example target direction:

```text
core concept + strong suitability      → higher target count
core concept + secondary suitability   → smaller target count
standard concept + strong suitability  → medium target count
niche concept                          → low/manual-friendly target count
not suitable                           → no automatic target
```

This gives the question bank an intentional shape instead of a flat distribution.

### Coverage and generation priority

Coverage is computed by comparing desired targets against current approved questions and pending AI drafts.

Generation priority combines signals such as:

```text
concept importance
question-type suitability
difficulty weight
approved question count
pending draft count
coverage gap
```

The result is a ranked list of useful missing content.

## Admin intelligence views

The current admin layer exposes this through focused work queues and audit pages:

- Importance audit views.
- Coverage audit views.
- Blueprint default target preview.
- Focused coverage rows.
- Top generation candidates.
- Suitability-aware AI Generation Create flow.
- Difficulty guidance and blocked-difficulty warnings.

The admin can inspect why a target is recommended instead of blindly trusting the generator.

## How it connects to AI generation

Current flow:

```text
Importance + suitability + difficulty weights
→ Blueprint default target cells
→ coverage gap calculation
→ generation priority ranking
→ Blueprint candidates in AI Generation Create
→ AI drafts
→ Backend Quality Engine checks
→ admin review
→ approved question bank
```

This makes Codiquiz an AI-assisted content planning system, not only an OpenAI wrapper.

## Future direction

The next natural extension is automatic generation from high-priority Blueprint gaps.

Future automation can:

- select top candidate cells,
- respect budget/model profile limits,
- include avoid-list hints,
- create normal or Batch API jobs,
- pause when enough pending drafts already exist,
- update coverage after approval.

The important principle remains the same: Codiquiz should generate where the bank needs useful content, not where generation is merely possible.
