"""Build Grade 8 Geometry map JSON (八年级 · 图形与几何).

Run: python3 scripts/_build_jm_g8_geometry.py

Pedagogical spine: 全等三角形 → 轴对称 → 勾股定理 → 平行四边形。
SSA 不能判定为软锁警示。本图自洽。
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

OUT = ROOT / "maps" / "junior-math" / "grade-8-geometry"
G = 8
STRAND = "图形与几何"
P = "jm-g8-geo"
MAP_ID = "jm-g8-geometry"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "全等形的意义", 1, [], ["cong", "ch-cong"], "能说明能够完全重合的两个图形全等，对应边相等、对应角相等。", mastery=MASTERY_CONCEPT),
    node(N(2), "全等三角形的对应", 2, [N(1)], ["cong", "ch-cong"], "能根据顶点对应顺序写出对应边、对应角，避免「看起来像」就乱对应。"),
    node(N(3), "SSS 判定", 3, [N(2)], ["cong", "ch-cong"], "能用三边对应相等判定两个三角形全等。", mastery=MASTERY_CONCEPT),
    node(N(4), "SAS 判定", 3, [N(2)], ["cong", "ch-cong"], "能用两边及其夹角对应相等判定全等。", mastery=MASTERY_CONCEPT),
    node(N(5), "ASA 与 AAS 判定", 3, [N(2)], ["cong", "ch-cong"], "能用两角及其夹边，或两角及一角的对边，判定全等。", mastery=MASTERY_CONCEPT),
    node(N(6), "HL 判定", 3, [N(5)], ["cong", "ch-cong"], "能在直角三角形中用斜边和一条直角边对应相等判定全等。"),
    node(N(7), "选择判定方法", 4, [N(3), N(4), N(6)], ["cong", "ch-cong"], "能根据已知条件选择 SSS、SAS、ASA、AAS 或 HL，并写出对应。", mastery=MASTERY_GATE),
    node(N(8), "全等的简单应用", 4, [N(7)], ["cong", "ch-cong", "boss-gate"], "能先证全等再得对应边或对应角，解决求线段或求角。", mastery=MASTERY_GATE),
    node(N(9), "轴对称图形", 2, [N(1)], ["sym", "ch-sym"], "能识别轴对称图形并找出对称轴，说明对应点到对称轴距离相等。", mastery=MASTERY_CONCEPT),
    node(N(10), "轴对称变换", 3, [N(9)], ["sym", "ch-sym"], "能作出一个简单图形关于给定直线的对称图形。"),
    node(N(11), "等腰三角形的轴对称", 3, [N(10), N(8)], ["sym", "ch-sym"], "能用轴对称理解等腰三角形三线合一，并用来求角。", mastery=MASTERY_GATE),
    node(N(12), "最短路径问题入门", 4, [N(11)], ["sym", "ch-sym"], "能用轴对称把「到直线再折返」的路径变成两点连线。"),
    node(N(13), "轴对称综合", 4, [N(12)], ["sym", "ch-sym"], "能在全等与轴对称之间切换：对称可以产生全等。", mastery=MASTERY_CONCEPT),
    node(N(14), "勾股定理", 3, [N(8)], ["pyth", "ch-pyth"], "能说明直角三角形两直角边的平方和等于斜边的平方，并用来求边。", mastery=MASTERY_GATE),
    node(N(15), "勾股定理的逆定理", 3, [N(14)], ["pyth", "ch-pyth"], "能用三边数量关系判定一个三角形是不是直角三角形。", mastery=MASTERY_CONCEPT),
    node(N(16), "勾股定理应用", 4, [N(15)], ["pyth", "ch-pyth", "boss-gate"], "能在长方形对角线、梯子、坐标格点等情境中用勾股求距离。", mastery=MASTERY_GATE),
    node(N(17), "平行四边形的定义", 2, [N(8)], ["para", "ch-para"], "能说明两组对边分别平行的四边形是平行四边形。", mastery=MASTERY_CONCEPT),
    node(N(18), "平行四边形的性质", 3, [N(17)], ["para", "ch-para"], "能推出对边相等、对角相等、对角线互相平分。", mastery=MASTERY_GATE),
    node(N(19), "平行四边形的判定", 4, [N(18)], ["para", "ch-para"], "能用对边平行且相等、对角线互相平分等条件判定平行四边形。", mastery=MASTERY_GATE),
    node(N(20), "矩形", 3, [N(19)], ["para", "ch-para"], "能说明矩形是有一个直角的平行四边形，对角线相等。", mastery=MASTERY_CONCEPT),
    node(N(21), "菱形", 3, [N(19)], ["para", "ch-para"], "能说明菱形是一组邻边相等的平行四边形，对角线互相垂直。", mastery=MASTERY_CONCEPT),
    node(N(22), "正方形", 3, [N(20), N(21)], ["para", "ch-para"], "能说明正方形既是矩形又是菱形，兼有两者性质。"),
    node(N(23), "特殊平行四边形综合", 4, [N(22)], ["para", "ch-para", "boss-gate"], "能在矩形、菱形、正方形之间选用性质求边、角、对角线。", mastery=MASTERY_GATE),
    node(N(24), "八年级几何合练", 4, [N(16), N(23), N(13)], ["mixed", "ch-end"], "能综合全等、轴对称、勾股、平行四边形写短推理。", mastery=MASTERY_GATE),
    node(N(25), "八年级几何通关", 5, [N(24)], ["mixed", "ch-end", "boss-gate"], "能独立完成八年级图形与几何线的收束检查。", mastery=MASTERY_GATE),
    node(N(26), "SSA 不能判定", 3, [N(7)], ["cong", "ch-cong"], "能举出两边及其中一边的对角对应相等但三角形不一定全等的示意，从而记住 SSA 不是判定定理。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "等腰中的隐藏条件", 3, [N(11)], ["sym", "ch-sym"], "能在「看起来没写全等」的图里找出等腰带来的等边等角。", unlock=SOFT),
    node(N(28), "梯形的中位线入门", 3, [N(18)], ["para", "ch-para"], "能说明梯形中位线平行于两底并且等于两底和的一半（本图只作认识，不挡主线）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(29), "网格上的勾股", 3, [N(16)], ["pyth", "ch-pyth"], "能在方格纸上数直角边格数，用勾股求斜线段长。", unlock=SOFT),
    node(N(30), "对角线互相垂直平分", 3, [N(21)], ["para", "ch-para"], "能对照：互相平分是平行四边形，再垂直则到菱形，再等长则到矩形。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(4), "to": N(26), "type": "easily_confused", "note": "SAS 的角必须是两边的夹角；SSA 把角放在一边对面，不能判定。"},
    {"from": N(3), "to": N(5), "type": "related", "note": "边的条件和角的条件可以搭配，但要配对正确。"},
    {"from": N(9), "to": N(1), "type": "related", "note": "轴对称可以产生全等的两个图形。"},
    {"from": N(14), "to": N(15), "type": "easily_confused", "note": "定理由直角推边；逆定理由边推直角。方向不同。"},
    {"from": N(18), "to": N(19), "type": "easily_confused", "note": "性质由平行四边形推边角；判定由边角推它是平行四边形。"},
    {"from": N(20), "to": N(21), "type": "related", "note": "矩形管角，菱形管边，正方形两边都管。"},
    {"from": N(14), "to": N(20), "type": "application", "note": "矩形对角线可用勾股求。"},
]


QUESTS = [
    q(N(1), "explain", "什么叫完全重合", "用纸片或想象说明全等：对应边、对应角分别相等。", "全等比「形状相同」要求更严：大小也要一样。"),
    q(N(2), "practice", "写出对应", "根据顶点对应顺序写出对应边和对应角，共 6 题。", "对应顶点的顺序决定对应。", items=6),
    q(N(3), "practice", "用 SSS", "判断能否用 SSS 判定，并写出对应边。", "三边都要对应相等。", items=4),
    q(N(4), "practice", "用 SAS", "判断角是不是两边的夹角。", "夹角夹在两边中间。", items=4),
    q(N(5), "practice", "用 ASA 或 AAS", "6 题选择 ASA 还是 AAS。", "有夹边用 ASA；有对角的边用 AAS。", items=6),
    q(N(6), "practice", "直角里的 HL", "4 道直角三角形全等，指出斜边和直角边。", "HL 只用于直角三角形。", items=4),
    q(N(7), "practice", "选判定", "8 题根据已知选择判定方法，缺条件则写不能判定。", "先标已知再对号入座。", items=8),
    q(N(8), "practice", "先全等再求值", "6 题证全等后求对应边或角。", "对应关系写错，后面全错。", items=6),
    q(N(8), "mini_quiz", "全等小测", "对应、五种判定、简单推理。夹一道 SSA。", "SSA 不是判定定理。", items=10),
    q(N(8), "boss", "关主：全等判定官", "击败关主：①写出对应 ②选对判定 ③用全等求一条边或一个角。", "对应正确比套口诀更重要。", xp=80, items=12, qid=f"{P}-boss-congruent"),
    q(N(9), "practice", "找对称轴", "6 个图形判断是否轴对称并画出对称轴。", "对折能重合才是轴对称。", items=6),
    q(N(10), "practice", "作对称图形", "作出两个简单图形关于直线的对称图形。", "对应点连线被对称轴垂直平分。", items=2),
    q(N(11), "practice", "三线合一求角", "在等腰三角形中求角或说明三条线重合。", "底边上的高、中线、顶角平分线同一条。", items=4),
    q(N(12), "practice", "对称找最短路", "用轴对称作出直线另一侧的对称点，连接求最短折线示意。", "两点之间线段最短。", items=2),
    q(N(13), "explain", "对称产生全等", "说明一个图形和它的轴对称图形全等，对应关系由对称给出。", "对称是得到全等的一种办法。"),
    q(N(14), "practice", "用勾股求边", "已知两直角边求斜边，或已知斜边和一直角边求另一边，共 8 题。", "先确认哪条是斜边。", items=8),
    q(N(15), "practice", "由边判断直角", "6 组三边判断是否直角三角形。", "最大边当斜边去检验平方和。", items=6),
    q(N(16), "practice", "情境中的勾股", "对角线、梯子、格点距离等 6 题。", "构造出直角三角形再套定理。", items=6),
    q(N(16), "mini_quiz", "勾股小测", "求边、逆定理、简单应用。", "不是直角三角形，不能直接用勾股。", items=8),
    q(N(16), "boss", "关主：勾股测量员", "击败关主：①求直角三角形一边 ②用三边判断是否直角 ③在一个情境中求距离。", "先找直角，再平方和。", xp=80, items=10, qid=f"{P}-boss-pythagoras"),
    q(N(17), "explain", "两组对边平行", "用定义说明平行四边形，并在图上标出平行记号。", "定义是判定的起点。"),
    q(N(18), "practice", "用性质求值", "已知平行四边形求边或角或对角线被分成的段，共 6 题。", "对边相等、对角相等、对角线互相平分。", items=6),
    q(N(19), "practice", "判定平行四边形", "6 题选择用哪条判定，缺条件则不能判定。", "一组对边平行且相等也可以。", items=6),
    q(N(20), "practice", "矩形的性质", "求矩形对角线或角，共 4 题。", "四个角都是直角，对角线相等。", items=4),
    q(N(21), "practice", "菱形的性质", "求菱形边或对角线，共 4 题。", "四边相等，对角线互相垂直平分。", items=4),
    q(N(22), "explain", "正方形的两面身份", "说明正方形为什么既是矩形又是菱形，列出它可以用的性质。", "角的性质来自矩形，边的性质来自菱形。"),
    q(N(23), "practice", "特殊四边形闯关", "混合矩形菱形正方形求值 6 题。", "先命名图形，再选性质。", items=6),
    q(N(23), "mini_quiz", "平行四边形小测", "定义、性质、判定、特殊情形。", "性质和判定方向相反。", items=8),
    q(N(24), "practice", "合练卷", "全等、勾股、平行四边形短推理。", "每步写理由。", items=8),
    q(N(25), "practice", "通关综合练", "判定全等、用勾股、在平行四边形中求值。", "对应、直角、平行，三件抓手。", items=10),
    q(N(25), "boss", "关主：八年级几何通关试炼", "最终关主：①选全等判定 ②勾股求边或判定直角 ③平行四边形或矩形菱形求值。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(26), "explain", "为什么 SSA 不行", "画示意图或用语言说明：两边及一边的对角对应相等，三角形可能摆出两种样子。", "夹角对了才是 SAS。"),
    q(N(27), "practice", "把隐藏条件标出", "在 3 张等腰图中标出隐含的等边或等角。", "等腰会「白送」条件。", items=3),
    q(N(28), "explain", "中位线像一把尺", "说明梯形中位线与两底的关系，并画一个示意。", "平行两底，长度是两底和的一半。"),
    q(N(29), "practice", "数格求斜线", "在方格纸上求 4 条斜线段长。", "横格竖格当作直角边。", items=4),
    q(N(30), "explain", "对角线条件对照", "用一张表对照：平分 / 垂直 / 相等 分别把平行四边形推向哪里。", "条件加得越多，图形越特殊。"),
]


META = {
    "id": MAP_ID,
    "title": "八年级 · 图形与几何",
    "subject": "数学",
    "stage": "初中",
    "grade": 8,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "全等（关主 1）；轴对称从起点并行，在等腰处与全等汇合；勾股（关主 2）与平行四边形从全等后并行，终章汇合。SSA（n026）等为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-congruent", f"{P}-boss-pythagoras", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：全等判定官、勾股测量员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中八年级「图形与几何」地图：全等三角形、轴对称、勾股定理、平行四边形。独立通关。",
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
