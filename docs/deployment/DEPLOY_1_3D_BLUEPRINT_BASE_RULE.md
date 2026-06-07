# DEPLOY 1.3d — Default Blueprint Base Rule

## Why this patch exists

The preview deployment revealed that a fresh database can have taxonomy,
importance, suitability, and Blueprint target-budget data loaded while still
showing an empty Blueprint Coverage workspace.

The reason is that the Blueprint coverage engine expands active `blueprint_rules`
into concrete concept/question-type/difficulty cells. Without at least one active
base rule, the coverage layer has nothing to expand.

## Default rule

Fresh deployments now seed one active global Blueprint base rule:

```text
scope_level: global
scope_key: global
question_type_id: null
difficulty: null
target_count: 2
priority: 0
source: seed
is_active: true
```

`target_count = 2` is the agreed baseline for Codiquiz preview/production
coverage. Suitability and target-budget policy still decide the final automatic
targets; the global rule simply gives the engine a broad base rule to expand.

## Idempotency

The seed is safe to rerun:

- If an active global/all/all rule already exists, it is respected.
- If the active global/all/all rule was created by the seed, the seed refreshes
  it back to the canonical baseline of `target_count = 2`.
- If no active global/all/all rule exists, the seed creates one.

## Preview verification

After deploying and restarting `quiz-api`, verify:

```sql
select id, scope_key, scope_level, question_type_id, difficulty, target_count, priority, source, is_active
from blueprint_rules
where scope_key = 'global'
order by id;
```

The Blueprint Coverage admin page should show cells instead of an empty result.
