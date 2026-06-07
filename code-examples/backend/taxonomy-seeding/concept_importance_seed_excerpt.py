# Taxonomy seed helper with inline importance
# Source: quiz-api/app/seed_modules/common.py (excerpt lines 1-72)
# Public portfolio excerpt; not standalone application code.

from __future__ import annotations

from typing import Any

NodeData = dict[str, Any]


def concept(
    slug: str,
    name: str,
    *,
    priority: str = "important",
    content_status: str = "active",
    importance: int | None = None,
    importance_reason: str | None = None,
) -> NodeData:
    data: NodeData = {
        "slug": slug,
        "name": name,
        "priority": priority,
        "content_status": content_status,
    }
    if importance is not None:
        if importance < 0 or importance > 100:
            raise ValueError(f"Concept importance score must be between 0 and 100: {slug}={importance}")
        data["importance_score"] = importance
    if importance_reason:
        data["importance_reason"] = importance_reason
    return data


def subtopic(
    slug: str,
    name: str,
    concepts: list[NodeData],
    *,
    priority: str = "important",
    content_status: str = "active",
    short_description: str | None = None,
    description: str | None = None,
) -> NodeData:
    return {
        "slug": slug,
        "name": name,
        "short_description": short_description or name,
        "description": description or short_description or name,
        "priority": priority,
        "content_status": content_status,
        "concepts": concepts,
    }


def topic(
    slug: str,
    name: str,
    subtopics: list[NodeData],
    *,
    priority: str = "important",
    content_status: str = "active",
    short_description: str | None = None,
    description: str | None = None,
    concepts: list[NodeData] | None = None,
) -> NodeData:
    data: NodeData = {
        "slug": slug,
        "name": name,
        "short_description": short_description or name,
        "description": description or short_description or name,
        "priority": priority,
        "content_status": content_status,
        "subtopics": subtopics,
    }

# Python closures taxonomy seed with concept importance
# Source: quiz-api/app/seed_modules/fields/programming_languages/python/taxonomy/core_language/functions/closures.py (excerpt lines 1-67)
# Public portfolio excerpt; not standalone application code.

from app.seed_modules.common import concept, subtopic, topic


TOPIC = topic(
    'closures',
    'Closures',
    [
        subtopic(
            'closure-binding-traps',
            'Closure Binding Traps',
            [
            concept('closures-bind-names-not-values', 'closures bind names not values', importance=93),
            concept('default-argument-captures-loop-value', 'default argument captures loop value', importance=98),
            concept('closures-capture-variables-not-values', 'closures capture variables not values', importance=95),
            concept('loop-created-closures-share-loop-variable', 'loop-created closures share loop variable', importance=97),
            concept('late-binding-appears-when-function-called-later', 'late binding appears when function called later', importance=95),
            concept('default-argument-can-freeze-current-value', 'default argument can freeze current value', importance=97),
            concept('factory-function-can-create-separate-binding', 'factory function can create separate binding', importance=90),
            concept('closures-capture-names-not-frozen-values', 'closures capture names not frozen values', importance=93),
            concept('loop-created-closures-can-share-the-final-loop-value', 'loop-created closures can share the final loop value', importance=95),
            concept('default-argument-can-freeze-a-loop-value', 'default argument can freeze a loop value', importance=98),
            ],
        ),
        subtopic(
            'closure-state',
            'Closure State',
            [
            concept('closure-keeps-state-after-outer-returns', 'closure keeps state after outer returns', importance=95),
            concept('closure-can-preserve-private-state', 'closure can preserve private state', importance=93),
            concept('function-closure-stores-cell-objects', 'function __closure__ stores cell objects', importance=93),
            concept('stateful-closures-can-replace-simple-classes', 'stateful closures can replace simple classes', importance=95),
            concept('shared-closure-state-can-surprise-callers', 'shared closure state can surprise callers', importance=95),
            concept('closures-can-hold-references-and-extend-lifetime', 'closures can hold references and extend lifetime', importance=93),
            concept('closure-can-preserve-state-between-calls', 'closure can preserve state between calls', importance=93),
            concept('mutable-objects-in-closures-can-be-mutated-without-nonlocal', 'mutable objects in closures can be mutated without nonlocal', importance=95),
            concept('rebind-closed-over-name-requires-nonlocal', 'rebind closed over name requires nonlocal', importance=93),
            ],
        ),
        subtopic(
            'nested-functions-and-enclosing-scope',
            'Nested Functions & Enclosing Scope',
            [
            concept('inner-functions-capture-enclosing-variables', 'inner functions capture enclosing variables', importance=97),
            concept('nested-functions-create-enclosing-scope', 'nested functions create enclosing scope', importance=95),
            concept('nested-function-defined-inside-outer-function', 'nested function defined inside outer function', importance=95),
            concept('inner-function-can-read-enclosing-names', 'inner function can read enclosing names', importance=95),
            concept('inner-function-created-each-outer-call', 'inner function created each outer call', importance=95),
            concept('enclosing-variables-can-outlive-outer-call', 'enclosing variables can outlive outer call', importance=97),
            concept('nested-function-name-local-to-outer-function', 'nested function name local to outer function', importance=95),
            ],
        ),
        subtopic(
            'nonlocal-in-closures',
            'Nonlocal In Closures',
            [
            concept('nonlocal-rebinds-enclosing-name', 'nonlocal rebinds enclosing name', importance=93),
            concept('nonlocal-allows-rebinding-enclosing-variable', 'nonlocal allows rebinding enclosing variable', importance=95),
            concept('nonlocal-required-before-assigning-outer-scalar', 'nonlocal required before assigning outer scalar', importance=93),
            concept('nonlocal-cannot-create-new-binding', 'nonlocal cannot create new binding', importance=93),
            concept('nonlocal-affects-nearest-enclosing-binding', 'nonlocal affects nearest enclosing binding', importance=93),
            concept('mutating-captured-object-may-not-need-nonlocal', 'mutating captured object may not need nonlocal', importance=95),
            ],
        ),
    ],
    priority='core',
)
