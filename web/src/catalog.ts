/** Load every map directory via Vite glob so the SPA works offline after build. */
import type { KnowledgeEdge, KnowledgeNode, MapMeta, Quest, QuestMap } from "./types";

const metaModules = import.meta.glob("../../maps/**/map.meta.json", {
  eager: true,
  import: "default",
}) as Record<string, MapMeta>;

const nodeModules = import.meta.glob("../../maps/**/nodes.json", {
  eager: true,
  import: "default",
}) as Record<string, { map_id?: string; nodes?: KnowledgeNode[] } | KnowledgeNode[]>;

const edgeModules = import.meta.glob("../../maps/**/edges.json", {
  eager: true,
  import: "default",
}) as Record<string, { map_id?: string; edges?: KnowledgeEdge[] } | KnowledgeEdge[]>;

const questModules = import.meta.glob("../../maps/**/quests.json", {
  eager: true,
  import: "default",
}) as Record<string, { map_id?: string; quests?: Quest[] } | Quest[]>;

function dirOf(filePath: string): string {
  return filePath.replace(/\/[^/]+$/, "");
}

function byDir<T>(mods: Record<string, T>): Map<string, T> {
  const out = new Map<string, T>();
  for (const [file, value] of Object.entries(mods)) {
    out.set(dirOf(file), value);
  }
  return out;
}

function asList<T>(payload: unknown, key: string): T[] {
  if (Array.isArray(payload)) return payload as T[];
  if (payload && typeof payload === "object" && key in payload) {
    const val = (payload as Record<string, unknown>)[key];
    if (Array.isArray(val)) return val as T[];
  }
  return [];
}

function assemble(): QuestMap[] {
  const nodesByDir = byDir(nodeModules);
  const edgesByDir = byDir(edgeModules);
  const questsByDir = byDir(questModules);
  const maps: QuestMap[] = [];

  for (const [file, meta] of Object.entries(metaModules)) {
    const dir = dirOf(file);
    const nodes = asList<KnowledgeNode>(nodesByDir.get(dir), "nodes");
    const edges = asList<KnowledgeEdge>(edgesByDir.get(dir), "edges");
    const quests = asList<Quest>(questsByDir.get(dir), "quests");
    if (!meta?.id || nodes.length === 0) {
      console.warn(`[catalog] skip incomplete map at ${dir}`);
      continue;
    }
    maps.push({ dir, meta, nodes, edges, quests });
  }

  maps.sort((a, b) => {
    const stageRank = { 小学: 0, 初中: 1, 高中: 2 } as const;
    const sa = stageRank[a.meta.stage] ?? 9;
    const sb = stageRank[b.meta.stage] ?? 9;
    if (sa !== sb) return sa - sb;
    if (a.meta.grade !== b.meta.grade) return a.meta.grade - b.meta.grade;
    return a.meta.title.localeCompare(b.meta.title, "zh-CN");
  });
  return maps;
}

const ALL_MAPS = assemble();

export function listMaps(): QuestMap[] {
  return ALL_MAPS;
}

export function getMap(id: string): QuestMap | undefined {
  return ALL_MAPS.find((m) => m.meta.id === id);
}

export const STAGE_ORDER: Array<QuestMap["meta"]["stage"]> = ["小学", "初中", "高中"];
