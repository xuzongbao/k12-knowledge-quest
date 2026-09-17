"""Shared helpers for junior-math (初中数学) map builders. Reuses primary JSON shape."""

from __future__ import annotations

from typing import Any

from _map_common import (
    HARD,
    MASTERY_CONCEPT,
    MASTERY_GATE,
    MASTERY_SKILL,
    ROOT,
    SOFT,
    node as _node,
    q,
    sample_progress,
    write_map,
)

__all__ = [
    "HARD",
    "MASTERY_CONCEPT",
    "MASTERY_GATE",
    "MASTERY_SKILL",
    "ROOT",
    "SOFT",
    "node",
    "q",
    "sample_progress",
    "write_map",
]


def node(
    nid: str,
    title: str,
    grade: int,
    strand: str,
    difficulty: int,
    prereqs: list[str],
    tags: list[str],
    description: str,
    *,
    unlock: dict | None = None,
    mastery: dict | None = None,
) -> dict[str, Any]:
    return _node(
        nid,
        title,
        grade,
        strand,
        difficulty,
        prereqs,
        tags,
        description,
        unlock=unlock,
        mastery=mastery,
        stage="初中",
    )
