/** localStorage save. One player blob covers every map. */
import { createInitialProgress } from "./engine";
import type { PlayerProgress } from "./types";

const STORAGE_KEY = "k12-knowledge-quest.progress.v1";

export function loadProgress(): PlayerProgress {
  if (typeof localStorage === "undefined") return createInitialProgress();
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return createInitialProgress();
    const parsed = JSON.parse(raw) as Partial<PlayerProgress>;
    if (!parsed || typeof parsed !== "object") return createInitialProgress();
    return {
      player_id: typeof parsed.player_id === "string" ? parsed.player_id : "local-learner",
      display_name: parsed.display_name,
      xp_total: Number.isFinite(parsed.xp_total) ? Math.max(0, Number(parsed.xp_total)) : 0,
      current_map_id: parsed.current_map_id,
      cleared_map_ids: Array.isArray(parsed.cleared_map_ids) ? parsed.cleared_map_ids : [],
      nodes: parsed.nodes && typeof parsed.nodes === "object" ? parsed.nodes : {},
    };
  } catch (err) {
    console.warn("[storage] could not read save", err);
    return createInitialProgress();
  }
}

export function saveProgress(progress: PlayerProgress): void {
  if (typeof localStorage === "undefined") return;
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
}
