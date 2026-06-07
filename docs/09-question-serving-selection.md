# Question Serving and Selection Engine

The Question Serving and Selection Engine decides which approved questions a user receives.

This is different from AI generation. Generation creates candidate content. Serving decides how approved content is delivered to users.

## Purpose

The engine should:

- avoid repetition,
- balance coverage,
- support fixed sessions,
- support endless/rolling practice,
- respect quiz rules,
- personalize practice later,
- target weak concepts for registered users,
- avoid near-duplicates inside the same session.

## Serving styles

### Fixed/prepared session

The backend selects exactly N questions before the session starts.

Best for:

- normal quizzes,
- timed attempts,
- fair scoring,
- fixed practice sessions.

### Rolling pool endless mode

The backend prepares a buffer of questions, serves from it, and refills when low.

Best for:

- quick drill mode,
- browsing/crawling mode,
- adaptive practice.

Important correction:

> Dynamic serving does not mean recalculating one question from scratch every few seconds.

Even endless mode should use a rolling pool to avoid repeated heavy policy calculations.

Example:

```text
User starts Python → Lists → Slicing quick practice
Backend prepares 50 suitable questions
User clicks Next from the local/session pool
When 40-45 are consumed, backend refills another 40-50
```

## Selection policies

The engine can consider:

- selected taxonomy scope,
- difficulty,
- question task type,
- approved status,
- content priority,
- suitability score,
- user seen-history,
- recent repetition,
- near-duplicate avoidance,
- weak-concept boost,
- variety factor,
- overexposure penalty,
- curated quiz rules.

## Modes

### Static quiz

Uses curated question IDs assigned to a quiz.

### Normal practice session

Builds a fixed question set at session start from selected filters.

### Quick drill / crawl mode

Uses a rolling pool from selected taxonomy path/search.

### Adaptive learning mode

Uses block-based pool refills based on recent answers and mastery.

## Service boundary

The first version should live inside `quiz-api`, not as a separate microservice.

Reason: it depends heavily on the main product database:

- questions,
- users,
- sessions,
- attempts,
- taxonomy,
- concepts,
- approval status,
- user history.

Possible internal services:

```text
quiz-api/app/services/question_selection_service.py
  select_question_set_for_session(...)

quiz-api/app/services/question_serving_service.py
  create_rolling_pool(...)
  refill_rolling_pool(...)
  get_next_from_pool(...)
```

## Future data needs

- user question attempts,
- session question IDs,
- rolling question pools,
- question similarity matches,
- user concept mastery,
- overexposure counters,
- serving history.

## Future selection formula

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

This lets Codiquiz move from random practice to intelligent practice.
