"""Build Grade 8 Comprehensive Practice map JSON (八年级 · 综合与实践).

Run: python3 scripts/_build_jm_g8_practice.py

原创课题：校运会分组尽量公平；取水最短路径（轴对称思想）。
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

OUT = ROOT / "maps" / "junior-math" / "grade-8-practice"
G = 8
STRAND = "综合与实践"
P = "jm-g8-prac"
MAP_ID = "jm-g8-practice"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：分组总被嫌不公", 1, [], ["find", "ch-fair"], "能从「强队分到一起」感到：公平需要可检查的规则，而不是感觉。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：公平的操作定义", 2, [N(1)], ["plan", "ch-fair"], "能把公平写成可计算的目标，例如各组平均分接近、极差不要太大。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：收集能力数据", 3, [N(2)], ["do", "ch-fair"], "能用已有测验或自报项目整理一张能力表（可用合理假设数据）。"),
    node(N(4), "实施：试分两组", 3, [N(3)], ["do", "ch-fair"], "能给出一种分组，计算两组平均与极差。"),
    node(N(5), "实施：调整再比", 3, [N(4)], ["do", "ch-fair"], "能交换两名成员后重新计算，说明哪一种更接近目标。"),
    node(N(6), "交流：公平方案答辩", 3, [N(5)], ["share", "ch-fair", "boss-gate"], "能讲清目标函数、一次调整的理由，以及方案仍不完美之处。", mastery=MASTERY_GATE),
    node(N(7), "发现：取水要绕路", 2, [N(6)], ["find", "ch-path"], "能提出「从营地到河边取水再送到灶台」的最短路径问题。", mastery=MASTERY_CONCEPT),
    node(N(8), "计划：把河岸看成直线", 2, [N(7)], ["plan", "ch-path"], "能把河岸抽象成直线，营地和灶台抽象成直线同侧两点。", mastery=MASTERY_CONCEPT),
    node(N(9), "实施：作出对称点", 3, [N(8)], ["do", "ch-path"], "能作其中一点关于直线的对称点。"),
    node(N(10), "实施：连线得折点", 3, [N(9)], ["do", "ch-path"], "能连接对称点与另一点，与直线交点即为取水点。"),
    node(N(11), "实施：说明为什么最短", 3, [N(10)], ["do", "ch-path"], "能用「对称后变成两点一线」说明这条折线最短。"),
    node(N(12), "交流：路径说明会", 4, [N(11)], ["share", "ch-path"], "能向同学讲解作图步骤，并回答「如果两点在直线两侧呢」。", mastery=MASTERY_GATE),
    node(N(13), "发现：公平和路径能一起出现吗", 2, [N(6)], ["find", "ch-mix"], "能提出一个同时用到分组数据和路线的问题，例如后勤取水点怎么选。", mastery=MASTERY_CONCEPT),
    node(N(14), "计划：课题说明书", 2, [N(13)], ["plan", "ch-mix"], "能写问题、模型（表或对称作图）、步骤、交流时展示什么。", mastery=MASTERY_CONCEPT),
    node(N(15), "实施：走完四步", 3, [N(12), N(14)], ["do", "ch-mix"], "能按说明书完成计算或作图，并写下局限。"),
    node(N(16), "交流：成果卡", 3, [N(15)], ["share", "ch-mix"], "能用四句话写成果卡：问题、模型、结果、局限。", mastery=MASTERY_CONCEPT),
    node(N(17), "实践工具箱", 3, [N(16)], ["mixed", "ch-end"], "能列出四步以及「把公平或最短写成可操作的目标」这件事。", mastery=MASTERY_CONCEPT),
    node(N(18), "八年级实践合练", 4, [N(17)], ["mixed", "ch-end"], "能抽签完成分组或最短路径中的完整流程。", mastery=MASTERY_GATE),
    node(N(19), "八年级实践通关", 5, [N(18)], ["mixed", "ch-end", "boss-gate"], "能独立完成八年级综合与实践线的收束检查。", mastery=MASTERY_GATE),
    node(N(20), "公平还有别的定义", 3, [N(6)], ["fair", "ch-fair"], "能提出另一种公平，例如最强的两人必须分开，并说明与「平均接近」可能冲突。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(21), "河岸不是直线时", 3, [N(12)], ["path", "ch-path"], "能说明河岸弯曲时对称法只是近似，结论要降级。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(5), "type": "application", "note": "没有操作定义，就无法判断哪一次调整更好。"},
    {"from": N(4), "to": N(20), "type": "related", "note": "平均接近只是一种公平，还可以加别的约束。"},
    {"from": N(8), "to": N(11), "type": "application", "note": "模型把河岸看成直线之后，对称才合法。"},
    {"from": N(11), "to": N(21), "type": "easily_confused", "note": "直线假设不成立时，最短折点不必在对称连线上。"},
]


QUESTS = [
    q(N(1), "explain", "不公的感觉", "讲述一次分组被嫌不公，指出大家在比什么。", "先感到需要规则。"),
    q(N(2), "explain", "写成可计算的目标", "把公平写成至少一条可以算的句子。", "例如两组平均分相差不超过 2。"),
    q(N(3), "practice", "整理能力表", "列出至少 8 人的一项能力数据（可假设）。", "数据要有单位和来源说明。", items=1),
    q(N(4), "practice", "算两组指标", "给出一种分组，计算两组平均与极差。", "先算再评价。", items=1),
    q(N(5), "practice", "交换后再算", "交换两名成员，比较指标是否更接近目标。", "每一次调整都要留下计算。", items=1),
    q(N(6), "explain", "承认不完美", "说明方案仍可能被质疑的一点。", "公平定义本身就有取舍。"),
    q(N(6), "mini_quiz", "分组质量小测", "找三份方案的问题：无目标、无计算、只凭印象。", "不能检查的公平不是方案。", items=6),
    q(N(6), "boss", "关主：公平分组师", "击败关主：①写出公平的操作定义 ②展示一次调整前后的计算 ③说出局限。", "可计算才能答辩。", xp=80, items=8, qid=f"{P}-boss-fair"),
    q(N(7), "explain", "路径问题", "用自己的话提出取水最短路径，指出三个地点。", "问题要落到图上的点与线。"),
    q(N(8), "explain", "抽象成直线和点", "说明为什么把河岸看成直线，忽略宽度。", "模型要写清忽略了什么。"),
    q(N(9), "practice", "作对称点", "作出点关于直线的对称点，标出垂线。", "对应点连线被直线垂直平分。", items=1),
    q(N(10), "practice", "找到取水点", "连接并标出与河岸的交点。", "交点就是取水点。", items=1),
    q(N(11), "explain", "为什么最短", "用对称把折线变成线段，说明两点之间线段最短。", "对称把「到直线的距离」变成相等的另一段。"),
    q(N(12), "practice", "回答两侧情形", "说明两点在直线两侧时应直接相连，不必对称。", "模型假设变了，方法也变。", items=1),
    q(N(12), "mini_quiz", "路径质量小测", "找作图缺步骤或把两侧情形用错方法的例子。", "先看两点在同侧还是异侧。", items=4),
    q(N(13), "explain", "提出综合问题", "写出一个同时用到分组数据和路线的问题。", "两种模型都要用到。"),
    q(N(14), "explain", "写说明书", "写问题、模型、步骤、展示物。", "别人能按说明书开工。"),
    q(N(15), "practice", "留下证据", "完成计算或作图，写一句局限。", "局限对应模型假设。", items=1),
    q(N(16), "practice", "四句成果卡", "问题、模型、结果、局限。", "模型可以是指标，也可以是对称作图。", items=1),
    q(N(17), "explain", "打开工具箱", "说出四步，以及如何把「公平/最短」写成可操作目标。", "目标可检查，方案才能比较。"),
    q(N(18), "practice", "抽签走流程", "抽分组或路径之一完整做完。", "发现—计划—实施—交流。", items=1),
    q(N(19), "practice", "通关综合练", "独立完成一个带目标或作图的小项目。", "能说局限。", items=1),
    q(N(19), "boss", "关主：八年级实践通关试炼", "最终关主：①展示带计算的公平分组或调整 ②展示对称法得到的取水点 ③说出模型局限。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
    q(N(20), "explain", "两种公平打架", "举「平均接近」和「最强必须分开」冲突的例子，说明要先排优先级。", "多个目标时要说清谁优先。"),
    q(N(21), "explain", "弯曲河岸", "说明河岸弯曲时对称法只是近似。", "假设不成立，结论要降级。"),
]


META = {
    "id": MAP_ID,
    "title": "八年级 · 综合与实践",
    "subject": "数学",
    "stage": "初中",
    "grade": 8,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "公平分组为主线（关主 1）；取水最短路径在其后展开。另类公平定义（n020）、弯曲河岸（n021）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-fair", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：公平分组师、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "初中八年级「综合与实践」地图：公平分组建模、轴对称最短路径。独立通关。",
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
