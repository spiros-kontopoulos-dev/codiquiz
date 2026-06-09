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

A fixed session selects questions up front, stores the session shape, and then serves from that prepared list.

This is useful for:

- static quizzes,
- quick practice sessions,
- custom practice sessions,
- repeatable review.

### Quick Practice

Quick Practice is the fastest public entry point. It focuses on a small set of choices such as technology, domains, difficulty, and session settings, then starts a practice session without making the user navigate the full taxonomy.

### Custom Practice

Custom Practice is the deeper targeting flow. It can start from a taxonomy page or from the practice landing page, then narrow by technology, domain, module, topic, subtopic, and concept focus.

### Try Concept

Try Concept is a lightweight concept-level flow. A user can open it directly from a technology/taxonomy concept row or search with Concept Finder. The selected concept can show approved-question availability and style choices before serving a single focused question with feedback.

### Public quizzes

Public quiz cards can be filtered by technology and can be promoted or marked coming soon. Quizzes are more curated and fixed than practice sessions.

### Rolling pool endless mode

A rolling pool keeps selecting new questions while the user continues. It should avoid recently seen questions, balance difficulty, and adapt to user performance.

This is a future-serving style.

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

A curated quiz with a fixed question set or fixed selection rules. Public quiz cards now carry technology metadata so the list can be filtered by technology.

### Quick Practice

A fast public practice mode for users who want to start quickly with minimal configuration.

### Custom Practice

A deeper public practice mode for users who want to choose taxonomy targets such as module, topic, subtopic, or concept.

### Try Concept

A lightweight concept-focused mode for trying one concept at a time. Concept Finder and technology pages can route users into this mode.

### Adaptive learning mode

A future registered-user mode that uses attempts, mastery, and seen-question history to choose the next best question.

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
