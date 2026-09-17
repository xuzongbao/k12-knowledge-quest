/** Shared types for map JSON + player save (aligned with schema/). */

export type Stage = "小学" | "初中" | "高中";

export type NodeState = "locked" | "available" | "learning" | "lit" | "needs_review";

export type EdgeType = "prerequisite" | "related" | "easily_confused" | "application";

export type QuestType = "explain" | "practice" | "mini_quiz" | "boss";

export type UnlockRuleType = "hard_all_prereqs" | "soft_recommended";

export interface UnlockRule {
  type: UnlockRuleType;
  allow_teacher_override?: boolean;
}

export interface MasteryCriteria {
  min_quests_cleared: number;
  min_quiz_accuracy?: number;
  require_quest_types?: QuestType[];
  review_after_days?: number;
}

export interface KnowledgeNode {
  id: string;
  title: string;
  subject: string;
  stage: Stage;
  grade: number;
  strand: string;
  difficulty: number;
  prerequisites: string[];
  tags: string[];
  unlock_rule: UnlockRule;
  mastery_criteria: MasteryCriteria;
  description: string;
}

export interface KnowledgeEdge {
  from: string;
  to: string;
  type: EdgeType;
  note?: string;
}

export interface Quest {
  id: string;
  node_id: string;
  title: string;
  type: QuestType;
  xp: number;
  prompt: string;
  success_hint?: string;
  items_suggested?: number;
}

export interface WinCondition {
  type: string;
  required_node_ids: "all" | string[];
  required_boss_quest_ids: string[];
  summary: string;
}

export interface MapMeta {
  id: string;
  title: string;
  subject: string;
  stage: Stage;
  grade: number;
  strand: string;
  version?: string;
  locale?: string;
  start_node_ids: string[];
  recommended_path_note?: string;
  win_condition: WinCondition;
  content_disclaimer?: string;
  description: string;
}

export interface NodeProgress {
  state: NodeState;
  xp_earned?: number;
  cleared_quest_ids?: string[];
  updated_at?: string;
}

export interface PlayerProgress {
  player_id: string;
  display_name?: string;
  xp_total: number;
  current_map_id?: string;
  cleared_map_ids: string[];
  nodes: Record<string, NodeProgress>;
}

export interface QuestMap {
  dir: string;
  meta: MapMeta;
  nodes: KnowledgeNode[];
  edges: KnowledgeEdge[];
  quests: Quest[];
}

export interface CompleteQuestResult {
  progress: PlayerProgress;
  nodeId: string;
  questId: string;
  alreadyCleared: boolean;
  nodeJustLit: boolean;
  mapJustCleared: boolean;
  xpGained: number;
  blockedReason?: string;
}
