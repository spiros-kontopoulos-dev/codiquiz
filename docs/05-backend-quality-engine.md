# Backend Quality Engine

The Backend Quality Engine protects Codiquiz from turning into a large pile of duplicate, repetitive, or low-quality AI-generated questions.

It is the quality layer between AI generation and the approved question bank.

## Purpose

The Backend Quality Engine answers questions like:

- Is this generated question already covered?
- Is it a duplicate of an approved question?
- Is it a duplicate of another live AI draft?
- Does it test the same concept/pattern with only superficial changes?
- Is this pattern already overused?
- Should the reviewer see a blocking duplicate warning or a light related-pattern note?

## Semantic uniqueness rule

Codiquiz aims for semantic uniqueness, not text uniqueness.

Superficial changes do not automatically create a new question:

- reworded prompt,
- different variable names,
- different list values,
- shuffled answer order,
- small formatting differences.

Example:

```python
x = [1, 2, 3]
print(len(x))
```

and

```python
values = [4, 5, 6]
print(len(values))
```

are different strings but may test the same semantic pattern: `len(list_literal)`.

## Layered duplicate strategy

Codiquiz uses a layered approach.

### Exact signatures

Catch identical prompts/code.

### Normalized signatures

Catch formatting, casing, punctuation, whitespace, and simple text variants.

### Code signatures

Catch code snippets with the same structure but different literals or variable names.

### Concept/pattern matching

Catch questions that test the same concept and structural pattern.

### Related-pattern notes

Show non-blocking reviewer context when a question is related to existing patterns but not a hard duplicate.

### Future embedding similarity

Use vector similarity to detect semantically similar questions that deterministic checks miss.

## Active duplicate source policy

Only active content should block future content.

Active sources:

- active approved question-bank questions,
- pending AI drafts from non-archived batches,
- pending same-batch drafts from the current active batch.

Excluded sources:

- archived AI batches,
- approved AI drafts as draft sources,
- rejected/non-pending drafts,
- archived/inactive question-bank questions.

The approved question bank is the source of truth.

## Canonical duplicate policy

When multiple live pending drafts are similar, the oldest live pending draft can become the canonical source.

Example:

```text
Draft 402 = clean canonical draft
Draft 403 = duplicate of 402
Draft 404 = duplicate of 402
```

If draft 402 is rejected or archived, another live draft can become canonical.

If a canonical draft is approved into the question bank, the approved question becomes the canonical source for future duplicates.

## Same-concept vs different-concept policy

Same concept + strong prompt/code similarity:

```text
hard duplicate / blocking warning
```

Different concept + broad pattern similarity:

```text
related-pattern note / non-blocking reviewer context
```

This prevents overblocking while still giving reviewers useful context.

## Avoid-list support

The avoid-list is used before generation. It gives the model compact guidance about patterns that are already overused.

Example:

```text
Avoid generating new questions similar to:
- len(list_literal)
- append returns None
- simple positive indexing
```

The avoid-list should be compact. It should not include the full database or huge prompt context.

## Anti-repetition inside generated batches

The system should also compare drafts inside the same generated batch.

This prevents one generation run from producing many variations of the same idea.

## Answer shuffling rule

Answer option order belongs to the serving system, not duplicate database rows.

Store one canonical question and shuffle answer display order per user/session later.

This avoids creating duplicate DB rows just to show different option orders.

## Review workflow

Quality warnings should help the admin reviewer.

A draft can be:

- clean,
- duplicate blocked,
- related-pattern noted,
- warning state,
- needs review.

The admin can then:

- approve,
- reject,
- edit,
- regenerate,
- use warning context to decide.

## Future upgrade: semantic similarity

The deterministic system is the first layer. Later, embeddings and pgvector can provide semantic similarity warnings.

Future flow:

```text
new draft
→ build embedding text
→ create embedding vector
→ find nearest approved questions/drafts
→ show top matches and similarity scores
```

Embedding warnings should start as reviewer assistance, not automatic rejection.
