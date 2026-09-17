import { useMemo, useState } from "react";
import { STAGE_ORDER } from "../catalog";
import { litCount } from "../engine";
import { STAGE_EMPTY } from "../labels";
import type { PlayerProgress, QuestMap, Stage } from "../types";

interface Props {
  maps: QuestMap[];
  progress: PlayerProgress;
  onOpenMap: (id: string) => void;
}

export default function Home({ maps, progress, onOpenMap }: Props) {
  const [query, setQuery] = useState("");
  const q = query.trim().toLowerCase();

  const grouped = useMemo(() => {
    const match = (m: QuestMap) => {
      if (!q) return true;
      const hay = `${m.meta.title} ${m.meta.strand} ${m.meta.subject} ${m.meta.grade}年级`.toLowerCase();
      return hay.includes(q);
    };
    const groups: Record<Stage, QuestMap[]> = { 小学: [], 初中: [], 高中: [] };
    for (const map of maps) {
      if (match(map)) groups[map.meta.stage].push(map);
    }
    return groups;
  }, [maps, q]);

  return (
    <div>
      <input
        className="search"
        type="search"
        value={query}
        placeholder="搜索地图标题、领域……"
        onChange={(e) => setQuery(e.target.value)}
        aria-label="搜索地图"
      />

      {STAGE_ORDER.map((stage) => {
        const items = grouped[stage];
        return (
          <section className="stage-block" key={stage}>
            <h2>{stage}</h2>
            {items.length === 0 ? (
              <p className="empty">{q ? `没有匹配「${query}」的${stage}地图。` : STAGE_EMPTY[stage]}</p>
            ) : (
              <div className="map-grid">
                {items.map((map) => {
                  const { lit, total } = litCount(map, progress);
                  const cleared = progress.cleared_map_ids.includes(map.meta.id);
                  return (
                    <a
                      key={map.meta.id}
                      className="map-card"
                      href={`#/m/${encodeURIComponent(map.meta.id)}`}
                      onClick={(e) => {
                        e.preventDefault();
                        onOpenMap(map.meta.id);
                      }}
                    >
                      <div className="kicker">
                        {map.meta.subject} · {map.meta.grade}年级 · {map.meta.strand}
                      </div>
                      <h3>{map.meta.title}</h3>
                      <p>{map.meta.description}</p>
                      <div className="meta-row">
                        <span className="badge">
                          点亮 {lit}/{total}
                        </span>
                        {cleared && <span className="badge cleared">已通关</span>}
                      </div>
                    </a>
                  );
                })}
              </div>
            )}
          </section>
        );
      })}
    </div>
  );
}
