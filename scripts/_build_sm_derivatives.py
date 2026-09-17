"""Build senior-math 导数及其应用 map.

Run: python3 scripts/_build_sm_derivatives.py

Pedagogical spine: 变化率 → 导数定义与运算 → 切线 → 单调性极值最值与优化。
尖点不可导、极值不是最值、复合漏乘、实际定义域为软锁。课标在选必「函数」主题，grade=11。
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

OUT = ROOT / "maps" / "senior-math" / "derivatives"
G = 11
STRAND = "数与代数"
P = "sm-der"
MAP_ID = "sm-derivatives"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "平均变化率", 1, [], ["der", "ch-def"], "能计算 [f(x2)-f(x1)]/(x2-x1)，并说明它是割线的斜率。本图从变化率讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "瞬时变化率直觉", 2, [N(1)], ["der", "ch-def"], "能说明让间隔越来越小，平均变化率可以逼近某一点的瞬时变化率。", mastery=MASTERY_CONCEPT),
    node(N(3), "导数的定义", 3, [N(2)], ["der", "ch-def"], "能把导数理解为极限意义下的瞬时变化率，并读出 f'(x0) 的符号含义。", mastery=MASTERY_CONCEPT),
    node(N(4), "导函数", 3, [N(3)], ["der", "ch-def"], "能说明对每个 x 求导数得到新函数 f'，叫做导函数。"),
    node(N(5), "导数的几何意义", 3, [N(3)], ["der", "ch-def"], "能说明 f'(x0) 是曲线在该点切线的斜率。", mastery=MASTERY_GATE),
    node(N(6), "导数的物理意义", 2, [N(3)], ["der", "ch-def"], "能把位移对时间的导数说成瞬时速度（入门）。", mastery=MASTERY_CONCEPT),
    node(N(7), "多项式求导", 3, [N(4)], ["der", "ch-op"], "能对幂函数 x^n 与多项式逐项求导。", mastery=MASTERY_GATE),
    node(N(8), "指数与对数求导", 3, [N(7)], ["der", "ch-op"], "能使用 e^x、(a^x)、ln x 的导数公式做计算（公式可作为已知）。"),
    node(N(9), "三角函数求导", 3, [N(7)], ["der", "ch-op"], "能使用 sin x、cos x 的导数公式，并注意符号。"),
    node(N(10), "加减与数乘法则", 3, [N(7)], ["der", "ch-op"], "能对函数的和、差、常数倍求导。"),
    node(N(11), "积商法则入门", 4, [N(10)], ["der", "ch-op"], "能对简单乘积、商求导，写下法则再代入。", mastery=MASTERY_GATE),
    node(N(12), "复合函数导数入门", 4, [N(11), N(8)], ["der", "ch-op", "boss-gate"], "能对 f(g(x)) 使用链式法则：先外后内相乘。", mastery=MASTERY_GATE),
    node(N(13), "切线方程", 4, [N(5), N(7)], ["der", "ch-app"], "能由一点处的导数写出切线：过该点、斜率为导数。", mastery=MASTERY_GATE),
    node(N(14), "单调性与导数", 4, [N(12)], ["der", "ch-app"], "能用 f'>0、f'<0 判断增、减（在区间上），并说明等于 0 的点要单独看。", mastery=MASTERY_GATE),
    node(N(15), "极值", 4, [N(14)], ["der", "ch-app"], "能用导数变号判断极大、极小，并指出导数为 0 不一定是极值。", mastery=MASTERY_CONCEPT),
    node(N(16), "闭区间最值", 4, [N(15)], ["der", "ch-app"], "能比较区间端点与极值，得到闭区间上的最大、最小值。", mastery=MASTERY_GATE),
    node(N(17), "生活中的优化", 4, [N(16)], ["der", "ch-app"], "能把「围栏最大面积」「用料最省」写成函数，求定义域内最值。", mastery=MASTERY_GATE),
    node(N(18), "作函数草图", 3, [N(16)], ["der", "ch-app"], "能根据单调区间和极值画出多项式一类函数的草图。"),
    node(N(19), "导数法证不等式入门", 4, [N(14)], ["der", "ch-app"], "能通过构造函数、看单调，说明一个简单不等式（入门）。"),
    node(N(20), "导数应用合练", 4, [N(13), N(17), N(18)], ["mixed", "ch-end"], "能在切线、单调、最值、优化之间切换。", mastery=MASTERY_GATE),
    node(N(21), "导数通关", 5, [N(20), N(19)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(22), "可导与连续直觉", 3, [N(5)], ["der", "ch-def"], "能说明可导通常连续，但连续不一定可导（尖点）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(23), "尖点不可导", 3, [N(22)], ["der", "ch-def"], "能指出 |x| 在原点连续但左右变化率不同，因而不可导。", unlock=SOFT),
    node(N(24), "极值不是最值", 3, [N(16)], ["der", "ch-app"], "能举开区间或端点更大的例子，说明极值只是附近最高/最低。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(25), "复合漏乘内层", 3, [N(12)], ["der", "ch-op"], "能专门改错：对外层求导后忘记乘内层导数。", unlock=SOFT),
    node(N(26), "实际问题的定义域", 3, [N(17)], ["der", "ch-app"], "能在优化题里先写自变量的实际范围，再求最值。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "切线与割线", 2, [N(13)], ["der", "ch-def"], "能对照割线斜率（平均）与切线斜率（瞬时）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "导数为零不一定极值", 3, [N(15)], ["der", "ch-app"], "能举 y=x³ 在原点：导数为 0 但单调仍过。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(1), "to": N(5), "type": "related", "note": "割线变切线，平均变瞬时。"},
    {"from": N(11), "to": N(12), "type": "easily_confused", "note": "积法则是两项相加；链式是两层相乘。"},
    {"from": N(14), "to": N(15), "type": "related", "note": "先会判断升降，再在变号处谈极值。"},
    {"from": N(15), "to": N(16), "type": "easily_confused", "note": "极值看附近，最值看整个给定区间。"},
    {"from": N(12), "to": N(25), "type": "application", "note": "会链式之后，专门抓漏乘。"},
    {"from": N(17), "to": N(26), "type": "application", "note": "优化题的坑往往在定义域，不在求导。"},
    {"from": N(5), "to": N(22), "type": "related", "note": "切线存在与图象是否「尖」连在一起。"},
]


QUESTS = [
    q(N(1), "practice", "算平均变化率", "6 道求两点间平均变化率，并在图上标出割线。", "差商：纵坐标差比横坐标差。", items=6),
    q(N(2), "explain", "间隔越来越小", "用一张表让 Δx 缩小，观察差商往哪靠近。", "逼近的是那一点的瞬时。"),
    q(N(3), "explain", "导数是什么", "用自己的话写两句：变化率、切线斜率。", "一个数，不是又一条曲线（那是导函数）。"),
    q(N(4), "practice", "导函数与一点的导数", "区分「f'(2)」和「f'(x)」各 4 例。", "一个是数，一个是函数。", items=4),
    q(N(5), "practice", "读切线斜率", "由图或已知导数指出 6 个点的切线斜率，含水平切线。", "斜率为 0 则水平。", items=6),
    q(N(6), "explain", "速度是导数", "用位移函数说明某一时刻的速度为什么不是平均速度。", "平均速度对应一段时间。"),
    q(N(7), "practice", "多项式求导", "10 道多项式求导。", "x^n 变成 n x^{n-1}。", items=10),
    q(N(8), "practice", "指数对数求导", "6 道套公式。", "e^x 的导数还是 e^x。", items=6),
    q(N(9), "practice", "正弦余弦求导", "6 道，注意 cos 的导数带负号。", "sin'=cos，cos'=-sin。", items=6),
    q(N(10), "practice", "和差数乘", "8 道。", "常数提到外面。", items=8),
    q(N(11), "practice", "积与商", "8 道写下法则再算。", "积：前导后 + 前导后；商：记住分子那一行。", items=8),
    q(N(12), "practice", "链式法则", "8 道复合求导，圈出内层。", "外层导数乘内层导数。", items=8),
    q(N(12), "mini_quiz", "求导运算小测", "多项式、积商、复合。夹一道漏乘内层。", "先认结构再动笔。", items=10),
    q(N(12), "boss", "关主：求导运算官", "击败关主：①多项式 ②积或商 ③一个复合函数。", "结构认错，法则再熟也错。", xp=80, items=12, qid=f"{P}-boss-op"),
    q(N(13), "practice", "写切线方程", "6 道：先求该点导数，再点斜式。", "点在曲线上，斜率是导数。", items=6),
    q(N(14), "practice", "用导数判断单调", "6 个函数求单调区间。", "先求 f'，再看正负。", items=6),
    q(N(15), "practice", "求极值", "4 个函数求极值点与极值。", "看 f' 是否变号。", items=4),
    q(N(16), "practice", "闭区间最值", "4 道比较端点与极值。", "三个地方都要算：端点、驻点。", items=4),
    q(N(17), "practice", "一道优化", "2 个短情境：设未知数、写函数、求定义域、求最值、写答。", "实际范围先写出来。", items=2),
    q(N(18), "practice", "画草图", "根据单调与极值画 2 个三次函数草图。", "升降对了，形状就对了。", items=2),
    q(N(19), "practice", "构造函数看单调", "用导数说明 2 个简单不等式在某区间成立。", "作差，再看导数符号。", items=2),
    q(N(20), "practice", "合练卷", "切线、单调、最值、优化各几题。", "先问要斜率还是要最值。", items=12),
    q(N(20), "mini_quiz", "应用小测", "切线、极值最值、一道应用。夹一道把极值当最值。", "看清区间。", items=8),
    q(N(20), "boss", "关主：单调最值工程师", "击败关主：①判断单调 ②求闭区间最值 ③一个优化或切线。", "端点不要忘。", xp=80, items=10, qid=f"{P}-boss-app"),
    q(N(21), "practice", "通关综合练", "独立完成：复合求导、切线、闭区间最值。", "运算和应用各一刀。", items=12),
    q(N(21), "boss", "关主：导数通关试炼", "最终关主：①求导 ②切线或单调 ③最值或优化。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(22), "explain", "连续但可能尖", "说明可导比连续要求更「光滑」。", "尖了就没有唯一切线。"),
    q(N(23), "practice", "看 |x|", "画出 y=|x|，说明原点左右平均变化率不同。", "一边 1，一边 -1。", items=1),
    q(N(24), "explain", "附近最高不是全程最高", "举一个端点比极更大的闭区间例子。", "极值只管附近。"),
    q(N(25), "practice", "改漏乘", "改 4 道复合求导错解。", "内层导数常是常数或一次项。", items=4),
    q(N(26), "practice", "先写定义域", "2 道应用题只要求写出自变量范围并说明理由。", "长度不能为负。", items=2),
    q(N(27), "explain", "割线变切线", "在同一图上画割线与切线，说明导数对应哪一条。", "切线是极限位置。"),
    q(N(28), "explain", "水平但不拐", "用 y=x³ 说明导数为 0 只是水平切线，不一定是峰或谷。", "还要看是否变号。"),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 导数及其应用",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "导数及其应用",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "变化率与求导运算（关主 1）→ 切线、单调与最值（关主 2）后收束。可导连续（n022）、尖点（n023）、极值非最值（n024）、漏乘（n025）、实际定义域（n026）、割线切线（n027）、水平非极值（n028）为软锁。grade=11。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-op", f"{P}-boss-app", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：求导运算官、单调最值工程师、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中选必「导数及其应用」地图：变化率 → 求导 → 切线与单调最值 → 优化入门。独立通关。grade=11。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress(MAP_ID, N(1), f"{N(1)}-practice", N(2), N(4), f"{N(4)}-practice"),
    )


if __name__ == "__main__":
    main()
