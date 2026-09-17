"""Shared helpers for math map builders (primary and junior; statistics, practice, and similar strands)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

HARD = {"type": "hard_all_prereqs", "allow_teacher_override": False}
SOFT = {"type": "soft_recommended", "allow_teacher_override": True}

MASTERY_CONCEPT = {
    "min_quests_cleared": 1,
    "require_quest_types": ["explain"],
    "review_after_days": 10,
}
MASTERY_SKILL = {
    "min_quests_cleared": 1,
    "min_quiz_accuracy": 0.8,
    "require_quest_types": ["practice"],
    "review_after_days": 7,
}
MASTERY_GATE = {
    "min_quests_cleared": 2,
    "min_quiz_accuracy": 0.85,
    "require_quest_types": ["practice"],
    "review_after_days": 5,
}

XP_DEFAULT = {"explain": 10, "practice": 20, "mini_quiz": 30, "boss": 80}


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
    stage: str = "小学",
) -> dict[str, Any]:
    return {
        "id": nid,
        "title": title,
        "subject": "数学",
        "stage": stage,
        "grade": grade,
        "strand": strand,
        "difficulty": difficulty,
        "prerequisites": prereqs,
        "tags": tags,
        "unlock_rule": unlock or HARD,
        "mastery_criteria": mastery or MASTERY_SKILL,
        "description": description,
    }


def quest(
    qid: str,
    node_id: str,
    title: str,
    qtype: str,
    xp: int,
    prompt: str,
    hint: str,
    items: int | None = None,
) -> dict[str, Any]:
    q: dict[str, Any] = {
        "id": qid,
        "node_id": node_id,
        "title": title,
        "type": qtype,
        "xp": xp,
        "prompt": prompt,
        "success_hint": hint,
    }
    if items is not None:
        q["items_suggested"] = items
    return q


def q(
    node_id: str,
    qtype: str,
    title: str,
    prompt: str,
    hint: str,
    *,
    xp: int | None = None,
    items: int | None = None,
    qid: str | None = None,
) -> dict[str, Any]:
    """Shorthand: default quest id is `{node_id}-{qtype}` (bosses should pass qid)."""
    if qid is None:
        qid = f"{node_id}-{qtype.replace('_', '-')}"
    return quest(
        qid,
        node_id,
        title,
        qtype,
        xp if xp is not None else XP_DEFAULT[qtype],
        prompt,
        hint,
        items,
    )


def prereq_edges(nodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    edges = []
    for n in nodes:
        for src in n["prerequisites"]:
            edges.append(
                {
                    "from": src,
                    "to": n["id"],
                    "type": "prerequisite",
                    "note": f"{src} 需先于 {n['id']}",
                }
            )
    return edges


def dump(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def assert_field_limits(
    nodes: list[dict[str, Any]],
    quests: list[dict[str, Any]],
    extra_edges: list[dict[str, Any]],
) -> None:
    for n in nodes:
        assert 1 <= len(n["title"]) <= 40, n["title"]
        assert 8 <= len(n["description"]) <= 160, (n["id"], len(n["description"]), n["description"])
    for item in quests:
        assert 1 <= len(item["title"]) <= 40, item["title"]
        assert 4 <= len(item["prompt"]) <= 400, (item["id"], len(item["prompt"]))
        hint = item.get("success_hint") or ""
        assert len(hint) <= 200, (item["id"], len(hint))
    for e in extra_edges:
        note = e.get("note") or ""
        assert len(note) <= 120, (e["from"], e["to"], len(note), note)
    covered = {item["node_id"] for item in quests}
    missing = [n["id"] for n in nodes if n["id"] not in covered]
    assert not missing, f"nodes without quests: {missing}"


def sample_progress(
    map_id: str,
    start_id: str,
    start_quest_id: str,
    available_id: str,
    learning_id: str,
    learning_quest_id: str,
) -> dict[str, Any]:
    return {
        "player_id": "demo-learner",
        "display_name": "小明",
        "xp_total": 20,
        "current_map_id": map_id,
        "cleared_map_ids": [],
        "nodes": {
            start_id: {
                "state": "lit",
                "xp_earned": 10,
                "cleared_quest_ids": [start_quest_id],
                "updated_at": "2026-09-17T10:00:00Z",
            },
            available_id: {
                "state": "available",
                "xp_earned": 0,
                "cleared_quest_ids": [],
                "updated_at": "2026-09-17T10:00:00Z",
            },
            learning_id: {
                "state": "learning",
                "xp_earned": 10,
                "cleared_quest_ids": [learning_quest_id],
                "updated_at": "2026-09-17T10:08:00Z",
            },
        },
    }


def write_map(
    out_dir: Path,
    meta: dict[str, Any],
    nodes: list[dict[str, Any]],
    extra_edges: list[dict[str, Any]],
    quests: list[dict[str, Any]],
    sample: dict[str, Any],
) -> None:
    assert_field_limits(nodes, quests, extra_edges)
    out_dir.mkdir(parents=True, exist_ok=True)
    edges = prereq_edges(nodes) + extra_edges
    dump(out_dir / "nodes.json", {"map_id": meta["id"], "nodes": nodes})
    dump(out_dir / "edges.json", {"map_id": meta["id"], "edges": edges})
    dump(out_dir / "quests.json", {"map_id": meta["id"], "quests": quests})
    dump(out_dir / "map.meta.json", meta)
    dump(out_dir / "player-progress.sample.json", sample)
