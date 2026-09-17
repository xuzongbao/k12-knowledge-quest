"""Build Grade 9 Algebra map JSON (九年级 · 数与代数).

Run: python3 scripts/_build_jm_g9_algebra.py

Pedagogical spine: 二次根式（含实数入门）→ 一元二次方程 → 二次函数。
锐角三角比放在九年级图形图。韦达与图象对照为软锁。本图自洽。
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

OUT = ROOT / "maps" / "junior-math" / "grade-9-algebra"
G = 9
STRAND = "数与代数"
P = "jm-g9-alg"
MAP_ID = "jm-g9-algebra"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "算术平方根", 1, [], ["radical", "ch-radical"], "能说明非负数 a 的算术平方根是平方等于 a 的那个非负数，记作 √a。", mastery=MASTERY_CONCEPT),
    node(N(2), "平方根", 2, [N(1)], ["radical", "ch-radical"], "能说明正数有两个平方根，互为相反数；0 的平方根是 0。", mastery=MASTERY_CONCEPT),
    node(N(3), "立方根", 2, [N(2)], ["radical", "ch-radical"], "能求简单数的立方根，说明负数也有立方根。"),
    node(N(4), "无理数与实数", 3, [N(3)], ["radical", "ch-radical"], "能举例说明无限不循环小数是无理数，有理数与无理数合称实数。", mastery=MASTERY_CONCEPT),
    node(N(5), "二次根式", 2, [N(4)], ["radical", "ch-radical"], "能识别二次根式，并指出被开方数必须非负。", mastery=MASTERY_CONCEPT),
    node(N(6), "最简二次根式", 3, [N(5)], ["radical", "ch-radical"], "能把被开方数中能开得尽的因数开出来，写成最简二次根式。"),
    node(N(7), "二次根式的乘除", 3, [N(6)], ["radical", "ch-radical"], "能用 √a·√b=√(ab)、√a/√b=√(a/b)（a≥0,b>0）计算。"),
    node(N(8), "二次根式的加减", 4, [N(7)], ["radical", "ch-radical"], "能合并同类二次根式，说明被开方数不同不能直接加减。", mastery=MASTERY_GATE),
    node(N(9), "二次根式综合", 4, [N(8)], ["radical", "ch-radical", "boss-gate"], "能化简、乘除、加减二次根式，并指出使式子有意义的取值。", mastery=MASTERY_GATE),
    node(N(10), "一元二次方程的意义", 2, [N(9)], ["quad", "ch-quad"], "能识别只含一个未知数且未知数最高次数是 2 的方程，一般形式 ax²+bx+c=0（a≠0）。", mastery=MASTERY_CONCEPT),
    node(N(11), "直接开平方法", 3, [N(10)], ["quad", "ch-quad"], "能把方程化成 (x+p)²=q 的形状后开平方求解（q≥0）。"),
    node(N(12), "配方法", 4, [N(11)], ["quad", "ch-quad"], "能给二次项系数为 1 的方程配方，得到完全平方式。", mastery=MASTERY_GATE),
    node(N(13), "求根公式", 4, [N(12)], ["quad", "ch-quad"], "能用公式 x=(-b±√(b²-4ac))/(2a) 求根，并先算判别式。", mastery=MASTERY_GATE),
    node(N(14), "因式分解法解方程", 3, [N(10)], ["quad", "ch-quad"], "能把方程左边因式分解成两个一次因式相乘等于 0 来求解。"),
    node(N(15), "根的判别式", 3, [N(13)], ["quad", "ch-quad"], "能用 Δ=b²-4ac 判断根的个数：大于 0 两个不等实根，等于 0 两个相等实根，小于 0 无实根。", mastery=MASTERY_CONCEPT),
    node(N(16), "选择解法", 4, [N(14), N(15)], ["quad", "ch-quad"], "能根据方程特点选择开平方、分解、公式等方法。"),
    node(N(17), "列方程简单应用", 4, [N(16)], ["quad", "ch-quad", "word"], "能在面积、数字关系等情境中列出一元二次方程并取符合题意的根。"),
    node(N(18), "一元二次方程综合", 4, [N(17)], ["quad", "ch-quad", "boss-gate"], "能求解并说明为什么舍去某个根，或说明无实根。", mastery=MASTERY_GATE),
    node(N(19), "二次函数的意义", 2, [N(18)], ["fn", "ch-fn"], "能识别 y=ax²+bx+c（a≠0），说明它描述的是二次关系。", mastery=MASTERY_CONCEPT),
    node(N(20), "y=ax² 的图象", 3, [N(19)], ["fn", "ch-fn"], "能说明图象是抛物线，a>0 开口向上，a<0 开口向下，|a| 越大开口越窄。", mastery=MASTERY_CONCEPT),
    node(N(21), "平移得到的抛物线", 3, [N(20)], ["fn", "ch-fn"], "能说明 y=a(x-h)²+k 是由 y=ax² 平移得到，顶点是 (h,k)。"),
    node(N(22), "顶点式与一般式", 4, [N(21)], ["fn", "ch-fn"], "能在顶点式与一般式之间转换（配方或展开）。", mastery=MASTERY_GATE),
    node(N(23), "对称轴与最值", 3, [N(22)], ["fn", "ch-fn"], "能求对称轴 x=-b/(2a) 和顶点，从而求最大值或最小值。"),
    node(N(24), "二次函数与方程", 4, [N(23), N(15)], ["fn", "ch-fn"], "能说明抛物线与 x 轴交点的横坐标就是对应方程的根，交点个数由判别式决定。", mastery=MASTERY_GATE),
    node(N(25), "二次函数简单应用", 4, [N(24)], ["fn", "ch-fn", "word"], "能在面积、利润或抛体示意中读出顶点或交点的含义。"),
    node(N(26), "二次函数综合", 4, [N(25)], ["fn", "ch-end"], "能画出草图：开口、顶点、与坐标轴交点。", mastery=MASTERY_GATE),
    node(N(27), "九年级代数合练", 4, [N(26)], ["mixed", "ch-end"], "能化简根式、解一元二次方程、读二次函数图象。", mastery=MASTERY_GATE),
    node(N(28), "九年级代数通关", 5, [N(27)], ["mixed", "ch-end", "boss-gate"], "能独立完成九年级数与代数线的收束检查。", mastery=MASTERY_GATE),
    node(N(29), "根与系数的关系入门", 4, [N(18)], ["quad", "ch-quad"], "能对两根之和、两根之积写出与系数的关系（韦达公式入门），并用来检验。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(30), "判别式与开口对照", 3, [N(24)], ["fn", "ch-fn"], "能对照：Δ>0 穿轴两点，Δ=0 顶点在 x 轴上，Δ<0 与 x 轴不相交。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(31), "二次根式有意义的条件", 3, [N(5)], ["radical", "ch-radical"], "能列出使含字母的二次根式有意义的不等式，并在数轴上表示。", unlock=SOFT),
    node(N(32), "配方法与顶点", 3, [N(22)], ["fn", "ch-fn"], "能说明解方程时的配方，和求二次函数顶点时的配方，是同一件事的两种用法。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(1), "to": N(2), "type": "easily_confused", "note": "算术平方根只取非负的那一个；平方根有两个。"},
    {"from": N(7), "to": N(8), "type": "easily_confused", "note": "乘除可以对被开方数运算；加减必须先化成同类根式。"},
    {"from": N(12), "to": N(13), "type": "related", "note": "求根公式可以由配方法推出来。"},
    {"from": N(14), "to": N(16), "type": "related", "note": "能分解时往往比套公式更快。"},
    {"from": N(15), "to": N(24), "type": "application", "note": "判别式决定抛物线与 x 轴有几个交点。"},
    {"from": N(18), "to": N(29), "type": "related", "note": "先会求根，再用两根之和与积做检验。"},
    {"from": N(12), "to": N(32), "type": "related", "note": "配方既解方程也找顶点。"},
]


QUESTS = [
    q(N(1), "explain", "非负的那一个", "说明 √9=3 而不是 ±3，±3 是平方根。", "算术平方根带根号时表示非负数。"),
    q(N(2), "practice", "求平方根", "求 8 个数的平方根，含 0 和正数。", "正数两个，0 一个，负数没有实数平方根。", items=8),
    q(N(3), "practice", "求立方根", "求 6 个数的立方根，含负数。", "负数的立方根是负的。", items=6),
    q(N(4), "explain", "无理数举例", "举两个无理数，说明它们不能写成两整数之比，并说出实数包括哪些。", "无限不循环是直观特征。"),
    q(N(5), "practice", "识别二次根式", "判断哪些是二次根式，并指出被开方数的要求。", "被开方数≥0。", items=8),
    q(N(6), "practice", "化成最简", "把 8 个二次根式化成最简。", "开得尽的因数要开出来。", items=8),
    q(N(7), "practice", "根式乘除", "8 道乘除，结果最简。", "先乘除被开方数，再化简。", items=8),
    q(N(8), "practice", "根式加减", "6 道，先化最简再合并同类项。", "被开方数相同才能合并。", items=6),
    q(N(9), "practice", "根式闯关", "化简、乘除、加减混合，并写有意义条件。", "先有意义，再运算。", items=8),
    q(N(9), "mini_quiz", "二次根式小测", "算术平方根与平方根、化简、加减陷阱。", "加减最容易乱合并。", items=10),
    q(N(9), "boss", "关主：二次根式化简官", "击败关主：①区分算术平方根与平方根 ②化简并运算 ③指出有意义的条件。", "被开方数非负是底线。", xp=80, items=12, qid=f"{P}-boss-radical"),
    q(N(10), "practice", "识别一元二次方程", "从一列方程里挑出一元二次方程，并写成一般形式。", "二次项系数不能为 0。", items=6),
    q(N(11), "practice", "开平方求解", "6 道 (x+p)²=q。", "q<0 无实根；记得 ±。", items=6),
    q(N(12), "practice", "配方", "把 5 道方程配成完全平方。", "一次项系数一半再平方。", items=5),
    q(N(13), "practice", "用公式求根", "6 道用公式，先写 Δ。", "Δ<0 不要硬开平方。", items=6),
    q(N(14), "practice", "分解求解", "6 道左边能分解的方程。", "积为 0 则因子之一为 0。", items=6),
    q(N(15), "practice", "只判断根的个数", "8 道只求 Δ 并判断个数，不必求出根。", "先算 Δ。", items=8),
    q(N(16), "practice", "选方法再解", "6 道先写方法再解。", "能分解就分解，一般用公式。", items=6),
    q(N(17), "practice", "列方程取根", "3 个情境，注意边长为正等限制。", "求出的根要回头看题意。", items=3),
    q(N(18), "practice", "方程闯关", "求解并说明舍根或无实根。", "检验和题意两道关。", items=6),
    q(N(18), "mini_quiz", "一元二次方程小测", "识别、Δ、公式、分解、应用。", "先看 a 是否为 0。", items=10),
    q(N(18), "boss", "关主：一元二次方程考官", "击败关主：①判断根的个数 ②用一种方法求根 ③在应用中取符合题意的根。", "Δ 先说话。", xp=80, items=12, qid=f"{P}-boss-quadratic"),
    q(N(19), "explain", "二次关系", "举一个 y 随 x 二次变化的例子，对照一次函数。", "最高次是 2。"),
    q(N(20), "practice", "开口方向与宽窄", "根据 a 判断开口和宽窄，共 6 题。", "a 的符号管方向，绝对值管宽窄。", items=6),
    q(N(21), "practice", "说出顶点", "根据顶点式写出顶点坐标，共 6 题。", "注意 (x-h) 里 h 的符号。", items=6),
    q(N(22), "practice", "两种形式转换", "一般式配方成顶点式，或顶点式展开，共 4 题。", "配方找顶点。", items=4),
    q(N(23), "practice", "求最值", "求对称轴和最大值或最小值，共 6 题。", "开口向上有最低点。", items=6),
    q(N(24), "practice", "交点与根", "根据图象或 Δ 判断交点个数，并求交点横坐标。", "交点横坐标就是根。", items=4),
    q(N(25), "practice", "读顶点含义", "在面积或利润示意中解释顶点。", "顶点常常是最大或最小。", items=3),
    q(N(26), "practice", "画抛物线草图", "标开口、顶点、与轴交点，画 3 个草图。", "先顶点后开口，再找交点。", items=3),
    q(N(27), "practice", "合练卷", "根式、方程、二次函数各几题。", "先辨题型。", items=12),
    q(N(28), "practice", "通关综合练", "化简根式、解方程、读抛物线。", "有意义条件、Δ、顶点，三件抓手。", items=12),
    q(N(28), "boss", "关主：九年级代数通关试炼", "最终关主：①二次根式化简 ②解一元二次方程 ③读二次函数顶点或交点。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(29), "practice", "两根之和与积", "已知方程写出两根之和、积，或用来检验所求的根。", "和是 -b/a，积是 c/a。", items=4),
    q(N(30), "explain", "三种穿轴情形", "对照 Δ 与抛物线和 x 轴的位置关系。", "不相交不是图坏了，是没有实根。"),
    q(N(31), "practice", "有意义条件", "列出 4 个含字母根式有意义的不等式。", "被开方数≥0。", items=4),
    q(N(32), "explain", "同一种配方", "对照解方程的配方和求顶点的配方，指出相同步骤。", "都是凑成完全平方。"),
]


META = {
    "id": MAP_ID,
    "title": "九年级 · 数与代数",
    "subject": "数学",
    "stage": "初中",
    "grade": 9,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "二次根式（关主 1）→ 一元二次方程（关主 2）→ 二次函数。韦达入门（n029）、Δ 与开口对照（n030）、有意义条件（n031）、配方对照（n032）为软锁。锐角三角比见九年级图形图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-radical", f"{P}-boss-quadratic", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：二次根式化简官、一元二次方程考官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中九年级「数与代数」地图：二次根式、一元二次方程、二次函数。独立通关。",
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
