# User Accounts and Progress System

Codiquiz is designed to support both anonymous practice and registered learner accounts. The early alpha can keep quick practice lightweight, while the long-term platform uses registered accounts to store progress, scoring, mastery, and personalization data.

## Purpose

The user system turns Codiquiz from a static question bank into a learning platform. Once the system knows what a learner has answered, it can avoid repetition, measure progress, recommend weak concepts, and calculate fair ranking scores.

## User modes

### Anonymous practice

Anonymous practice allows a visitor to start quickly without an account. It is useful for public demos, quick drills, and low-friction exploration.

Possible anonymous data:

- temporary practice session,
- browser/session seen-question history,
- lightweight answer history for the current session,
- no long-term ranking or mastery.

### Registered learner

A registered learner account stores long-term progress.

Planned capabilities:

- saved practice sessions,
- persistent attempt history,
- scoring history,
- topic and concept mastery,
- seen-question history,
- weak-concept recommendations,
- future ranking and leaderboards.

### Admin user

An admin user is a protected role for managing content and platform operations.

Admin capabilities include:

- taxonomy management,
- question-bank management,
- AI generation planning,
- draft review and approval,
- Blueprint coverage planning,
- suitability rules,
- async automation visibility.

## Attempt history

An attempt is one answer by one user to one question. Useful attempt fields include:

- user/session id,
- question id,
- selected answer,
- correctness,
- time taken,
- difficulty,
- question task type,
- taxonomy path,
- concept id,
- created timestamp.

Attempt history powers scoring, mastery, adaptive practice, and question quality metrics.

## Seen-question history

Seen-question history helps Codiquiz avoid showing the same question or near-duplicate questions too often.

This connects to:

- question serving and selection,
- rolling pools,
- anti-repetition,
- semantic similarity warnings,
- adaptive practice.

## Progress and mastery

A future mastery profile can track user strength at different levels:

```text
Python / Lists / indexing: strong
Python / Lists / slicing: weak
Python / Lists / mutation: needs practice
```

Mastery should become more precise over time, moving from broad topic accuracy to concept-level learning signals.

## Ranking score

A future ranking score can combine:

- correctness,
- difficulty-weighted points,
- accuracy,
- consistency,
- streaks,
- topic/concept breadth,
- repeat penalties,
- time efficiency where appropriate.

The score should reward meaningful learning and broad skill, not only repeated easy questions.

## Relationship to other Codiquiz engines

The user system connects many future engines:

```text
user attempts
→ scoring
→ mastery
→ adaptive serving
→ better practice recommendations
→ question quality metrics
```

It also helps the question bank improve because aggregate user answers can reveal which questions are too easy, too hard, confusing, or poorly written.

## Implementation direction

This should start inside `quiz-api`, because it depends on users, quiz sessions, questions, answers, taxonomy, scoring, and practice selection. Some aggregate analytics can later move to worker jobs or an analytics service.
