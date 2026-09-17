"""Build Grade 9 Comprehensive Practice map JSON (九年级 · 综合与实践).

Run: python3 scripts/_build_jm_g9_practice.py

原创课题：用样本估计全年级偏好；无障碍坡道坡度设计。
流程：发现问题 → 建模 → 求解 → 交流。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _junior_common import (
    MASTERY_CONCEPT,
    MASTERY_GATE,
    ROOT,
    SOFT,
    node as _node,
    q,
    sample_progress,
    write_map,
)

OUT = ROOT / "maps" / "junior-math" / "grade-9-practice"
G = 9
STRAND = "综合与实践"
P = "jm-g9-prac"
MAP_ID = "jm-g9-practice"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：全年级的口味说不清", 1, [], ["find", "ch-survey"], "能从「众说纷纭」感到：要了解全年级偏好，不能只问自己的朋友。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：抽样方案", 2, [N(1)], ["plan", "ch-survey"], "能写出总体、样本容量、如何尽量做到每个同学被抽到的机会相近。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：收集样本", 3, [N(2)], ["do", "ch-survey"], "能按方案收集样本（可用合理假设数据），注明来源和时间。"),
    node(N(4), "实施：整理与估计", 3, [N(3)], ["do", "ch-survey"], "能整理频数，用样本比例估计总体偏好，并写「估计」。"),
    node(N(5), "实施：指出局限", 3, [N(4)], ["do", "ch-survey"], "能写出样本可能缺了哪一类人，因而估计可能偏。"),
    node(N(6), "交流：偏好估计答辩", 3, [N(5)], ["share", "ch-survey", "boss-gate"], "能讲清方案、估计结果和不能代表谁。", mastery=MASTERY_GATE),
    node(N(7), "发现：台阶难上", 2, [N(6)], ["find", "ch-ramp"], "能提出为一级台阶或短高差做无障碍坡道的问题，指出要控制坡度。", mastery=MASTERY_CONCEPT),
    node(N(8), "计划：坡度模型", 2, [N(7)], ["plan", "ch-ramp"], "能把坡道抽象成直角三角形：高度、水平长度、坡度（或仰角）。", mastery=MASTERY_CONCEPT),
    node(N(9), "实施：测量高度", 3, [N(8)], ["do", "ch-ramp"], "能测量或合理假设高差，并注明单位。"),
    node(N(10), "实施：按限制求长度", 3, [N(9)], ["do", "ch-ramp"], "能根据给定的最大坡度（或最大仰角）求至少需要多长的水平距离。"),
    node(N(11), "实施：检查场地够不够", 3, [N(10)], ["do", "ch-ramp"], "能对照场地实际长度，判断方案是否放得下，放不下就改折线坡道或说明做不到。"),
    node(N(12), "交流：坡道说明会", 4, [N(11)], ["share", "ch-ramp"], "能讲解模型、计算和场地限制，回答「为什么不能更陡」。", mastery=MASTERY_GATE),
    node(N(13), "发现：调查和坡道能一起做吗", 2, [N(6)], ["find", "ch-mix"], "能提出一个同时用到抽样估计和坡度计算的问题，例如「多少人需要缓坡」。", mastery=MASTERY_CONCEPT),
    node(N(14), "计划：课题说明书", 2, [N(13)], ["plan", "ch-mix"], "能写问题、数据与尺寸来源、步骤、交流展示。", mastery=MASTERY_CONCEPT),
    node(N(15), "实施：走完四步", 3, [N(12), N(14)], ["do", "ch-mix"], "能按说明书完成估计或计算，并写下局限。"),
    node(N(16), "交流：初中实践成果卡", 3, [N(15)], ["share", "ch-mix"], "能用四句话写成果卡：问题、模型、结果、局限。", mastery=MASTERY_CONCEPT),
    node(N(17), "实践工具箱", 3, [N(16)], ["mixed", "ch-end"], "能列出四步，以及抽样估计与直角三角形模型两种常用工具。", mastery=MASTERY_CONCEPT),
    node(N(18), "九年级实践合练", 4, [N(17)], ["mixed", "ch-end"], "能抽签完成偏好估计或坡道设计的完整流程。", mastery=MASTERY_GATE),
    node(N(19), "九年级实践通关", 5, [N(18)], ["mixed", "ch-end", "boss-gate"], "能独立完成九年级综合与实践线的收束检查。", mastery=MASTERY_GATE),
    node(N(20), "只问志愿者会怎样", 3, [N(6)], ["survey", "ch-survey"], "能说明只让自愿填表会导致样本偏向爱发表意见的人。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(21), "坡度限制从哪来", 3, [N(12)], ["ramp", "ch-ramp"], "能说明最大坡度是外部约定（规范或使用者需求），不是数学推出来的，但数学负责在限制下求长度。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(4), "type": "application", "note": "方案决定样本，样本决定估计能不能代表总体。"},
    {"from": N(5), "to": N(20), "type": "related", "note": "缺某一类人的极端情形就是只问志愿者。"},
    {"from": N(8), "to": N(10), "type": "application", "note": "直角三角形模型让「不能太陡」变成可计算的最小水平长度。"},
    {"from": N(11), "to": N(21), "type": "related", "note": "场地不够时，要回到坡度限制是谁定的、能不能改方案。"},
]


QUESTS = [
    q(N(1), "explain", "不能只问朋友", "说明只问朋友为什么不能代表全年级。", "朋友圈往往更像你。"),
    q(N(2), "explain", "写出抽样方案", "写总体、大约抽多少、怎么抽。", "尽量让每个人机会相近。"),
    q(N(3), "practice", "留下样本记录", "记录一组样本（可假设），注明来源时间。", "没有来源不能答辩。", items=1),
    q(N(4), "practice", "估计偏好", "整理频数并用样本比例估计总体，结论带「估计」。", "不要写成全年级确定值。", items=1),
    q(N(5), "explain", "可能缺了谁", "指出样本可能缺少的一类人。", "缺了谁，估计就可能偏。"),
    q(N(6), "explain", "不能代表谁", "明确说出结论不能推广到谁。", "对象范围要小于等于样本能代表的范围。"),
    q(N(6), "mini_quiz", "调查质量小测", "找无方案、无来源、结论越界的报告。", "估计用语和对象范围都要在。", items=6),
    q(N(6), "boss", "关主：偏好估计员", "击败关主：①写出抽样方案 ②用样本估计并写「估计」 ③说出局限。", "代表性先于百分比。", xp=80, items=8, qid=f"{P}-boss-survey"),
    q(N(7), "explain", "问题落到坡度", "说明台阶难上与坡度、高度有关。", "要控制的是陡不陡。"),
    q(N(8), "explain", "画直角三角形", "画出高、水平长、斜面，标出坡度或仰角。", "模型忽略扶手宽度等细节。"),
    q(N(9), "practice", "记下高差", "测量或假设高差，写单位。", "单位错了后面全错。", items=1),
    q(N(10), "practice", "求最小水平长", "根据最大坡度求至少多长。", "坡度是高与水平长的比，或用正切。", items=1),
    q(N(11), "practice", "对照场地", "比较需要的长度和场地，给出放得下或改方案的结论。", "放不下不是计算错，是约束冲突。", items=1),
    q(N(12), "practice", "回答为什么不能更陡", "用模型说明更陡会超过约定限制。", "限制是约定，计算负责检查。", items=1),
    q(N(12), "mini_quiz", "坡道质量小测", "找无高差、无限制、无场地对照的方案。", "三数都要在。", items=4),
    q(N(13), "explain", "提出综合问题", "写出同时用到抽样和坡度的问题。", "两种模型都要用到。"),
    q(N(14), "explain", "写说明书", "写问题、来源、步骤、展示物。", "别人能开工。"),
    q(N(15), "practice", "留下证据", "完成估计或计算，写局限。", "局限对应抽样或场地假设。", items=1),
    q(N(16), "practice", "四句成果卡", "问题、模型、结果、局限。", "模型可以是抽样，也可以是直角三角形。", items=1),
    q(N(17), "explain", "打开工具箱", "说出四步和两种常用模型。", "估计总体、计算坡度。"),
    q(N(18), "practice", "抽签走流程", "抽调查或坡道之一完整做完。", "发现—计划—实施—交流。", items=1),
    q(N(19), "practice", "通关综合练", "独立完成一个带估计或坡度计算的项目。", "能说局限。", items=1),
    q(N(19), "boss", "关主：九年级实践通关试炼", "最终关主：①展示带方案的偏好估计 ②展示坡道直角三角形计算 ③说出局限。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
    q(N(20), "explain", "志愿者偏差", "说明自愿填表会偏向谁。", "爱说话的人更容易进样本。"),
    q(N(21), "explain", "限制不是公式给的", "区分「规范要求的最大坡度」和「由高差算出的长度」。", "数学管计算，限制来自使用需求。"),
]


META = {
    "id": MAP_ID,
    "title": "九年级 · 综合与实践",
    "subject": "数学",
    "stage": "初中",
    "grade": 9,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "全年级偏好抽样估计为主线（关主 1）；无障碍坡道在其后展开。志愿者偏差（n020）、坡度限制来源（n021）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-survey", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：偏好估计员、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "初中九年级「综合与实践」地图：用样本估计偏好、无障碍坡道坡度。独立通关。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress(MAP_ID, N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
