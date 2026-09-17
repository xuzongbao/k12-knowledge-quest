import { describe, expect, it } from "vitest";
import grade1Edges from "../../maps/primary-math/grade-1-numbers/edges.json";
import grade1Meta from "../../maps/primary-math/grade-1-numbers/map.meta.json";
import grade1Nodes from "../../maps/primary-math/grade-1-numbers/nodes.json";
import grade1Quests from "../../maps/primary-math/grade-1-numbers/quests.json";
import { listMaps } from "./catalog";
import {
  canEnterNode,
  completeQuest,
  createInitialProgress,
  deriveNodeState,
  FIRST_LIGHT_XP,
  isMapCleared,
  litCount,
  MAP_CLEAR_XP,
  resetMapProgress,
  unlockLayers,
} from "./engine";
import type { KnowledgeEdge, KnowledgeNode, MapMeta, Quest, QuestMap } from "./types";

function pack(
  meta: MapMeta,
  nodes: KnowledgeNode[],
  edges: KnowledgeEdge[],
  quests: Quest[],
): QuestMap {
  return { dir: "fixture", meta, nodes, edges, quests };
}

function tinyMap(): QuestMap {
  const node = (
    id: string,
    title: string,
    prereqs: string[],
    unlock: "hard_all_prereqs" | "soft_recommended",
  ): KnowledgeNode => ({
    id,
    title,
    subject: "数学",
    stage: "小学",
    grade: 1,
    strand: "数与代数",
    difficulty: 1,
    prerequisites: prereqs,
    tags: [],
    unlock_rule: { type: unlock },
    mastery_criteria: { min_quests_cleared: 1, require_quest_types: ["explain"] },
    description: `${title}的学习目标说明。`,
  });

  return pack(
    {
      id: "tiny",
      title: "小图",
      subject: "数学",
      stage: "小学",
      grade: 1,
      strand: "数与代数",
      start_node_ids: ["a"],
      description: "用于单元测试的小地图。",
      win_condition: {
        type: "light_all_nodes_and_bosses",
        required_node_ids: "all",
        required_boss_quest_ids: ["boss-e"],
        summary: "点亮全部并击败关主。",
      },
    },
    [
      node("a", "起点", [], "hard_all_prereqs"),
      {
        ...node("b", "硬前置左", ["a"], "hard_all_prereqs"),
        mastery_criteria: {
          min_quests_cleared: 2,
          require_quest_types: ["explain", "practice"],
        },
      },
      node("c", "硬前置右", ["a"], "hard_all_prereqs"),
      node("d", "软锁支线", ["c"], "soft_recommended"),
      node("e", "关主点", ["c"], "hard_all_prereqs"),
    ],
    [
      { from: "a", to: "b", type: "prerequisite" },
      { from: "a", to: "c", type: "prerequisite" },
      { from: "c", to: "d", type: "prerequisite" },
      { from: "c", to: "e", type: "prerequisite" },
    ],
    [
      { id: "q-a", node_id: "a", title: "讲A", type: "explain", xp: 10, prompt: "讲A" },
      { id: "q-b", node_id: "b", title: "讲B", type: "explain", xp: 10, prompt: "讲B" },
      { id: "q-b-p", node_id: "b", title: "练B", type: "practice", xp: 15, prompt: "练B" },
      { id: "q-c", node_id: "c", title: "讲C", type: "explain", xp: 10, prompt: "讲C" },
      { id: "q-d", node_id: "d", title: "讲D", type: "explain", xp: 10, prompt: "讲D" },
      { id: "q-e", node_id: "e", title: "讲E", type: "explain", xp: 10, prompt: "讲E" },
      { id: "boss-e", node_id: "e", title: "关主", type: "boss", xp: 80, prompt: "打关主" },
    ],
  );
}

function lightWithRequiredQuests(map: QuestMap, progress: ReturnType<typeof createInitialProgress>, nodeId: string) {
  const node = map.nodes.find((n) => n.id === nodeId);
  if (!node) throw new Error(nodeId);
  const bound = map.quests.filter((q) => q.node_id === nodeId);
  const required = new Set(node.mastery_criteria.require_quest_types ?? []);
  const chosen: typeof bound = [];
  for (const type of required) {
    const q = bound.find((item) => item.type === type);
    if (q) chosen.push(q);
  }
  for (const q of bound) {
    if (chosen.length >= node.mastery_criteria.min_quests_cleared) break;
    if (!chosen.some((c) => c.id === q.id)) chosen.push(q);
  }
  let next = progress;
  for (const q of chosen) {
    const result = completeQuest(map, next, q.id);
    if (result.blockedReason) throw new Error(`${nodeId} ${q.id}: ${result.blockedReason}`);
    next = result.progress;
  }
  return next;
}

describe("unlock DAG", () => {
  it("starts available and unlocks hard dependents after lighting", () => {
    const map = tinyMap();
    let p = createInitialProgress();
    expect(deriveNodeState(map, p, "a")).toBe("available");
    expect(deriveNodeState(map, p, "b")).toBe("locked");
    expect(canEnterNode(map, p, "b")).toBe(false);
    expect(canEnterNode(map, p, "d")).toBe(true);
    expect(canEnterNode(map, p, "e")).toBe(false);

    const litA = completeQuest(map, p, "q-a");
    expect(litA.nodeJustLit).toBe(true);
    expect(litA.xpGained).toBe(10 + FIRST_LIGHT_XP);
    p = litA.progress;
    expect(deriveNodeState(map, p, "a")).toBe("lit");
    expect(deriveNodeState(map, p, "b")).toBe("available");
    expect(deriveNodeState(map, p, "c")).toBe("available");
    expect(deriveNodeState(map, p, "d")).toBe("locked");
    expect(canEnterNode(map, p, "d")).toBe(true);

    p = completeQuest(map, p, "q-c").progress;
    expect(deriveNodeState(map, p, "e")).toBe("available");
    expect(deriveNodeState(map, p, "d")).toBe("available");
    expect(deriveNodeState(map, p, "b")).toBe("available");

    const midB = completeQuest(map, p, "q-b");
    expect(midB.progress.nodes.b?.state).toBe("learning");
    expect(midB.nodeJustLit).toBe(false);
  });

  it("does not let a soft-lock branch block the main path", () => {
    const map = tinyMap();
    let p = createInitialProgress();
    p = completeQuest(map, p, "q-a").progress;
    p = completeQuest(map, p, "q-c").progress;
    expect(deriveNodeState(map, p, "e")).toBe("available");
    expect(deriveNodeState(map, p, "d")).not.toBe("lit");
    p = completeQuest(map, p, "q-e").progress;
    p = completeQuest(map, p, "boss-e").progress;
    expect(deriveNodeState(map, p, "e")).toBe("lit");
    expect(isMapCleared(map, p)).toBe(false);
    p = completeQuest(map, p, "q-b").progress;
    p = completeQuest(map, p, "q-b-p").progress;
    p = completeQuest(map, p, "q-d").progress;
    expect(isMapCleared(map, p)).toBe(true);
    expect(p.cleared_map_ids).toContain("tiny");
    expect(p.xp_total).toBeGreaterThan(MAP_CLEAR_XP);
  });

  it("rejects hard-locked quests and can reset one map", () => {
    const map = tinyMap();
    let p = createInitialProgress();
    const blocked = completeQuest(map, p, "q-b");
    expect(blocked.blockedReason).toMatch(/前置/);
    p = completeQuest(map, p, "q-a").progress;
    const other: QuestMap = {
      ...map,
      meta: { ...map.meta, id: "other" },
      nodes: [{ ...map.nodes[0], id: "z", prerequisites: [] }],
      quests: [{ id: "q-z", node_id: "z", title: "Z", type: "explain", xp: 10, prompt: "z" }],
      edges: [],
    };
    p = completeQuest(other, p, "q-z").progress;
    p = resetMapProgress(map, p);
    expect(deriveNodeState(map, p, "a")).toBe("available");
    expect(p.nodes["z"]?.state).toBe("lit");
  });
});

describe("grade-1-numbers smoke", () => {
  const map = pack(
    grade1Meta as MapMeta,
    grade1Nodes.nodes as KnowledgeNode[],
    grade1Edges.edges as KnowledgeEdge[],
    grade1Quests.quests as Quest[],
  );

  it("loads in the catalog and follows the authored DAG", () => {
    const listed = listMaps();
    expect(listed.length).toBeGreaterThanOrEqual(47);
    expect(listed.filter((m) => m.meta.stage === "小学").length).toBeGreaterThanOrEqual(24);
    expect(listed.filter((m) => m.meta.stage === "初中").length).toBeGreaterThanOrEqual(12);
    expect(listed.filter((m) => m.meta.stage === "高中").length).toBeGreaterThanOrEqual(11);
    expect(listed.some((m) => m.meta.id === "pm-g1-numbers")).toBe(true);
    expect(listed.some((m) => m.dir.includes("junior-math"))).toBe(true);
    expect(listed.some((m) => m.dir.includes("senior-math"))).toBe(true);
    expect(listed.every((m) => ["小学", "初中", "高中"].includes(m.meta.stage))).toBe(true);

    const layers = unlockLayers(map);
    expect(layers[0]).toContain("pm-g1-n001");
    expect(layers.flat().sort()).toEqual([...map.nodes.map((n) => n.id)].sort());
  });

  it("plays through from 数一数 to map clear", () => {
    let p = createInitialProgress();
    expect(deriveNodeState(map, p, "pm-g1-n001")).toBe("available");
    expect(canEnterNode(map, p, "pm-g1-n004")).toBe(true);
    expect(canEnterNode(map, p, "pm-g1-n002")).toBe(false);

    p = lightWithRequiredQuests(map, p, "pm-g1-n001");
    expect(deriveNodeState(map, p, "pm-g1-n001")).toBe("lit");
    expect(deriveNodeState(map, p, "pm-g1-n002")).toBe("available");
    expect(deriveNodeState(map, p, "pm-g1-n003")).toBe("available");
    expect(litCount(map, p).lit).toBe(1);

    const n003 = completeQuest(map, p, "pm-g1-n003-explain");
    expect(n003.nodeJustLit).toBe(true);
    expect(n003.progress.nodes["pm-g1-n003"]?.state).toBe("lit");
    p = n003.progress;

    for (const layer of unlockLayers(map)) {
      for (const id of layer) {
        if (deriveNodeState(map, p, id) === "lit") continue;
        p = lightWithRequiredQuests(map, p, id);
        for (const quest of map.quests.filter((q) => q.node_id === id && q.type === "boss")) {
          const result = completeQuest(map, p, quest.id);
          if (result.blockedReason) throw new Error(result.blockedReason);
          p = result.progress;
        }
      }
    }

    expect(isMapCleared(map, p)).toBe(true);
    expect(p.cleared_map_ids).toContain("pm-g1-numbers");
    expect(litCount(map, p).lit).toBe(map.nodes.length);
    expect(
      map.meta.win_condition.required_boss_quest_ids.every((id) =>
        Object.values(p.nodes).some((row) => row.cleared_quest_ids?.includes(id)),
      ),
    ).toBe(true);
  });
});
