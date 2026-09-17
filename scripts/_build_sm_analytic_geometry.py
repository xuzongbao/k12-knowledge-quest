"""Build senior-math 平面解析几何 map (直线、圆、圆锥曲线入门).

Run: python3 scripts/_build_sm_analytic_geometry.py

Pedagogical spine: 直线方程 → 圆 → 椭圆 → 双曲线入门 → 抛物线。
渐近线、离心率比较、椭圆参数直觉为软锁。课标中直线与圆、圆锥曲线在选必「平面解析几何」；本图 grade=11。
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

OUT = ROOT / "maps" / "senior-math" / "analytic-geometry"
G = 11
STRAND = "图形与几何"
P = "sm-ag"
MAP_ID = "sm-analytic-geometry"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "用坐标研究图形", 1, [], ["line", "ch-line"], "能说明解析几何是用方程表示曲线、用代数研究几何。本图从直线讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "倾斜角与斜率", 2, [N(1)], ["line", "ch-line"], "能指出倾斜角范围，斜率 k=tan α，并说明竖直线没有斜率。", mastery=MASTERY_CONCEPT),
    node(N(3), "两点斜率", 2, [N(2)], ["line", "ch-line"], "能用两点坐标求斜率，分母为 0 时判定为竖直线。"),
    node(N(4), "点斜式", 3, [N(3)], ["line", "ch-line"], "能由一点和斜率写出直线方程 y-y0=k(x-x0)。", mastery=MASTERY_CONCEPT),
    node(N(5), "斜截式", 2, [N(4)], ["line", "ch-line"], "能识别 y=kx+b 中 b 是 y 轴截距。"),
    node(N(6), "两点式与一般式", 3, [N(4)], ["line", "ch-line"], "能在两点式与 Ax+By+C=0 之间互化，并处理竖直线。", mastery=MASTERY_GATE),
    node(N(7), "两条直线平行", 3, [N(6)], ["line", "ch-line"], "能用斜率相等（或一般式系数比例）判断平行，并排除重合。"),
    node(N(8), "两条直线垂直", 3, [N(7)], ["line", "ch-line"], "能用 k1k2=-1 判断垂直（斜率都存在时），并处理一条竖直的情形。", mastery=MASTERY_GATE),
    node(N(9), "点到直线距离", 3, [N(6)], ["line", "ch-line"], "能用距离公式求点到直线的距离。", mastery=MASTERY_GATE),
    node(N(10), "直线综合", 4, [N(8), N(9)], ["line", "ch-line", "boss-gate"], "能求交点、平行垂直、距离，并把几何条件写成方程。", mastery=MASTERY_GATE),
    node(N(11), "圆的标准方程", 2, [N(1)], ["circle", "ch-circle"], "能写出 (x-a)²+(y-b)²=r²，读出圆心和半径。", mastery=MASTERY_CONCEPT),
    node(N(12), "圆的一般方程", 3, [N(11)], ["circle", "ch-circle"], "能把一般式配方成标准式，并判断是否表示圆。", mastery=MASTERY_GATE),
    node(N(13), "直线与圆的位置", 4, [N(12), N(9)], ["circle", "ch-circle"], "能用圆心到直线距离与半径比较，判断相离、相切、相交。", mastery=MASTERY_GATE),
    node(N(14), "圆的切线", 3, [N(13)], ["circle", "ch-circle"], "能写出过圆上一点的切线，或已知斜率求切线入门。"),
    node(N(15), "圆与圆位置入门", 3, [N(12)], ["circle", "ch-circle"], "能用圆心距与两半径比较，判断外离、外切、相交、内切、内含。"),
    node(N(16), "直线与圆综合", 4, [N(10), N(14), N(15)], ["circle", "ch-circle", "boss-gate"], "能把直线与圆联立或用几何量解决简单问题。", mastery=MASTERY_GATE),
    node(N(17), "椭圆的定义", 2, [N(11)], ["conic", "ch-conic"], "能说明椭圆是到两焦点距离之和为常数（大于焦距）的点的轨迹。", mastery=MASTERY_CONCEPT),
    node(N(18), "椭圆标准方程", 4, [N(17)], ["conic", "ch-conic"], "能写出 x²/a²+y²/b²=1（a>b>0），并求 a、b、c、焦点。", mastery=MASTERY_GATE),
    node(N(19), "椭圆简单性质", 3, [N(18)], ["conic", "ch-conic"], "能指出范围、对称性、顶点，并说明离心率 e=c/a 在 (0,1)。"),
    node(N(20), "双曲线的定义", 2, [N(17)], ["conic", "ch-conic"], "能说明双曲线是到两焦点距离之差的绝对值为常数（小于焦距）的点的轨迹。", mastery=MASTERY_CONCEPT),
    node(N(21), "双曲线标准方程入门", 4, [N(20), N(18)], ["conic", "ch-conic"], "能识别 x²/a²-y²/b²=1 的焦点在 x 轴，并求 a、b、c。", mastery=MASTERY_GATE),
    node(N(22), "抛物线的定义", 2, [N(17)], ["conic", "ch-conic"], "能说明抛物线是到定点（焦点）与定直线（准线）距离相等的点的轨迹。", mastery=MASTERY_CONCEPT),
    node(N(23), "抛物线标准方程", 3, [N(22)], ["conic", "ch-conic"], "能识别 y²=2px 等四种开口，并读出焦点与准线。", mastery=MASTERY_GATE),
    node(N(24), "圆锥曲线对照", 3, [N(19), N(21), N(23)], ["conic", "ch-conic"], "能用「和、差、等距」对照椭圆、双曲线、抛物线的定义。", mastery=MASTERY_CONCEPT),
    node(N(25), "直线与圆锥曲线入门", 4, [N(16), N(24)], ["conic", "ch-conic"], "能把直线代入圆锥曲线方程，用判别式看交点个数（入门，不深挖弦长技巧）。", mastery=MASTERY_GATE),
    node(N(26), "解析几何合练", 4, [N(25)], ["mixed", "ch-end"], "能在直线、圆、圆锥曲线入门之间切换，先写定义再写方程。", mastery=MASTERY_GATE),
    node(N(27), "解析几何通关", 5, [N(26)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(28), "渐近线直觉", 3, [N(21)], ["conic", "ch-conic"], "能说明双曲线两条直线「越走越贴但不相交」，并写出标准方程的渐近线。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(29), "离心率比较", 3, [N(19)], ["conic", "ch-conic"], "能说明椭圆离心率越接近 1 越扁，越接近 0 越圆。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(30), "椭圆参数直觉", 3, [N(18)], ["conic", "ch-conic"], "能把椭圆看成圆压扁，用 x=a cos t, y=b sin t 理解点的位置（不要求运算技巧）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(31), "坐标法证平面几何入门", 3, [N(10)], ["line", "ch-line"], "能把直角三角形放在坐标系里，用斜率或距离证一条简单性质。", unlock=SOFT),
    node(N(32), "抛物线焦点弦入门", 3, [N(23)], ["conic", "ch-conic"], "能指出过焦点的弦的两端在抛物线上，并说明焦半径与到准线距离相等。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(4), "to": N(6), "type": "related", "note": "点斜式方便写，一般式能覆盖竖直线。"},
    {"from": N(7), "to": N(8), "type": "easily_confused", "note": "平行是斜率相等，垂直是乘积为 -1，不要记反。"},
    {"from": N(13), "to": N(15), "type": "related", "note": "都是比较距离与半径，一个对直线，一个对另一圆。"},
    {"from": N(17), "to": N(20), "type": "easily_confused", "note": "椭圆是距离之和为常数，双曲线是差的绝对值为常数。"},
    {"from": N(17), "to": N(22), "type": "related", "note": "抛物线只有一个焦点和一条准线，是「和/差」退化成「相等」。"},
    {"from": N(21), "to": N(28), "type": "application", "note": "先有标准方程，再写渐近线。"},
    {"from": N(19), "to": N(29), "type": "related", "note": "e=c/a 已经出现，再谈扁与圆。"},
]


QUESTS = [
    q(N(1), "explain", "为什么要方程", "用「直线可以写成一次式」说明坐标能把图形变成运算。", "点满足方程就在曲线上。"),
    q(N(2), "practice", "读倾斜角与斜率", "8 组由角求斜率或由斜率估计角，含竖直线无斜率。", "正切在 90° 没有意义。", items=8),
    q(N(3), "practice", "两点求斜率", "8 道两点求 k，含竖直线。", "分母为零就是竖直。", items=8),
    q(N(4), "practice", "写点斜式", "6 道由点与斜率写方程。", "先代入再整理。", items=6),
    q(N(5), "practice", "读截距", "6 个斜截式指出斜率和截距。", "b 是与 y 轴交点的纵坐标。", items=6),
    q(N(6), "practice", "方程互化", "6 组点斜、斜截、一般式互化，含竖直线。", "竖直线写成 x=常数。", items=6),
    q(N(7), "practice", "判断平行", "6 对直线判断平行、重合或相交。", "斜率相等还要检查是不是同一条。", items=6),
    q(N(8), "practice", "判断垂直", "6 对直线判断垂直。", "一条竖直则另一条要水平。", items=6),
    q(N(9), "practice", "点到直线距离", "6 道套公式，注意一般式要先整理。", "分子取绝对值，分母是系数平方和开方。", items=6),
    q(N(10), "practice", "直线综合", "4 题：交点、过点作平行或垂直、距离。", "先写方程，再运算。", items=4),
    q(N(10), "mini_quiz", "直线小测", "斜率、方程、平行垂直、距离。夹一道竖直线。", "没有斜率不等于没有方程。", items=8),
    q(N(11), "practice", "读圆心半径", "8 个标准方程读圆心、半径。", "注意平方前的符号。", items=8),
    q(N(12), "practice", "配方", "6 个一般式配方，判断是不是圆。", "半径平方必须为正。", items=6),
    q(N(13), "practice", "直线与圆位置", "6 组用距离与半径比较。", "等于则相切。", items=6),
    q(N(14), "practice", "写切线", "4 道过圆上一点写切线。", "半径与切线垂直。", items=4),
    q(N(15), "practice", "两圆位置", "5 组用圆心距判断。", "比较 d 与 r1+r2、|r1-r2|。", items=5),
    q(N(16), "practice", "直线与圆综合", "3 题联立或几何法求交点、切线。", "判别式看个数。", items=3),
    q(N(16), "mini_quiz", "圆小测", "标准式一般式、位置、切线。夹一道半径平方为负。", "先配方。", items=8),
    q(N(16), "boss", "关主：直线与圆测绘员", "击败关主：①直线平行或垂直 ②圆的方程 ③直线与圆位置。", "距离与半径要会比。", xp=80, items=12, qid=f"{P}-boss-line"),
    q(N(17), "explain", "绳子定义", "用「两焦点距离之和不变」说明椭圆怎么画出来。", "绳子长度要大于两焦点距离。"),
    q(N(18), "practice", "椭圆标准方程", "6 道求 a、b、c、焦点坐标。", "c²=a²-b²。", items=6),
    q(N(19), "practice", "椭圆性质卡", "对 3 个椭圆填写范围、顶点、离心率。", "e=c/a 小于 1。", items=3),
    q(N(20), "explain", "差是常数", "对照椭圆，说明双曲线为什么是「差」而不是「和」。", "差要小于焦距，否则画不出来。"),
    q(N(21), "practice", "双曲线入门计算", "4 道识别焦点在哪一轴，求 a、b、c。", "c²=a²+b²。", items=4),
    q(N(22), "explain", "焦点与准线", "说明抛物线上一点到焦点和到准线一样远。", "一个点、一条线。"),
    q(N(23), "practice", "抛物线读写", "6 个方程读开口、焦点、准线。", "一次项变量决定对称轴。", items=6),
    q(N(24), "explain", "三种定义对照", "用一张三列对照：和、差、等距。", "先定义，后方程。"),
    q(N(25), "practice", "联立看交点个数", "4 组直线与椭圆或抛物线，用判别式说个数。", "不要急着求具体点。", items=4),
    q(N(25), "boss", "关主：圆锥曲线入门官", "击败关主：①椭圆或抛物线定义 ②标准方程求焦点 ③说明与直线交点个数怎么看。", "定义优先于套公式。", xp=80, items=10, qid=f"{P}-boss-conic"),
    q(N(26), "practice", "合练卷", "直线、圆、一种圆锥曲线各几题。", "先命名曲线。", items=12),
    q(N(27), "practice", "通关综合练", "独立完成：直线垂直、圆的位置、一个椭圆或抛物线方程。", "坐标计算要写清公式名。", items=12),
    q(N(27), "boss", "关主：解析几何通关试炼", "最终关主：①直线或圆 ②一种圆锥曲线的定义与方程 ③交点个数或简单性质。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(28), "practice", "写渐近线", "为 3 个双曲线写出渐近线方程。", "±(b/a)x 或 ±(a/b)x 看焦点在哪轴。", items=3),
    q(N(29), "explain", "扁还是圆", "比较两个椭圆的 e，说明哪个更扁。", "e 越接近 1 越扁。"),
    q(N(30), "explain", "圆压扁", "说明参数 t 从 0 到 2π 时点如何走完椭圆。", "和圆的参数方程很像，只是轴长不同。"),
    q(N(31), "practice", "放进坐标系", "把一个直角三角形放上坐标，用斜率证一次垂直或用距离证一次等长。", "直角顶点放原点往往最省事。", items=1),
    q(N(32), "explain", "焦半径", "在抛物线图上标出焦点、准线、弦的一端，解释等距。", "垂直于准线去量。"),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 平面解析几何",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "平面解析几何",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "直线（汇入圆）→ 直线与圆（关主 1）→ 圆锥曲线入门（关主 2）后收束。渐近线（n028）、离心率（n029）、椭圆参数（n030）、坐标法证题（n031）、焦点弦（n032）为软锁。grade=11 表示选必学段带。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-line", f"{P}-boss-conic", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：直线与圆测绘员、圆锥曲线入门官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中选必「平面解析几何」入门地图：直线 → 圆 → 椭圆、双曲线、抛物线。独立通关。grade=11。",
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
