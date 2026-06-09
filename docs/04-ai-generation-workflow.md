# AI Generation Workflow

Codiquiz uses AI to generate candidate coding questions, but it does not blindly publish model output. The AI generation workflow is controlled, staged, validated, reviewed, and connected to the question-bank quality systems.

## Core rule

> OpenAI generates candidates. Codiquiz decides what gets accepted.

This rule keeps the platform safe from duplicate, repetitive, low-quality, or badly formatted generated questions.

## Generation planning

The workflow starts in the admin system. An admin chooses or receives recommended generation targets based on:

- technology,
- domain,
- module,
- topic,
- subtopic,
- concept,
- difficulty,
- question task type,
- requested count,
- suitability rules,
- Blueprint coverage gaps.

The generation planner should avoid random taxonomy combinations. It should prefer targets that are useful, under-covered, and suitable for the selected question task type.

## Generation target contract

A generation request should describe the exact learning target, not only a broad topic. A strong target includes:

- taxonomy path,
- concept or behavior,
- question task type,
- difficulty,
- answer format,
- requested count,
- suitability tier,
- Blueprint/gap reason,
- avoid-list or pattern guidance.

Example target:

```text
Python / Core Language / Data Structures / Lists / List Methods / append returns None
question task type: predict_output
difficulty: beginner
answer format: single_choice
reason: underfilled Blueprint row with strong suitability
```

## Prompt rules

Prompt rules are used to keep generated output consistent and reviewable. They are backend-controlled generation constraints, not frontend suggestions. They define how the model should behave for a specific taxonomy target and how Codiquiz expects the result to be structured.

The prompt should tell the model:

- the target technology and taxonomy path,
- the specific concept or behavior to test,
- the question task type,
- the difficulty,
- the expected answer format,
- whether code is required,
- how many answer options are needed,
- how explanations should be written,
- what patterns to avoid,
- how much variation is expected between requested questions,
- whether the question should focus on behavior, misconception, edge case, or debugging,
- which answer options should be plausible but clearly wrong.

Important prompt rules:

- Generate structured JSON, not free-form text.
- Keep `question_text` separate from `code_snippet`.
- Do not duplicate code inside the question text if a code snippet field exists.
- Provide one correct answer and plausible distractors.
- Use explanations that clarify the underlying concept.
- Respect the selected difficulty.
- Avoid patterns already covered by the avoid-list.
- Do not generate questions outside the requested taxonomy target.
- Do not generate multiple questions that only differ by variable names, literal values, or answer order.
- Prefer testable behavior over documentation-style trivia.

Prompt rules should be composed from reusable layers:

```text
system/provider safety rules
+ Codiquiz output JSON contract
+ technology-specific rules
+ question task type rules
+ taxonomy/concept target
+ difficulty guidance
+ avoid-list hints
+ batch variation instructions
```

This keeps prompt behavior consistent while still allowing each concept and question task type to receive focused guidance.

## Avoid-list guidance

Codiquiz should not send the entire database to OpenAI. Instead, it can pass compact avoid-list hints for the selected target area.

Example:

```text
Avoid generating questions similar to these already-covered patterns:
- len() on a flat list literal
- append() return value
- simple positive list index access
```

The avoid-list helps reduce repetitive generation before the model output even reaches the backend validation layer.

## Execution modes

Codiquiz supports two execution modes.

### Normal API mode

Normal API mode is used for smaller or immediate generation runs.

Flow:

```text
Admin starts generation
→ backend calls provider immediately
→ provider returns structured question JSON
→ backend validates and stores staged drafts
```

### Batch API mode

Batch API mode is used for larger asynchronous generation runs.

Flow:

```text
Prepare request jobs
→ Submit JSONL to OpenAI Batch API
→ Check provider status
→ Collect provider output/error files
→ Reconcile provider result lines into staged drafts
→ Admin review
```

Batch API uses many small request jobs so each result can be matched back to the correct target and generation batch.

## Batch API lifecycle states

Typical lifecycle:

```text
prepared
submitted
batch_processing
batch_completed
batch_results_collected
completed
```

Operational steps:

1. **Prepare** — create provider request jobs.
2. **Submit** — upload request JSONL and create OpenAI batch.
3. **Check status** — poll provider state and file IDs.
4. **Collect results** — download output/error JSONL and store result lines.
5. **Reconcile drafts** — parse successful result lines and create staged AI drafts.
6. **Review** — admin edits, rejects, or approves drafts.

## Provider output contract

The provider response should be structured so the backend can validate and store it without guessing. A generated question should include:

- question text,
- optional code snippet,
- answer options,
- correct answer,
- explanation,
- difficulty,
- question task type,
- taxonomy/concept metadata when available,
- optional pattern/misconception hints.

The backend still treats model output as untrusted. It parses, validates, normalizes, and checks it before draft review.

## Draft storage and normalization

Generated provider output is normalized before becoming staged drafts.

Normalization includes:

- JSON parsing,
- schema validation,
- field cleanup,
- question text cleanup,
- code snippet extraction,
- answer option validation,
- explanation validation,
- difficulty/question type assignment,
- generation metadata tracking.

Important formatting rule:

```text
question_text should contain the question prompt.
code_snippet should contain code.
```

If the model puts fenced code inside the question text and a code snippet is also present, the backend should remove the duplicated code from the question text. If the model puts code only inside the question text, the backend can extract it into `code_snippet`.

## Quality checks before review

Before or during review, generated drafts can receive checks such as:

- exact duplicate signature,
- normalized duplicate signature,
- code signature,
- same-concept similarity,
- related-pattern note,
- avoid-list/repetition warning,
- future semantic embedding similarity.

The goal is not to reject everything automatically. The goal is to give the admin enough context to approve, edit, reject, or regenerate intelligently.

## Draft review and approval

Generated questions are staged as drafts.

Admin actions:

- review content,
- inspect warnings,
- edit prompt/code/options/explanation,
- reject weak drafts,
- approve good drafts.

Approved drafts become real question-bank entries. The approved question bank is treated as the source of truth for future duplicate checks and serving.

## Model profiles, pricing, and cost metadata

Codiquiz treats model selection as an admin-facing profile system instead of scattering raw provider model names throughout the UI.

Typical profile roles include:

- **Budget Draft** — low-cost generation for broad coverage expansion.
- **Balanced Draft** — a middle option for everyday generation quality.
- **Premium / Advanced** — stronger model choice for harder or more important generation targets.
- **Validation Only** — lower-cost validation/review support where applicable.

Each profile stores a stable Codiquiz key, while the configured provider/model can be changed from admin settings. This allows the platform to keep historical metadata stable while still allowing model upgrades over time.

The admin settings layer exposes:

- provider,
- configured model,
- profile purpose,
- enabled status,
- Normal API compatibility,
- Batch API compatibility,
- input cost per 1M tokens,
- output cost per 1M tokens,
- Batch API input/output costs,
- relative cost comparison against the lowest-cost model in the catalog.

Generation batches and drafts track useful metadata such as:

- execution mode,
- model profile,
- resolved provider model,
- prompt/input tokens,
- completion/output tokens,
- total tokens,
- estimated cost,
- actual cost when provider usage data is available,
- number of request jobs,
- number of successful provider result lines,
- number of failed/unmatched lines,
- number of drafts created,
- review outcomes such as approved/rejected/pending.

Before a run, Codiquiz estimates token usage and cost with `tiktoken` and the configured model pricing. After a run, actual cost accounting should prefer provider-returned usage tokens.

The Cost & Quality dashboard uses this metadata to summarize approval rate, rejection rate, duplicate-warning rate, total tracked cost, cost per generated draft, cost per approved question, and performance by profile/provider/model.

## Chunking, retries, and variation control

Larger generation runs are split into smaller provider calls or Batch API request jobs. This gives Codiquiz better control over failures, retries, and result matching.

Useful policies:

- keep each provider request small enough to validate clearly,
- retry failed chunks without repeating successful chunks,
- pass compact avoid-list hints to later chunks,
- avoid asking for too many similar questions in one prompt,
- track success, failure, unmatched lines, generated count, and cost per batch.

## Automation

Batch API lifecycle can be managed manually from the admin detail page or automatically through scheduled workers.

Current automation direction:

- Celery Beat runs bounded scanner passes.
- Scanner finds eligible Batch API batches.
- Worker checks status, collects results, and reconciles drafts when safe.
- Dry-run mode can report candidates without processing.
- Manual buttons remain available as override/debug controls.

## Future direction

Future AI generation will become more Blueprint-driven:

```text
Blueprint detects gaps
→ generation candidates are ranked
→ batches are created
→ Batch API submits jobs
→ workers poll/collect/reconcile
→ drafts enter review
→ approved question bank grows
```
