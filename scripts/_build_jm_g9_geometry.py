"""Build Grade 9 Geometry map JSON (九年级 · 图形与几何).

Run: python3 scripts/_build_jm_g9_geometry.py

Pedagogical spine: 相似 → 锐角三角函数 → 圆 → 投影与视图。
本图自洽。锐角三角比放在本图而非代数图。
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

OUT = ROOT / "maps" / "junior-math" / "grade-9-geometry"
G = 9
STRAND = "图形与几何"
P = "jm-g9-geo"
MAP_ID = "jm-g9-geometry"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "比例线段", 1, [], ["sim", "ch-sim"], "能说明两条线段的比，并求简单的比例中项。", mastery=MASTERY_CONCEPT),
    node(N(2), "相似图形", 2, [N(1)], ["sim", "ch-sim"], "能说明形状相同、大小不一定相等的图形相似，对应角相等、对应边成比例。", mastery=MASTERY_CONCEPT),
    node(N(3), "相似三角形的判定", 4, [N(2)], ["sim", "ch-sim"], "能用两角对应相等，或两边成比例且夹角相等，或三边成比例判定相似。", mastery=MASTERY_GATE),
    node(N(4), "相似三角形的性质", 3, [N(3)], ["sim", "ch-sim"], "能由相似得到对应角相等、对应边成比例，以及对应高的比等于相似比。"),
    node(N(5), "位似入门", 3, [N(4)], ["sim", "ch-sim"], "能说明位似是一种特殊的相似，对应点连线过位似中心。", mastery=MASTERY_CONCEPT),
    node(N(6), "相似综合", 4, [N(5)], ["sim", "ch-sim", "boss-gate"], "能在图形中找出相似三角形并求线段长。", mastery=MASTERY_GATE),
    node(N(7), "锐角的正弦", 2, [N(6)], ["trig", "ch-trig"], "能在直角三角形中把锐角的对边比斜边叫做正弦。", mastery=MASTERY_CONCEPT),
    node(N(8), "余弦与正切", 3, [N(7)], ["trig", "ch-trig"], "能说出余弦是邻边比斜边，正切是对边比邻边。", mastery=MASTERY_CONCEPT),
    node(N(9), "特殊角的三角比", 3, [N(8)], ["trig", "ch-trig"], "能熟记 30°、45°、60° 的正弦、余弦、正切。", mastery=MASTERY_GATE),
    node(N(10), "解直角三角形", 4, [N(9)], ["trig", "ch-trig"], "能在已知一边一锐角或两边时，选用三角比或勾股求其余边角。", mastery=MASTERY_GATE),
    node(N(11), "仰角俯角与坡度入门", 4, [N(10)], ["trig", "ch-trig", "boss-gate"], "能在简单测量情境中识别仰角、俯角或坡度，并列出三角比。", mastery=MASTERY_GATE),
    node(N(12), "圆的有关概念", 2, [N(1)], ["circle", "ch-circle"], "能指出圆心、半径、直径、弦、弧，并说明直径是最长的弦。", mastery=MASTERY_CONCEPT),
    node(N(13), "垂径定理", 4, [N(12)], ["circle", "ch-circle"], "能说明垂直于弦的直径平分这条弦，并且平分弦所对的弧。", mastery=MASTERY_GATE),
    node(N(14), "圆心角与圆周角", 4, [N(13)], ["circle", "ch-circle"], "能说明同弧所对圆周角等于圆心角的一半。", mastery=MASTERY_GATE),
    node(N(15), "直径所对圆周角", 3, [N(14)], ["circle", "ch-circle"], "能说明直径所对的圆周角是直角，以及直角所对的弦是直径。"),
    node(N(16), "切线", 4, [N(15)], ["circle", "ch-circle"], "能说明切线垂直于过切点的半径，并用来求角或半径。", mastery=MASTERY_GATE),
    node(N(17), "弧长与扇形面积入门", 3, [N(16)], ["circle", "ch-circle"], "能用圆心角占周角的份数求弧长和扇形面积（公式意识）。"),
    node(N(18), "圆综合", 4, [N(17)], ["circle", "ch-circle", "boss-gate"], "能综合垂径、圆周角、切线求角或线段。", mastery=MASTERY_GATE),
    node(N(19), "投影", 2, [N(12)], ["view", "ch-view"], "能区分平行投影与中心投影，指出阳光下影子近似平行投影。", mastery=MASTERY_CONCEPT),
    node(N(20), "正投影与三视图", 3, [N(19)], ["view", "ch-view"], "能根据简单组合体画出或识别主视图、左视图、俯视图。", mastery=MASTERY_GATE),
    node(N(21), "视图与展开对照", 3, [N(20)], ["view", "ch-view"], "能说明三视图看「从哪边看」，展开图看「拆开哪面」，二者互补。"),
    node(N(22), "九年级几何合练", 4, [N(11), N(18), N(21)], ["mixed", "ch-end"], "能在相似、三角比、圆、视图之间切换。", mastery=MASTERY_GATE),
    node(N(23), "九年级几何通关", 5, [N(22)], ["mixed", "ch-end", "boss-gate"], "能独立完成九年级图形与几何线的收束检查。", mastery=MASTERY_GATE),
    node(N(24), "相似比与面积比", 4, [N(4)], ["sim", "ch-sim"], "能说明相似三角形面积比等于相似比的平方（本图作认识）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(25), "正弦余弦互相余", 3, [N(9)], ["trig", "ch-trig"], "能说明互余两角的正弦与余弦互换：sin(90°-α)=cos α。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(26), "圆周角不是圆心角", 3, [N(14)], ["circle", "ch-circle"], "能纠正把圆周角当成圆心角去用「一半」的错误：必须是同弧。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "切线长定理入门", 3, [N(16)], ["circle", "ch-circle"], "能说明从圆外一点引两条切线，切线长相等（认识）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(3), "type": "related", "note": "相似比全等更松：边成比例即可，不必相等。"},
    {"from": N(7), "to": N(8), "type": "easily_confused", "note": "正弦对斜，余弦邻斜，正切对邻；分母是谁要想清楚。"},
    {"from": N(14), "to": N(15), "type": "related", "note": "直径所对弧是半圆，圆心角 180°，圆周角就是 90°。"},
    {"from": N(14), "to": N(26), "type": "easily_confused", "note": "不是同弧，就不能用「一半」。"},
    {"from": N(16), "to": N(27), "type": "related", "note": "切线垂直半径之后，两条切线长相等是常用推论。"},
    {"from": N(19), "to": N(20), "type": "application", "note": "三视图是正投影的应用。"},
    {"from": N(10), "to": N(6), "type": "application", "note": "测不到的高常常先构成直角三角形，有时也先找相似。"},
]


QUESTS = [
    q(N(1), "practice", "求线段比", "求 6 组线段比，能化简的化简。", "比的前后项单位要一致。", items=6),
    q(N(2), "explain", "相似不是全等", "对照相似与全等：哪些必须相等，哪些只需成比例。", "全等是相似比为 1 的相似。"),
    q(N(3), "practice", "判定相似", "8 题选择判定方法，缺条件则不能。", "先标对应角。", items=8),
    q(N(4), "practice", "用相似求边", "6 题求对应边。", "对应边是对应顶点的边。", items=6),
    q(N(5), "explain", "位似中心", "说明位似图形对应点连线交于一点。", "位似是带中心的相似。"),
    q(N(6), "practice", "找相似求线段", "在稍复杂图中找出一对相似三角形并求边。", "先找角再写比例。", items=4),
    q(N(6), "mini_quiz", "相似小测", "判定、性质、对应。", "对应写错比例就反。", items=8),
    q(N(6), "boss", "关主：相似测绘员", "击败关主：①说明相似与全等差别 ②用一种判定 ③求一条对应边。", "先对应，再比例。", xp=80, items=10, qid=f"{P}-boss-similar"),
    q(N(7), "practice", "写出正弦", "在直角三角形中写出指定锐角的正弦，共 6 题。", "对边 / 斜边。", items=6),
    q(N(8), "practice", "三种比", "同一角写出正弦、余弦、正切。", "先标对边邻边斜边。", items=6),
    q(N(9), "practice", "特殊角", "默写并使用 30°、45°、60° 的三角比，共 8 题。", "30° 正弦是 1/2。", items=8),
    q(N(10), "practice", "解直角三角形", "6 题选用三角比或勾股。", "已知斜边和对边就用正弦。", items=6),
    q(N(11), "practice", "仰角俯角坡度", "4 个测量情境列出三角比并求解。", "先画直角三角形，再标角。", items=4),
    q(N(11), "mini_quiz", "三角比小测", "定义、特殊角、解直角三角形。", "对边邻边不要对调。", items=8),
    q(N(11), "boss", "关主：解直角三角形向导", "击败关主：①写出一个锐角的三种比 ②用特殊角求值 ③在测量情境中求解。", "先画图再选比。", xp=80, items=10, qid=f"{P}-boss-trig"),
    q(N(12), "practice", "给圆的零件起名", "在图中指出半径、直径、弦、弧。", "直径过圆心，弦不必。", items=6),
    q(N(13), "practice", "用垂径求长度", "4 题用垂径定理求弦长或距圆心距离。", "垂直于弦的直径平分弦。", items=4),
    q(N(14), "practice", "圆心角圆周角", "6 题求同弧所对的圆周角或圆心角。", "圆周角是圆心角的一半。", items=6),
    q(N(15), "practice", "直径与直角", "4 题判断或求直角、直径。", "直径所对圆周角是直角。", items=4),
    q(N(16), "practice", "切线求角", "4 题用切线垂直半径。", "切点处半径与切线垂直。", items=4),
    q(N(17), "practice", "弧长扇形意识", "3 题按圆心角占周角的份数求弧长或扇形面积。", "先看圆心角是周角的几分之几。", items=3),
    q(N(18), "practice", "圆闯关", "混合垂径、圆周角、切线。", "先标已知半径、切线、直径。", items=6),
    q(N(18), "mini_quiz", "圆小测", "概念、垂径、圆周角、切线。", "同弧才能用一半。", items=8),
    q(N(19), "explain", "两种投影", "对照平行投影与中心投影，各举一例。", "阳光下的影子常常当作平行投影。"),
    q(N(20), "practice", "三视图配对", "组合体与三视图配对或补画一个视图，共 6 题。", "长对正、高平齐、宽相等。", items=6),
    q(N(21), "explain", "视图还是展开", "说明什么时候画三视图、什么时候画展开图。", "看外形用视图，算表面用展开。"),
    q(N(22), "practice", "合练卷", "相似求边、解直角三角形、圆中求角、读三视图。", "先辨图形类型。", items=8),
    q(N(23), "practice", "通关综合练", "四块各一题并写理由。", "对应、对边邻边、同弧、从哪边看。", items=10),
    q(N(23), "boss", "关主：九年级几何通关试炼", "最终关主：①相似求边 ②解一个直角三角形 ③圆中求角或用切线 ④认三视图。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(24), "explain", "面积比是平方", "说明相似比为 2 时面积比为 4，并举网格示意。", "边是一次，面积是二次。"),
    q(N(25), "practice", "互余两角", "写出 sin 30° 与 cos 60° 等对照，共 4 题。", "互余则正弦余弦互换。", items=4),
    q(N(26), "explain", "必须同弧", "画一个不同弧的圆周角与圆心角，说明不能用一半。", "先找它们对着的是不是同一段弧。"),
    q(N(27), "explain", "两条切线一样长", "从圆外一点画两条切线，说明切线长相等。", "两个直角三角形全等可以解释。"),
]


META = {
    "id": MAP_ID,
    "title": "九年级 · 图形与几何",
    "subject": "数学",
    "stage": "初中",
    "grade": 9,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "相似（关主 1）→ 锐角三角函数（关主 2）；圆从比例线段后并行；投影视图从圆概念后并行。面积比、互余、同弧警示、切线长（n024–n027）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-similar", f"{P}-boss-trig", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：相似测绘员、解直角三角形向导、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中九年级「图形与几何」地图：相似、锐角三角函数、圆、投影与视图。独立通关。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress(MAP_ID, N(1), f"{N(1)}-practice", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
