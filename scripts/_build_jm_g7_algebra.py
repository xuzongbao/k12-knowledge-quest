"""Build Grade 7 Algebra map JSON (七年级 · 数与代数).

Run: python3 scripts/_build_jm_g7_algebra.py

Pedagogical spine (课标脉络，自撰短描述，非教材页原文):
  有理数 → 整式加减 → 一元一次方程 → 不等式入门。
科学记数法、近似计算为软锁支线。本图自洽，不引用小学或其他初中地图节点。
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

OUT = ROOT / "maps" / "junior-math" / "grade-7-algebra"
G = 7
STRAND = "数与代数"
P = "jm-g7-alg"
MAP_ID = "jm-g7-algebra"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    # A. 有理数
    node(N(1), "正数、负数和 0", 1, [], ["rational", "ch-rational"], "能用正负表示相反意义的量，并说明 0 既不是正数也不是负数。本图从这里系统学习有理数。", mastery=MASTERY_CONCEPT),
    node(N(2), "有理数的意义", 2, [N(1)], ["rational", "ch-rational"], "能说出整数和分数（含小数）合起来叫做有理数，并举出正负分数的例子。", mastery=MASTERY_CONCEPT),
    node(N(3), "数轴", 2, [N(2)], ["rational", "ch-rational", "axis"], "能在数轴上标出给定有理数，并说明原点、正方向、单位长度三要素。"),
    node(N(4), "相反数", 2, [N(3)], ["rational", "ch-rational"], "能求一个有理数的相反数，并说明数轴上关于原点对称。", mastery=MASTERY_CONCEPT),
    node(N(5), "绝对值", 2, [N(4)], ["rational", "ch-rational"], "能求有理数的绝对值：到原点的距离；知道绝对值是非负数。", mastery=MASTERY_CONCEPT),
    node(N(6), "有理数比大小", 3, [N(5)], ["rational", "ch-rational"], "能借助数轴或「右边的数更大」比较有理数，包括两个负数。"),
    node(N(7), "有理数加法", 3, [N(6)], ["rational", "ch-rational", "add"], "能按同号相加、异号相减的法则计算有理数加法，并说明和的符号。", mastery=MASTERY_GATE),
    node(N(8), "有理数减法", 3, [N(7)], ["rational", "ch-rational", "sub"], "能把减法转化成加上相反数，完成有理数减法。"),
    node(N(9), "加减混合与运算律", 3, [N(8)], ["rational", "ch-rational"], "能在有理数加减混合中使用交换律、结合律，合理凑整。"),
    node(N(10), "有理数乘法", 3, [N(9)], ["rational", "ch-rational", "mul"], "能用「负负得正、异号得负」计算有理数乘法，并说明 0 乘任何数得 0。", mastery=MASTERY_GATE),
    node(N(11), "有理数除法", 3, [N(10)], ["rational", "ch-rational", "div"], "能把除法转化成乘倒数；除数不能为 0。"),
    node(N(12), "乘方", 3, [N(11)], ["rational", "ch-rational", "power"], "能计算有理数的乘方，注意负数的偶次方为正、奇次方为负，括号不能丢。"),
    node(N(13), "有理数混合运算", 4, [N(12)], ["rational", "ch-rational", "boss-gate"], "能按乘方、乘除、加减的顺序完成有理数混合运算，有括号先算括号。", mastery=MASTERY_GATE),
    # B. 整式加减
    node(N(14), "用字母表示数", 2, [N(13)], ["poly", "ch-poly"], "能用字母表示变化的量或一般规律，并说明字母可以取有理数。", mastery=MASTERY_CONCEPT),
    node(N(15), "代数式", 2, [N(14)], ["poly", "ch-poly"], "能识别代数式，说出其中的运算，并与「只含数字的算式」区分。", mastery=MASTERY_CONCEPT),
    node(N(16), "代数式的值", 3, [N(15)], ["poly", "ch-poly"], "能把字母换成指定有理数，求出代数式的值。"),
    node(N(17), "单项式", 2, [N(16)], ["poly", "ch-poly"], "能指出单项式的系数和次数，注意系数含前面的符号。", mastery=MASTERY_CONCEPT),
    node(N(18), "多项式与整式", 2, [N(17)], ["poly", "ch-poly"], "能把几个单项式的和叫做多项式，整式包括单项式和多项式。", mastery=MASTERY_CONCEPT),
    node(N(19), "同类项", 3, [N(18)], ["poly", "ch-poly"], "能判断两个单项式所含字母及相同字母的次数是否都相同。"),
    node(N(20), "合并同类项", 3, [N(19)], ["poly", "ch-poly"], "能把同类项的系数相加、字母部分不变，完成合并。", mastery=MASTERY_GATE),
    node(N(21), "去括号", 3, [N(20)], ["poly", "ch-poly"], "能按括号前是正号或负号正确去括号：负号改变每一项的符号。"),
    node(N(22), "整式加减", 4, [N(21)], ["poly", "ch-poly", "boss-gate"], "能去括号、合并同类项，完成整式加减，并按某个字母降幂排列。", mastery=MASTERY_GATE),
    # C. 一元一次方程
    node(N(23), "等式的性质", 2, [N(22)], ["eq", "ch-eq"], "能说明等式两边同时加（或减、乘、除以不为 0 的数）后仍相等。", mastery=MASTERY_CONCEPT),
    node(N(24), "方程与方程的解", 2, [N(23)], ["eq", "ch-eq"], "能指出含未知数的等式叫做方程，并使方程成立的未知数的值叫做解。", mastery=MASTERY_CONCEPT),
    node(N(25), "一元一次方程", 2, [N(24)], ["eq", "ch-eq"], "能识别只含一个未知数且未知数次数是 1 的方程。", mastery=MASTERY_CONCEPT),
    node(N(26), "移项", 3, [N(25)], ["eq", "ch-eq"], "能把方程中的项改变符号后移到另一边，这是等式两边同时加减的简便写法。"),
    node(N(27), "去分母与去括号", 3, [N(26)], ["eq", "ch-eq"], "能先去分母（两边同乘最简公分母）、再去括号，为解方程做准备。"),
    node(N(28), "解一元一次方程", 4, [N(27)], ["eq", "ch-eq"], "能按去分母、去括号、移项、合并、系数化为 1 的步骤求解，并检验。", mastery=MASTERY_GATE),
    node(N(29), "列方程解决简单问题", 4, [N(28)], ["eq", "ch-eq", "word"], "能设未知数、找等量关系、列出一元一次方程并求解、写答。"),
    # D. 不等式入门
    node(N(30), "不等式的意义", 2, [N(28)], ["ineq", "ch-ineq"], "能用不等号表示数量关系，并说明不等式的解通常是一个范围。", mastery=MASTERY_CONCEPT),
    node(N(31), "不等式的性质", 3, [N(30)], ["ineq", "ch-ineq"], "能说明两边同乘（或除以）负数时，不等号方向要改变。", mastery=MASTERY_GATE),
    node(N(32), "解一元一次不等式", 4, [N(31)], ["ineq", "ch-ineq"], "能模仿解方程的步骤解一元一次不等式，特别注意乘除负数。"),
    node(N(33), "解集在数轴上表示", 3, [N(32), N(3)], ["ineq", "ch-ineq"], "能在数轴上用空心点或实心点、射线表示不等式的解集。"),
    node(N(34), "方程与不等式对照", 3, [N(29), N(33)], ["eq", "ineq", "ch-end"], "能对照「等于某个数」和「大于或小于某个数」，说明解是点还是范围。", mastery=MASTERY_CONCEPT),
    node(N(35), "七年级代数合练", 4, [N(34)], ["mixed", "ch-end"], "能在有理数运算、整式加减、解方程与解不等式之间切换，不混用法则。", mastery=MASTERY_GATE),
    node(N(36), "七年级代数通关", 5, [N(35)], ["mixed", "ch-end", "boss-gate"], "能独立完成七年级数与代数线的收束检查。", mastery=MASTERY_GATE),
    # 软锁
    node(N(37), "科学记数法", 3, [N(12)], ["rational", "ch-rational"], "能把很大或很小的正数写成 a×10^n（1≤a<10）的形式，并读出数量级。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(38), "近似计算入门", 3, [N(13)], ["rational", "ch-rational"], "能按指定精确度对有理数运算结果取近似值，并说明为什么有时不必算得过细。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(4), "to": N(5), "type": "easily_confused", "note": "相反数管符号翻转，绝对值管到原点的距离，不要互相替代。"},
    {"from": N(7), "to": N(10), "type": "easily_confused", "note": "加法看同号异号「加还是减」；乘法看同号异号「正还是负」。"},
    {"from": N(8), "to": N(11), "type": "related", "note": "减法化加相反数，除法化乘倒数，都是「转化成另一种运算」。"},
    {"from": N(12), "to": N(37), "type": "application", "note": "乘方熟悉后，10 的幂用来写很大很小的数。"},
    {"from": N(19), "to": N(20), "type": "easily_confused", "note": "字母相同但次数不同，不是同类项，不能合并。"},
    {"from": N(23), "to": N(31), "type": "easily_confused", "note": "等式两边同乘负数仍相等；不等式两边同乘负数要变号。"},
    {"from": N(26), "to": N(32), "type": "related", "note": "移项在方程和不等式里都可用，但不等式还要盯系数的符号。"},
    {"from": N(13), "to": N(38), "type": "application", "note": "会精确算之后，才谈何时取近似。"},
]


QUESTS = [
    q(N(1), "explain", "相反意义的量", "举温度、盈亏、升降各一例，说明用正负怎么记，并指出 0 表示什么。", "0 是分界，不是正也不是负。"),
    q(N(2), "explain", "哪些是有理数", "从整数、分数、有限小数、循环小数里指出有理数，并各举一个负数例子。", "能写成两整数之比的是有理数。"),
    q(N(3), "practice", "在数轴上描点", "在数轴上标出至少 6 个有理数，含正负分数。", "先找原点，再按单位长度数格。", items=6),
    q(N(4), "practice", "求相反数", "求 8 个有理数的相反数，并在数轴上指出对称点。", "互为相反数的两点关于原点对称。", items=8),
    q(N(5), "practice", "求绝对值", "求 8 个有理数的绝对值，并说明「绝对值相等、符号相反」意味着什么。", "绝对值是到原点的距离，结果≥0。", items=8),
    q(N(6), "practice", "比较有理数", "比较 10 组有理数大小，其中至少 4 组是两个负数。", "在数轴上越靠右越大；两个负数绝对值大的反而更小。", items=10),
    q(N(7), "practice", "有理数加法", "完成 10 道有理数加法，写出和的符号从哪来。", "同号相加；异号相减，符号跟绝对值大的走。", items=10),
    q(N(8), "practice", "减法变加法", "把 8 道减法改写成加上相反数再计算。", "减去一个数等于加上它的相反数。", items=8),
    q(N(9), "practice", "加减混合凑整", "6 道加减混合，用运算律先凑成整十或抵消。", "先找互为相反数的项。", items=6),
    q(N(10), "practice", "有理数乘法", "12 道乘法，含多个负数相乘，说出负号的个数如何决定符号。", "负号奇数个得负，偶数个得正。", items=12),
    q(N(11), "practice", "有理数除法", "10 道除法，含除以负数；另加 2 道指出「除数是 0」不合法。", "除以一个数等于乘它的倒数。", items=12),
    q(N(12), "practice", "计算乘方", "8 道乘方，对比 (-2)^4 与 -2^4。", "没有括号时，乘方只作用于紧挨着的数。", items=8),
    q(N(13), "practice", "混合运算闯关", "按运算顺序完成 8 道有理数混合运算。", "乘方→乘除→加减；括号优先。", items=8),
    q(N(13), "mini_quiz", "有理数小测", "混合：比大小、加减乘除、乘方、运算顺序。夹一道 (-3)^2 与 -3^2。", "先符号，再绝对值。", items=10),
    q(N(13), "boss", "关主：有理数运算官", "击败关主：①在数轴上比较并求绝对值 ②完成加减乘除与乘方 ③说明一步混合运算的顺序。", "符号法则和运算顺序两件都要稳。", xp=80, items=12, qid=f"{P}-boss-rational"),
    q(N(14), "explain", "字母能表示什么", "用字母写出「比 a 大 3」「a 的相反数」，并说明 a 可以换成哪些有理数。", "字母是占位符，不是某种神秘新数。"),
    q(N(15), "practice", "识别代数式", "从一列式子里挑出代数式，并指出其中的运算。", "含字母的运算式是代数式；方程有等号。", items=8),
    q(N(16), "practice", "求代数式的值", "给定字母取值，求 8 个代数式的值，注意负数代入要加括号。", "负号代入先加括号再运算。", items=8),
    q(N(17), "practice", "系数和次数", "指出 8 个单项式的系数与次数。", "系数带着前面的符号；次数把各字母指数加起来。", items=8),
    q(N(18), "explain", "整式家族", "用自己的话区分单项式、多项式、整式，并各举一例。", "整式是单项式与多项式的总称。"),
    q(N(19), "practice", "找同类项", "在多项式里圈出同类项，指出哪些只是「长得像」但次数不同。", "字母及相同字母的次数都要相同。", items=6),
    q(N(20), "practice", "合并同类项", "合并 8 个多项式中的同类项。", "系数相加，字母部分照抄。", items=8),
    q(N(21), "practice", "去括号", "完成 8 道去括号，其中至少 4 道括号前是负号。", "负号改变括号里每一项的符号。", items=8),
    q(N(22), "practice", "整式加减综合", "去括号并合并，完成 6 道整式加减，按字母降幂排列。", "先去括号，再合并，再整理顺序。", items=6),
    q(N(22), "mini_quiz", "整式小测", "识别同类项、去括号、合并、求值。夹一道漏变号。", "括号前的负号最容易漏。", items=10),
    q(N(22), "boss", "关主：整式整理员", "击败关主：①指出系数次数 ②去括号合并同类项 ③求一个整式的值。", "整理清楚，再代入。", xp=80, items=12, qid=f"{P}-boss-poly"),
    q(N(23), "explain", "等式还能怎样变", "用天平或自己的话说明：两边同时加同一个数，或同乘不为 0 的数，仍相等。", "两边要做同样的事。"),
    q(N(24), "practice", "检验是不是解", "把数代入方程，判断是不是解，共 8 题。", "代入后左右两边相等才是解。", items=8),
    q(N(25), "practice", "挑出一元一次方程", "从一列方程里挑出一元一次方程，说明其他为什么不是。", "一个未知数，次数是 1。", items=8),
    q(N(26), "practice", "移项练习", "8 道方程只要求正确移项，暂不解完。", "过去的项要变号。", items=8),
    q(N(27), "practice", "去分母去括号", "6 道含分母或括号的方程，先写清同乘的数，再去括号。", "每一项都要乘，包括没有分母的项。", items=6),
    q(N(28), "practice", "解方程并检验", "解 8 道一元一次方程，每题代入检验。", "系数化为 1 时，两边同除以系数。", items=8),
    q(N(29), "practice", "列方程短故事", "4 个短情境：设未知数、写等量关系、求解、写答。", "等量关系是列方程的灵魂。", items=4),
    q(N(30), "explain", "解是一个范围", "对比 x=3 与 x>3，说明后者有多少个解、怎么描述。", "不等式的解通常是无穷多个数组成的集合。"),
    q(N(31), "practice", "变号还是不变", "判断 8 组「两边同乘某数」后不等号要不要变向，并各举一例。", "乘正数不变向，乘负数变向。", items=8),
    q(N(32), "practice", "解一元一次不等式", "解 8 道一元一次不等式，写出解集。", "最后一步除以负数时记得变号。", items=8),
    q(N(33), "practice", "画在数轴上", "把 6 个不等式的解集画在数轴上，分清空心实心。", "≥、≤ 用实心；>、< 用空心。", items=6),
    q(N(34), "explain", "点还是射线", "用一句话对照方程的解和不等式的解在数轴上长什么样。", "方程常常是一个点，不等式常常是一条射线。"),
    q(N(35), "practice", "合练卷", "有理数运算、整式加减、解方程、解不等式各几题。", "先辨题型，再选法则。", items=12),
    q(N(36), "practice", "通关综合练", "独立完成：混合运算、整式整理、列方程、解不等式并画数轴。", "符号、括号、变号，三处最容易漏。", items=12),
    q(N(36), "boss", "关主：七年级代数通关试炼", "最终关主：①有理数混合运算 ②整式加减 ③解一元一次方程并解一个不等式、画数轴。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(37), "practice", "写成科学记数法", "把 6 个很大或很小的正数写成 a×10^n。", "a 要满足 1≤a<10。", items=6),
    q(N(38), "explain", "何时取近似", "举一个生活计算，说明精确到哪一位就够用，不必算到很多位小数。", "精确程度要匹配问题需要。"),
]


META = {
    "id": MAP_ID,
    "title": "七年级 · 数与代数",
    "subject": "数学",
    "stage": "初中",
    "grade": 7,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "有理数运算（关主 1）→ 整式加减（关主 2）→ 一元一次方程；不等式入门与方程对照后收束。科学记数法（n037）、近似计算（n038）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-rational", f"{P}-boss-poly", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：有理数运算官、整式整理员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中七年级「数与代数」地图：有理数 → 整式加减 → 一元一次方程 → 不等式入门。独立通关，不引用跨图节点。",
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
