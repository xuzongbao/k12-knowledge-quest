"""Build Grade 7 Geometry map JSON (七年级 · 图形与几何).

Run: python3 scripts/_build_jm_g7_geometry.py

Pedagogical spine: 几何语言 → 相交线与平行线 → 三角形初步 → 生活中的立体图形。
余角补角辨认、尺规作垂线欣赏为软锁。本图自洽。
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

OUT = ROOT / "maps" / "junior-math" / "grade-7-geometry"
G = 7
STRAND = "图形与几何"
P = "jm-g7-geo"
MAP_ID = "jm-g7-geometry"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "点、线、面、体", 1, [], ["lang", "ch-lang"], "能从身边物体指出点、线、面、体，并说明几何里把它们当作理想化的模型。", mastery=MASTERY_CONCEPT),
    node(N(2), "直线、射线、线段", 2, [N(1)], ["lang", "ch-lang"], "能区分直线、射线、线段：两端是否延伸、如何用字母表示。", mastery=MASTERY_CONCEPT),
    node(N(3), "两点确定一条直线", 2, [N(2)], ["lang", "ch-lang"], "能说明两点确定一条直线，两点之间线段最短。"),
    node(N(4), "角及其表示", 2, [N(3)], ["lang", "ch-lang"], "能用三个字母或数字表示一个角，指出顶点和边。", mastery=MASTERY_CONCEPT),
    node(N(5), "几何语句与图形互译", 3, [N(4)], ["lang", "ch-lang"], "能把「点在直线上」「两直线相交」等语句画成图，也能看图写成语句。", mastery=MASTERY_GATE),
    node(N(6), "相交线与对顶角", 3, [N(5)], ["parallel", "ch-parallel"], "能指出两直线相交形成的对顶角，说明对顶角相等。", mastery=MASTERY_CONCEPT),
    node(N(7), "邻补角", 3, [N(6)], ["parallel", "ch-parallel"], "能指出邻补角：有公共顶点、一条公共边，另一边互为反向延长线，和为 180°。"),
    node(N(8), "垂线", 3, [N(7)], ["parallel", "ch-parallel"], "能说明两条直线互相垂直，过一点有且只有一条直线与已知直线垂直。", mastery=MASTERY_CONCEPT),
    node(N(9), "点到直线的距离", 3, [N(8)], ["parallel", "ch-parallel"], "能说明点到直线的距离是垂线段的长度。"),
    node(N(10), "平行线", 2, [N(8)], ["parallel", "ch-parallel"], "能说明在同一平面内不相交的两条直线叫做平行线，过直线外一点有且只有一条平行线。", mastery=MASTERY_CONCEPT),
    node(N(11), "三线八角", 3, [N(10), N(6)], ["parallel", "ch-parallel"], "能在「两条直线被第三条直线所截」的图中指出同位角、内错角、同旁内角。", mastery=MASTERY_GATE),
    node(N(12), "平行线的判定", 4, [N(11)], ["parallel", "ch-parallel"], "能用同位角相等、内错角相等、同旁内角互补判定两直线平行。", mastery=MASTERY_GATE),
    node(N(13), "平行线的性质", 4, [N(12)], ["parallel", "ch-parallel"], "能由两直线平行推出同位角相等、内错角相等、同旁内角互补。", mastery=MASTERY_GATE),
    node(N(14), "平行线综合", 4, [N(13)], ["parallel", "ch-parallel", "boss-gate"], "能在稍复杂的图形里选用判定或性质，说明哪一步用了哪条理由。", mastery=MASTERY_GATE),
    node(N(15), "三角形的边", 2, [N(5)], ["tri", "ch-tri"], "能指出三角形三边，说明任意两边之和大于第三边。", mastery=MASTERY_CONCEPT),
    node(N(16), "三角形内角和", 3, [N(15), N(13)], ["tri", "ch-tri"], "能说明三角形内角和是 180°，并用来求未知角。", mastery=MASTERY_GATE),
    node(N(17), "高、中线、角平分线", 3, [N(16)], ["tri", "ch-tri"], "能画出三角形的高、中线、角平分线，并说明它们的定义。"),
    node(N(18), "等腰三角形", 3, [N(17)], ["tri", "ch-tri"], "能说出等腰三角形两底角相等，顶角平分线、底边上的中线、高互相重合。", mastery=MASTERY_CONCEPT),
    node(N(19), "等边三角形", 3, [N(18)], ["tri", "ch-tri"], "能说明等边三角形是特殊的等腰三角形，三个角都是 60°。"),
    node(N(20), "直角三角形初步", 3, [N(16)], ["tri", "ch-tri"], "能指出直角、直角边、斜边，并说明两锐角互余。", mastery=MASTERY_CONCEPT),
    node(N(21), "三角形综合", 4, [N(19), N(20)], ["tri", "ch-tri", "boss-gate"], "能综合边的关系、内角和、等腰与直角，求边或角并写出理由。", mastery=MASTERY_GATE),
    node(N(22), "从不同方向看", 2, [N(1)], ["solid", "ch-solid"], "能根据从正面、左面、上面看到的形状，想象简单组合体。", mastery=MASTERY_CONCEPT),
    node(N(23), "立体图形的展开图", 3, [N(22)], ["solid", "ch-solid"], "能判断哪些平面图形可以折成正方体或长方体，哪些不能。"),
    node(N(24), "棱柱的直观认识", 3, [N(23)], ["solid", "ch-solid"], "能指出棱柱的底面、侧面、棱，并与椎体、球体直观区分。", mastery=MASTERY_CONCEPT),
    node(N(25), "生活中的立体分类", 3, [N(24)], ["solid", "ch-solid"], "能给包装盒、罐、球等分类，并说明为什么有的要画展开图、有的看三视图。"),
    node(N(26), "几何语言收束", 3, [N(14), N(21)], ["lang", "ch-end"], "能用规范语句写出「因为…所以…」的短推理，每步对应图形。", mastery=MASTERY_CONCEPT),
    node(N(27), "七年级几何合练", 4, [N(26), N(25)], ["mixed", "ch-end"], "能在平行线、三角形、立体直观之间切换，不混用名称。", mastery=MASTERY_GATE),
    node(N(28), "七年级几何通关", 5, [N(27)], ["mixed", "ch-end", "boss-gate"], "能独立完成七年级图形与几何线的收束检查。", mastery=MASTERY_GATE),
    node(N(29), "余角与补角", 3, [N(7)], ["parallel", "ch-parallel"], "能区分互余（和 90°）与互补（和 180°），并与邻补角对照：邻补角一定互补，互补不一定相邻。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(30), "作一条垂线", 3, [N(8)], ["parallel", "ch-parallel"], "能用三角尺或尺规从直线上（或外）一点作已知直线的垂线，并说明「唯一」。", unlock=SOFT),
    node(N(31), "平移与平行", 3, [N(10)], ["parallel", "ch-parallel"], "能说明把一条直线平移后与原直线平行，生活中的滑轨、栅栏可以这样看。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(32), "三角形分类总表", 3, [N(21)], ["tri", "ch-tri"], "能按边（不等边、等腰、等边）和按角（锐角、直角、钝角）给三角形分类，并指出交叉。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(6), "to": N(7), "type": "easily_confused", "note": "对顶角相等；邻补角互补。位置不同，结论也不同。"},
    {"from": N(7), "to": N(29), "type": "easily_confused", "note": "邻补角是位置关系，互补是数量关系。"},
    {"from": N(12), "to": N(13), "type": "easily_confused", "note": "判定是「由角推平行」；性质是「由平行推角」。方向不能反着用而不说明。"},
    {"from": N(11), "to": N(12), "type": "related", "note": "先认清同位、内错、同旁内，再谈判定。"},
    {"from": N(18), "to": N(19), "type": "related", "note": "等边是等腰的特殊情形，三边都相等。"},
    {"from": N(20), "to": N(16), "type": "application", "note": "直角三角形两锐角互余，来自内角和 180°。"},
    {"from": N(22), "to": N(23), "type": "related", "note": "三视图看「从哪边看」；展开图看「拆开哪面」。"},
    {"from": N(8), "to": N(30), "type": "application", "note": "理解垂直之后，动手作出垂线。"},
]


QUESTS = [
    q(N(1), "explain", "从物体到模型", "指着教室里的一样东西，说出哪是当作点、哪是当作面、哪是当作体。", "几何图形是抽象出来的，可以忽略厚度或大小。"),
    q(N(2), "practice", "三种线怎么表示", "画出直线、射线、线段，并用字母标注，说明它们的端点个数。", "直线没有端点，射线一个，线段两个。", items=3),
    q(N(3), "explain", "两点一线", "说明为什么过两点只能画一条直线，过一点可以画无数条。", "两点把方向完全定死。"),
    q(N(4), "practice", "读角写角", "用三种方式表示图中的角，避免只写顶点导致分不清。", "三个字母时顶点写在中间。", items=6),
    q(N(5), "practice", "语句与图形互译", "把 6 句几何话画成图，再把 4 张图写成语句。", "相交、平行、在……上，用词要准。", items=10),
    q(N(6), "practice", "找出对顶角", "在相交线图中标出对顶角，并填写相等关系。", "对顶角面对面，不相邻。", items=6),
    q(N(7), "practice", "找出邻补角", "标出邻补角并计算未知角。", "邻补角拼起来是一条直线。", items=6),
    q(N(8), "explain", "什么叫垂直", "用自己的话定义互相垂直，并说明过一点作垂线为什么是唯一的。", "夹角是直角。"),
    q(N(9), "practice", "量点到直线距离", "在图上作出垂线段，读出点到直线的距离（可用格点）。", "斜着连过去不是距离。", items=4),
    q(N(10), "explain", "平行是不相交", "说明同一平面内不相交才叫平行，并解释「过直线外一点只有一条平行线」。", "先强调在同一平面内。"),
    q(N(11), "practice", "给八角起名", "在标准「三线八角」图中指出指定的同位角、内错角、同旁内角。", "先看哪两条被截，再看角的位置。", items=8),
    q(N(12), "practice", "判定两直线平行", "给出角的条件，判断能否判定平行，并写理由。", "同位角相等就可以判定。", items=6),
    q(N(13), "practice", "由平行推角", "已知平行，求图中未知角，每步写下用了哪条性质。", "平行 → 同位角相等，是性质不是判定。", items=6),
    q(N(14), "practice", "判定还是性质", "混合题：有的要证平行，有的已知平行求角。", "先问：现在已经知道平行了吗？", items=8),
    q(N(14), "mini_quiz", "平行线小测", "认八角、判定、性质、对顶角邻补角混用。", "先标已知，再选定理。", items=10),
    q(N(14), "boss", "关主：平行线调度员", "击败关主：①认出同位角内错角 ②用判定说明平行 ③用性质求角并写理由。", "判定和性质方向相反。", xp=80, items=12, qid=f"{P}-boss-parallel"),
    q(N(15), "practice", "三边能不能围成", "判断 8 组三边能否围成三角形。", "任意两边之和大于第三边，差小于第三边。", items=8),
    q(N(16), "practice", "求未知角", "用内角和求 8 个三角形中的未知角。", "三个角加起来是 180°。", items=8),
    q(N(17), "practice", "画三条重要线", "在锐角三角形中画出一条高、一条中线、一条角平分线并标注。", "高要垂直；中线平分对边；角平分线平分角。", items=3),
    q(N(18), "practice", "等腰里求角求边", "已知等腰的底角或顶角、腰或底，求其余。", "两底角相等；三线合一可在需要时用。", items=6),
    q(N(19), "practice", "等边三角形", "求等边三角形中与 60° 有关的角，并说明它为什么也是等腰。", "三个角都是 60°。", items=4),
    q(N(20), "practice", "直角三角形求锐角", "已知一个锐角求另一个，说明互余。", "两个锐角加起来是 90°。", items=6),
    q(N(21), "practice", "三角形闯关", "混合：三边关系、内角和、等腰、直角。", "先分类：这是什么三角形？", items=8),
    q(N(21), "mini_quiz", "三角形小测", "夹一道「两边之和等于第三边」的陷阱。", "等于就退化成线段，围不成。", items=10),
    q(N(21), "boss", "关主：三角形鉴定官", "击败关主：①判断能否围成 ②求角 ③在等腰或直角中写清所用性质。", "边的不等关系和角的 180° 是两条底线。", xp=80, items=12, qid=f"{P}-boss-triangle"),
    q(N(22), "practice", "三视图配对", "把简单组合体与三视图配对。", "先约定从哪一面看是正面。", items=6),
    q(N(23), "practice", "哪些能折成正方体", "判断 8 个平面图能否折成正方体。", "相对的面折起来不能重叠错位。", items=8),
    q(N(24), "explain", "棱柱长什么样", "对照棱柱、圆柱、圆锥、球，指出棱柱的底面是多边形。", "棱柱两个底面平行且全等。"),
    q(N(25), "explain", "给生活物品分类", "列出五种生活物品，说明更适合用展开图还是三视图来描述。", "包装盒常用展开图；堆叠积木常用三视图。"),
    q(N(26), "practice", "写两步推理", "根据平行线或三角形，写两句「因为…所以…」。", "每句只推一步。", items=4),
    q(N(27), "practice", "合练卷", "平行线求角、三角形求边角、读一个展开图。", "先看图再选题型。", items=10),
    q(N(28), "practice", "通关综合练", "几何语言互译、平行线理由、三角形计算、立体直观各一题。", "名称和理由都要写出来。", items=10),
    q(N(28), "boss", "关主：七年级几何通关试炼", "最终关主：①语句与图形互译 ②平行线判定或性质 ③三角形求角 ④认一个展开图或三视图。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(29), "explain", "余角补角邻补角", "用韦恩图或对照表区分这三对词。", "邻补角一定互补；互补的两个角不一定相邻。"),
    q(N(30), "practice", "作出垂线", "过直线上一点和直线外一点各作一条垂线。", "三角尺的直角靠在已知直线上。", items=2),
    q(N(31), "explain", "平移后平行", "用栅栏或笔记本横线说明平移不改变方向，因而平行。", "方向不变就是互相平行。"),
    q(N(32), "explain", "两套分类", "画一个表：按边分类、按角分类，并指出等腰直角可以同时属于两套。", "分类标准不同，同一三角形可以有两个名字。"),
]


META = {
    "id": MAP_ID,
    "title": "七年级 · 图形与几何",
    "subject": "数学",
    "stage": "初中",
    "grade": 7,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "几何语言 → 相交线平行线（关主 1）；三角形可从几何语言并行，在内角和处用到平行线性质（关主 2）；立体直观从起点并行。余角补角（n029）、作垂线（n030）、平移与平行（n031）、分类总表（n032）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-parallel", f"{P}-boss-triangle", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：平行线调度员、三角形鉴定官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中七年级「图形与几何」地图：几何语言、相交线平行线、三角形初步、生活中的立体图形。独立通关。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress(MAP_ID, N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-explain"),
    )


if __name__ == "__main__":
    main()
