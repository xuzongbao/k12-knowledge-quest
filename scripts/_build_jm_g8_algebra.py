"""Build Grade 8 Algebra map JSON (八年级 · 数与代数).

Run: python3 scripts/_build_jm_g8_algebra.py

Pedagogical spine: 二元一次方程组 → 整式乘除与因式分解 → 分式 → 一次函数。
反比例函数对照为软锁。本图自洽。
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

OUT = ROOT / "maps" / "junior-math" / "grade-8-algebra"
G = 8
STRAND = "数与代数"
P = "jm-g8-alg"
MAP_ID = "jm-g8-algebra"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "二元一次方程", 1, [], ["sys", "ch-sys"], "能识别含两个未知数且每个未知数次数都是 1 的方程，并说明一组解是一对有序数。", mastery=MASTERY_CONCEPT),
    node(N(2), "方程组的解", 2, [N(1)], ["sys", "ch-sys"], "能说明二元一次方程组的解是同时满足两个方程的未知数取值。", mastery=MASTERY_CONCEPT),
    node(N(3), "代入消元", 3, [N(2)], ["sys", "ch-sys"], "能从一个方程解出用另一个未知数表示的式子，代入另一方程消元。", mastery=MASTERY_GATE),
    node(N(4), "加减消元", 3, [N(2)], ["sys", "ch-sys"], "能把两个方程适当变形后相加或相减，消去一个未知数。", mastery=MASTERY_GATE),
    node(N(5), "选择消元方法", 3, [N(3), N(4)], ["sys", "ch-sys"], "能根据系数特点选择代入或加减，使计算更简单。"),
    node(N(6), "方程组简单应用", 4, [N(5)], ["sys", "ch-sys", "word"], "能设两个未知数，根据两个等量关系列出方程组并求解、写答。"),
    node(N(7), "方程组综合", 4, [N(6)], ["sys", "ch-sys", "boss-gate"], "能解较整洁的二元一次方程组，并检查是否同时满足两个方程。", mastery=MASTERY_GATE),
    node(N(8), "同底数幂相乘", 2, [N(7)], ["poly", "ch-factor"], "能用 a^m · a^n = a^(m+n) 计算，底数相同才可直接加指数。", mastery=MASTERY_CONCEPT),
    node(N(9), "幂的乘方与积的乘方", 3, [N(8)], ["poly", "ch-factor"], "能用 (a^m)^n = a^(mn) 和 (ab)^n = a^n b^n 化简。"),
    node(N(10), "同底数幂相除", 3, [N(9)], ["poly", "ch-factor"], "能用 a^m / a^n = a^(m-n)（a≠0）计算，并理解负整数指数与倒数的关系入门。"),
    node(N(11), "整式乘法", 3, [N(10)], ["poly", "ch-factor"], "能计算单项式乘多项式、多项式乘多项式（分配律展开）。", mastery=MASTERY_GATE),
    node(N(12), "平方差公式", 3, [N(11)], ["poly", "ch-factor"], "能识别并使用 (a+b)(a-b)=a²-b²。", mastery=MASTERY_CONCEPT),
    node(N(13), "完全平方公式", 3, [N(11)], ["poly", "ch-factor"], "能识别并使用 (a±b)²=a²±2ab+b²，注意中间项。", mastery=MASTERY_CONCEPT),
    node(N(14), "因式分解的意义", 2, [N(12), N(13)], ["poly", "ch-factor"], "能说明因式分解是把一个多项式写成几个整式相乘，与整式乘法方向相反。", mastery=MASTERY_CONCEPT),
    node(N(15), "提公因式", 3, [N(14)], ["poly", "ch-factor"], "能提出各项的公因式，包括数字系数与字母。"),
    node(N(16), "公式法因式分解", 4, [N(15)], ["poly", "ch-factor"], "能用平方差、完全平方把多项式因式分解，必要时先提公因式。", mastery=MASTERY_GATE),
    node(N(17), "整式乘除综合", 4, [N(16)], ["poly", "ch-factor", "boss-gate"], "能在展开与因式分解之间切换，说明何时该乘开、何时该分解。", mastery=MASTERY_GATE),
    node(N(18), "分式的意义", 2, [N(17)], ["frac", "ch-frac"], "能说明分式是整式相除、分母含字母，并指出分母不能为 0。", mastery=MASTERY_CONCEPT),
    node(N(19), "分式的基本性质", 3, [N(18)], ["frac", "ch-frac"], "能把分子分母同乘或同除以同一个不为 0 的整式，分式值不变。", mastery=MASTERY_CONCEPT),
    node(N(20), "约分与通分", 3, [N(19)], ["frac", "ch-frac"], "能约去分子分母的公因式，也能通分后准备加减。"),
    node(N(21), "分式乘除", 3, [N(20)], ["frac", "ch-frac"], "能把分式乘法写成分子分母分别相乘，除法转化为乘倒数。"),
    node(N(22), "分式加减", 4, [N(21)], ["frac", "ch-frac"], "能先通分再加减，结果要约成最简。", mastery=MASTERY_GATE),
    node(N(23), "分式方程入门", 4, [N(22)], ["frac", "ch-frac"], "能去分母把分式方程化为整式方程，并检验是否使分母为 0。", mastery=MASTERY_GATE),
    node(N(24), "变量与函数", 2, [N(7)], ["fn", "ch-fn"], "能说明在一个变化过程中，一个量随另一个量变化，可以用函数来描述。", mastery=MASTERY_CONCEPT),
    node(N(25), "函数的表示", 2, [N(24)], ["fn", "ch-fn"], "能用解析式、表格、图象三种方式表示简单函数关系。", mastery=MASTERY_CONCEPT),
    node(N(26), "正比例函数", 3, [N(25)], ["fn", "ch-fn"], "能识别 y=kx（k≠0），说明图象是过原点的直线，k 决定倾斜。"),
    node(N(27), "一次函数解析式", 3, [N(26)], ["fn", "ch-fn"], "能识别 y=kx+b（k≠0），说明它是正比例函数向上或向下平移。", mastery=MASTERY_CONCEPT),
    node(N(28), "一次函数的图象", 3, [N(27)], ["fn", "ch-fn"], "能根据 k、b 画出直线：k 是斜率意识，b 是与 y 轴交点。", mastery=MASTERY_GATE),
    node(N(29), "一次函数与方程", 4, [N(28), N(5)], ["fn", "ch-fn"], "能说明直线与 x 轴交点对应方程 kx+b=0 的解；两条直线交点对应方程组的解。"),
    node(N(30), "一次函数简单应用", 4, [N(29)], ["fn", "ch-fn", "word"], "能在简单计费、行程等情境中写出一次函数并读图回答问题。"),
    node(N(31), "一次函数综合", 4, [N(30), N(23)], ["fn", "ch-end", "boss-gate"], "能把方程组、分式检验与一次函数读图放在同一张检查里切换。", mastery=MASTERY_GATE),
    node(N(32), "八年级代数合练", 4, [N(31)], ["mixed", "ch-end"], "能解方程组、做因式分解、化简分式、读一次函数图象。", mastery=MASTERY_GATE),
    node(N(33), "八年级代数通关", 5, [N(32)], ["mixed", "ch-end", "boss-gate"], "能独立完成八年级数与代数线的收束检查。", mastery=MASTERY_GATE),
    node(N(34), "十字相乘入门", 4, [N(16)], ["poly", "ch-factor"], "能对简单二次三项式尝试十字相乘因式分解，并说明不是所有式子都能这样拆。", unlock=SOFT),
    node(N(35), "分式方程的增根", 4, [N(23)], ["frac", "ch-frac"], "能举出「去分母后得到的解使原分母为 0」的例子，说明必须检验。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(36), "反比例函数对照", 3, [N(26)], ["fn", "ch-fn"], "能识别 y=k/x（k≠0），说明图象是双曲线，并与正比例函数对照：一个过原点直线，一个不经过原点。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(3), "to": N(4), "type": "related", "note": "代入和加减都是消元，系数整齐时加减往往更快。"},
    {"from": N(12), "to": N(13), "type": "easily_confused", "note": "平方差没有中间项；完全平方有 2ab。"},
    {"from": N(11), "to": N(14), "type": "easily_confused", "note": "乘法是展开，因式分解是反过来写成乘积。"},
    {"from": N(18), "to": N(23), "type": "application", "note": "分母不为 0 的约定，在解分式方程时变成检验。"},
    {"from": N(23), "to": N(35), "type": "easily_confused", "note": "使分母为 0 的数不是原方程的解，即使它满足去分母后的整式方程。"},
    {"from": N(26), "to": N(27), "type": "related", "note": "正比例是 b=0 的一次函数。"},
    {"from": N(26), "to": N(36), "type": "easily_confused", "note": "正比例是直线过原点；反比例是双曲线，不要画成直线。"},
    {"from": N(5), "to": N(29), "type": "application", "note": "方程组的解可以看成两条直线的交点。"},
]


QUESTS = [
    q(N(1), "explain", "两个未知数", "举一个需要两个未知数才能说清的关系，并写出一个二元一次方程。", "一对解是两个数，要同时说。"),
    q(N(2), "practice", "检验是不是解", "把数对代入方程组，判断是不是解，共 8 题。", "两个方程都要成立。", items=8),
    q(N(3), "practice", "代入消元", "解 6 道适合代入的方程组。", "选出容易解出的那个未知数。", items=6),
    q(N(4), "practice", "加减消元", "解 6 道系数容易抵消的方程组。", "必要时先把某一方程两边同乘一个数。", items=6),
    q(N(5), "practice", "选方法再解", "8 道混合，先写选用代入还是加减，再解。", "有现成「x=…」用代入；系数相反用加减。", items=8),
    q(N(6), "practice", "列方程组", "3 个短情境：设两个未知数、写两个等量关系、求解。", "两个未知数通常需要两个关系。", items=3),
    q(N(7), "practice", "方程组闯关", "解 6 道并代入两个方程检验。", "只代一个方程不够。", items=6),
    q(N(7), "mini_quiz", "方程组小测", "检验、代入、加减、应用各有。", "消元后得到的是一元方程。", items=10),
    q(N(7), "boss", "关主：消元指挥官", "击败关主：①判断数对是不是解 ②用两种方法之一求解 ③列一个简单方程组。", "消元是为了变成熟悉的一元。", xp=80, items=12, qid=f"{P}-boss-system"),
    q(N(8), "practice", "同底数幂相乘", "10 道，夹一道底数不同不能直接加指数。", "底数必须相同。", items=10),
    q(N(9), "practice", "乘方法则", "8 道 (a^m)^n 与 (ab)^n。", "指数相乘；积的乘方是各自乘方。", items=8),
    q(N(10), "practice", "同底数幂相除", "8 道，结果写成正指数或分数。", "指数相减；底数不为 0。", items=8),
    q(N(11), "practice", "多项式相乘", "6 道单项式乘多项式、多项式乘多项式。", "每一项都要乘到。", items=6),
    q(N(12), "practice", "平方差", "8 道识别并展开或反过来写。", "一看和与差，二看平方减平方。", items=8),
    q(N(13), "practice", "完全平方", "8 道，专门盯中间项符号和 2 倍。", "中间项是 2ab，不要漏 2。", items=8),
    q(N(14), "explain", "分解是反过来", "用一个展开式对照说明因式分解在做什么。", "乘开与拆开是一对逆操作。"),
    q(N(15), "practice", "提公因式", "8 道，含数字与字母公因式。", "提出来后括号里应是整式。", items=8),
    q(N(16), "practice", "公式法分解", "8 道平方差或完全平方，先提公因式再套公式。", "先看能否提取。", items=8),
    q(N(17), "practice", "展开还是分解", "混合 8 题，先判断方向再计算。", "题目要乘开就展开，要写成积就分解。", items=8),
    q(N(17), "mini_quiz", "乘除分解小测", "幂的运算、公式、提公因式。夹一道漏中间项。", "完全平方的中间项最容易丢。", items=10),
    q(N(17), "boss", "关主：因式分解工匠", "击败关主：①幂的运算 ②套用一个乘法公式 ③把一个多项式因式分解。", "先提公因式，再套公式。", xp=80, items=12, qid=f"{P}-boss-factor"),
    q(N(18), "explain", "分母不能为 0", "举一个字母取值使分母为 0 的例子，说明此时分式无意义。", "先找使分母为 0 的值并排除。"),
    q(N(19), "practice", "约分通分准备", "把 6 个分式化成最简或通分到相同分母。", "分子分母同乘同除同一个不为 0 的整式。", items=6),
    q(N(20), "practice", "约分与通分", "约分 4 题、通分 4 题。", "约分靠公因式，通分靠公分母。", items=8),
    q(N(21), "practice", "分式乘除", "8 道乘除，能约分的先约。", "除以一个分式等于乘它的倒数。", items=8),
    q(N(22), "practice", "分式加减", "6 道，先通分再加减，结果最简。", "通分时分子也要乘。", items=6),
    q(N(23), "practice", "解分式方程并检验", "5 道，写出使分母为 0 的值并检验。", "增根要舍去。", items=5),
    q(N(24), "explain", "谁随谁变", "举一个生活中「一个量随另一个量变」的例子，指出自变量和因变量。", "函数描述的是对应关系。"),
    q(N(25), "practice", "三种表示互译", "把表格改成解析式或图象草图，共 4 题。", "三种表示说的是同一关系。", items=4),
    q(N(26), "practice", "正比例函数", "判断哪些是正比例函数，并指出 k 的符号如何影响倾斜。", "必须过原点，且是直线。", items=6),
    q(N(27), "explain", "平移出来的直线", "说明 y=kx+b 相对 y=kx 做了什么，b 的意义是什么。", "b 是与 y 轴交点的纵坐标。"),
    q(N(28), "practice", "画一次函数", "根据 k、b 画出 4 条直线，标出与两轴交点。", "先描两个点再连线。", items=4),
    q(N(29), "practice", "交点与方程", "求直线与 x 轴交点，以及两条直线交点，对照解方程/方程组。", "交点的坐标就是方程（组）的解。", items=4),
    q(N(30), "practice", "读图回答", "在计费或行程图象上读出费用、时间或交点含义，共 4 题。", "先看轴的单位。", items=4),
    q(N(31), "practice", "函数与式子合练", "读一次函数、解一个方程组、化简一个分式。", "先辨题型。", items=6),
    q(N(32), "practice", "合练卷", "方程组、因式分解、分式、一次函数各几题。", "公式和检验两处最容易漏。", items=12),
    q(N(33), "practice", "通关综合练", "独立完成四块各一题并口头说理由。", "消元、分解、分母、斜率意识。", items=12),
    q(N(33), "boss", "关主：八年级代数通关试炼", "最终关主：①解二元一次方程组 ②因式分解或公式 ③分式化简或分式方程并检验 ④读一次函数图象。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(34), "practice", "试着十字相乘", "对 4 个简单二次三项式尝试分解，分解不了就写「不能」。", "常数项拆成两数之积、一次项拆成两数之和。", items=4),
    q(N(35), "explain", "增根从哪来", "举一个去分母后多出来的根，说明它为什么不是原方程的解。", "它让原分母变成 0。"),
    q(N(36), "explain", "直线还是双曲线", "对照 y=2x 与 y=2/x 的图象形状和是否过原点。", "反比例函数图象不过原点，也不是直线。"),
]


META = {
    "id": MAP_ID,
    "title": "八年级 · 数与代数",
    "subject": "数学",
    "stage": "初中",
    "grade": 8,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "方程组（关主 1）→ 整式乘除与因式分解（关主 2）→ 分式；一次函数从方程组后并行，在 n031 汇合。十字相乘（n034）、增根（n035）、反比例对照（n036）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-system", f"{P}-boss-factor", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：消元指挥官、因式分解工匠、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中八年级「数与代数」地图：二元一次方程组、整式乘除与因式分解、分式、一次函数。独立通关。",
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
