"""Build senior-math 数学建模 / 综合与实践 map.

Run: python3 scripts/_build_sm_practice.py

原创课题骨架（不抄教材课题长文）：
  流量套餐怎么选（分段计费模型）；
  讲座后排看得见吗（视线约束剖面）；
  把两件事合成一份建模报告。
流程：发现问题 → 建立模型 → 求解 → 交流与局限。grade=12 表示综合收束学段带。
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

OUT = ROOT / "maps" / "senior-math" / "practice"
G = 12
STRAND = "综合与实践"
P = "sm-prac"
MAP_ID = "sm-practice"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：套餐总超支", 1, [], ["find", "ch-plan"], "能从「流量总是不够或总是浪费」感到：计费规则可能是分段函数，需要先写清楚。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：用量是自变量", 2, [N(1)], ["plan", "ch-plan"], "能约定：月用量 x（GB）为自变量，应付费 y 为因变量，并声明单位。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：写出计费规则", 3, [N(2)], ["do", "ch-plan"], "能把「套餐内固定费 + 超出部分单价」写成分段解析式（可用合理假设数）。"),
    node(N(4), "实施：算三种用量", 3, [N(3)], ["do", "ch-plan"], "能代入偏少、刚好、偏多三种用量，比较应付费。"),
    node(N(5), "实施：在两档套餐间选", 3, [N(4)], ["do", "ch-plan"], "能画出或列表比较两档套餐，指出用量落在哪一段时换套餐更划算。"),
    node(N(6), "交流：套餐答辩", 4, [N(5)], ["share", "ch-plan", "boss-gate"], "能讲清模型假设、分段点、选择建议，并回答「如果下月用量波动怎么办」。", mastery=MASTERY_GATE),
    node(N(7), "发现：后排看不清", 2, [N(6)], ["find", "ch-sight"], "能提出讲座座位视线被前排挡住的问题，并说明要测量哪些高度与距离。", mastery=MASTERY_CONCEPT),
    node(N(8), "计划：视线约束清单", 2, [N(7)], ["plan", "ch-sight"], "能列出约束：屏幕下沿高度、前排头顶高度、最小仰角或间隙，座椅数量尽量不减。", mastery=MASTERY_CONCEPT),
    node(N(9), "实施：画剖面草图", 3, [N(8)], ["do", "ch-sight"], "能用简化线段画教室纵向剖面，标出屏幕、前排、后排的关键尺寸。"),
    node(N(10), "实施：两种抬升方案", 3, [N(9)], ["do", "ch-sight"], "能提出两种方案（抬屏幕、抬后排、拉大排距等），并算出后排视线是否越过前排。"),
    node(N(11), "实施：比较与取舍", 3, [N(10)], ["do", "ch-sight"], "能用「看得见、座位数量、改造成本直觉」比较方案，选出一个并说明放弃另一个的原因。"),
    node(N(12), "交流：座位说明会", 4, [N(11)], ["share", "ch-sight", "boss-gate"], "能向非数学听众讲解剖面图，回答「为什么不把屏幕再挂高一点」。", mastery=MASTERY_GATE),
    node(N(13), "发现：两件事能合在一起吗", 2, [N(6)], ["find", "ch-mix"], "能提出一个同时用到分段计费和空间约束的问题，例如活动室租赁时长与座位视线。", mastery=MASTERY_CONCEPT),
    node(N(14), "计划：建模说明书", 2, [N(13)], ["plan", "ch-mix"], "能写问题、变量、假设、数据从哪来、准备交流什么。", mastery=MASTERY_CONCEPT),
    node(N(15), "实施：走完建模四步", 3, [N(12), N(14)], ["do", "ch-mix"], "能按说明书收集或合理假设数据，算出一个结果，并写下局限。"),
    node(N(16), "交流：一页成果卡", 3, [N(15)], ["share", "ch-mix"], "能用问题、模型、结果、局限四句话写成果卡。", mastery=MASTERY_CONCEPT),
    node(N(17), "建模工具箱", 3, [N(16)], ["mixed", "ch-end"], "能列出数学建模四步，以及每一步应留下的证据（式子、图、数据、局限）。", mastery=MASTERY_CONCEPT),
    node(N(18), "实践合练", 4, [N(17)], ["mixed", "ch-end"], "能抽签完成套餐或视线课题中的完整流程。", mastery=MASTERY_GATE),
    node(N(19), "建模实践通关", 5, [N(18)], ["mixed", "ch-end", "boss-gate"], "能独立完成高中数学建模活动线的收束检查。", mastery=MASTERY_GATE),
    node(N(20), "套餐隐藏条款", 3, [N(6)], ["plan", "ch-plan"], "能假设「超出后整档跳价」与「只对超出部分计价」两种条款，比较模型要怎么改。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(21), "视线测量误差", 3, [N(11)], ["sight", "ch-sight"], "能说明高度差 2 厘米时，结论应怎样写得更谨慎。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(22), "模型假设清单", 3, [N(14)], ["mix", "ch-mix"], "能把「人坐直、屏幕是矩形、用量独立」等假设列成清单，指出哪一条最脆弱。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(23), "向非数学老师讲解", 3, [N(16)], ["share", "ch-end"], "能把成果卡改写成不出现符号也能听懂的五句话。", unlock=SOFT),
    node(N(24), "数据是别人给的", 3, [N(15)], ["mix", "ch-mix"], "能说明二手数据缺测量过程时，结论要降级为「在该数据下」。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(3), "to": N(5), "type": "application", "note": "分段点写错，比较两档套餐的交叉点就会错。"},
    {"from": N(8), "to": N(11), "type": "application", "note": "比较方案时要回到约束清单，不能只看「看起来高一点」。"},
    {"from": N(9), "to": N(10), "type": "related", "note": "剖面图是模型，两种方案是对模型的两次求解。"},
    {"from": N(6), "to": N(20), "type": "related", "note": "条款一改，分段函数的表达式就要改。"},
    {"from": N(11), "to": N(21), "type": "application", "note": "选完方案，还要承认尺子和目测都不完美。"},
    {"from": N(14), "to": N(22), "type": "related", "note": "说明书里的假设应能被单独挑出来攻击。"},
]


QUESTS = [
    q(N(1), "explain", "超支的感觉", "讲述或假设一次流量不够用，指出你不知道的是规则还是自己的用量。", "先感到「要写成函数」，再谈分段。"),
    q(N(2), "explain", "变量约定", "写出 x、y 的含义和单位，并声明一个月只看一个总量。", "单位不一致后面全错。"),
    q(N(3), "practice", "写成分段函数", "用合理假设写出至少两段的 y(x)，标出分界点。", "分界点属于哪一段要写明。", items=1),
    q(N(4), "practice", "三种用量", "代入三个 x 求 y，并指出落在哪一段。", "先看落在哪一段再代入。", items=3),
    q(N(5), "practice", "两档对照表", "列出两档套餐在三个用量下的费用，指出更划算的区间（可用草图）。", "交叉点附近最值得算细。", items=1),
    q(N(6), "explain", "回答波动", "假设下月用量上下浮动 20%，你的建议还站不站得住。", "建议要带用量范围。"),
    q(N(6), "mini_quiz", "套餐模型小测", "找三份模拟方案的问题：无单位、无分段点、只算了一个用量。", "一个点不能代表整条规则。", items=6),
    q(N(6), "boss", "关主：套餐建模师", "击败关主：①写出分段计费规则 ②比较两档套餐 ③说明用量波动时建议如何改口。", "模型先于推荐。", xp=80, items=8, qid=f"{P}-boss-plan"),
    q(N(7), "explain", "挡在哪", "描述后排被挡住时，你认为要量的三个尺寸。", "问题要落到可以量的量。"),
    q(N(8), "explain", "约束写成清单", "写出至少三条不可破或尽量不破的约束。", "座位数量往往是硬约束。"),
    q(N(9), "practice", "画剖面", "画纵向剖面，标屏幕下沿、前排头顶、后排眼高、水平距离。", "没有尺寸的图只是愿望。", items=1),
    q(N(10), "practice", "两种方案", "写出两种改造，并各判断后排视线是否越过前排（可用相似或正切粗算）。", "不要求精确到毫米，但要有不等式。", items=2),
    q(N(11), "practice", "比较取舍", "用一张对照表比较两种方案，写出选择理由。", "理由要对应约束。", items=1),
    q(N(12), "practice", "回答质疑", "准备两个提问：为什么不继续加高屏幕、会不会挡灯。", "每个回答指回测量或约束。", items=2),
    q(N(12), "mini_quiz", "视线模型小测", "给几份方案找缺：无尺寸、减少座位却不声明、没比较第二种。", "没有对照的方案只是偏好。", items=6),
    q(N(12), "boss", "关主：视线规划员", "击败关主：①列出约束 ②展示带尺寸的剖面或方案 ③说明取舍理由。", "看得见是不等式，不是感觉。", xp=80, items=8, qid=f"{P}-boss-sight"),
    q(N(13), "explain", "提出综合问题", "写出一个同时用到计费分段和空间约束的问题。", "两种办法都要用到，才叫综合。"),
    q(N(14), "explain", "写说明书", "写问题、变量、假设、数据来源、交流时展示什么。", "别人按说明书能开工。"),
    q(N(15), "practice", "留下证据", "收集或合理假设数据，算出结果，写一句局限。", "局限不是谦虚，是范围。", items=1),
    q(N(16), "practice", "四句成果卡", "问题、模型、结果、局限各一句。", "模型可以是分段函数，也可以是剖面不等式。", items=1),
    q(N(17), "explain", "打开工具箱", "说出四步名称，以及每步留下什么证据。", "没有证据的交流只是讲故事。"),
    q(N(18), "practice", "抽签走流程", "抽套餐或视线之一完整做完四步。", "发现—计划—实施—交流。", items=1),
    q(N(19), "practice", "通关综合练", "独立完成一个带函数或不等式的小项目，并主动说局限。", "能说局限，才像真做完。", items=1),
    q(N(19), "boss", "关主：数学建模通关试炼", "最终关主：①展示一个分段或约束模型 ②给出可检验的结论 ③说出局限与假设。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
    q(N(20), "explain", "改条款", "针对「整档跳价」，重写分段函数并指出原来的建议哪里失效。", "规则变了模型就要变。"),
    q(N(21), "explain", "误差下的结论", "假设关键高度可能差 2 厘米，说明结论应怎样改口。", "证据变弱，说法要降级。"),
    q(N(22), "explain", "最脆的假设", "从清单里挑一条最容易被现实打破的假设，说明打破后结论怎么变。", "假设要能被攻击。"),
    q(N(23), "practice", "五句白话", "把成果卡改写成给班主任听的五句话，不出现 y=f(x)。", "听众不是阅卷老师。", items=1),
    q(N(24), "explain", "二手数据", "说明如果用量数据来自运营商截图而不是自己记录，结论应加什么前缀。", "在该数据下。"),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 数学建模与综合实践",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "数学建模活动与数学探究活动",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "流量套餐分段模型（关主 1）；讲座视线约束在套餐交流后展开（关主 2）；综合课题与成果卡收束。隐藏条款（n020）、测量误差（n021）、假设清单（n022）、白话讲解（n023）、二手数据（n024）为软锁。课题骨架原创，不抄教材长文。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-plan", f"{P}-boss-sight", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：套餐建模师、视线规划员、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标数学建模活动风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "高中「数学建模活动」地图：套餐分段计费、讲座视线约束、综合报告。独立通关。grade=12 为综合收束学段带。",
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
