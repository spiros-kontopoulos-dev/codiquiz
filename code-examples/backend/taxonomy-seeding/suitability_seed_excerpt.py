# Reviewed suitability seed excerpt
# Source: quiz-api/app/seed_modules/fields/programming_languages/python/suitability/reviewed/core_language/functions/closures.py (excerpt lines 1-95)
# Public portfolio excerpt; not standalone application code.

"""Reviewed suitability mappings for Closures.

Generated as the first full reviewed-profile layer for TAX 1.5b-2.
Each concept is explicitly assigned to a suitability profile; the shared profile
holds the question-type scores and difficulty weights.
"""

from __future__ import annotations

from app.seed_modules.fields.programming_languages.python.suitability.common import concept_suitability


CONCEPT_SUITABILITY = {
    "closures-bind-names-not-values": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: closures bind names not values.',
    ),
    "default-argument-captures-loop-value": concept_suitability(
        "loop_trace_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: default argument captures loop value.',
    ),
    "closures-capture-variables-not-values": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: closures capture variables not values.',
    ),
    "loop-created-closures-share-loop-variable": concept_suitability(
        "loop_trace_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: loop-created closures share loop variable.',
    ),
    "late-binding-appears-when-function-called-later": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: late binding appears when function called later.',
    ),
    "default-argument-can-freeze-current-value": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: default argument can freeze current value.',
    ),
    "factory-function-can-create-separate-binding": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: factory function can create separate binding.',
    ),
    "closures-capture-names-not-frozen-values": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: closures capture names not frozen values.',
    ),
    "loop-created-closures-can-share-the-final-loop-value": concept_suitability(
        "loop_trace_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: loop-created closures can share the final loop value.',
    ),
    "default-argument-can-freeze-a-loop-value": concept_suitability(
        "loop_trace_behavior",
        notes='Reviewed-profile mapping for Closures / Closure Binding Traps; concept: default argument can freeze a loop value.',
    ),
    "closure-keeps-state-after-outer-returns": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: closure keeps state after outer returns.',
    ),
    "closure-can-preserve-private-state": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: closure can preserve private state.',
    ),
    "function-closure-stores-cell-objects": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: function __closure__ stores cell objects.',
    ),
    "stateful-closures-can-replace-simple-classes": concept_suitability(
        "string_methods_api",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: stateful closures can replace simple classes.',
    ),
    "shared-closure-state-can-surprise-callers": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: shared closure state can surprise callers.',
    ),
    "closures-can-hold-references-and-extend-lifetime": concept_suitability(
        "copy_aliasing_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: closures can hold references and extend lifetime.',
    ),
    "closure-can-preserve-state-between-calls": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: closure can preserve state between calls.',
    ),
    "mutable-objects-in-closures-can-be-mutated-without-nonlocal": concept_suitability(
        "copy_aliasing_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: mutable objects in closures can be mutated without nonlocal.',
    ),
    "rebind-closed-over-name-requires-nonlocal": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Closure State; concept: rebind closed over name requires nonlocal.',
    ),
    "inner-functions-capture-enclosing-variables": concept_suitability(
        "scope_closure_behavior",
        notes='Reviewed-profile mapping for Closures / Nested Functions & Enclosing Scope; concept: inner functions capture enclosing variables.',
    ),
    "nested-functions-create-enclosing-scope": concept_suitability(
        "scope_closure_behavior",
