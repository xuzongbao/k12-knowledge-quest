"""Build Grade 5 Comprehensive Practice map JSON.

Run: python3 scripts/_build_grade5_practice.py

原创活动骨架：小路旁间隔摆花、通知全班的传递方案、校园浪费小调查。
「模型误差讨论」为软锁。本图自洽，不引用跨图节点。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _map_common import (
    MASTERY_CONCEPT,
    MASTERY_GATE,
    ROOT,
    SOFT,
    node as _node,
    q,
    sample_progress,
    write_map,
)

OUT = ROOT / "maps" / "primary-math" / "grade-5-practice"
G = 5
STRAND = "综合与实践"
P = "pm-g5-prac"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：花盆怎么摆才匀", 1, [], ["find", "ch-space"], "能提出在一段小路旁按差不多的间隔摆花盆，两端要不要放的问题。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：先画线段图", 2, [N(1)], ["plan", "ch-space"], "能把路画成线段，标出端点和间隔，先分清「段数」和「盆数」。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：两端都放", 3, [N(2)], ["do", "ch-space"], "能在两端都放的情况下，根据路长和间隔算出大约需要几盆。"),
    node(N(4), "实施：一端放或不放", 3, [N(3)], ["do", "ch-space"], "能比较两端都放、只放一端、两端都不放时盆数的差别。"),
    node(N(5), "实施：间隔改了", 3, [N(4)], ["do", "ch-space"], "能在间隔变大或变小时重新估算，并说明盆数如何变。"),
    node(N(6), "交流：图纸和现场", 3, [N(5)], ["share", "ch-space", "boss-gate"], "能讨论现场转弯、门口不能摆时，图纸上的数要怎样改。", mastery=MASTERY_GATE),
    node(N(7), "发现：通知怎样最快到全班", 2, [N(6)], ["find", "ch-msg"], "能提出把一条通知从一人传到全班，怎样比较「轮数」或「总次数」。", mastery=MASTERY_CONCEPT),
    node(N(8), "计划：约定传递规则", 2, [N(7)], ["plan", "ch-msg"], "能约定每人每轮最多通知几人、不能重复通知已知道的人。", mastery=MASTERY_CONCEPT),
    node(N(9), "实施：画传递图", 3, [N(8)], ["do", "ch-msg"], "能画出几轮后知道的人数，做成树状或分层图。"),
    node(N(10), "实施：比较两种规则", 3, [N(9)], ["do", "ch-msg"], "能比较「每次只通知一人」和「每次通知两人」谁更快覆盖全班。"),
    node(N(11), "交流：规则的代价", 3, [N(10)], ["share", "ch-msg"], "能说明更快的规则可能让有的人通知次数更多，讨论公不公平。", mastery=MASTERY_CONCEPT),
    node(N(12), "发现：浪费藏在哪", 2, [N(6)], ["find", "ch-waste"], "能提出调查校园里一种可计数的浪费（纸巾、水龙头流水、剩余饭菜份数等）。", mastery=MASTERY_CONCEPT),
    node(N(13), "计划：调查表与对象", 2, [N(12)], ["plan", "ch-waste"], "能设计调查表：问谁、问几天、怎样计数，并写清不能代表的范围。", mastery=MASTERY_CONCEPT),
    node(N(14), "实施：收集几天数据", 3, [N(13)], ["do", "ch-waste"], "能收集不少于 3 个时段或天数的数据并整理成表。"),
    node(N(15), "实施：选一张图呈现", 3, [N(14)], ["do", "ch-waste"], "能选择条形或折线呈现，并写一句不超过数据的结论。"),
    node(N(16), "交流：建议要可执行", 3, [N(15)], ["share", "ch-waste"], "能把结论变成一条可以在班里试行的建议，并想怎样检查有没有用。", mastery=MASTERY_CONCEPT),
    node(N(17), "模型与调查合练", 4, [N(11), N(16)], ["mixed", "ch-end"], "能对照间隔模型和通知模型、浪费调查：都要先约定规则再收集或计算。", mastery=MASTERY_GATE),
    node(N(18), "模型误差讨论", 3, [N(6)], ["space", "ch-space"], "能指出间隔模型忽略了花盆本身的宽度或转弯，估计会偏差什么方向。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(19), "如果班额变了", 3, [N(17)], ["msg", "ch-end"], "能假设班级人数增减，说明通知轮数或摆花盆数怎样重算。", mastery=MASTERY_CONCEPT),
    node(N(20), "跨项目海报", 3, [N(19)], ["share", "ch-end"], "能用一张海报同时展示一个模型问题和一个调查问题的要点。"),
    node(N(21), "答辩：数字从哪来", 3, [N(20)], ["share", "ch-end"], "能指出海报上每个关键数字的来源：量的、算的，还是问来的。"),
    node(N(22), "五年级实践合练", 4, [N(21)], ["mixed", "ch-end"], "能抽签完成间隔、通知或调查中的完整项目。", mastery=MASTERY_GATE),
    node(N(23), "五年级实践通关", 4, [N(22)], ["mixed", "ch-end", "boss-gate"], "能独立完成一个带模型或调查的综合项目并答辩来源。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(4), "type": "easily_confused", "note": "段数和盆数不是同一个数，两端放不放会差 1。"},
    {"from": N(8), "to": N(10), "type": "related", "note": "传递规则不同，覆盖全班的轮数就不同。"},
    {"from": N(9), "to": N(10), "type": "easily_confused", "note": "图上的人数是「已经知道的」，不是「这一轮新通知的」。"},
    {"from": N(13), "to": N(16), "type": "application", "note": "调查对象写清了，建议才不会说成全校一定怎样。"},
    {"from": N(6), "to": N(18), "type": "application", "note": "图纸能用之后，再谈它忽略了什么。"},
]


QUESTS = [
    q(N(1), "explain", "提出间隔问题", "描述一段真实或想象的小路，问花盆怎样摆才看起来匀。", "要提到两端和间隔。"),
    q(N(2), "explain", "线段图", "画线段，标出路长、间隔、端点是否放盆，并写出段数、盆数各指什么。", "先分清段和点。"),
    q(N(3), "practice", "两端都放", "3 组路长与间隔，估算两端都放时的盆数。", "盆数常常是段数加 1。", items=3),
    q(N(4), "practice", "三种放法", "同一段路比较三种端点放法的盆数。", "差在两端这两个点。", items=3),
    q(N(5), "practice", "改间隔", "间隔变成原来大约两倍，盆数大约怎样变，用两组数验证。", "间隔变大，盆变少。", items=2),
    q(N(6), "explain", "现场要改图", "假设有一个门口不能摆，说明图纸怎样改、盆数怎样变。", "模型要给现场让路。"),
    q(N(6), "mini_quiz", "间隔项目小测", "段数盆数、端点放法、现场改图。", "先画线段再算。", items=8),
    q(N(6), "boss", "关主：间隔规划员", "击败关主：①画线段区分段与点 ②算不同端点放法 ③说明现场障碍怎么改图。", "点不是段。", xp=80, items=10, qid=f"{P}-boss-space"),
    q(N(7), "explain", "提出传递问题", "说明要把通知传到全班，可以比轮数或比总说话次数。", "先约定比什么。"),
    q(N(8), "explain", "写出规则", "写下每轮每人最多通知几人、已知道的人不再通知。", "规则含糊就没法画图。"),
    q(N(9), "practice", "画三轮", "从 1 人开始，按「每轮每人通知 2 人」画到第 3 轮，写出知道的人数。", "不要把同一人画两次。", items=1),
    q(N(10), "practice", "比较两种规则", "比较每次通知 1 人和 2 人，覆盖 16 人大约几轮。", "可以用列表模拟。", items=2),
    q(N(11), "explain", "快和公平", "说明更快的规则是否让少数人通知次数特别多。", "快不等于每个人一样累。"),
    q(N(12), "explain", "选定一种浪费", "选定可计数的一种浪费，说明为什么能数。", "不能数就不要选。"),
    q(N(13), "explain", "设计调查", "写出对象、天数、计数方法和结论不能代表谁。", "范围先写在表头。"),
    q(N(14), "practice", "收集整理", "收集至少 3 组数据并填表。", "每天同一时刻更可比。", items=3),
    q(N(15), "practice", "选图写结论", "选条形或折线画出，并写一句不越界结论。", "问变化用折线，问哪天最多用条形。", items=1),
    q(N(16), "explain", "可试行的建议", "写一条班内建议，并写怎样检查一周后有没有用。", "建议要带检查办法。"),
    q(N(17), "explain", "模型和调查", "对照间隔/通知模型和浪费调查的共同点。", "都要先约定，才能算或收。"),
    q(N(18), "explain", "模型漏了什么", "指出间隔模型至少忽略的一件事，以及盆数可能偏多还是偏少。", "误差要有方向。"),
    q(N(19), "explain", "人数变了", "班额加减 8 人，说明通知轮数或花盆数哪一个要重算。", "输入变，输出变。"),
    q(N(20), "practice", "一张海报", "海报上同时出现模型要点和调查要点，各不超过四句。", "数字旁注明来源。", items=1),
    q(N(21), "practice", "来源答辩", "指着三个数字说：量的、算的还是问的。", "来源说不清的数字不要上海报。", items=3),
    q(N(22), "practice", "抽签完整项目", "抽间隔/通知/调查之一走完四步。", "规则和数据都要能检查。", items=1),
    q(N(23), "practice", "通关综合练", "独立完成一个综合项目并回答来源与误差。", "模型让路给现场，结论让路给对象范围。", items=1),
    q(N(23), "boss", "关主：五年级实践通关试炼", "最终关主：完成一个间隔或传递模型，或一个可计数浪费调查；能画图、能比较方案、能说明局限。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g5-practice",
    "title": "五年级 · 综合与实践",
    "subject": "数学",
    "stage": "小学",
    "grade": 5,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "间隔摆花为主线（关主 1）；通知传递与浪费调查可并行，在 n017 汇合。模型误差讨论（n018）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-space", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：间隔规划员、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "小学五年级「综合与实践」地图：间隔模型、传递方案、校园调查。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g5-practice", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
