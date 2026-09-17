import {
  canEnterNode,
  completeQuest,
  deriveNodeState,
  isBossNode,
  isSoftRecommended,
  isStartNode,
  meetsMastery,
  prerequisiteHints,
  questsForNode,
  storedProgress,
} from "../engine";
import { QUEST_LABEL, STATE_LABEL } from "../labels";
import type { CompleteQuestResult, PlayerProgress, QuestMap } from "../types";

interface Props {
  map: QuestMap;
  nodeId: string;
  progress: PlayerProgress;
  onBack: () => void;
  onProgress: (next: PlayerProgress, note: CompleteQuestResult) => void;
}

export default function NodeView({ map, nodeId, progress, onBack, onProgress }: Props) {
  const node = map.nodes.find((n) => n.id === nodeId);
  if (!node) {
    return (
      <div>
        <a
          className="back-link"
          href={`#/m/${encodeURIComponent(map.meta.id)}`}
          onClick={(e) => {
            e.preventDefault();
            onBack();
          }}
        >
          ← 返回地图
        </a>
        <p>找不到这个知识点。</p>
      </div>
    );
  }

  const state = deriveNodeState(map, progress, node.id);
  const enter = canEnterNode(map, progress, node.id);
  const row = storedProgress(progress, node.id);
  const quests = questsForNode(map, node.id);
  const hints = prerequisiteHints(map, progress, node.id);
  const missing = hints.filter((h) => !h.mastered);
  const mastered = meetsMastery(node, map, row.cleared_quest_ids);

  return (
    <div>
      <a
        className="back-link"
        href={`#/m/${encodeURIComponent(map.meta.id)}`}
        onClick={(e) => {
          e.preventDefault();
          onBack();
        }}
      >
        ← {map.meta.title}
      </a>

      <div className="map-head">
        <div className="meta-row">
          <span className={`badge ${state === "lit" ? "cleared" : ""}`}>{STATE_LABEL[state]}</span>
          {isStartNode(map, node.id) && <span className="badge start">起点</span>}
          {isBossNode(map, node) && <span className="badge boss">关主</span>}
          {isSoftRecommended(node) && <span className="badge soft">软锁支线</span>}
        </div>
        <h2>{node.title}</h2>
        <p className="desc">{node.description}</p>
      </div>

      {hints.length > 0 && (
        <p className="note">
          {isSoftRecommended(node) ? "建议先点亮：" : "前置知识点："}
          {hints.map((h) => `${h.title}${h.mastered ? "（已亮）" : "（未亮）"}`).join("、")}
        </p>
      )}

      {!enter && (
        <p className="note">
          还锁着
          {missing.length ? `，需要先点亮：${missing.map((m) => m.title).join("、")}` : "。"}
          最多可以看看标题。
        </p>
      )}

      {enter && (
        <>
          <p className="muted">
            点亮条件：完成至少 {node.mastery_criteria.min_quests_cleared} 个任务
            {node.mastery_criteria.require_quest_types?.length
              ? `，并包含 ${node.mastery_criteria.require_quest_types.map((t) => QUEST_LABEL[t]).join("、")}`
              : ""}
            。{mastered ? "已经达到掌握标准。" : ""}
          </p>
          <div className="quest-list">
            {quests.map((quest) => {
              const done = row.cleared_quest_ids.includes(quest.id);
              return (
                <article className="quest-card panel" key={quest.id}>
                  <div className="meta-row">
                    <span className={`badge ${quest.type === "boss" ? "boss" : ""}`}>
                      {QUEST_LABEL[quest.type]}
                    </span>
                    <span className="badge">+{quest.xp} 经验</span>
                    {done && <span className="badge cleared">已完成</span>}
                  </div>
                  <h3>{quest.title}</h3>
                  <p>{quest.prompt}</p>
                  {quest.success_hint && <p className="muted">提示：{quest.success_hint}</p>}
                  <button
                    type="button"
                    className="primary"
                    disabled={done}
                    onClick={() => {
                      const result = completeQuest(map, progress, quest.id);
                      onProgress(result.progress, result);
                    }}
                  >
                    {done ? "已完成" : quest.type === "boss" ? "我击败了关主" : "我完成了"}
                  </button>
                </article>
              );
            })}
          </div>
        </>
      )}
    </div>
  );
}
