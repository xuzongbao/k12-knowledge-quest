"""Build senior-math 概率与统计 (必修) map.

Run: python3 scripts/_build_sm_probability_statistics.py

Pedagogical spine: 获取数据与抽样 → 数字特征与估计 → 随机事件与古典概型。
方便样本、回归不是因果、组距、普查不是抽样为软锁。条件概率与随机变量见 counting-probability 图。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _senior_common import (
    MASTERY_CONCEPT,
    MASTERY_GATE,
    ROOT,
    SOFT,
    node as _node,
    q,
    sample_progress,
    write_map,
)

OUT = ROOT / "maps" / "senior-math" / "probability-statistics"
G = 10
STRAND = "统计与概率"
P = "sm-stat"
MAP_ID = "sm-probability-statistics"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "问题先于数据", 1, [], ["stat", "ch-stat"], "能把统计问题写成「想了解什么、向谁收集、收集什么量」。本图从问题开始。", mastery=MASTERY_CONCEPT),
    node(N(2), "简单随机抽样", 2, [N(1)], ["stat", "ch-stat"], "能说明总体中每个个体被抽到的机会相同，并描述抽签或随机数的做法。", mastery=MASTERY_CONCEPT),
    node(N(3), "分层抽样", 3, [N(2)], ["stat", "ch-stat"], "能按层的比例分配样本量，说明层内差异小、层间差异大时更合适。", mastery=MASTERY_GATE),
    node(N(4), "系统抽样入门", 2, [N(2)], ["stat", "ch-stat"], "能说明等距抽取，并指出名单若有周期可能偏。"),
    node(N(5), "频率分布与直方图", 3, [N(2)], ["stat", "ch-stat"], "能编制频率分布表并画直方图，说明组距影响形状。"),
    node(N(6), "平均数与加权", 3, [N(5)], ["stat", "ch-num"], "能计算平均数，并用权表示「占的份量不同」。", mastery=MASTERY_CONCEPT),
    node(N(7), "中位数", 2, [N(5)], ["stat", "ch-num"], "能求中位数，并说明它比平均数更不怕极端值。"),
    node(N(8), "百分位数入门", 3, [N(7)], ["stat", "ch-num"], "能解释第 25、75 百分位数把数据切成四段的直觉。", mastery=MASTERY_CONCEPT),
    node(N(9), "方差与标准差", 3, [N(6)], ["stat", "ch-num"], "能说明方差衡量偏离平均数的程度，标准差与原数据同单位。", mastery=MASTERY_GATE),
    node(N(10), "用样本估计总体", 4, [N(3), N(9)], ["stat", "ch-stat", "boss-gate"], "能用样本平均数、比例、标准差去估计总体对应量，并说明这是估计不是普查。", mastery=MASTERY_GATE),
    node(N(11), "散点图", 2, [N(1)], ["stat", "ch-reg"], "能把成对数据画成散点，观察是否有趋势。", mastery=MASTERY_CONCEPT),
    node(N(12), "正相关与负相关", 3, [N(11)], ["stat", "ch-reg"], "能判断正相关、负相关或看不出线性相关。"),
    node(N(13), "线性回归直觉", 4, [N(12), N(6)], ["stat", "ch-reg"], "能说明回归直线是让「竖直偏差」整体变小的一条线，不要求推导公式。", mastery=MASTERY_CONCEPT),
    node(N(14), "统计案例分析骨架", 3, [N(10), N(13)], ["stat", "ch-stat"], "能按「问题—抽样—图表与数字特征—结论与局限」写一份短案例提纲。"),
    node(N(15), "有限样本空间", 2, [N(1)], ["prob", "ch-prob"], "能列出一次随机试验的全部可能结果，构成样本空间。", mastery=MASTERY_CONCEPT),
    node(N(16), "随机事件", 2, [N(15)], ["prob", "ch-prob"], "能把事件看成样本空间的子集，含不可能事件与必然事件。", mastery=MASTERY_CONCEPT),
    node(N(17), "事件的包含与相等", 3, [N(16)], ["prob", "ch-prob"], "能判断事件包含、相等，并用集合语言书写。"),
    node(N(18), "并与交", 3, [N(17)], ["prob", "ch-prob"], "能用并表示「至少一个发生」，用交表示「同时发生」。"),
    node(N(19), "互斥事件", 3, [N(18)], ["prob", "ch-prob"], "能说明互斥是不能同时发生，交为空。", mastery=MASTERY_CONCEPT),
    node(N(20), "对立事件", 3, [N(19)], ["prob", "ch-prob"], "能说明对立是互斥且并起来是全集，概率和为 1。"),
    node(N(21), "古典概型", 4, [N(15), N(20)], ["prob", "ch-prob"], "能在等可能的有限样本空间中用「有利结果数 / 总结果数」求概率。", mastery=MASTERY_GATE),
    node(N(22), "概率加法", 3, [N(21), N(19)], ["prob", "ch-prob"], "能对互斥事件使用 P(A∪B)=P(A)+P(B)。", mastery=MASTERY_GATE),
    node(N(23), "概率的基本性质", 3, [N(22)], ["prob", "ch-prob"], "能使用 0≤P≤1、必然事件为 1、不可能事件为 0。"),
    node(N(24), "频率与概率", 3, [N(21)], ["prob", "ch-prob"], "能说明大量重复试验下频率稳定在概率附近，但有限次会波动。", mastery=MASTERY_CONCEPT),
    node(N(25), "概率统计合练", 4, [N(14), N(23), N(24)], ["mixed", "ch-end"], "能区分「用数据估计」和「在模型里计算概率」，不把频率直接叫成概率而不加说明。", mastery=MASTERY_GATE),
    node(N(26), "概率与统计通关", 5, [N(25)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(27), "方便样本偏差", 3, [N(2)], ["stat", "ch-stat"], "能指出只调查「身边的人」为什么不能代表总体。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "回归不是因果", 3, [N(13)], ["stat", "ch-reg"], "能举「一起升降但不一定谁导致谁」的例子。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(29), "直方图组距", 2, [N(5)], ["stat", "ch-stat"], "能说明组距过大过小都会让形状难读。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(30), "普查不是抽样", 2, [N(10)], ["stat", "ch-stat"], "能区分普查与抽样：总体不大时可以全查，否则才抽样。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(31), "互斥不是对立", 3, [N(20)], ["prob", "ch-prob"], "能举两个互斥但不是对立的事件（并起来还不是全集）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(32), "等可能要检查", 3, [N(21)], ["prob", "ch-prob"], "能指出「硬币弯曲」「骰子不匀」时不能直接用古典概型。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(3), "type": "related", "note": "分层是在简单随机之前先分组，不是另一种「随便抽」。"},
    {"from": N(6), "to": N(7), "type": "easily_confused", "note": "平均数会被极端值拉走，中位数更稳。"},
    {"from": N(19), "to": N(20), "type": "easily_confused", "note": "对立一定互斥；互斥不一定对立。"},
    {"from": N(21), "to": N(24), "type": "easily_confused", "note": "古典概型是模型里的比；频率是做出来的比。"},
    {"from": N(13), "to": N(28), "type": "application", "note": "会画回归直线之后，更要防止因果话说过头。"},
    {"from": N(2), "to": N(27), "type": "related", "note": "对照真正的随机，才看见方便样本的偏。"},
    {"from": N(5), "to": N(29), "type": "application", "note": "会画直方图之后，再谈组距。"},
]


QUESTS = [
    q(N(1), "explain", "先把问题写清", "写一个校园统计问题：想了解什么、向谁、量什么。", "问题含糊，后面全废。"),
    q(N(2), "practice", "设计简单随机", "为 40 人的名单设计抽 8 人的办法，说明每人机会相同。", "抽签或随机数。", items=1),
    q(N(3), "practice", "按层分配", "两层人数 30 与 70，样本 20，按比例分配并说明为什么分层。", "层内抽简单随机。", items=1),
    q(N(4), "explain", "等距的风险", "说明名单若按「男女男女…」排，隔一个抽可能怎样偏。", "周期和间距重合就会偏。"),
    q(N(5), "practice", "画一张直方图", "给 20 个数分组、求频率、画直方图。", "组距一致，纵轴是频率或频数要标明。", items=1),
    q(N(6), "practice", "平均数与加权", "6 道求平均数，其中 2 道加权。", "权是份量。", items=6),
    q(N(7), "practice", "求中位数", "6 组求中位数，含偶数个数据。", "先排序。", items=6),
    q(N(8), "explain", "四分位在说什么", "解释 Q1、Q3 把中间一半数据框起来。", "不是「百分之二十五分」。"),
    q(N(9), "practice", "方差直觉", "比较 3 组平均数相近但分散不同的数据，指出谁方差更大，并算其中一组。", "离平均数越散越大。", items=3),
    q(N(10), "practice", "用样本说话", "给一个样本，写出对总体平均数或比例的估计，并加一句局限。", "估计要带局限。", items=1),
    q(N(10), "mini_quiz", "抽样与数字特征小测", "抽样方法、平均数中位数、方差、估计。夹一道方便样本。", "先问样本怎么来的。", items=8),
    q(N(10), "boss", "关主：抽样估计员", "击败关主：①选一种抽样并说明理由 ②计算一个数字特征 ③用样本估计总体并说局限。", "没有抽样设计就没有估计。", xp=80, items=10, qid=f"{P}-boss-stat"),
    q(N(11), "practice", "画散点图", "把 8 对数据画成散点。", "每个点是一对观测。", items=1),
    q(N(12), "practice", "判断相关方向", "6 张散点（可手绘示意）判断正、负或看不出。", "整体趋势，不要盯一个点。", items=6),
    q(N(13), "explain", "偏差往哪量", "说明为什么看竖直方向的偏差来配直线。", "我们常用 x 去说 y。"),
    q(N(14), "practice", "写案例提纲", "用四段写一份不超过十句的案例提纲。", "结论必须对应问题。", items=1),
    q(N(15), "practice", "列样本空间", "为 4 个试验列出样本空间（掷币、骰子、抽球简化）。", "不重不漏。", items=4),
    q(N(16), "practice", "事件是子集", "在一个样本空间里用列举法表示 6 个事件。", "事件是一些结果组成的集合。", items=6),
    q(N(17), "practice", "包含还是相等", "6 组事件判断包含、相等或都不是。", "每个结果都检查。", items=6),
    q(N(18), "practice", "写并与交", "4 个情境写出并、交的含义与列举。", "并是或，交是且。", items=4),
    q(N(19), "practice", "判断互斥", "6 组事件是否互斥。", "能不能同时发生。", items=6),
    q(N(20), "practice", "写对立", "为 4 个事件写出对立，并检查并是否为全集。", "对立要把剩下的结果全收走。", items=4),
    q(N(21), "practice", "古典概型计算", "8 道等可能计数求概率。", "先确认等可能，再数个数。", items=8),
    q(N(22), "practice", "互斥相加", "6 道用互斥加法，夹 1 道指出不能加。", "有重叠不能直接加。", items=6),
    q(N(23), "practice", "性质判断", "8 个说法判断是否符合概率性质。", "概率不能大于 1。", items=8),
    q(N(24), "explain", "频率会晃", "说明为什么做 20 次和做 2000 次，频率表现不同。", "次数少，晃动大。"),
    q(N(24), "mini_quiz", "古典概型小测", "样本空间、互斥对立、古典概型、频率。夹一道不等可能。", "等可能是前提。", items=8),
    q(N(24), "boss", "关主：古典概型绘图员", "击败关主：①列出样本空间 ②判断互斥或对立 ③求一个古典概率。", "先模型后数字。", xp=80, items=10, qid=f"{P}-boss-prob"),
    q(N(25), "practice", "合练卷", "抽样估计与古典概型各几题，并有一道「这句话说过头了」。", "统计说估计，概率说模型。", items=12),
    q(N(26), "practice", "通关综合练", "独立完成：一种抽样+一个数字特征，以及一个古典概型。", "两套语言不要混。", items=10),
    q(N(26), "boss", "关主：概率与统计通关试炼", "最终关主：①抽样与估计 ②古典概型 ③指出一句不严谨的统计或概率表述。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(27), "explain", "只问身边的人", "写三句：总体是谁、方便样本是谁、会偏向哪。", "偏的方向要说得具体。"),
    q(N(28), "explain", "一起变不是导致", "举一个共同升降的例子，说明不能直接说因果。", "可能有第三因素。"),
    q(N(29), "explain", "组距太大太小", "同一组数据设想两种组距，说明图形会怎样难看。", "太大只剩一两根柱，太碎看不出趋势。"),
    q(N(30), "explain", "什么时候全查", "举一个该普查和一个该抽样的情境。", "总体很小或必须精确时普查。"),
    q(N(31), "explain", "互斥但不是对立", "在掷骰子里举两个互斥事件，说明它们并起来不是全部结果。", "对立必须「补满」。"),
    q(N(32), "explain", "能不能用古典", "举一个表面像骰子其实不等可能的试验。", "模型要符合实际。"),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 概率与统计（必修）",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "概率与统计（必修）",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "抽样与数字特征（关主 1）；散点回归可并行；古典概型（关主 2）后收束。方便样本（n027）、回归非因果（n028）、组距（n029）、普查（n030）、互斥非对立（n031）、等可能检查（n032）为软锁。计数原理与随机变量不在本图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-stat", f"{P}-boss-prob", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：抽样估计员、古典概型绘图员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中必修「概率与统计」地图：抽样与数字特征 → 相关与回归直觉 → 随机事件与古典概型。独立通关。grade=10。",
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
