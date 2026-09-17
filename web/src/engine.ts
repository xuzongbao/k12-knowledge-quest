/**
 * Unlock / mastery / win-condition engine.
 * UI state is derived from saved lit/learning progress + prerequisite DAG.
 */
import type {
  CompleteQuestResult,
  KnowledgeNode,
  NodeState,
  PlayerProgress,
  Quest,
  QuestMap,
} from "./types";

export const FIRST_LIGHT_XP = 10;
export const MAP_CLEAR_XP = 100;

const MASTERED: ReadonlySet<NodeState> = new Set(["lit", "needs_review"]);
const IN_PROGRESS: ReadonlySet<NodeState> = new Set(["lit", "learning", "needs_review"]);

export function nowIso(): string {
  return new Date().toISOString();
}

export function createInitialProgress(): PlayerProgress {
  return {
    player_id: "local-learner",
    display_name: "同学",
    xp_total: 0,
    cleared_map_ids: [],
    nodes: {},
  };
}

export function nodeById(map: QuestMap, id: string): KnowledgeNode | undefined {
  return map.nodes.find((n) => n.id === id);
}

export function questById(map: QuestMap, id: string): Quest | undefined {
  return map.quests.find((q) => q.id === id);
}

export function questsForNode(map: QuestMap, nodeId: string): Quest[] {
  return map.quests.filter((q) => q.node_id === nodeId);
}

export function isBossNode(map: QuestMap, node: KnowledgeNode): boolean {
  if (node.tags.includes("boss-gate")) return true;
  return questsForNode(map, node.id).some((q) => q.type === "boss");
}

export function isStartNode(map: QuestMap, nodeId: string): boolean {
  return map.meta.start_node_ids.includes(nodeId);
}

export function isMasteredState(state: NodeState | undefined): boolean {
  return state !== undefined && MASTERED.has(state);
}

export function storedProgress(progress: PlayerProgress, nodeId: string): NodeProgressView {
  const stored = progress.nodes[nodeId];
  return {
    state: stored?.state,
    xp_earned: stored?.xp_earned ?? 0,
    cleared_quest_ids: stored?.cleared_quest_ids ?? [],
    updated_at: stored?.updated_at,
  };
}

interface NodeProgressView {
  state: NodeState | undefined;
  xp_earned: number;
  cleared_quest_ids: string[];
  updated_at?: string;
}

/** Direct hard/soft prerequisites: node.prerequisites, falling back to incoming edges. */
export function directPrerequisites(map: QuestMap, node: KnowledgeNode): string[] {
  if (node.prerequisites.length > 0) return node.prerequisites;
  return map.edges
    .filter((e) => e.type === "prerequisite" && e.to === node.id)
    .map((e) => e.from);
}

export function isUnlockReady(map: QuestMap, progress: PlayerProgress, nodeId: string): boolean {
  if (isStartNode(map, nodeId)) return true;
  const node = nodeById(map, nodeId);
  if (!node) return false;
  const prereqs = directPrerequisites(map, node);
  if (prereqs.length === 0) return true;
  return prereqs.every((id) => isMasteredState(storedProgress(progress, id).state));
}

/**
 * Display state. lit / learning / needs_review come from the save;
 * available vs locked is always recomputed from the DAG.
 */
export function deriveNodeState(map: QuestMap, progress: PlayerProgress, nodeId: string): NodeState {
  const stored = storedProgress(progress, nodeId).state;
  if (stored && IN_PROGRESS.has(stored)) return stored;
  if (isUnlockReady(map, progress, nodeId)) return "available";
  return "locked";
}

export function isSoftRecommended(node: KnowledgeNode): boolean {
  return node.unlock_rule.type === "soft_recommended";
}

/** Soft-lock branches can be opened before their recommended prereqs are lit. */
export function canEnterNode(map: QuestMap, progress: PlayerProgress, nodeId: string): boolean {
  const state = deriveNodeState(map, progress, nodeId);
  if (state !== "locked") return true;
  const node = nodeById(map, nodeId);
  return Boolean(node && isSoftRecommended(node));
}

export function prerequisiteHints(
  map: QuestMap,
  progress: PlayerProgress,
  nodeId: string,
): { id: string; title: string; mastered: boolean }[] {
  const node = nodeById(map, nodeId);
  if (!node) return [];
  return directPrerequisites(map, node).map((id) => {
    const prereq = nodeById(map, id);
    return {
      id,
      title: prereq?.title ?? id,
      mastered: isMasteredState(storedProgress(progress, id).state),
    };
  });
}

export function meetsMastery(node: KnowledgeNode, map: QuestMap, clearedIds: string[]): boolean {
  const bound = questsForNode(map, node.id);
  const cleared = bound.filter((q) => clearedIds.includes(q.id));
  if (cleared.length < node.mastery_criteria.min_quests_cleared) return false;
  const required = node.mastery_criteria.require_quest_types ?? [];
  const types = new Set(cleared.map((q) => q.type));
  if (!required.every((t) => types.has(t))) return false;
  // No live quiz scorer yet: completing a mini_quiz counts as meeting min_quiz_accuracy.
  return true;
}

export function requiredNodeIds(map: QuestMap): string[] {
  const spec = map.meta.win_condition.required_node_ids;
  if (spec === "all" || spec == null) return map.nodes.map((n) => n.id);
  return spec;
}

export function isMapCleared(map: QuestMap, progress: PlayerProgress): boolean {
  const nodesOk = requiredNodeIds(map).every((id) =>
    isMasteredState(deriveNodeState(map, progress, id)),
  );
  const bossesOk = (map.meta.win_condition.required_boss_quest_ids ?? []).every((qid) =>
    Object.values(progress.nodes).some((np) => np.cleared_quest_ids?.includes(qid)),
  );
  return nodesOk && bossesOk;
}

export function litCount(map: QuestMap, progress: PlayerProgress): { lit: number; total: number } {
  let lit = 0;
  for (const node of map.nodes) {
    if (isMasteredState(deriveNodeState(map, progress, node.id))) lit += 1;
  }
  return { lit, total: map.nodes.length };
}

export function mapXpEarned(map: QuestMap, progress: PlayerProgress): number {
  let xp = 0;
  for (const node of map.nodes) {
    xp += storedProgress(progress, node.id).xp_earned;
  }
  if (progress.cleared_map_ids.includes(map.meta.id)) xp += MAP_CLEAR_XP;
  return xp;
}

function patchNode(
  progress: PlayerProgress,
  nodeId: string,
  patch: Partial<NodeProgressView> & { state: NodeState },
): PlayerProgress {
  const prev = storedProgress(progress, nodeId);
  return {
    ...progress,
    nodes: {
      ...progress.nodes,
      [nodeId]: {
        state: patch.state,
        xp_earned: patch.xp_earned ?? prev.xp_earned,
        cleared_quest_ids: patch.cleared_quest_ids ?? prev.cleared_quest_ids,
        updated_at: nowIso(),
      },
    },
  };
}

export function completeQuest(
  map: QuestMap,
  progress: PlayerProgress,
  questId: string,
): CompleteQuestResult {
  const quest = questById(map, questId);
  if (!quest) {
    return {
      progress,
      nodeId: "",
      questId,
      alreadyCleared: false,
      nodeJustLit: false,
      mapJustCleared: false,
      xpGained: 0,
      blockedReason: "找不到这个任务。",
    };
  }

  const node = nodeById(map, quest.node_id);
  if (!node) {
    return {
      progress,
      nodeId: quest.node_id,
      questId,
      alreadyCleared: false,
      nodeJustLit: false,
      mapJustCleared: false,
      xpGained: 0,
      blockedReason: "找不到对应的知识点。",
    };
  }

  if (!canEnterNode(map, progress, node.id)) {
    const missing = prerequisiteHints(map, progress, node.id)
      .filter((h) => !h.mastered)
      .map((h) => h.title)
      .join("、");
    return {
      progress,
      nodeId: node.id,
      questId,
      alreadyCleared: false,
      nodeJustLit: false,
      mapJustCleared: false,
      xpGained: 0,
      blockedReason: missing ? `还没点亮前置：${missing}` : "这个知识点还锁着。",
    };
  }

  const prev = storedProgress(progress, node.id);
  if (prev.cleared_quest_ids.includes(questId)) {
    return {
      progress,
      nodeId: node.id,
      questId,
      alreadyCleared: true,
      nodeJustLit: false,
      mapJustCleared: false,
      xpGained: 0,
    };
  }

  const wasMastered = isMasteredState(prev.state);
  const wasMapCleared = progress.cleared_map_ids.includes(map.meta.id);
  const cleared = [...prev.cleared_quest_ids, questId];
  let xpGained = quest.xp;
  let state: NodeState = prev.state && IN_PROGRESS.has(prev.state) ? prev.state : "learning";
  let nodeJustLit = false;

  let next: PlayerProgress = patchNode(progress, node.id, {
    state,
    xp_earned: prev.xp_earned + quest.xp,
    cleared_quest_ids: cleared,
  });
  next = { ...next, xp_total: next.xp_total + quest.xp, current_map_id: map.meta.id };

  if (!wasMastered && meetsMastery(node, map, cleared)) {
    nodeJustLit = true;
    xpGained += FIRST_LIGHT_XP;
    next = patchNode(next, node.id, {
      state: "lit",
      xp_earned: (next.nodes[node.id]?.xp_earned ?? 0) + FIRST_LIGHT_XP,
      cleared_quest_ids: cleared,
    });
    next = { ...next, xp_total: next.xp_total + FIRST_LIGHT_XP };
  }

  const mapJustCleared = !wasMapCleared && isMapCleared(map, next);
  if (mapJustCleared) {
    xpGained += MAP_CLEAR_XP;
    next = {
      ...next,
      xp_total: next.xp_total + MAP_CLEAR_XP,
      cleared_map_ids: [...next.cleared_map_ids, map.meta.id],
    };
  }

  return {
    progress: next,
    nodeId: node.id,
    questId,
    alreadyCleared: false,
    nodeJustLit,
    mapJustCleared,
    xpGained,
  };
}

/** Drop one map's node rows and its clear bonus; leave other maps untouched. */
export function resetMapProgress(map: QuestMap, progress: PlayerProgress): PlayerProgress {
  const nodeIds = new Set(map.nodes.map((n) => n.id));
  const nodes: PlayerProgress["nodes"] = {};
  let subtract = 0;
  for (const [id, row] of Object.entries(progress.nodes)) {
    if (nodeIds.has(id)) {
      subtract += row.xp_earned ?? 0;
    } else {
      nodes[id] = row;
    }
  }
  const wasCleared = progress.cleared_map_ids.includes(map.meta.id);
  if (wasCleared) subtract += MAP_CLEAR_XP;
  return {
    ...progress,
    xp_total: Math.max(0, progress.xp_total - subtract),
    current_map_id: progress.current_map_id === map.meta.id ? undefined : progress.current_map_id,
    cleared_map_ids: progress.cleared_map_ids.filter((id) => id !== map.meta.id),
    nodes,
  };
}

/**
 * Topological layers: a node appears when all direct prereqs are in earlier layers.
 * Matches scripts/validate_map.py unlock_layers (used for map layout + tests).
 */
export function unlockLayers(map: QuestMap): string[][] {
  const nodeIds = new Set(map.nodes.map((n) => n.id));
  const pred = new Map<string, Set<string>>();
  for (const id of nodeIds) pred.set(id, new Set());
  for (const node of map.nodes) {
    for (const p of directPrerequisites(map, node)) {
      if (nodeIds.has(p)) pred.get(node.id)?.add(p);
    }
  }

  const remaining = new Set(nodeIds);
  const lit = new Set<string>();
  const layers: string[][] = [];
  let layer = map.meta.start_node_ids.filter((id) => remaining.has(id));
  for (const id of [...remaining].sort()) {
    if (!layer.includes(id) && (pred.get(id)?.size ?? 0) === 0) layer.push(id);
  }

  while (layer.length > 0) {
    const unique = [...new Set(layer)].sort();
    layers.push(unique);
    for (const id of unique) {
      lit.add(id);
      remaining.delete(id);
    }
    layer = [...remaining]
      .sort()
      .filter((id) => {
        const need = pred.get(id) ?? new Set();
        for (const p of need) {
          if (!lit.has(p)) return false;
        }
        return true;
      });
  }

  if (remaining.size > 0) layers.push([...remaining].sort());
  return layers;
}
