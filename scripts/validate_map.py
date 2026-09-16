#!/usr/bin/env python3
"""Validate a knowledge-quest map directory.

Checks:
  - JSON files parse
  - node / edge / quest objects match JSON Schema when jsonschema is installed
  - unique node and quest ids
  - edges reference existing nodes; no self-loops
  - node.prerequisites match incoming prerequisite edges
  - prerequisite graph is a DAG (no cycles)
  - every non-start node is reachable from start_node_ids along prerequisite edges
  - every node has at least one quest
  - boss ids in win_condition exist and have type=boss

Usage:
  python3 scripts/validate_map.py maps/primary-math/grade-1-numbers
  python3 scripts/validate_map.py --all
  python3 scripts/validate_map.py maps/primary-math/grade-1-numbers --tree
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schema"
MAPS_DIR = ROOT / "maps"

try:
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - optional dependency
    jsonschema = None
    Draft202012Validator = None


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_schema(name: str) -> dict[str, Any] | None:
    path = SCHEMA_DIR / name
    if not path.exists():
        return None
    return load_json(path)


def schema_validate_items(
    report: Report,
    schema_name: str,
    items: list[dict[str, Any]],
    label: str,
) -> None:
    schema = load_schema(schema_name)
    if schema is None:
        report.err(f"missing schema file schema/{schema_name}")
        return
    if Draft202012Validator is None:
        report.warn(
            "package 'jsonschema' not installed; skipped Draft 2020-12 checks "
            f"for {label} (graph checks still run). pip install jsonschema"
        )
        return
    validator = Draft202012Validator(schema)
    for i, item in enumerate(items):
        for error in sorted(validator.iter_errors(item), key=lambda e: list(e.path)):
            loc = ".".join(str(p) for p in error.path) or "(root)"
            ident = item.get("id") or f"{item.get('from')}->{item.get('to')}"
            report.err(f"{label}[{i}] {ident} {loc}: {error.message}")


def require_files(map_dir: Path, report: Report) -> dict[str, Path]:
    needed = ["nodes.json", "edges.json", "quests.json", "map.meta.json"]
    paths = {}
    for name in needed:
        p = map_dir / name
        if not p.exists():
            report.err(f"missing {name}")
        else:
            paths[name] = p
    return paths


def as_item_list(payload: Any, key: str, report: Report, filename: str) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and key in payload and isinstance(payload[key], list):
        return payload[key]
    report.err(f"{filename} must be a list or an object with '{key}' array")
    return []


def unlock_layers(
    start_ids: list[str],
    prereq_pred: dict[str, set[str]],
    node_ids: set[str],
) -> list[list[str]]:
    """Layers in which a node can become available (all direct prereqs already lit)."""
    remaining = set(node_ids)
    lit: set[str] = set()
    layers: list[list[str]] = []
    layer = [nid for nid in start_ids if nid in remaining]
    for nid in sorted(remaining):
        if nid not in layer and not prereq_pred.get(nid):
            layer.append(nid)
    while layer:
        layers.append(sorted(set(layer)))
        lit.update(layer)
        remaining.difference_update(layer)
        layer = [
            nid
            for nid in sorted(remaining)
            if prereq_pred.get(nid, set()) <= lit
        ]
    if remaining:
        layers.append(sorted(remaining))
    return layers


def detect_cycles(node_ids: set[str], succ: dict[str, list[str]]) -> list[list[str]]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {nid: WHITE for nid in node_ids}
    stack: list[str] = []
    cycles: list[list[str]] = []

    def dfs(u: str) -> None:
        color[u] = GRAY
        stack.append(u)
        for v in succ.get(u, []):
            if v not in color:
                continue
            if color[v] == GRAY:
                i = stack.index(v)
                cycles.append(stack[i:] + [v])
            elif color[v] == WHITE:
                dfs(v)
        stack.pop()
        color[u] = BLACK

    for nid in sorted(node_ids):
        if color[nid] == WHITE:
            dfs(nid)
    return cycles


def print_tree(
    meta: dict[str, Any],
    nodes: list[dict[str, Any]],
    pred: dict[str, set[str]],
) -> None:
    titles = {n["id"]: n["title"] for n in nodes}
    start = meta.get("start_node_ids") or []
    node_ids = {n["id"] for n in nodes}
    layers = unlock_layers(start, pred, node_ids)
    print(f"\n地图：{meta.get('title')} ({meta.get('id')})")
    print(f"起点：{', '.join(start)}")
    win = meta.get("win_condition") or {}
    print(f"通关：{win.get('summary', win.get('type', ''))}")
    print("解锁层（上一层全部点亮后，本层变为 available）：")
    for i, layer in enumerate(layers):
        print(f"  L{i}:")
        for nid in layer:
            need = "、".join(titles.get(p, p) for p in sorted(pred.get(nid, set()))) or "（起点）"
            print(f"    - {nid}  {titles.get(nid, '')}  前置：{need}")


def validate_map(map_dir: Path, tree: bool = False) -> Report:
    report = Report()
    map_dir = map_dir.resolve()
    if not map_dir.is_dir():
        report.err(f"not a directory: {map_dir}")
        return report

    paths = require_files(map_dir, report)
    if report.errors:
        return report

    try:
        nodes_payload = load_json(paths["nodes.json"])
        edges_payload = load_json(paths["edges.json"])
        quests_payload = load_json(paths["quests.json"])
        meta = load_json(paths["map.meta.json"])
    except json.JSONDecodeError as e:
        report.err(f"invalid JSON: {e}")
        return report

    nodes = as_item_list(nodes_payload, "nodes", report, "nodes.json")
    edges = as_item_list(edges_payload, "edges", report, "edges.json")
    quests = as_item_list(quests_payload, "quests", report, "quests.json")
    if not isinstance(meta, dict):
        report.err("map.meta.json must be an object")
        return report

    if not isinstance(meta.get("id"), str) or not meta["id"]:
        report.err("map.meta.json missing id")
    if not isinstance(meta.get("title"), str) or not meta["title"]:
        report.err("map.meta.json missing title")
    start_ids = meta.get("start_node_ids")
    if not isinstance(start_ids, list) or not start_ids:
        report.err("map.meta.json.start_node_ids must be a non-empty list")
        start_ids = []
    win = meta.get("win_condition")
    if not isinstance(win, dict):
        report.err("map.meta.json.win_condition must be an object")
        win = {}

    schema_validate_items(report, "knowledge-node.schema.json", nodes, "node")
    schema_validate_items(report, "knowledge-edge.schema.json", edges, "edge")
    schema_validate_items(report, "quest.schema.json", quests, "quest")

    node_ids: list[str] = []
    seen_nodes: set[str] = set()
    node_by_id: dict[str, dict[str, Any]] = {}
    for n in nodes:
        nid = n.get("id")
        if not isinstance(nid, str):
            report.err("node without string id")
            continue
        if nid in seen_nodes:
            report.err(f"duplicate node id: {nid}")
        seen_nodes.add(nid)
        node_ids.append(nid)
        node_by_id[nid] = n

    start_set = [s for s in start_ids if isinstance(s, str)]
    for s in start_set:
        if s not in seen_nodes:
            report.err(f"start_node_id not in nodes: {s}")

    prereq_succ: dict[str, list[str]] = defaultdict(list)
    prereq_pred: dict[str, set[str]] = defaultdict(set)
    edge_keys: set[tuple[str, str, str]] = set()

    for e in edges:
        frm, to, typ = e.get("from"), e.get("to"), e.get("type")
        if not isinstance(frm, str) or not isinstance(to, str) or not isinstance(typ, str):
            report.err(f"edge missing from/to/type: {e}")
            continue
        if frm == to:
            report.err(f"self-loop forbidden: {frm}")
        if frm not in seen_nodes:
            report.err(f"edge.from unknown node: {frm} -> {to} ({typ})")
        if to not in seen_nodes:
            report.err(f"edge.to unknown node: {frm} -> {to} ({typ})")
        key = (frm, to, typ)
        if key in edge_keys:
            report.err(f"duplicate edge: {frm} -> {to} ({typ})")
        edge_keys.add(key)
        if typ == "prerequisite":
            prereq_succ[frm].append(to)
            prereq_pred[to].add(frm)

    # prerequisites field vs incoming edges
    for n in nodes:
        nid = n.get("id")
        if nid not in seen_nodes:
            continue
        listed = n.get("prerequisites") or []
        if not isinstance(listed, list):
            report.err(f"{nid} prerequisites must be a list")
            listed = []
        listed_set = set(listed)
        incoming = prereq_pred.get(nid, set())
        extra = listed_set - incoming
        missing = incoming - listed_set
        if extra:
            report.err(f"{nid} prerequisites not represented as edges: {sorted(extra)}")
        if missing:
            report.err(f"{nid} incoming prerequisite edges missing from node.prerequisites: {sorted(missing)}")
        for p in listed:
            if p not in seen_nodes:
                report.err(f"{nid} prerequisite unknown: {p}")
        unlock = (n.get("unlock_rule") or {}).get("type")
        if nid in start_set:
            if listed_set:
                report.err(f"start node {nid} must have empty prerequisites")
        elif unlock == "hard_all_prereqs" and not listed_set:
            report.err(f"non-start hard node {nid} has no prerequisites")

    cycles = detect_cycles(seen_nodes, prereq_succ)
    for cyc in cycles:
        report.err("prerequisite cycle: " + " -> ".join(cyc))

    # reachability from starts along prerequisite edges
    reachable: set[str] = set()
    dq = deque(s for s in start_set if s in seen_nodes)
    reachable.update(dq)
    while dq:
        u = dq.popleft()
        for v in prereq_succ.get(u, []):
            if v not in reachable:
                reachable.add(v)
                dq.append(v)
    for nid in sorted(seen_nodes):
        if nid not in start_set and nid not in reachable:
            report.err(f"node not reachable from start via prerequisite edges: {nid}")

    quest_ids: set[str] = set()
    quests_by_node: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for q in quests:
        qid = q.get("id")
        nid = q.get("node_id")
        if not isinstance(qid, str):
            report.err("quest without string id")
            continue
        if qid in quest_ids:
            report.err(f"duplicate quest id: {qid}")
        quest_ids.add(qid)
        if nid not in seen_nodes:
            report.err(f"quest {qid} node_id unknown: {nid}")
        else:
            quests_by_node[nid].append(q)

    for nid in sorted(seen_nodes):
        if not quests_by_node.get(nid):
            report.err(f"node has no quests: {nid}")

    boss_ids = win.get("required_boss_quest_ids") or []
    if not isinstance(boss_ids, list) or len(boss_ids) < 2:
        report.warn("win_condition.required_boss_quest_ids should list at least 2–3 chapter bosses")
    for bid in boss_ids:
        if bid not in quest_ids:
            report.err(f"win_condition boss quest missing: {bid}")
        else:
            q = next(x for x in quests if x.get("id") == bid)
            if q.get("type") != "boss":
                report.err(f"win_condition quest {bid} is type={q.get('type')}, expected boss")

    sample = map_dir / "player-progress.sample.json"
    if sample.exists():
        try:
            progress = load_json(sample)
        except json.JSONDecodeError as e:
            report.err(f"player-progress.sample.json invalid JSON: {e}")
        else:
            schema = load_schema("player-progress.schema.json")
            if schema and Draft202012Validator is not None:
                for error in Draft202012Validator(schema).iter_errors(progress):
                    loc = ".".join(str(p) for p in error.path) or "(root)"
                    report.err(f"player-progress.sample.json {loc}: {error.message}")
            for nid in (progress.get("nodes") or {}):
                if nid not in seen_nodes:
                    report.err(f"player-progress.sample.json unknown node: {nid}")

    if tree and not report.errors:
        print_tree(meta, nodes, prereq_pred)

    report.warn(f"{len(seen_nodes)} nodes, {len(edges)} edges, {len(quests)} quests")
    return report


def discover_maps() -> list[Path]:
    found = []
    if not MAPS_DIR.exists():
        return found
    for meta in MAPS_DIR.rglob("map.meta.json"):
        found.append(meta.parent)
    return sorted(found)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate knowledge-quest map JSON")
    parser.add_argument(
        "map_dir",
        nargs="?",
        help="Path to a map folder containing nodes.json / edges.json / quests.json / map.meta.json",
    )
    parser.add_argument("--all", action="store_true", help="Validate every map under maps/")
    parser.add_argument("--tree", action="store_true", help="Print unlock layers after a successful check")
    args = parser.parse_args(argv)

    targets: list[Path] = []
    if args.all:
        targets = discover_maps()
        if not targets:
            print("No maps found under maps/", file=sys.stderr)
            return 2
    elif args.map_dir:
        targets = [Path(args.map_dir)]
    else:
        default = ROOT / "maps" / "primary-math" / "grade-1-numbers"
        if default.exists():
            targets = [default]
        else:
            parser.print_help()
            return 2

    any_fail = False
    for t in targets:
        rel = t if t.is_absolute() else t
        print(f"== {rel}")
        report = validate_map(t, tree=args.tree)
        for w in report.warnings:
            print(f"  warn: {w}")
        for e in report.errors:
            print(f"  error: {e}")
            any_fail = True
        print("  PASS" if report.ok else "  FAIL")
    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
