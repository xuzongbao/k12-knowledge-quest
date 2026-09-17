import { useMemo, useState } from "react";
import {
  canEnterNode,
  deriveNodeState,
  isBossNode,
  isSoftRecommended,
  isStartNode,
  litCount,
  prerequisiteHints,
  resetMapProgress,
  unlockLayers,
} from "../engine";
import { STATE_LABEL } from "../labels";
import type { NodeState, PlayerProgress, QuestMap } from "../types";

type Filter = "all" | "playable" | "lit" | "boss";

interface Props {
  map: QuestMap;
  progress: PlayerProgress;
  onBack: () => void;
  onOpenNode: (nodeId: string) => void;
  onBlocked: (message: string) => void;
  onReset: (next: PlayerProgress) => void;
}

export default function MapView({ map, progress, onBack, onOpenNode, onBlocked, onReset }: Props) {
  const [filter, setFilter] = useState<Filter>("all");
  const { lit, total } = litCount(map, progress);
  const pct = total === 0 ? 0 : Math.round((lit / total) * 100);
  const layers = useMemo(() => unlockLayers(map), [map]);
  const cleared = progress.cleared_map_ids.includes(map.meta.id);

  const visible = (id: string) => {
    const node = map.nodes.find((n) => n.id === id);
    if (!node) return false;
    const state = deriveNodeState(map, progress, id);
    if (filter === "playable") return canEnterNode(map, progress, id) && state !== "lit";
    if (filter === "lit") return state === "lit" || state === "needs_review";
    if (filter === "boss") return isBossNode(map, node);
    return true;
  };

  return (
    <div>
      <a
        className="back-link"
        href="#/"
        onClick={(e) => {
          e.preventDefault();
          onBack();
        }}
      >
        ← 全部地图
      </a>

      <div className="map-head">
        <div className="kicker">
          {map.meta.stage} · {map.meta.grade}年级 · {map.meta.strand}
        </div>
        <h2>{map.meta.title}</h2>
        <p className="desc">{map.meta.description}</p>
      </div>

      <div className="progress-bar" aria-label={`点亮 ${lit} / ${total}`}>
        <span style={{ width: `${pct}%` }} />
      </div>
      <p>
        点亮 {lit}/{total}
        {cleared ? " · 已通关" : ""}
      </p>
      <p className="note">{map.meta.win_condition.summary}</p>
      {map.meta.recommended_path_note && <p className="note">{map.meta.recommended_path_note}</p>}

      <div className="toolbar">
        <div className="chip-row">
          {(
            [
              ["all", "全部"],
              ["playable", "可学"],
              ["lit", "已点亮"],
              ["boss", "关主"],
            ] as const
          ).map(([id, label]) => (
            <button
              key={id}
              type="button"
              className={`chip ${filter === id ? "active" : ""}`}
              onClick={() => setFilter(id)}
            >
              {label}
            </button>
          ))}
        </div>
        <button
          type="button"
          className="danger"
          onClick={() => {
            if (window.confirm("确定清除这张地图的进度吗？本图经验和通关记录会一起清掉。")) {
              onReset(resetMapProgress(map, progress));
            }
          }}
        >
          重置本图进度
        </button>
      </div>

      <div className="layers">
        {layers.map((layer, i) => {
          const shown = layer.filter(visible);
          if (shown.length === 0) return null;
          return (
            <div className="layer" key={i}>
              <div className="layer-label">第 {i + 1} 层</div>
              {shown.map((id) => {
                const node = map.nodes.find((n) => n.id === id);
                if (!node) return null;
                const state = deriveNodeState(map, progress, id);
                const enter = canEnterNode(map, progress, id);
                const hints = prerequisiteHints(map, progress, id);
                const missing = hints.filter((h) => !h.mastered);
                const classes = [
                  "node-card",
                  `state-${state}`,
                  state === "locked" && !enter ? "locked" : "",
                  state === "locked" && enter ? "soft-open" : "",
                ]
                  .filter(Boolean)
                  .join(" ");

                return (
                  <button
                    key={id}
                    type="button"
                    className={classes}
                    onClick={() => {
                      if (!enter) {
                        onBlocked(
                          missing.length
                            ? `还锁着。需要先点亮：${missing.map((m) => m.title).join("、")}`
                            : "这个知识点还锁着。",
                        );
                        return;
                      }
                      onOpenNode(id);
                    }}
                  >
                    <h3>{node.title}</h3>
                    <p className="sub">{STATE_LABEL[state as NodeState]}</p>
                    <div className="meta-row">
                      {isStartNode(map, id) && <span className="badge start">起点</span>}
                      {isBossNode(map, node) && <span className="badge boss">关主</span>}
                      {isSoftRecommended(node) && <span className="badge soft">软锁支线</span>}
                    </div>
                    {missing.length > 0 && (
                      <p className="sub">
                        {isSoftRecommended(node) ? "建议先点亮：" : "需要先点亮："}
                        {missing.map((m) => m.title).join("、")}
                      </p>
                    )}
                  </button>
                );
              })}
            </div>
          );
        })}
      </div>

      {map.meta.content_disclaimer && <p className="disclaimer">{map.meta.content_disclaimer}</p>}
    </div>
  );
}
