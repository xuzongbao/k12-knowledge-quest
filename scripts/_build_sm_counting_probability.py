"""Build senior-math 计数原理与随机变量 map (选必).

Run: python3 scripts/_build_sm_counting_probability.py

Pedagogical spine: 分类分步 → 排列组合 → 二项式定理入门 → 离散型随机变量与分布列 → 条件概率与独立。
组合恒等式、放回不放回、独立与互斥、期望不是众数为软锁。grade=11。
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

OUT = ROOT / "maps" / "senior-math" / "counting-probability"
G = 11
STRAND = "统计与概率"
P = "sm-count"
MAP_ID = "sm-counting-probability"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "分类加法计数", 1, [], ["count", "ch-count"], "能说明完成一件事有几类办法、各类互不重叠时，总数是各类相加。本图从计数讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "分步乘法计数", 2, [N(1)], ["count", "ch-count"], "能说明分几步完成、每步有若干选择时，总数是各步相乘。", mastery=MASTERY_CONCEPT),
    node(N(3), "加还是乘", 3, [N(2)], ["count", "ch-count"], "能判断情境是分类还是分步，避免把「或」乘成「且」。", mastery=MASTERY_GATE),
    node(N(4), "排列的意义", 2, [N(2)], ["count", "ch-arr"], "能说明从 n 个不同元素中取出 m 个按顺序排，顺序不同算不同。", mastery=MASTERY_CONCEPT),
    node(N(5), "排列数公式", 3, [N(4)], ["count", "ch-arr"], "能使用 A_n^m=n(n-1)…(n-m+1) 计算，并知道 A_n^n=n!。", mastery=MASTERY_GATE),
    node(N(6), "组合的意义", 2, [N(4)], ["count", "ch-arr"], "能说明组合只问取出哪些、不问顺序。", mastery=MASTERY_CONCEPT),
    node(N(7), "组合数公式", 3, [N(6), N(5)], ["count", "ch-arr"], "能使用 C_n^m=A_n^m/m! 计算，并理解除以 m! 是因为顺序被消去。", mastery=MASTERY_GATE),
    node(N(8), "排列还是组合", 4, [N(7), N(3)], ["count", "ch-arr"], "能根据「要不要排队」选择排列或组合，并处理简单混合。", mastery=MASTERY_GATE),
    node(N(9), "二项式定理入门", 3, [N(7)], ["count", "ch-bin"], "能把 (a+b)^n 展开写成各项 C_n^k a^{n-k} b^k。", mastery=MASTERY_CONCEPT),
    node(N(10), "二项式系数性质", 3, [N(9)], ["count", "ch-bin"], "能使用对称性 C_n^k=C_n^{n-k} 以及相邻系数关系的直觉。"),
    node(N(11), "计数与二项合练", 4, [N(8), N(10)], ["count", "ch-count", "boss-gate"], "能完成分类分步、排列组合与二项展开的综合练习。", mastery=MASTERY_GATE),
    node(N(12), "离散型随机变量", 2, [N(11)], ["rv", "ch-rv"], "能把随机试验的数值结果看成随机变量，列出它可能取的值。", mastery=MASTERY_CONCEPT),
    node(N(13), "分布列", 3, [N(12)], ["rv", "ch-rv"], "能列出每个取值的概率，检查非负且和为 1。", mastery=MASTERY_GATE),
    node(N(14), "两点分布", 2, [N(13)], ["rv", "ch-rv"], "能识别只取 0 和 1 的随机变量，写出 P(X=1)=p。", mastery=MASTERY_CONCEPT),
    node(N(15), "二项分布", 4, [N(14), N(9)], ["rv", "ch-rv"], "能说明 n 次独立重复、每次成功概率 p 时，成功次数服从二项分布。", mastery=MASTERY_GATE),
    node(N(16), "超几何分布入门", 3, [N(13), N(7)], ["rv", "ch-rv"], "能说明不放回抽取中「抽到指定类的个数」用组合比来写概率。"),
    node(N(17), "期望", 4, [N(13)], ["rv", "ch-rv"], "能用 Σ x_i p_i 求期望，并说明它是加权平均，不一定是某个取值。", mastery=MASTERY_GATE),
    node(N(18), "方差", 3, [N(17)], ["rv", "ch-rv"], "能理解方差衡量取值相对期望的分散程度，会算简单分布列的方差。"),
    node(N(19), "条件概率", 3, [N(13)], ["rv", "ch-cond"], "能用 P(A|B)=P(A∩B)/P(B) 计算「已知 B 发生后 A 的概率」。", mastery=MASTERY_CONCEPT),
    node(N(20), "全概率入门", 4, [N(19)], ["rv", "ch-cond"], "能把样本空间分成几块，用各块上的条件概率拼出事件的概率。", mastery=MASTERY_GATE),
    node(N(21), "独立事件", 3, [N(19)], ["rv", "ch-cond"], "能说明独立是「一个发生不改变另一个的概率」，此时 P(A∩B)=P(A)P(B)。", mastery=MASTERY_CONCEPT),
    node(N(22), "随机变量合练", 4, [N(15), N(18), N(21), N(16)], ["rv", "ch-rv", "boss-gate"], "能在分布列、二项、期望、条件概率之间切换。", mastery=MASTERY_GATE),
    node(N(23), "计数与随机变量通关", 5, [N(22), N(20)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(24), "放回与不放回", 3, [N(16), N(15)], ["rv", "ch-rv"], "能对照放回（二项）与不放回（超几何）何时近似、何时必须分开。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(25), "独立不是互斥", 3, [N(21)], ["rv", "ch-cond"], "能说明互斥时一个发生另一个必不发生，这通常不是独立。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(26), "期望不是最可能的值", 3, [N(17)], ["rv", "ch-rv"], "能举期望不是任何一个取值的例子（如两点分布 p≠0.5）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "组合恒等式直觉", 3, [N(10)], ["count", "ch-bin"], "能用「选 k 个等于留下 n-k 个」解释对称性。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "正态曲线直觉", 2, [N(18)], ["rv", "ch-rv"], "能说明大量独立随机因素叠加时，直方图常常中间高两边低（不作计算要求）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(29), "排列组合混合陷阱", 3, [N(8)], ["count", "ch-arr"], "能改一道「有的位置要排队、有的只要选人」的错解。", unlock=SOFT),
]


EXTRA_EDGES = [
    {"from": N(1), "to": N(2), "type": "easily_confused", "note": "分类用加，分步用乘；「或」与「且」说反最常见。"},
    {"from": N(4), "to": N(6), "type": "easily_confused", "note": "排列管顺序，组合不管顺序。"},
    {"from": N(15), "to": N(16), "type": "easily_confused", "note": "二项每次独立（可放回或恢复）；超几何不放回。"},
    {"from": N(19), "to": N(21), "type": "related", "note": "独立是条件概率等于原来的概率。"},
    {"from": N(21), "to": N(25), "type": "application", "note": "会独立之后，专门和互斥对照。"},
    {"from": N(17), "to": N(26), "type": "related", "note": "期望是加权中心，不是众数。"},
    {"from": N(9), "to": N(15), "type": "application", "note": "二项概率里的组合数来自二项式系数。"},
]


QUESTS = [
    q(N(1), "explain", "什么时候该加", "用自己的话说明：完成一件事有几类互不重叠的办法时，为什么把各类办法数加起来。", "分类是「或」，用加法。"),
    q(N(1), "practice", "分类相加", "4 个「两类办法」情境求总数，检查有没有重叠。", "重叠了要减去或重新分类。", items=4),
    q(N(2), "practice", "分步相乘", "4 个「先…再…」情境求总数。", "每一步的选择数相乘。", items=4),
    q(N(3), "practice", "判断加或乘", "8 个短句只要求判断用加还是乘，再选 4 个算出数。", "看到「或」先想加。", items=8),
    q(N(4), "explain", "顺序算不算", "举一个排队和一个只选人不排队的例子。", "站位不同就是不同排列。"),
    q(N(5), "practice", "算排列数", "8 道 A_n^m，含阶乘。", "从 n 往下乘 m 个。", items=8),
    q(N(6), "explain", "为什么除顺序", "说明同一组人的不同排法在组合里只算一次。", "组合是一堆，不是一列。"),
    q(N(7), "practice", "算组合数", "8 道 C_n^m。", "先排后除以顺序数。", items=8),
    q(N(8), "practice", "先判断再计算", "6 题先写排列或组合，再计算。", "问顺序就排。", items=6),
    q(N(9), "practice", "二项展开", "展开 3 个 (a+b)^n（n 较小），写出通项。", "指数和为 n。", items=3),
    q(N(10), "practice", "用对称性", "6 道用 C_n^k=C_n^{n-k} 简化计算。", "靠近两端的更好算。", items=6),
    q(N(11), "practice", "计数综合", "6 道混合，含简单二项系数。", "先画步骤再写公式。", items=6),
    q(N(11), "mini_quiz", "计数小测", "分类分步、排列组合、二项系数。夹一道把组合当排列。", "先问要不要顺序。", items=10),
    q(N(11), "boss", "关主：计数原理调度员", "击败关主：①判断加或乘 ②一道排列或组合 ③写出一个二项展开项。", "分类与顺序两处最容易混。", xp=80, items=12, qid=f"{P}-boss-count"),
    q(N(12), "explain", "结果变成数", "把「掷两枚骰子的点数和」说成随机变量，列出可能取值。", "随机变量是函数，值是数。"),
    q(N(13), "practice", "写分布列", "3 个简单试验写出分布列并检查和为 1。", "每个概率 ≥0，总和 1。", items=3),
    q(N(14), "practice", "两点分布", "4 道识别或写出 0-1 分布。", "成功记 1，失败记 0。", items=4),
    q(N(15), "practice", "二项概率", "4 道求恰好 k 次成功的概率。", "C_n^k p^k (1-p)^{n-k}。", items=4),
    q(N(16), "practice", "不放回计数", "3 道用组合写超几何概率。", "分子分母都是组合。", items=3),
    q(N(17), "practice", "求期望", "4 个分布列求期望。", "取值乘概率再相加。", items=4),
    q(N(18), "practice", "求方差", "3 个分布列求方差。", "先期望，再偏差平方的期望。", items=3),
    q(N(19), "practice", "条件概率", "4 道用定义计算 P(A|B)。", "分母是 B 的概率，不能为 0。", items=4),
    q(N(20), "practice", "分块相加", "2 道全概率：画出两三个互斥条件再拼。", "条件要铺满样本空间。", items=2),
    q(N(21), "practice", "判断独立", "4 组事件判断是否独立，并验证乘法公式。", "独立才能把交拆成乘积。", items=4),
    q(N(22), "practice", "随机变量综合", "分布列、二项、期望、条件概率各一题。", "先写取值再写概率。", items=4),
    q(N(22), "mini_quiz", "随机变量小测", "分布列、期望、二项或条件概率。夹一道期望不是取值。", "先检查分布列是否合法。", items=8),
    q(N(22), "boss", "关主：随机变量分析官", "击败关主：①写一个分布列 ②求期望 ③一道二项或条件概率。", "概率和必须为 1。", xp=80, items=10, qid=f"{P}-boss-rv"),
    q(N(23), "practice", "通关综合练", "独立完成：一道排列组合、一个分布列与期望、一道条件概率。", "计数为概率服务。", items=10),
    q(N(23), "boss", "关主：计数与随机变量通关试炼", "最终关主：①计数 ②分布列或二项 ③条件概率或独立。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(24), "explain", "放回还是不放回", "同一个罐子，对照两次抽取的模型选择。", "总体很大时两者接近。"),
    q(N(25), "explain", "互斥很依赖", "说明互斥时 P(A|B)=0，通常不等于 P(A)。", "互斥是强烈依赖。"),
    q(N(26), "explain", "期望可以「不在名单上」", "举一个期望为 1.5 但取值只有 1 和 2 的例子。", "期望是中心，不是必须取到的值。"),
    q(N(27), "explain", "选 k 等于留 n-k", "用选代表的故事解释组合数对称。", "选中的和留下的是同一件事的两面。"),
    q(N(28), "explain", "中间高两边低", "说明为什么很多测量误差看起来像钟形。", "只要求形状直觉，不要求积分。"),
    q(N(29), "practice", "改一道混合题", "改 2 道把「先选后排」顺序做反的解。", "先选人再排队，或反过来要想清。", items=2),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 计数原理与随机变量",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "计数原理与随机变量",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "分类分步与排列组合（关主 1）→ 分布列、二项与期望（关主 2）→ 条件概率后收束。放回对照（n024）、独立非互斥（n025）、期望非众数（n026）、组合对称（n027）、正态直觉（n028）、混合陷阱（n029）为软锁。grade=11。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-count", f"{P}-boss-rv", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：计数原理调度员、随机变量分析官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中选必「计数原理、随机变量」地图。独立通关。grade=11。",
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
