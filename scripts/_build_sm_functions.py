"""Build senior-math 函数概念与基本初等函数 map.

Run: python3 scripts/_build_sm_functions.py

Pedagogical spine: 函数概念与性质 → 幂函数 → 指数函数 → 对数函数 → 函数应用。
反函数直觉、二分法求零点、图象平移伸缩为软锁。本图自洽。数列见 sequences 图，三角函数见 trig 图。
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

OUT = ROOT / "maps" / "senior-math" / "functions"
G = 10
STRAND = "数与代数"
P = "sm-func"
MAP_ID = "sm-functions"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "对应关系与函数", 1, [], ["fn", "ch-fn"], "能说明函数是一种对应：每个允许的 x 都对应唯一的 y。本图从概念重新讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "定义域", 2, [N(1)], ["fn", "ch-fn"], "能根据解析式求定义域：分母不为 0、偶次根下非负、对数真数为正等。", mastery=MASTERY_CONCEPT),
    node(N(3), "值域入门", 2, [N(2)], ["fn", "ch-fn"], "能对简单函数说出值域或值的范围，并说明它依赖于定义域。"),
    node(N(4), "解析式表示", 2, [N(1)], ["fn", "ch-fn"], "能从对应规则写出 y=f(x)，并求指定自变量的函数值。", mastery=MASTERY_CONCEPT),
    node(N(5), "图象表示", 2, [N(4)], ["fn", "ch-fn"], "能在坐标平面上描点连线表示函数，并说明竖直直线至多交图象一次。"),
    node(N(6), "表格表示", 2, [N(4)], ["fn", "ch-fn"], "能从表格读对应，并说明表格往往只给出部分点。"),
    node(N(7), "分段函数", 3, [N(2), N(5)], ["fn", "ch-fn"], "能按自变量所在区间选用不同对应规则，求值和画折线型图象。", mastery=MASTERY_GATE),
    node(N(8), "单调性", 3, [N(5)], ["fn", "ch-prop"], "能用「随 x 增大，f(x) 增大或减小」描述单调，并用定义比较 f(x1) 与 f(x2)。", mastery=MASTERY_CONCEPT),
    node(N(9), "奇偶性", 3, [N(5)], ["fn", "ch-prop"], "能用 f(-x)=f(x) 或 -f(x) 判断偶函数、奇函数，并联系图象对称。", mastery=MASTERY_CONCEPT),
    node(N(10), "最大最小值", 3, [N(8)], ["fn", "ch-prop"], "能在给定区间上读出或求出函数的最大、最小值，并说明端点也可能取到。"),
    node(N(11), "函数的零点", 3, [N(5), N(8)], ["fn", "ch-prop"], "能说明 f(x)=0 的根就是图象与 x 轴交点的横坐标，叫做零点。", mastery=MASTERY_CONCEPT),
    node(N(12), "性质综合", 4, [N(7), N(9), N(10), N(11)], ["fn", "ch-prop", "boss-gate"], "能对同一个函数同时讨论定义域、单调、奇偶、最值与零点。", mastery=MASTERY_GATE),
    node(N(13), "幂函数概念", 2, [N(12)], ["power", "ch-elem"], "能识别 y=x^α（α 为给定实数）叫做幂函数，并指出定义域随 α 变化。", mastery=MASTERY_CONCEPT),
    node(N(14), "常见幂函数图象", 3, [N(13)], ["power", "ch-elem"], "能比较 y=x, x², x³, √x, 1/x 在第一象限的升降快慢与公共点。", mastery=MASTERY_GATE),
    node(N(15), "整数指数幂回顾", 2, [N(13)], ["exp", "ch-elem"], "能计算负整数指数幂，并说明 a^{-n}=1/a^n（a≠0）。"),
    node(N(16), "根式与分数指数", 3, [N(15)], ["exp", "ch-elem"], "能把根式写成分数指数幂，并注意偶次根下非负。", mastery=MASTERY_CONCEPT),
    node(N(17), "有理指数幂运算", 3, [N(16)], ["exp", "ch-elem"], "能用同底数幂法则完成有理指数的乘除与乘方。", mastery=MASTERY_GATE),
    node(N(18), "指数函数定义", 2, [N(17)], ["exp", "ch-elem"], "能识别 y=a^x（a>0, a≠1），说明定义域为 R、值域为正。", mastery=MASTERY_CONCEPT),
    node(N(19), "指数函数性质", 4, [N(18), N(8)], ["exp", "ch-elem"], "能根据 a>1 或 0<a<1 说出单调性，并指出过定点 (0,1)。", mastery=MASTERY_GATE),
    node(N(20), "指数增长与衰减", 3, [N(19)], ["exp", "ch-elem"], "能用指数函数描述翻倍、半衰期一类变化，并说明底数含义。"),
    node(N(21), "对数的定义", 2, [N(18)], ["log", "ch-elem"], "能说明 log_a N 是「a 的多少次方等于 N」，并写出指数对数互化。", mastery=MASTERY_CONCEPT),
    node(N(22), "对数运算性质", 3, [N(21)], ["log", "ch-elem"], "能用积商幂的对数法则化简，并指出真数必须为正。", mastery=MASTERY_GATE),
    node(N(23), "换底公式", 3, [N(22)], ["log", "ch-elem"], "能把对数换到底数 10 或 e 以便计算，并用来比较不同底的对数值。"),
    node(N(24), "对数函数定义", 2, [N(21)], ["log", "ch-elem"], "能识别 y=log_a x（a>0, a≠1），定义域 x>0。", mastery=MASTERY_CONCEPT),
    node(N(25), "对数函数性质", 4, [N(24), N(19)], ["log", "ch-elem"], "能根据底数大于 1 或在 0 与 1 之间说出单调性，并指出过定点 (1,0)。", mastery=MASTERY_GATE),
    node(N(26), "指数与对数互逆", 3, [N(25)], ["log", "ch-elem"], "能说明指数函数与对数函数（同底）图象关于 y=x 对称，运算上互为逆运算。", mastery=MASTERY_CONCEPT),
    node(N(27), "指数对数方程入门", 4, [N(22), N(26)], ["log", "ch-elem", "boss-gate"], "能解简单指数方程、对数方程：化为同底或利用互逆，并检查定义域。", mastery=MASTERY_GATE),
    node(N(28), "函数模型选择", 3, [N(20), N(14)], ["app", "ch-app"], "能根据「线性、多项式、指数」增长形态选择简单模型，不要求精确拟合。", mastery=MASTERY_CONCEPT),
    node(N(29), "函数应用短题", 4, [N(28), N(27)], ["app", "ch-app"], "能把增长率、衰减、分段计费写成函数并求值、比较。"),
    node(N(30), "基本初等函数合练", 4, [N(29), N(12)], ["mixed", "ch-end"], "能在幂、指、对与一般性质之间切换，不把底数限制说错。", mastery=MASTERY_GATE),
    node(N(31), "函数通关", 5, [N(30)], ["mixed", "ch-end", "boss-gate"], "能独立完成函数概念、性质与指数对数的收束检查。", mastery=MASTERY_GATE),
    node(N(32), "反函数直觉", 3, [N(26)], ["fn", "ch-fn"], "能说明反函数是把对应反过来，并指出要先一一对应才谈得上。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(33), "用二分法求零点", 3, [N(11)], ["fn", "ch-prop"], "能在连续变号区间上用中点逐步逼近零点，说明得到的是近似。", unlock=SOFT),
    node(N(34), "图象平移与伸缩", 3, [N(19)], ["fn", "ch-prop"], "能说明 f(x)+k、f(x-h)、af(x) 对图象的上下、左右、伸缩作用。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(35), "对数不等式入门", 4, [N(27)], ["log", "ch-elem"], "能解简单对数不等式，并强调先写定义域、再看底数是否大于 1。", unlock=SOFT),
]


EXTRA_EDGES = [
    {"from": N(8), "to": N(9), "type": "related", "note": "单调看升降，奇偶看对称，可以同时成立也可以只居其一。"},
    {"from": N(18), "to": N(24), "type": "easily_confused", "note": "指数函数底数在幂的位置固定、自变量在指数；对数函数自变量在真数。"},
    {"from": N(19), "to": N(25), "type": "easily_confused", "note": "底数在 (0,1) 时，指数函数与对数函数都递减，但定义域完全不同。"},
    {"from": N(21), "to": N(22), "type": "easily_confused", "note": "log(A+B) 不能拆成 log A + log B；那是积的对数。"},
    {"from": N(11), "to": N(33), "type": "application", "note": "先确认变号，再用二分逼近。"},
    {"from": N(20), "to": N(28), "type": "application", "note": "会描述指数变化之后，才谈在几种模型里怎么选。"},
    {"from": N(5), "to": N(34), "type": "related", "note": "先会画原图，再谈平移伸缩。"},
]


QUESTS = [
    q(N(1), "explain", "一对一还是多对一", "举一个「每个 x 一个 y」的例子，再举一个「一个 x 两个 y」说明它不是函数。", "竖直方向不能一对多。"),
    q(N(2), "practice", "求定义域", "求 8 个函数的定义域，含分母、偶次根、对数。", "先找「不合法」的 x。", items=8),
    q(N(3), "practice", "说值域", "对 6 个简单函数说出值域或范围（可结合图象）。", "值域是 y 实际能取到的。", items=6),
    q(N(4), "practice", "求函数值", "给定解析式求 8 个函数值，含负数代入要加括号。", "代入先加括号。", items=8),
    q(N(5), "practice", "描点画图", "画出 3 个简单函数图象，并用竖直直线检验。", "描点—连线—看趋势。", items=3),
    q(N(6), "explain", "表只能看见一部分", "同一对应，表格只列出 5 个 x。说明从表能读出什么、读不出什么。", "没列出的 x 不能瞎猜。"),
    q(N(7), "practice", "分段求值画图", "2 个分段函数：求值、画图、指出分界点取哪一段。", "分界点看属于哪个区间。", items=2),
    q(N(8), "practice", "判断单调", "6 个函数（可给图或表）指出增区间、减区间。", "比较两个自变量对应的函数值。", items=6),
    q(N(9), "practice", "判断奇偶", "8 个函数判断奇、偶或既非奇又非偶。", "先看定义域是否关于原点对称。", items=8),
    q(N(10), "practice", "读最值", "在给定区间上读 6 个图象或简单解析式的最值。", "闭区间上连续函数必有最值。", items=6),
    q(N(11), "practice", "找零点", "由图或解析式指出 6 个函数的零点个数与大致位置。", "零点是交 x 轴的地方。", items=6),
    q(N(12), "practice", "一张性质卡", "对 2 个函数填写：定义域、单调、奇偶、最值、零点。", "先定义域，再谈其他。", items=2),
    q(N(12), "mini_quiz", "函数性质小测", "定义域、分段、单调奇偶、零点。夹一道定义域不对称却谈奇偶。", "奇偶先看定义域。", items=10),
    q(N(12), "boss", "关主：函数性质鉴定官", "击败关主：①求定义域 ②判断单调或奇偶 ③读最值或零点。", "性质要挂在定义域上。", xp=80, items=12, qid=f"{P}-boss-prop"),
    q(N(13), "explain", "幂函数长什么样", "写出三个不同 α 的幂函数，指出哪些 x 能代入。", "α 改了，定义域可能改。"),
    q(N(14), "practice", "第一象限比较", "在同一坐标系比较至少 4 种常见幂函数，标公共点。", "第一象限 (1,1) 常常是公共点。", items=4),
    q(N(15), "practice", "负整数指数", "计算 8 个负整数指数幂。", "负指数是倒数，底数不能为 0。", items=8),
    q(N(16), "practice", "根式改写", "8 组根式与分数指数互写。", "偶次根要注意非负。", items=8),
    q(N(17), "practice", "有理指数运算", "10 道同底数幂的乘除乘方。", "指数相加、相减或相乘。", items=10),
    q(N(18), "explain", "底数限制", "说明为什么指数函数要求 a>0 且 a≠1。", "负底数时有的 x 没有实意义；a=1 是常函数。"),
    q(N(19), "practice", "指数函数性质卡", "对 a=2 与 a=1/2 填写单调、定点、图象大致位置。", "底数大于 1 递增。", items=2),
    q(N(20), "practice", "翻倍与半衰期", "2 个情境写成指数函数并求指定时刻的值。", "先确认「每次乘同一个数」。", items=2),
    q(N(21), "practice", "指数对数互化", "10 组 a^b=N 与对数式互写。", "对数是问指数。", items=10),
    q(N(22), "practice", "对数运算法则", "8 道化简，夹 2 道指出 log(A+B) 不能拆。", "积商幂才能拆，加减不能。", items=10),
    q(N(23), "practice", "换底比较", "用换底比较 6 组不同底对数的大小。", "换到同一底再比。", items=6),
    q(N(24), "explain", "真数必须为正", "说明对数函数为什么定义域是 x>0。", "正底数的任何次方都是正的。"),
    q(N(25), "practice", "对数函数性质卡", "对底数 2 与 1/2 填写单调、定点 (1,0)。", "底数大于 1 时递增。", items=2),
    q(N(26), "explain", "互为逆运算", "用一对数说明：先指数再对数（同底）回到原数，并提到 y=x 对称。", "定义域值域对调。"),
    q(N(27), "practice", "解简单方程", "解 8 道指数或对数方程，并检查是否在定义域内。", "真数、底数限制不能忘。", items=8),
    q(N(27), "mini_quiz", "指数对数小测", "互化、运算法则、性质、简单方程。夹一道真数不大于 0。", "先定义域后运算。", items=10),
    q(N(27), "boss", "关主：指数对数航海士", "击败关主：①指数或对数性质 ②运算法则化简 ③解一个方程并检查定义域。", "底数和真数的限制最容易漏。", xp=80, items=12, qid=f"{P}-boss-exp"),
    q(N(28), "explain", "选哪种增长", "给三组「随时间变化」的描述，判断更像一次、二次还是指数。", "看是加一个数、乘一个数还是加速弯曲。"),
    q(N(29), "practice", "写成函数再算", "2 个短情境：分段计费或增长率，写出函数并求值比较。", "先写对应规则，再代入。", items=2),
    q(N(30), "practice", "合练卷", "性质、幂函数、指数对数、简单应用各几题。", "先辨是哪一类函数。", items=12),
    q(N(31), "practice", "通关综合练", "独立完成：定义域与奇偶、指数对数互化、一个应用短题。", "限制条件写在答案前面。", items=12),
    q(N(31), "boss", "关主：函数通关试炼", "最终关主：①函数性质卡 ②指数与对数互化并化简 ③选一个模型或解一个方程。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(32), "explain", "反过来还是不是函数", "举一个可以反过来的对应和一个不可以的，说明反函数需要什么。", "先要一对一。"),
    q(N(33), "practice", "二分两次", "在一个变号区间上做两次二分，写下近似零点。", "每次取中点，看哪半边变号。", items=1),
    q(N(34), "practice", "说出怎么移", "6 组：由解析式说出平移或伸缩，或反过来。", "x 里面减 h 是向右。", items=6),
    q(N(35), "practice", "简单对数不等式", "解 4 道，先写 x>0 和底数情形。", "底数在 (0,1) 时不等号方向与化成同底后可能相反。", items=4),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 函数概念与基本初等函数",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "函数",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "函数概念与性质（关主 1）→ 幂函数与指数对数（关主 2）→ 模型选择与应用后收束。反函数直觉（n032）、二分法（n033）、平移伸缩（n034）、对数不等式（n035）为软锁。三角函数与数列不在本图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-prop", f"{P}-boss-exp", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：函数性质鉴定官、指数对数航海士、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中必修「函数」地图：概念与性质 → 幂函数 → 指数函数 → 对数函数 → 简单应用。独立通关。grade=10 表示必修学段带。",
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
