"""Build Grade 8 Statistics map JSON (八年级 · 统计与概率).

Run: python3 scripts/_build_jm_g8_statistics.py

Pedagogical spine: 加权平均 → 极差与方差入门 → 频数直方图 → 概率定义与简单计算。
本图自洽。
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

OUT = ROOT / "maps" / "junior-math" / "grade-8-statistics"
G = 8
STRAND = "统计与概率"
P = "jm-g8-stat"
MAP_ID = "jm-g8-statistics"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "平均数还不够", 1, [], ["avg", "ch-avg"], "能举出各组人数不同时，直接把组平均数再平均会不公平，从而感到需要加权。", mastery=MASTERY_CONCEPT),
    node(N(2), "权的意义", 2, [N(1)], ["avg", "ch-avg"], "能说明权表示这一组占的份量，如人数、学分或时长。", mastery=MASTERY_CONCEPT),
    node(N(3), "加权平均数", 3, [N(2)], ["avg", "ch-avg"], "能计算加权平均数：各数据乘以权后相加，再除以权的总和。", mastery=MASTERY_GATE),
    node(N(4), "权变了结果变", 3, [N(3)], ["avg", "ch-avg"], "能比较同一组数据在不同权下的加权平均，说明权大的组更能拉动结果。"),
    node(N(5), "加权平均应用", 3, [N(4)], ["avg", "ch-avg"], "能在成绩、单价、平均速度等简单情境中选用加权平均。"),
    node(N(6), "数据的波动", 2, [N(5)], ["var", "ch-var"], "能说明两组平均数相近时，仍可能一组更「散」、一组更「挤」。", mastery=MASTERY_CONCEPT),
    node(N(7), "极差", 2, [N(6)], ["var", "ch-var"], "能用最大值减最小值得到极差，并说明它只看两端、不管中间。"),
    node(N(8), "方差入门", 4, [N(7)], ["var", "ch-var"], "能理解方差用「每个数据与平均数差的平方的平均」刻画整体偏离程度。", mastery=MASTERY_GATE),
    node(N(9), "方差小表示更整齐", 3, [N(8)], ["var", "ch-var"], "能比较两组方差，说明方差小的一组更整齐（在平均数相近时）。"),
    node(N(10), "波动量综合", 4, [N(9)], ["var", "ch-var", "boss-gate"], "能对同一组数据求加权平均或算术平均、极差，并解释方差大小的含义。", mastery=MASTERY_GATE),
    node(N(11), "把数据分组", 2, [N(6)], ["hist", "ch-hist"], "能把一组数值数据分成若干组，说明组距要适当。", mastery=MASTERY_CONCEPT),
    node(N(12), "频数分布表", 3, [N(11)], ["hist", "ch-hist"], "能填写各组频数，必要时加频率。"),
    node(N(13), "直方图长什么样", 3, [N(12)], ["hist", "ch-hist"], "能说明直方图用矩形面积（组距相等时用高度）表示频数，矩形之间通常不留缝。", mastery=MASTERY_CONCEPT),
    node(N(14), "读直方图", 3, [N(13)], ["hist", "ch-hist"], "能读出哪一组人数最多、大约集中在哪一段。"),
    node(N(15), "直方图与条形图", 3, [N(14)], ["hist", "ch-hist"], "能区分：条形图的类是名称，直方图的横轴是数值分段。", mastery=MASTERY_CONCEPT),
    node(N(16), "直方图综合", 4, [N(15), N(10)], ["hist", "ch-hist"], "能根据问题选择直方图或条形图，并结合平均数或方差读数据。", mastery=MASTERY_GATE),
    node(N(17), "随机事件再认识", 2, [N(10)], ["prob", "ch-prob"], "能在较复杂的校园情境中指出随机事件，并说明条件。", mastery=MASTERY_CONCEPT),
    node(N(18), "概率的意义", 3, [N(17)], ["prob", "ch-prob"], "能把概率理解为刻画随机事件发生可能性大小的数，它在 0 和 1 之间。", mastery=MASTERY_CONCEPT),
    node(N(19), "等可能与古典概型入门", 3, [N(18)], ["prob", "ch-prob"], "能在结果有限且等可能时，用有利结果数除以全部结果数求概率。", mastery=MASTERY_GATE),
    node(N(20), "列表法", 3, [N(19)], ["prob", "ch-prob"], "能用表格列出两个一步试验的全部结果，再数有利格。"),
    node(N(21), "树状图入门", 3, [N(19)], ["prob", "ch-prob"], "能画简单树状图表示分步结果，再求概率。"),
    node(N(22), "概率计算综合", 4, [N(20), N(21)], ["prob", "ch-prob", "boss-gate"], "能选择列表或树状图求简单概率，并检查是否等可能。", mastery=MASTERY_GATE),
    node(N(23), "频率稳定趋势", 3, [N(18)], ["prob", "ch-prob"], "能说明大量重复试验时频率会靠近概率，但有限次不必相等。", mastery=MASTERY_CONCEPT),
    node(N(24), "统计与概率合练", 4, [N(16), N(22), N(23)], ["mixed", "ch-end"], "能在同一课题里用直方图或加权平均描述数据，并用概率描述尚未发生的等可能结果。", mastery=MASTERY_GATE),
    node(N(25), "八年级统计通关", 5, [N(24)], ["mixed", "ch-end", "boss-gate"], "能独立完成八年级统计与概率线的收束检查。", mastery=MASTERY_GATE),
    node(N(26), "权不是分数本身", 3, [N(3)], ["avg", "ch-avg"], "能纠正「权必须是百分数」的误解：权是份量，可以是人数。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "组距不等的提醒", 3, [N(13)], ["hist", "ch-hist"], "能说明组距不等时不能只比矩形高度，而要看面积（本图只提醒，不要求复杂计算）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "不是等可能就别硬除", 3, [N(19)], ["prob", "ch-prob"], "能举出图钉落地等结果不等可能的例子，说明此时不能用古典概型硬除。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(3), "to": N(1), "type": "application", "note": "加权平均就是为了纠正「组平均数再平均」的不公平。"},
    {"from": N(7), "to": N(8), "type": "easily_confused", "note": "极差只看两端；方差看每一个数离平均有多远。"},
    {"from": N(13), "to": N(15), "type": "easily_confused", "note": "直方图的横轴是数轴分段，条形图的横轴常常是类别名称。"},
    {"from": N(20), "to": N(21), "type": "related", "note": "两步试验用树状图有时比表格更清楚。"},
    {"from": N(19), "to": N(28), "type": "easily_confused", "note": "古典概型的前提是等可能，不是「结果有几种就除几」。"},
    {"from": N(18), "to": N(23), "type": "related", "note": "概率是模型值，频率是试验值，次数多了会靠近。"},
]


QUESTS = [
    q(N(1), "explain", "为什么不能再平均一次", "两个班人数不同、平均分不同，说明直接把两个平均分再平均为什么不公平。", "人数就是权。"),
    q(N(2), "explain", "权是份量", "举人数、时间、学分三个权的例子。", "权越大，这一组越能拉动结果。"),
    q(N(3), "practice", "算加权平均", "6 组数据计算加权平均数。", "先乘权再加，最后除以权的和。", items=6),
    q(N(4), "practice", "改权看变化", "同一组成绩改两组权，比较加权平均。", "权大的那一组更能把结果拽过去。", items=3),
    q(N(5), "practice", "选对平均", "6 个情境判断用算术平均还是加权平均。", "份量不同就要加权。", items=6),
    q(N(6), "explain", "散还是挤", "画两组平均数相近、一散一挤的点，说明只看平均不够。", "波动是另一件事。"),
    q(N(7), "practice", "求极差", "8 组数据求极差。", "最大减最小。", items=8),
    q(N(8), "practice", "体会方差", "对两组小数据计算或比较方差（可用计算器），说出哪一组更整齐。", "差的平方再平均。", items=4),
    q(N(9), "explain", "方差小意味着什么", "在平均数差不多时，解释方差小的一组更整齐。", "不要离开平均数单独谈方差。"),
    q(N(10), "practice", "波动量闯关", "求加权平均或平均、极差，并比较方差含义。", "先问问题要的是中心还是波动。", items=6),
    q(N(10), "mini_quiz", "平均与波动小测", "加权、极差、方差含义。夹一道「组平均再平均」。", "权是份量。", items=8),
    q(N(10), "boss", "关主：加权与波动分析员", "击败关主：①计算加权平均 ②求极差 ③说明哪一组方差更小、意味着什么。", "中心和波动要分开看。", xp=80, items=10, qid=f"{P}-boss-spread"),
    q(N(11), "practice", "分成几组", "给一组数据选择合理组距并分组。", "组不宜过多或过少。", items=2),
    q(N(12), "practice", "填频数表", "根据分组填写频数（和频率）。", "每条数据只进一组。", items=2),
    q(N(13), "explain", "直方图的矩形", "说明组距相等时，矩形高表示频数，矩形一般紧挨着。", "紧挨着是因为横轴是连续分段。"),
    q(N(14), "practice", "读直方图", "读最多的一组、大约范围、合计是否合理，共 6 题。", "先看组距和图例。", items=6),
    q(N(15), "practice", "选直方图还是条形图", "6 个问题选择图种。", "数值分段用直方图，名称类别用条形图。", items=6),
    q(N(16), "practice", "图表与统计量", "读一幅直方图并指出用平均还是方差更合适回答给定问题。", "问集中用平均，问整齐用方差。", items=2),
    q(N(17), "explain", "指出随机事件", "在校园情境中列出一个随机事件并写清条件。", "条件变了，事件可能不再随机。"),
    q(N(18), "explain", "概率是 0 到 1 的数", "说明 0 表示不可能，1 表示必然，越靠近 1 越可能发生。", "概率不是百分数必须，但可以改写成百分数。"),
    q(N(19), "practice", "古典概型入门", "8 个等可能事件求概率。", "有利个数 / 全部个数。", items=8),
    q(N(20), "practice", "列表求概率", "两个骰子或两个转盘用表列出再求概率，共 4 题。", "每格是否等可能要先确认。", items=4),
    q(N(21), "practice", "树状图求概率", "画 3 个简单树状图并求概率。", "每条完整路径是一个结果。", items=3),
    q(N(22), "practice", "选工具求概率", "混合列表与树状图 4 题，并写是否等可能。", "不等可能就不要硬除。", items=4),
    q(N(22), "mini_quiz", "概率小测", "意义、古典概型、列表或树状图。", "先检查等可能。", items=8),
    q(N(22), "boss", "关主：概率绘图员", "击败关主：①说出概率在 0 与 1 之间 ②用列表或树状图求一个概率 ③指出一个不能用古典概型的例子。", "工具服务于等可能假设。", xp=80, items=10, qid=f"{P}-boss-probability"),
    q(N(23), "explain", "频率会靠近吗", "用自己的话说明大量重复时频率靠近概率。", "靠近不是次次相等。"),
    q(N(24), "practice", "课题两手抓", "一组数据：加权或直方图 + 一个等可能概率。", "已有数据用统计，尚未发生用概率。", items=1),
    q(N(25), "practice", "通关综合练", "加权平均、方差含义、读直方图、求简单概率。", "先辨题型。", items=12),
    q(N(25), "boss", "关主：八年级统计通关试炼", "最终关主：①加权平均 ②说明方差或极差 ③读直方图 ④求一个等可能概率。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(26), "explain", "权可以是人数", "纠正「权必须写成百分数」的说法。", "人数、次数都可以当权。"),
    q(N(27), "explain", "高度不能直接比", "画一个组距不同的示意，说明只比高度会误导。", "面积才对应频数。"),
    q(N(28), "explain", "图钉的两面", "说明图钉尖朝上与朝下不必等可能，因而不能用 1/2 硬套。", "等可能要有理由。"),
]


META = {
    "id": MAP_ID,
    "title": "八年级 · 统计与概率",
    "subject": "数学",
    "stage": "初中",
    "grade": 8,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "加权平均与波动（关主 1）；直方图从波动后并行；概率在波动关后并行（关主 2）。权的误解、组距提醒、不等可能（n026–n028）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-spread", f"{P}-boss-probability", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：加权与波动分析员、概率绘图员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中八年级「统计与概率」地图：加权平均、极差与方差入门、直方图、概率定义与列表树状图。独立通关。",
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
