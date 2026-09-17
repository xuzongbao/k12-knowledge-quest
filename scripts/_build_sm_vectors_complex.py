"""Build senior-math 平面向量与复数 map.

Run: python3 scripts/_build_sm_vectors_complex.py

Pedagogical spine: 平面向量概念与线性运算 → 坐标与数量积 → 复数概念与运算 → 复数与向量对照。
功的几何意义、单位向量、乘法旋转直觉为软锁。解三角形见 trig 图，本图不写跨图前置。
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

OUT = ROOT / "maps" / "senior-math" / "vectors-complex"
G = 10
STRAND = "图形与几何"
P = "sm-vec"
MAP_ID = "sm-vectors-complex"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "向量的概念", 1, [], ["vec", "ch-vec"], "能说明向量既有大小又有方向，并与只有大小的数量区分。本图从向量讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "向量的几何表示", 2, [N(1)], ["vec", "ch-vec"], "能用有向线段表示向量，指出起点、终点可以平移。", mastery=MASTERY_CONCEPT),
    node(N(3), "相等向量与共线", 2, [N(2)], ["vec", "ch-vec"], "能判断相等（同向等长）与共线（平行），注意零向量与任意向量平行的约定。"),
    node(N(4), "向量加法", 3, [N(3)], ["vec", "ch-vec"], "能用平行四边形法则或三角形法则做向量加法。", mastery=MASTERY_CONCEPT),
    node(N(5), "向量减法", 3, [N(4)], ["vec", "ch-vec"], "能把减法看成加上相反向量，并用三角形法则画出差。"),
    node(N(6), "数乘向量", 3, [N(3)], ["vec", "ch-vec"], "能说明数乘改变长度、负数还反向，零乘得零向量。", mastery=MASTERY_CONCEPT),
    node(N(7), "向量线性运算", 3, [N(5), N(6)], ["vec", "ch-vec"], "能计算若干向量的线性组合，并说明运算律（交换、结合、分配）。", mastery=MASTERY_GATE),
    node(N(8), "平面向量基本定理", 3, [N(7)], ["vec", "ch-coord"], "能说明不共线的两个向量可以作为基底，平面内任一向量可唯一写成线性组合。", mastery=MASTERY_CONCEPT),
    node(N(9), "向量的坐标", 3, [N(8)], ["vec", "ch-coord"], "能在正交基底下写出向量坐标，并由坐标画出向量。"),
    node(N(10), "坐标运算", 3, [N(9)], ["vec", "ch-coord"], "能用坐标做加减与数乘：对应分量分别运算。", mastery=MASTERY_GATE),
    node(N(11), "向量的模", 3, [N(10)], ["vec", "ch-dot"], "能用坐标求模：根号下分量平方和，并说明模是长度。"),
    node(N(12), "数量积定义", 3, [N(11)], ["vec", "ch-dot"], "能用 |a||b|cos θ 定义数量积，并指出结果是数量不是向量。", mastery=MASTERY_CONCEPT),
    node(N(13), "数量积坐标公式", 3, [N(12)], ["vec", "ch-dot"], "能用对应分量乘积之和计算数量积。", mastery=MASTERY_GATE),
    node(N(14), "夹角与垂直平行", 4, [N(13)], ["vec", "ch-dot"], "能用数量积判断垂直（积为 0）、求夹角；用坐标比例判断平行。", mastery=MASTERY_GATE),
    node(N(15), "向量投影", 3, [N(14)], ["vec", "ch-dot"], "能说明一个向量在另一个方向上的投影长度与数量积的关系。"),
    node(N(16), "向量证平面几何入门", 4, [N(10), N(14)], ["vec", "ch-vec", "boss-gate"], "能用向量表示中点、重心或证明两边垂直/平行的简单结论。", mastery=MASTERY_GATE),
    node(N(17), "数系为什么要扩充", 2, [N(16)], ["cx", "ch-cx"], "能说明实数里负数不能开偶次方，从而需要新数 i。", mastery=MASTERY_CONCEPT),
    node(N(18), "复数的概念", 2, [N(17)], ["cx", "ch-cx"], "能写出 z=a+bi（a,b 实数），指出实部、虚部、虚数单位 i²=-1。", mastery=MASTERY_CONCEPT),
    node(N(19), "复数相等", 2, [N(18)], ["cx", "ch-cx"], "能说明两个复数相等当且仅当实部、虚部分别相等。"),
    node(N(20), "复数的几何意义", 3, [N(19), N(9)], ["cx", "ch-cx"], "能在复平面上用点或向量表示复数，横轴实部、纵轴虚部。", mastery=MASTERY_CONCEPT),
    node(N(21), "复数加减", 3, [N(20)], ["cx", "ch-cx"], "能按实部虚部分别相加（减），并解释为平面向量加减。"),
    node(N(22), "共轭复数", 3, [N(21)], ["cx", "ch-cx"], "能写出共轭 a-bi，说明它是关于实轴的对称。", mastery=MASTERY_CONCEPT),
    node(N(23), "复数的模", 3, [N(22), N(11)], ["cx", "ch-cx"], "能求 |a+bi|=√(a²+b²)，并说明模是到原点的距离。"),
    node(N(24), "复数乘法", 4, [N(23)], ["cx", "ch-cx"], "能用分配律计算 (a+bi)(c+di)，并整理成实部加虚部。", mastery=MASTERY_GATE),
    node(N(25), "复数除法", 4, [N(24), N(22)], ["cx", "ch-cx"], "能通过乘共轭把分母实数化，完成除法。", mastery=MASTERY_GATE),
    node(N(26), "向量与复数对照", 3, [N(25), N(14)], ["cx", "ch-cx"], "能对照：加减与模像向量；乘法比向量多了「转角」这一层（本图只要求直觉）。", mastery=MASTERY_CONCEPT),
    node(N(27), "向量复数合练", 4, [N(26)], ["mixed", "ch-end"], "能在向量坐标运算、数量积、复数四则之间切换，不把数量积当成向量。", mastery=MASTERY_GATE),
    node(N(28), "向量与复数通关", 5, [N(27)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(29), "单位向量", 2, [N(11)], ["vec", "ch-vec"], "能把非零向量除以模得到同方向的单位向量。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(30), "数量积与功", 3, [N(12)], ["vec", "ch-dot"], "能把「力沿位移方向的分量乘位移」说成数量积的一个实际意义。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(31), "乘法的旋转直觉", 3, [N(24)], ["cx", "ch-cx"], "能说明乘 i 相当于逆时针转 90°，不要求一般辐角公式作为硬考点。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(32), "零向量的特殊性", 2, [N(6)], ["vec", "ch-vec"], "能说明零向量没有确定方向、模为 0，与任何向量的数量积为 0。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(33), "用向量证中点", 3, [N(16)], ["vec", "ch-vec"], "能用 (A+B)/2 一类表示写出线段中点，完成一道短证明骨架。", unlock=SOFT),
]


EXTRA_EDGES = [
    {"from": N(4), "to": N(5), "type": "related", "note": "加法用三角形接龙，减法是接到相反方向。"},
    {"from": N(12), "to": N(13), "type": "easily_confused", "note": "定义里有夹角余弦；坐标公式是分量乘积和，两者要能互相推导直觉。"},
    {"from": N(14), "to": N(3), "type": "easily_confused", "note": "垂直看数量积是否为 0；平行看坐标是否成比例，不要用反。"},
    {"from": N(21), "to": N(24), "type": "easily_confused", "note": "加减像向量；乘法不是分量分别相乘。"},
    {"from": N(11), "to": N(23), "type": "related", "note": "向量模与复数模公式长得一样，因为复平面就是坐标平面。"},
    {"from": N(24), "to": N(31), "type": "application", "note": "算出 i·i=-1 之后，再谈转 90°。"},
    {"from": N(16), "to": N(33), "type": "application", "note": "会线性表示之后，中点是最常用的一刀。"},
]


QUESTS = [
    q(N(1), "explain", "有方向的量", "举位移、力各一例说明向量，再举温度说明数量。", "有方向才能叫向量。"),
    q(N(2), "practice", "画出有向线段", "画出 4 个向量，其中两个相等但位置不同。", "平移不改变向量。", items=4),
    q(N(3), "practice", "相等还是共线", "8 组判断相等、共线或都不是。", "共线不一定等长。", items=8),
    q(N(4), "practice", "加法作图", "用三角形或平行四边形法则作 4 组加法。", "首尾相接。", items=4),
    q(N(5), "practice", "减法作图", "作 4 组 a-b，写成 a+(-b)。", "减 b 就是加相反。", items=4),
    q(N(6), "practice", "数乘", "计算并画出 6 个数乘，含负倍数。", "负号先反向。", items=6),
    q(N(7), "practice", "线性组合", "计算 6 个 2a-3b+c 一类，可先几何或先坐标（若已给）。", "先同类运算再合并。", items=6),
    q(N(8), "explain", "为什么要两个不共线", "说明一个向量不能当平面基底，两个共线的也不行。", "要能张成整个平面。"),
    q(N(9), "practice", "读写坐标", "8 个向量与坐标互写。", "横分量、纵分量。", items=8),
    q(N(10), "practice", "坐标加减数乘", "10 道坐标运算。", "分量分别算。", items=10),
    q(N(11), "practice", "求模", "求 8 个向量的模。", "平方和再开方。", items=8),
    q(N(12), "explain", "结果是数", "用自己的话区分数量积与向量加法：一个得到数，一个得到向量。", "名称里的「数」要当真。"),
    q(N(13), "practice", "坐标求数量积", "8 道用分量求数量积。", "x1x2+y1y2。", items=8),
    q(N(14), "practice", "夹角垂直平行", "6 道求夹角或判断垂直平行。", "垂直：积为 0；平行：坐标成比例。", items=6),
    q(N(15), "practice", "投影长度", "4 道求投影的数量。", "数量积除以对方的模。", items=4),
    q(N(16), "practice", "向量短证明", "2 道：中点或垂直，用向量等式写出骨架。", "先设向量，再运算，再翻译回几何。", items=2),
    q(N(16), "mini_quiz", "向量小测", "线性运算、坐标、数量积、垂直平行。夹一道把数量积当成向量。", "看结果是数还是箭头。", items=10),
    q(N(16), "boss", "关主：平面向量调度员", "击败关主：①线性运算或坐标 ②数量积 ③判断垂直或平行。", "坐标和几何两种语言要能切换。", xp=80, items=12, qid=f"{P}-boss-vec"),
    q(N(17), "explain", "为什么需要 i", "说明实数里哪一件事做不成，因而引进 i。", "负数没有实的平方根。"),
    q(N(18), "practice", "指出实部虚部", "8 个复数指出实部、虚部，含纯虚数与实数。", "bi 的虚部是 b，不是 bi。", items=8),
    q(N(19), "practice", "复数相等", "6 组由相等列出关于实部虚部的方程。", "两个实数方程。", items=6),
    q(N(20), "practice", "画在复平面", "在复平面标出 6 个复数。", "横实纵虚。", items=6),
    q(N(21), "practice", "复数加减", "8 道加减，并在图上表示其中 2 道。", "实部与虚部分开。", items=8),
    q(N(22), "practice", "写共轭", "求 8 个共轭，指出对称轴。", "虚部变号。", items=8),
    q(N(23), "practice", "求模", "求 8 个复数的模。", "与向量模相同。", items=8),
    q(N(24), "practice", "复数乘法", "8 道乘法，整理成 a+bi。", "i²=-1。", items=8),
    q(N(25), "practice", "复数除法", "6 道除法：分子分母同乘分母的共轭。", "分母变成模的平方。", items=6),
    q(N(25), "mini_quiz", "复数小测", "实部虚部、加减乘除、模。夹一道把虚部写成 bi。", "虚部是实数 b。", items=8),
    q(N(25), "boss", "关主：复数运算官", "击败关主：①指出实部虚部并画在复平面 ②完成乘或除 ③求模。", "乘除不要做成分量分别运算。", xp=80, items=10, qid=f"{P}-boss-cx"),
    q(N(26), "explain", "像在哪不像在哪", "对照向量与复数：哪些运算一样，乘法多了什么。", "加减一样；乘法带来旋转缩放。"),
    q(N(27), "practice", "合练卷", "向量数量积、复数乘除、复平面各几题。", "先看是箭头问题还是 a+bi 问题。", items=12),
    q(N(28), "practice", "通关综合练", "独立完成：向量垂直判定、复数除法、复平面表示。", "两种坐标语言不要混公式。", items=12),
    q(N(28), "boss", "关主：向量与复数通关试炼", "最终关主：①向量数量积或夹角 ②复数乘或除 ③在图上表示一个向量或复数。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(29), "practice", "写成单位向量", "把 4 个非零向量写成模乘单位向量。", "除以模。", items=4),
    q(N(30), "explain", "功为什么是数量积", "用「只算沿位移方向的力」说明为什么出现余弦。", "垂直的力不做功。"),
    q(N(31), "explain", "乘 i 转直角", "计算 i、i²、i³、i⁴ 并在复平面上标出，说明每次转 90°。", "乘 i 逆时针转直角。"),
    q(N(32), "explain", "零向量怎么说方向", "说明为什么「与零向量平行」要单独约定。", "没有确定方向，只能靠定义。"),
    q(N(33), "practice", "中点向量式", "用向量写出 2 条线段中点，并验证一组坐标。", "两端点向量相加除以 2。", items=2),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 平面向量与复数",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "几何与代数",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "平面向量运算与数量积（关主 1）→ 复数四则（关主 2）→ 对照收束。单位向量（n029）、功（n030）、乘 i 旋转（n031）、零向量（n032）、中点证法（n033）为软锁。解三角形见 trig 图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-vec", f"{P}-boss-cx", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：平面向量调度员、复数运算官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中必修「几何与代数」中的平面向量与复数地图。独立通关。grade=10。",
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
