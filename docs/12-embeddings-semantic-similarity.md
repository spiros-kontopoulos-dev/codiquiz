# Embeddings and Semantic Similarity

Codiquiz currently uses deterministic duplicate detection. The future semantic layer will use embeddings and PostgreSQL/pgvector to detect near-duplicates that deterministic signatures cannot catch.

## What embeddings are

An embedding is a numeric vector representation of text meaning.

Plain text search asks:

```text
Does this row contain these words?
```

Vector search asks:

```text
Which rows have similar meaning, even if the words differ?
```

Example:

```text
Question A: What is the output of len([1, 2, 3])?
Question B: What does Python print when calling len on a three-item list?
```

These are different strings but they test almost the same idea.

## Generation and embeddings are separate

Question generation and embedding creation are separate operations.

```text
OpenAI generation API
→ structured question JSON

OpenAI embeddings API
→ vector numbers representing meaning
```

Future flow:

```text
OpenAI generates draft question
→ Codiquiz stores staged draft
→ Codiquiz builds embedding text
→ Embeddings API returns vector
→ Store vector in PostgreSQL/pgvector
→ Search similar approved questions/drafts
→ Show admin similarity warnings
```

## Why pgvector fits Codiquiz

pgvector is a natural first vector implementation because Codiquiz already uses PostgreSQL.

Benefits:

- keeps relational question metadata and vectors close together,
- avoids adding a separate vector database too early,
- supports nearest-neighbor vector search,
- is simple for deployment compared with another infrastructure service,
- is strong portfolio material for AI engineering.

## Embedding text design

Bad embedding input creates weak similarity results. Codiquiz should build a stable text representation from multiple fields.

Possible embedding text:

```text
Technology: Python
Taxonomy path: Core Language / Data Structures / Lists / List Methods
Concept: append returns None
Question type: predict_output
Difficulty: beginner
Prompt: What is printed by the following code?
Code: numbers = [1, 2, 3]; result = numbers.append(4); print(result)
Correct answer: None
Explanation: append mutates the list and returns None.
```

## Future schema direction

Possible tables:

```text
question_embeddings
- id
- question_id
- embedding_model
- embedding_vector
- source_text_hash
- created_at
- updated_at

ai_generated_question_embeddings
- id
- generated_question_id
- embedding_model
- embedding_vector
- source_text_hash
- created_at
```

The `source_text_hash` prevents unnecessary re-embedding when the content has not changed.

## Similarity warning workflow

Future admin review flow:

```text
new AI draft
→ generate embedding
→ search nearest approved questions
→ search nearest live drafts
→ store similarity matches
→ show top matches in review UI
```

Warnings should include:

- matched question ID,
- similarity score,
- taxonomy context,
- matched prompt/code summary,
- warning severity,
- decision support.

## Severity model

Embeddings should not replace deterministic duplicate checks.

Recommended layers:

- exact/full signature = hard duplicate,
- same concept + strong code/prompt match = hard duplicate,
- different concept + similar pattern = related note,
- embedding nearest neighbor = tunable semantic warning,
- borderline cases = admin review.

## Async processing

Embedding work should run through workers.

Use cases:

- embedding new drafts,
- embedding approved questions,
- backfilling existing bank,
- refreshing embeddings after edits,
- semantic similarity maintenance.

OpenAI Batch API may also be useful for large embedding backfills.
