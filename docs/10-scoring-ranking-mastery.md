# Scoring, Ranking, and Mastery Engine

The Scoring, Ranking, and Mastery Engine turns raw user answers into meaningful progress.

It is a future engine, but it is central to the long-term Codiquiz product. It depends on the user/accounts layer because persistent attempts are required before real progress, mastery, and ranking can be calculated.

## Purpose

The engine should support:

- fair scoring,
- session scores,
- difficulty-weighted points,
- leaderboards,
- topic/concept mastery,
- question quality metrics,
- real difficulty calibration,
- adaptive practice signals.

## User system dependency

Before advanced scoring can be meaningful, Codiquiz needs persistent user data:

- registered learner accounts,
- practice sessions,
- user question attempts,
- seen-question history,
- selected answers and correctness,
- time taken,
- taxonomy/concept metadata,
- difficulty and question task type metadata.

Anonymous sessions can still support quick practice, but registered users unlock long-term progress, mastery, and ranking.

## User scoring

Possible scoring factors:

- correctness,
- difficulty multiplier,
- time taken,
- streaks,
- question task type,
- attempts/retries,
- hint usage later,
- session mode.

A simple v1 can start with:

```text
score = correctness_points * difficulty_multiplier
```

Later scoring can add time and streak signals without making the system unfair.

## Ranking score

A future ranking score should not be only total correct answers. It can combine:

- correctness,
- difficulty-weighted points,
- accuracy,
- consistency,
- streaks,
- topic/concept breadth,
- recency windows such as weekly score,
- anti-farming limits for repeated questions.

Example direction:

```text
ranking_score =
  difficulty_weighted_points
* accuracy_factor
* consistency_factor
* variety_factor
- repeat_penalty
```

The exact formula should be tuned after real user data exists.

## Mastery tracking

Mastery should eventually work at concept level, not only broad topic level.

Example:

```text
Python / Lists / indexing: 86% strong
Python / Lists / slicing: 48% weak
Python / Lists / mutation: 55% needs practice
```

This allows the serving engine to target weak concepts.

## Question quality metrics

Codiquiz can use real user behavior to evaluate question quality.

Metrics:

- actual difficulty from success rates,
- average solve time,
- wrong-answer distribution,
- report rate,
- discrimination score,
- approval/rejection history,
- edit history,
- overexposure count.

## Ranking types

Future ranking systems can include:

- user leaderboards,
- weekly points,
- accuracy rankings,
- streak rankings,
- difficulty-weighted rankings,
- topic-specific rankings,
- mastery ranks,
- question quality rankings.

## Service design

Start inside `quiz-api` as internal services:

```text
quiz-api/app/services/scoring_service.py
  score_answer(...)
  calculate_session_score(...)

quiz-api/app/services/mastery_service.py
  update_user_mastery(...)

quiz-api/app/services/question_quality_service.py
  recalculate_question_metrics(...)

quiz-api/app/services/ranking_service.py
  calculate_leaderboard(...)
```

Some aggregate analytics can later move to workers or an analytics-service.

## Implementation stages

1. Basic answer scoring.
2. Attempt history persistence.
3. Mastery by topic.
4. Mastery by concept.
5. Question quality metrics.
6. Ranking/leaderboards.
7. Adaptive serving integration.

## Why this matters

AI generation creates content. Scoring and mastery turn user interaction into learning intelligence.

Together with Blueprint and serving systems, this lets Codiquiz learn which questions work, which concepts are weak, and what content should be improved next.
