import type { NodeState, QuestType, Stage } from "./types";

export const STATE_LABEL: Record<NodeState, string> = {
  locked: "锁定",
  available: "可学",
  learning: "学习中",
  lit: "已点亮",
  needs_review: "待复习",
};

export const QUEST_LABEL: Record<QuestType, string> = {
  explain: "讲解",
  practice: "练习",
  mini_quiz: "小测",
  boss: "关主",
};

export const STAGE_EMPTY: Record<Stage, string> = {
  小学: "小学地图会显示在这里。",
  初中: "初中地图会显示在这里。",
  高中: "高中地图会显示在这里。",
};
