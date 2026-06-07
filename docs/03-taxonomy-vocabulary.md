# Taxonomy and Vocabulary

Codiquiz uses precise vocabulary because many systems depend on the same concepts: generation, Blueprint coverage, suitability, duplicate detection, serving, scoring, and future semantic similarity.

## Taxonomy hierarchy

### Technology

A programming ecosystem or subject area.

Examples:

- Python,
- JavaScript,
- SQL.

### Domain

A broad area inside a technology.

Examples for Python:

- Core Language,
- Standard Library,
- OOP,
- Testing.

### Module

A major learning area inside a domain.

Examples:

- Data Structures,
- Functions,
- Control Flow.

### Topic

A focused area inside a module.

Examples:

- Lists,
- Dictionaries,
- Loops.

### Subtopic

A smaller grouping inside a topic.

Examples:

- List Methods,
- List Slicing,
- Dictionary Iteration.

### Concept

A testable behavior, rule, trap, misconception, or comparison.

A concept is not just an API item. Codiquiz is a practice platform, not a reference website.

Examples:

- `append()` mutates the list in place,
- `append()` returns `None`,
- `append` vs `extend`,
- shallow copy vs reference,
- list slicing creates a new list,
- loop variable scope behavior,
- closure captures free variables.

Good concept design asks:

- What behavior is being tested?
- What misconception might the learner have?
- What bug or trap does this concept produce?
- What reasoning step does the question require?

## Question vocabulary

### Question task type

The cognitive task the user must perform.

Examples:

- predict output,
- code understanding,
- bug finding,
- fill missing code,
- conceptual reasoning,
- edge-case reasoning,
- scenario reasoning.

### Answer format

How the user answers.

Examples:

- single choice,
- multiple choice,
- true/false,
- text input,
- code input,
- ordering,
- matching.

Current Codiquiz questions can all be single-choice while still having different question task types.

Example:

```text
Question task type: predict_output
Answer format: single_choice
```

## AI generation vocabulary

### AI generation batch

A group of generation requests created from an admin generation plan.

### Execution mode

How a generation batch is sent to the provider.

Current modes:

- Normal API,
- Batch API.

### Normal API mode

Immediate provider calls for smaller generation runs.

### Batch API mode

Asynchronous provider workflow for larger runs.

Lifecycle:

```text
prepared → submitted → provider completed → collected → reconciled
```

### Execution job

A small provider request unit inside a generation batch.

Batch API uses many small jobs so individual provider outputs can be matched back to the correct generation target.

### Provider result line

One result line returned by the provider output/error file.

### AI draft / staged draft

A generated question that is not yet approved. Drafts are reviewed, edited, rejected, or approved by an admin.

### Approved question

A question that belongs to the real question bank and can be served to users.

The approved question bank is the source of truth for published content.

## Quality engine vocabulary

### Signature

A deterministic normalized representation of the question text/code used for duplicate detection.

### Fingerprint

The identity of one question at the semantic/pattern level.

A fingerprint may include:

- concept,
- question task type,
- structural pattern,
- skill,
- misconception,
- difficulty,
- code signature.

### Duplicate

A candidate that tests the same idea as an active approved question or live pending draft.

Changing wording, variable names, values, or answer order does not automatically make a question unique.

### Related pattern

A non-blocking similarity note. It means the question is related to an existing pattern, but not necessarily a hard duplicate.

### Avoid-list

A compact list of overused or risky patterns passed into prompt context so the model avoids generating more of the same.

### Canonical duplicate source

The preferred source that later duplicates should point to.

Current policy:

- approved question bank is the source of truth,
- oldest live pending draft can be canonical if no approved question exists,
- archived batches/questions do not block future content.

## Blueprint vocabulary

### Blueprint

The content plan: what the question bank should contain.

It answers:

- What do we need?
- Where are the gaps?
- What should OpenAI generate next?

### Blueprint row

A target row representing a desired amount of content for a specific combination.

Example:

```text
Python / Core Language / Data Structures / Lists / append returns None /
predict_output / beginner

target_count = 5
```

### Target count

How many approved questions should exist for a Blueprint row.

### Approved count

How many approved questions currently satisfy the Blueprint row.

### Pending count

How many AI drafts are waiting for review and may satisfy the Blueprint row.

### Generation gap

How many questions are still missing.

```text
generation_gap = target_count - approved_count - pending_count
```

### Content priority score

How important, useful, popular, or strategically valuable a taxonomy entity is.

### Question type suitability score

How well a question task type fits a taxonomy entity or concept.

### Difficulty weight

How valuable a taxonomy entity/question type is at a specific difficulty.

### Generation priority score

A computed score that ranks what should be generated next.

It can combine:

- content priority,
- suitability,
- difficulty weight,
- generation gap,
- generation reliability,
- strategic weighting.

## Semantic similarity vocabulary

### Embedding

A numeric vector representation of a text's meaning.

### Vector search

Searching for nearest neighbors in vector space, useful for finding semantically similar questions even if wording differs.

### pgvector

A PostgreSQL extension that can store and search embedding vectors.

### Semantic duplicate warning

A future warning shown when an AI draft is semantically close to an approved question or another draft.

## Async vocabulary

### Worker

A background process that runs tasks outside normal HTTP request/response flow.

### Celery task

A named background function executed by a worker.

### Celery Beat

A scheduler that periodically enqueues Celery tasks.

### Task run

A logged execution of a worker task, including status, duration, dry-run/live mode, target batch, and error message.

### Dry-run mode

The worker reports what it would process without making changes.

### Live mode

The worker performs the actual lifecycle action.

## Serving and scoring vocabulary

### Fixed session

A quiz/practice session where the question set is selected before the session starts.

### Rolling pool

A buffer of questions prepared for endless or quick-drill practice and refilled when low.

### Mastery

A user's measured strength or weakness by topic/concept.

### Question quality score

A score based on real usage data such as success rate, solve time, report rate, and distractor behavior.

### Ranking score

A user score that can later combine correctness, difficulty, time, streaks, question type, and retries.

## Question lifecycle vocabulary

### Draft

A generated or imported candidate question that has not been approved yet. Drafts can be edited, rejected, approved, or marked with duplicate/similarity warnings.

### Approved question

A canonical question-bank item that can be served to users. Approved questions are the source of truth for duplicate checks and future serving.

### Rejected draft

A generated candidate that was reviewed and intentionally not accepted. Rejections can later help measure model quality, prompt quality, and generation reliability.

### Archived batch or archived question

Archived content is preserved for history but should not act as an active duplicate blocker or generation source.

## AI generation vocabulary

### Model profile

A named backend configuration that maps a generation workflow to a provider model and generation settings. Model profiles allow the admin UI to show which model strategy is being used without hardcoding provider details into the frontend.

### Generation batch

A group of requested AI questions created from one admin generation plan or automated generation target. A batch can use Normal API execution or Batch API execution.

### Execution job

A smaller provider request inside a generation batch. Batch API mode uses many small jobs so provider result lines can be matched back to the correct target and batch.

### Provider result line

One output or error line returned by the provider during Batch API collection. Codiquiz parses these lines and reconciles successful ones into staged drafts.

### Reconciliation

The process of turning collected provider result lines into staged AI drafts linked to the original generation jobs.

### Prompt rule

A backend rule that shapes what the model should generate: target taxonomy path, concept, difficulty, question task type, answer format, output JSON shape, code formatting, explanation style, and avoid-list constraints.

### Avoid-list

A compact list of overused or similar patterns passed to the model so it avoids generating repetitive candidates. Avoid-lists are prompt guidance, not a replacement for backend duplicate checks.

## Blueprint vocabulary

### Blueprint

The content plan: what the question bank should contain. It is different from the current question bank.

### Blueprint row

A target row such as:

```text
Python / Core Language / Data Structures / Lists / append returns None / predict_output / beginner
```

A row can have a target count, approved count, pending draft count, generation gap, suitability score, and generation priority score.

### Blueprint rule

A rule that defines or adjusts target counts and priority for a taxonomy entity, difficulty, and question task type. Rules can be global defaults, entity-specific overrides, or disabled targets.

### Coverage gap

The missing amount between desired content and existing/pending content.

```text
generation_gap = target_count - approved_count - pending_review_count
```

### Generation priority score

A computed score that ranks what should be generated next by combining content priority, suitability, difficulty relevance, current gap, and generation reliability.

## Similarity and semantic vocabulary

### Fingerprint

The identity/signature of one question. It helps answer: is this generated candidate really new, or is it the same idea as something already approved or pending?

### Deterministic signature

A repeatable hash or normalized representation of prompt/code/content. Useful for exact or near-exact duplicate checks.

### Pattern

A structural idea inside a question, such as `len(list_literal)` or `append_returns_none`. Patterns help detect duplicates even when variable names or literal values change.

### Related-pattern note

A non-blocking warning that two questions share a similar implementation pattern while testing different concepts.

### Embedding

A numeric vector representation of question meaning. Embeddings will support future semantic similarity search with PostgreSQL/pgvector.

### Semantic similarity

Similarity by meaning, not exact text. For example, two different prompts about `len()` on a three-item list may be semantically near-duplicates.

## User and learning vocabulary

### User

A person using Codiquiz. A user can be anonymous for quick practice or registered for persistent progress.

### Anonymous session

A temporary practice session that does not require account creation.

### Registered learner

A future user account with saved progress, attempt history, scoring, and mastery data.

### Admin user

A protected user role for managing taxonomy, question bank content, AI generation, draft review, Blueprint planning, and automation settings.

### Practice session

A user-facing run of selected questions. A session can be fixed/prepared or later powered by a rolling pool.

### Attempt

One user answer to one question. Attempts can store selected answer, correctness, time taken, difficulty, question type, and taxonomy context.

### Seen-question history

A record used to avoid showing the same or near-duplicate questions too often.

### Ranking score

A future user score that can combine correctness, difficulty, consistency, streaks, and possibly time efficiency.

### Mastery profile

A per-topic or per-concept estimate of user strength, weakness, and learning progress.

### Question quality metric

A signal calculated from real usage data, such as success rate, average solve time, report rate, distractor quality, or discrimination score.
