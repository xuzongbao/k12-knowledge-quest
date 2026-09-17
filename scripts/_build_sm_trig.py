"""Build senior-math 三角函数与解三角形 map.

Run: python3 scripts/_build_sm_trig.py

Pedagogical spine: 任意角与弧度 → 三角函数概念与诱导 → 图象性质与正弦型函数 → 和差公式入门 → 正弦/余弦定理解三角形。
辅助角、扇形回顾、SSA 解的个数警示为软锁。本图自洽；课标把解三角形放在平面向量应用中，本仓库并入本图，不写向量节点前置。
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

OUT = ROOT / "maps" / "senior-math" / "trig"
G = 10
STRAND = "数与代数"
P = "sm-trig"
MAP_ID = "sm-trig"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "任意角", 1, [], ["angle", "ch-rad"], "能把角理解为射线绕端点旋转，可超过 360°，也可是负角。本图从任意角讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "象限角", 2, [N(1)], ["angle", "ch-rad"], "能根据终边所在象限给角分类，并指出终边在坐标轴上的角不是象限角。"),
    node(N(3), "终边相同的角", 2, [N(2)], ["angle", "ch-rad"], "能写出与已知角终边相同的角的集合：差为 360° 的整数倍。", mastery=MASTERY_CONCEPT),
    node(N(4), "弧度制", 2, [N(1)], ["angle", "ch-rad"], "能说明 1 弧度是弧长等于半径的圆心角，并知道一周是 2π 弧度。", mastery=MASTERY_CONCEPT),
    node(N(5), "弧度与角度换算", 3, [N(4)], ["angle", "ch-rad"], "能在度与弧度之间换算，常用 180°=π。", mastery=MASTERY_GATE),
    node(N(6), "单位圆上的点", 2, [N(5), N(3)], ["tri", "ch-def"], "能在单位圆上标出终边与圆的交点，为定义三角函数做准备。", mastery=MASTERY_CONCEPT),
    node(N(7), "正弦", 3, [N(6)], ["tri", "ch-def"], "能用单位圆交点的纵坐标定义 sin θ，并指出其范围在 -1 到 1。", mastery=MASTERY_CONCEPT),
    node(N(8), "余弦", 3, [N(6)], ["tri", "ch-def"], "能用单位圆交点的横坐标定义 cos θ，范围同样在 -1 到 1。", mastery=MASTERY_CONCEPT),
    node(N(9), "正切", 3, [N(7), N(8)], ["tri", "ch-def"], "能用 sin/cos 定义 tan θ，并指出余弦为 0 时正切无意义。", mastery=MASTERY_CONCEPT),
    node(N(10), "同角关系", 3, [N(9)], ["tri", "ch-def"], "能使用 sin²θ+cos²θ=1 以及 tan θ=sinθ/cosθ 做简单求值。", mastery=MASTERY_GATE),
    node(N(11), "诱导公式", 4, [N(10)], ["tri", "ch-ind"], "能把 π±θ、2π-θ、负角等化为锐角或第一象限相关角求值，并说明符号看象限。", mastery=MASTERY_GATE),
    node(N(12), "正弦函数图象", 3, [N(7)], ["tri", "ch-graph"], "能画出 y=sin x 在一个周期上的图象，指出周期 2π、奇函数、最值 ±1。"),
    node(N(13), "余弦函数图象", 3, [N(8), N(12)], ["tri", "ch-graph"], "能画出 y=cos x，并说明它可由正弦图象平移得到。"),
    node(N(14), "正切函数图象", 3, [N(9)], ["tri", "ch-graph"], "能画出 y=tan x 在 (-π/2,π/2) 的图象，指出渐近线与周期 π。"),
    node(N(15), "周期、振幅、初相", 3, [N(12)], ["tri", "ch-graph"], "能从 y=A sin(ωx+φ) 读出振幅 |A|、周期 2π/|ω|、初相 φ。", mastery=MASTERY_CONCEPT),
    node(N(16), "正弦型函数图象", 4, [N(15), N(13)], ["tri", "ch-graph", "boss-gate"], "能由 A、ω、φ 画出 y=A sin(ωx+φ) 或反过来读参数，并指出平移与伸缩。", mastery=MASTERY_GATE),
    node(N(17), "简单三角方程", 4, [N(11), N(12)], ["tri", "ch-ind"], "能解 sin x=a、cos x=a 在一个周期内的解，并写成通解的入门形式。"),
    node(N(18), "两角和与差", 4, [N(11)], ["tri", "ch-id"], "能使用两角和与差的正弦、余弦公式做展开或求值，不要求默写全部推导。", mastery=MASTERY_GATE),
    node(N(19), "二倍角公式", 3, [N(18)], ["tri", "ch-id"], "能由和角公式得到 sin 2α、cos 2α 的常用形式并求值。"),
    node(N(20), "三角恒等入门", 4, [N(19), N(10)], ["tri", "ch-id", "boss-gate"], "能在同角关系、诱导、和差与二倍角之间选择一条路径化简。", mastery=MASTERY_GATE),
    node(N(21), "正弦定理", 3, [N(10)], ["solve", "ch-solve"], "能说明 a/sin A=b/sin B=c/sin C=2R 的使用场景：已知两角一边或两边一对角。", mastery=MASTERY_CONCEPT),
    node(N(22), "余弦定理", 3, [N(10)], ["solve", "ch-solve"], "能用 c²=a²+b²-2ab cos C 求边或求角，已知三边或两边夹角时优先。", mastery=MASTERY_CONCEPT),
    node(N(23), "解三角形选择定理", 4, [N(21), N(22)], ["solve", "ch-solve"], "能根据已知元素选择正弦定理或余弦定理，并检查角度是否可能。", mastery=MASTERY_GATE),
    node(N(24), "三角形面积", 3, [N(21)], ["solve", "ch-solve"], "能用 (1/2)ab sin C 求面积，并与海伦公式直觉对照（不要求后者作为考点）。"),
    node(N(25), "解三角形应用", 4, [N(23), N(24)], ["solve", "ch-solve"], "能把测高、测距等简化情境画成三角形并求解，标注已知与未知。"),
    node(N(26), "三角函数合练", 4, [N(16), N(20), N(25)], ["mixed", "ch-end"], "能在图象参数、恒等变形、解三角形之间切换。", mastery=MASTERY_GATE),
    node(N(27), "三角函数通关", 5, [N(26)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(28), "扇形弧长与面积", 2, [N(5)], ["angle", "ch-rad"], "能用弧度制写扇形弧长 l=rθ、面积 (1/2)r²θ，作为弧度的应用。", unlock=SOFT),
    node(N(29), "辅助角公式入门", 4, [N(18)], ["tri", "ch-id"], "能把 a sin x+b cos x 看成一个正弦型函数，读出振幅。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(30), "SSA 解的个数", 4, [N(23)], ["solve", "ch-solve"], "能说明只知两边和其中一边的对角时，可能无解、一解或两解。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(31), "诱导公式符号陷阱", 3, [N(11)], ["tri", "ch-ind"], "能专门练习「函数名变不变、符号看象限」，避免口诀用反。", unlock=SOFT),
    node(N(32), "周期与最小正周期", 3, [N(16)], ["tri", "ch-graph"], "能区分「一个周期」和「最小正周期」，例如 sin 2x 的最小正周期是 π。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(7), "to": N(8), "type": "related", "note": "正弦是纵坐标，余弦是横坐标，同一点的两个坐标。"},
    {"from": N(12), "to": N(13), "type": "easily_confused", "note": "正弦过原点，余弦过 (0,1)；平移 π/2 可以对上，不要画反。"},
    {"from": N(21), "to": N(22), "type": "easily_confused", "note": "正弦定理爱用角对边；余弦定理爱用夹角对边。已知种类不同。"},
    {"from": N(15), "to": N(32), "type": "easily_confused", "note": "ω 越大周期越小；写成 2π/|ω| 后还要确认是不是最小。"},
    {"from": N(18), "to": N(29), "type": "application", "note": "和差公式是辅助角的代数来源。"},
    {"from": N(4), "to": N(28), "type": "application", "note": "弧度就是为了让弧长公式不含 180。"},
    {"from": N(23), "to": N(30), "type": "related", "note": "选对定理之后，还要问这一组已知会不会对应两个三角形。"},
]


QUESTS = [
    q(N(1), "explain", "旋转出来的角", "画出一个大于 360° 的角和一个负角，说明终边怎么得到。", "角是旋转量，不只是几何里那一瞥。"),
    q(N(2), "practice", "判断象限", "10 个角判断终边象限或是否在轴上。", "先化到 0° 到 360° 再看。", items=10),
    q(N(3), "practice", "终边相同集合", "写出 4 个角的终边相同角的集合。", "加上 360° 的整数倍。", items=4),
    q(N(4), "explain", "一弧度有多大", "用自己的话说明 1 弧度，并估计它大约多少度。", "弧长等于半径时的圆心角。"),
    q(N(5), "practice", "度与弧度互化", "12 组换算，含 π/6、π/4、π/3、π/2。", "180°=π。", items=12),
    q(N(6), "practice", "在单位圆上标点", "标出至少 6 个常见角终边与单位圆的交点。", "半径是 1，坐标就是余弦、正弦。", items=6),
    q(N(7), "practice", "求正弦值", "求 8 个角的正弦，含象限符号。", "纵坐标；上正下负。", items=8),
    q(N(8), "practice", "求余弦值", "求 8 个角的余弦，含象限符号。", "横坐标；右正左负。", items=8),
    q(N(9), "practice", "求正切并指出无意义", "8 道正切，另加 2 道指出何处无意义。", "余弦为 0 时不能做商。", items=10),
    q(N(10), "practice", "同角关系求值", "已知正弦或余弦求其余，6 题，注意象限决定符号。", "平方和为 1，符号另判。", items=6),
    q(N(11), "practice", "诱导化简求值", "10 道诱导公式，写出化到哪一象限、符号怎么来。", "函数名与符号分开想。", items=10),
    q(N(12), "practice", "画正弦一周期", "画出 y=sin x 从 0 到 2π，标零点、最值。", "0、π/2、π、3π/2、2π 五个关键点。", items=1),
    q(N(13), "practice", "画余弦并对照", "画出 y=cos x，说明与正弦差一个平移。", "余弦在 0 处取 1。", items=1),
    q(N(14), "practice", "画正切主支", "画出 (-π/2,π/2) 上的正切，标渐近线。", "中间过原点，两边竖线挡着。", items=1),
    q(N(15), "practice", "读 A、ω、φ", "从 6 个解析式读振幅、周期、初相。", "周期是 2π 除以 |ω|。", items=6),
    q(N(16), "practice", "画正弦型函数", "根据参数画 2 个 y=A sin(ωx+φ)，或由图读参数。", "先周期，再左右移，再上下伸缩。", items=2),
    q(N(16), "mini_quiz", "图象小测", "正弦余弦对照、参数读写、一点平移。夹一道把 ω 当成周期。", "周期=2π/|ω|。", items=8),
    q(N(16), "boss", "关主：周期波动测绘员", "击败关主：①度弧度换算 ②诱导求值 ③读出或画出一个正弦型函数。", "符号和周期两处最容易混。", xp=80, items=12, qid=f"{P}-boss-graph"),
    q(N(17), "practice", "简单三角方程", "在 0 到 2π 内解 6 道 sin x=a 或 cos x=a。", "先找一象限的解，再对称。", items=6),
    q(N(18), "practice", "和差公式求值", "8 道化开或求值，如 75°、15° 一类。", "写成两个熟悉角的和或差。", items=8),
    q(N(19), "practice", "二倍角", "6 道用二倍角求值或化简。", "cos 2α 有三种常用写法，按已知选。", items=6),
    q(N(20), "practice", "选路化简", "6 道恒等化简，写下你用的是同角、诱导还是和差。", "先看角的关系，再选公式。", items=6),
    q(N(20), "mini_quiz", "恒等小测", "同角、诱导、和差、二倍角。夹一道符号看错象限。", "公式对了还要看象限。", items=8),
    q(N(20), "boss", "关主：三角恒等化简官", "击败关主：①同角关系 ②一道和差或二倍角 ③说明为什么不能乱拆。", "每一等号后面要有名字。", xp=80, items=10, qid=f"{P}-boss-id"),
    q(N(21), "practice", "用正弦定理", "4 个三角形：已知两角一边或两边一对角（暂避开两解）。", "角与对边成对出现。", items=4),
    q(N(22), "practice", "用余弦定理", "4 个：已知两边夹角求第三边，或三边求一角。", "夹角对着要求的边。", items=4),
    q(N(23), "practice", "先选定理再解", "6 个三角形先写「用正弦还是余弦」，再解。", "有夹角用余弦；有对角用正弦。", items=6),
    q(N(24), "practice", "求面积", "4 题用两边及其夹角正弦求面积。", "夹角必须是那两边的夹角。", items=4),
    q(N(25), "practice", "测高测距短题", "2 个简化情境：画出三角形、标已知、求解、写答。", "先图后式。", items=2),
    q(N(26), "practice", "合练卷", "图象参数、化简求值、解三角形各几题。", "先辨题型。", items=12),
    q(N(27), "practice", "通关综合练", "独立完成：诱导或和差求值、画或读正弦型、解一个三角形。", "单位圆、公式、三角形，三条线要能接通。", items=12),
    q(N(27), "boss", "关主：三角函数通关试炼", "最终关主：①正弦型参数 ②一道恒等或诱导 ③解一个三角形。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(28), "practice", "扇形计算", "4 道弧长或面积，角用弧度。", "公式里的 θ 必须是弧度。", items=4),
    q(N(29), "practice", "合成一个正弦", "把 3 个 a sin x+b cos x 写成振幅形式。", "振幅是根号下 a²+b²。", items=3),
    q(N(30), "explain", "会不会有两个三角形", "画草图说明 SSA 何时出现两解，何时无解。", "作图看另一边能不能碰上。"),
    q(N(31), "practice", "只练符号", "8 道只要求写出诱导后的符号与函数名，不必算出数值。", "奇变偶不变是口诀，象限才是理由。", items=8),
    q(N(32), "practice", "最小正周期", "6 个函数求最小正周期。", "先写成标准型再 2π/|ω|。", items=6),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 三角函数与解三角形",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "函数 / 解三角形",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "任意角与三角函数（关主 1：图象）→ 恒等变形入门（关主 2）→ 正弦/余弦定理解三角形后收束。扇形（n028）、辅助角（n029）、SSA 两解（n030）、诱导符号（n031）、最小正周期（n032）为软锁。解三角形不引用向量图节点。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-graph", f"{P}-boss-id", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：周期波动测绘员、三角恒等化简官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中「三角函数与解三角形」地图：任意角与弧度 → 三角函数 → 图象与恒等入门 → 解三角形。独立通关。grade=10。",
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
