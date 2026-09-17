"""Build senior-math 立体几何初步 map.

Run: python3 scripts/_build_sm_solid_geometry.py

Pedagogical spine: 空间几何体与三视图 → 点线面位置关系 → 平行垂直判定与性质 → 简单度量。
长方体中的异面直线、作图误差、三垂线直觉为软锁。空间向量在选必，本图不做。
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

OUT = ROOT / "maps" / "senior-math" / "solid-geometry"
G = 10
STRAND = "图形与几何"
P = "sm-solid"
MAP_ID = "sm-solid-geometry"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "空间几何体直观", 1, [], ["solid", "ch-body"], "能从实物抽象出柱、锥、台、球，并说明立体几何研究的是理想化的空间图形。", mastery=MASTERY_CONCEPT),
    node(N(2), "棱柱与棱锥", 2, [N(1)], ["solid", "ch-body"], "能指出棱柱、棱锥的底面、侧面、顶点，并比较侧棱是否垂直底面。", mastery=MASTERY_CONCEPT),
    node(N(3), "棱台", 2, [N(2)], ["solid", "ch-body"], "能说明棱台由棱锥被平行于底面的平面所截得到，上下底平行。"),
    node(N(4), "圆柱圆锥球", 2, [N(1)], ["solid", "ch-body"], "能指出圆柱、圆锥、球的母线、轴、半径，并与棱柱棱锥对照。", mastery=MASTERY_CONCEPT),
    node(N(5), "简单组合体", 3, [N(2), N(4)], ["solid", "ch-body"], "能把组合体拆成已知几何体，说明交界处如何衔接。"),
    node(N(6), "三视图", 3, [N(5)], ["solid", "ch-view"], "能由几何体画出正视图、侧视图、俯视图，并说明长对正、高平齐、宽相等。", mastery=MASTERY_GATE),
    node(N(7), "直观图", 3, [N(5)], ["solid", "ch-view"], "能用斜二测画水平面的直观图：横轴不变，纵轴 45° 且长度为原来一半。"),
    node(N(8), "表面积回顾", 3, [N(5)], ["solid", "ch-body"], "能求棱柱、圆柱等的表面积：把侧面展开再加底。"),
    node(N(9), "体积回顾", 3, [N(8)], ["solid", "ch-body", "boss-gate"], "能使用柱体 V=Sh、锥体 V=(1/3)Sh、球体公式求简单体积，组合体用加减。", mastery=MASTERY_GATE),
    node(N(10), "空间点线面", 2, [N(1)], ["pos", "ch-pos"], "能说明点、直线、平面是立体几何的基本元素，平面可无限延展。", mastery=MASTERY_CONCEPT),
    node(N(11), "平面的基本性质", 3, [N(10)], ["pos", "ch-pos"], "能使用公理：不共线三点确定平面；直线上两点在平面内则直线在平面内等。", mastery=MASTERY_CONCEPT),
    node(N(12), "空间两直线", 3, [N(11)], ["pos", "ch-pos"], "能区分相交、平行、异面三种位置，并说明异面既不相交也不平行。", mastery=MASTERY_GATE),
    node(N(13), "直线与平面平行", 3, [N(12)], ["pos", "ch-par"], "能叙述线面平行的判定（直线平行于面内一条直线）与性质。", mastery=MASTERY_CONCEPT),
    node(N(14), "平面与平面平行", 3, [N(13)], ["pos", "ch-par"], "能用「一个平面内两条相交直线都平行于另一平面」判定面面平行。", mastery=MASTERY_GATE),
    node(N(15), "直线与平面垂直", 4, [N(12)], ["pos", "ch-perp"], "能用「垂直于面内两条相交直线」判定线面垂直，并说明过一点垂线唯一。", mastery=MASTERY_GATE),
    node(N(16), "平面与平面垂直", 4, [N(15)], ["pos", "ch-perp"], "能用「一个平面过另一平面的垂线」判定面面垂直。", mastery=MASTERY_GATE),
    node(N(17), "判定与性质对照", 4, [N(14), N(16)], ["pos", "ch-pos", "boss-gate"], "能在平行、垂直两类问题里先选判定还是性质，并写出简短推理。", mastery=MASTERY_GATE),
    node(N(18), "线面角", 3, [N(15)], ["metric", "ch-met"], "能说明直线与平面所成角是直线和它在平面上的射影所成的角。", mastery=MASTERY_CONCEPT),
    node(N(19), "二面角直觉", 3, [N(16)], ["metric", "ch-met"], "能指出二面角的平面角：棱的垂面与两个半平面的交线所成的角。"),
    node(N(20), "点到平面距离", 3, [N(15)], ["metric", "ch-met"], "能说明点到平面距离是垂线段长，并在长方体中求出简单距离。"),
    node(N(21), "空间角与距离综合", 4, [N(18), N(19), N(20)], ["metric", "ch-met"], "能在长方体或正方体中指出所求的是哪种角或距离，再计算。", mastery=MASTERY_GATE),
    node(N(22), "立体几何合练", 4, [N(9), N(17), N(21)], ["mixed", "ch-end"], "能在几何体视图、位置关系、简单度量之间切换。", mastery=MASTERY_GATE),
    node(N(23), "立体几何通关", 5, [N(22)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(24), "长方体中的异面直线", 3, [N(12)], ["pos", "ch-pos"], "能在长方体中找出异面的棱，并说明怎样证明它们不共面。", unlock=SOFT),
    node(N(25), "三垂线定理直觉", 4, [N(18)], ["metric", "ch-met"], "能用「平面的垂线、斜线、射影」关系判断何时一条线垂直于面内直线。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(26), "展开图与作图误差", 3, [N(6)], ["solid", "ch-view"], "能说明三视图或展开图尺寸画不准时，还原几何体可能有多种理解。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "球的截面", 3, [N(4)], ["solid", "ch-body"], "能说明平面截球得圆，截面离球心越远圆越小。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "体积割补", 3, [N(9)], ["solid", "ch-body"], "能把不规则组合体补成柱或拆成锥再求体积。", unlock=SOFT),
    node(N(29), "平行垂直口诀陷阱", 3, [N(17)], ["pos", "ch-pos"], "能列出「线线、线面、面面」平行垂直的传递，指出哪一步不能想当然。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(6), "to": N(7), "type": "related", "note": "三视图是正投影，直观图是斜二测，用途不同。"},
    {"from": N(13), "to": N(14), "type": "related", "note": "线面平行是面面平行的踏板。"},
    {"from": N(15), "to": N(16), "type": "related", "note": "线面垂直是面面垂直的踏板。"},
    {"from": N(12), "to": N(24), "type": "application", "note": "异面定义清楚后，到长方体里找例子。"},
    {"from": N(15), "to": N(18), "type": "easily_confused", "note": "线面垂直是所成角为 90° 的特殊情形；一般线面角在 0° 到 90°。"},
    {"from": N(18), "to": N(19), "type": "easily_confused", "note": "线面角用射影；二面角用平面角。不要把棱当成线面角的边。"},
    {"from": N(9), "to": N(28), "type": "application", "note": "会公式之后才谈割补。"},
]


QUESTS = [
    q(N(1), "explain", "从实物到几何体", "指出教室里三种可以看成柱、锥或球的物体，并说明忽略了什么细节。", "几何体是模型。"),
    q(N(2), "practice", "标出名称", "在棱柱、棱锥图上标底面、侧棱、顶点，共 4 图。", "棱锥有一个公共顶点。", items=4),
    q(N(3), "explain", "台是怎样截出来的", "用一句话说明棱台和棱锥的关系。", "平行于底面去一截。"),
    q(N(4), "practice", "旋转体辨认", "6 个物体或图判断更接近柱、锥还是球。", "看母线是否平行或交于一点。", items=6),
    q(N(5), "practice", "拆组合体", "把 3 个组合体拆成已知几何体并命名。", "先找明显的柱或锥。", items=3),
    q(N(6), "practice", "画三视图", "为 2 个简单几何体画三视图，检查长对正高平齐宽相等。", "三个图要能对上尺寸。", items=2),
    q(N(7), "practice", "画水平面直观图", "把一个水平矩形画成斜二测。", "横不变，另一方向 45° 且减半。", items=1),
    q(N(8), "practice", "求表面积", "4 个柱或简单组合求表面积。", "展开侧面，别漏底。", items=4),
    q(N(9), "practice", "求体积", "4 个柱锥球或组合求体积。", "锥体记得三分之一。", items=4),
    q(N(9), "mini_quiz", "几何体小测", "三视图、表面积、体积。夹一道把锥当柱。", "先辨柱还是锥。", items=8),
    q(N(9), "boss", "关主：几何体还原师", "击败关主：①由三视图想象几何体 ②求一个表面积或体积 ③指出组合体怎么拆。", "视图和公式都要会。", xp=80, items=10, qid=f"{P}-boss-body"),
    q(N(10), "explain", "平面能延展", "说明为什么画出来的平行四边形只是平面的一部分。", "平面没有边界。"),
    q(N(11), "practice", "用公理判断", "6 个「能否确定平面 / 直线是否在面内」判断。", "不共线三点才能确定平面。", items=6),
    q(N(12), "practice", "三分类", "8 对直线判断相交、平行、异面（可在正方体中）。", "异面既不交也不平行。", items=8),
    q(N(13), "practice", "线面平行", "4 道判定或性质：指出用了哪一条。", "面内要有一条直线与它平行。", items=4),
    q(N(14), "practice", "面面平行", "4 道判定：写出面内那两条相交直线。", "两条必须相交。", items=4),
    q(N(15), "practice", "线面垂直", "4 道判定：写出面内两条相交直线。", "两条都要与已知直线垂直。", items=4),
    q(N(16), "practice", "面面垂直", "4 道：找出一个平面里的垂线。", "垂线要落在其中一个面内。", items=4),
    q(N(17), "practice", "先选判定还是性质", "6 道短推理，每步标注判定或性质。", "要证平行垂直先找判定；已知平行垂直才能用性质。", items=6),
    q(N(17), "mini_quiz", "位置关系小测", "异面、线面平行垂直、面面平行垂直。夹一道把异面当平行。", "先问是否共面。", items=8),
    q(N(17), "boss", "关主：空间位置裁判", "击败关主：①区分三线关系 ②线面或面面平行 ③线面或面面垂直。", "判定条件要写全。", xp=80, items=12, qid=f"{P}-boss-pos"),
    q(N(18), "explain", "射影在哪里", "在长方体中指出一条体对角线在底面上的射影，并说出线面角。", "垂足连出来才是射影。"),
    q(N(19), "practice", "指出二面角的平面角", "在 3 个图中标出棱和平面角。", "平面角的两边分别在两个半平面内且垂直于棱。", items=3),
    q(N(20), "practice", "点面距离", "在长方体中求 4 个点到指定面的距离。", "往往就是一条棱长。", items=4),
    q(N(21), "practice", "这是哪种量", "6 题先判断求角还是距离，再在长方体中计算简单情形。", "先命名，再动尺子。", items=6),
    q(N(22), "practice", "合练卷", "三视图或体积、位置关系、简单距离各几题。", "先看问的是体、关系还是度量。", items=12),
    q(N(23), "practice", "通关综合练", "独立完成：一个视图或体积、一段平行或垂直推理、一个距离。", "语言要规范：因为所以。", items=10),
    q(N(23), "boss", "关主：立体几何通关试炼", "最终关主：①几何体或三视图 ②一段位置关系推理 ③一个简单角或距离。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(24), "practice", "找出异面棱", "在长方体中找出至少 4 对异面棱。", "既不交于一点，也不平行。", items=4),
    q(N(25), "explain", "斜线的射影", "用自己的话说明：斜线垂直于面内一条直线时，它的射影也往往垂直于那条直线。", "先有面的垂线，再谈斜线。"),
    q(N(26), "explain", "图画歪了会怎样", "举一个三视图尺寸含糊导致两种还原的例子。", "缺尺寸就不能唯一确定。"),
    q(N(27), "practice", "截面圆半径", "已知球半径和截面到球心距离，求 3 个截面圆半径。", "直角三角形：半径、距离、截面半径。", items=3),
    q(N(28), "practice", "割或补", "2 个组合体选择割还是补并求体积。", "缺一块就补，多一块就减。", items=2),
    q(N(29), "explain", "哪一步不能传", "指出「两条直线都垂直于第三条，它们就平行」在空间中为什么不一定。", "空间里可以是异面或相交。"),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 立体几何初步",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "立体几何初步",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "空间几何体与三视图（关主 1）→ 点线面平行垂直（关主 2）→ 简单度量后收束。异面棱（n024）、三垂线直觉（n025）、作图误差（n026）、球截面（n027）、割补（n028）、传递陷阱（n029）为软锁。空间向量不在本图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-body", f"{P}-boss-pos", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：几何体还原师、空间位置裁判、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中必修「立体几何初步」地图：几何体与视图 → 位置关系 → 简单度量。独立通关。grade=10。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress(MAP_ID, N(1), f"{N(1)}-explain", N(2), N(4), f"{N(4)}-practice"),
    )


if __name__ == "__main__":
    main()
