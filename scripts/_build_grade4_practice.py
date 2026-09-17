"""Build Grade 4 Comprehensive Practice map JSON.

Run: python3 scripts/_build_grade4_practice.py

原创活动骨架：午餐盘数量约束、校园路线比较、值日表设计。
「时间冲突表」为软锁。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-4-practice"
G = 4
STRAND = "综合与实践"
P = "pm-g4-prac"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：盘子装不下", 1, [], ["find", "ch-lunch"], "能发现午餐要同时满足「有主食、有菜、总量别超」这类互相卡住的要求。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：先写下约束", 2, [N(1)], ["plan", "ch-lunch"], "能把要求写成几条可以检查的约束，例如份数上限、必须包含的类别。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：试配一盘", 2, [N(2)], ["do", "ch-lunch"], "能给出一盘搭配，并逐条核对约束。"),
    node(N(4), "实施：再配一盘更优", 3, [N(3)], ["do", "ch-lunch"], "能在同样约束下给出另一种搭配，比较哪一种更均衡或更省。"),
    node(N(5), "交流：约束能不能改", 3, [N(4)], ["share", "ch-lunch", "boss-gate"], "能讨论某条约束太严或太松时，可行方案会怎样变。", mastery=MASTERY_GATE),
    node(N(6), "发现：走哪条路更省", 2, [N(5)], ["find", "ch-route"], "能提出从教室到图书角（或类似地点）有几条路、哪条更省时间或更少拐弯。", mastery=MASTERY_CONCEPT),
    node(N(7), "计划：比较什么指标", 2, [N(6)], ["plan", "ch-route"], "能约定比较步行时间、拐弯次数或经过的门的个数，一次只主比一样。", mastery=MASTERY_CONCEPT),
    node(N(8), "实施：把路线画下来", 3, [N(7)], ["do", "ch-route"], "能画出两条以上路线的简图，标出比较用的数。"),
    node(N(9), "实施：走一走计时", 3, [N(8)], ["do", "ch-route"], "能实际走两条路并记录时间或步数，注意同样的出发时刻条件。"),
    node(N(10), "交流：推荐一条路", 3, [N(9)], ["share", "ch-route"], "能根据指标推荐一条路，并说明另一条在什么情况下更好。", mastery=MASTERY_CONCEPT),
    node(N(11), "发现：值日表常撞车", 2, [N(5)], ["find", "ch-duty"], "能发现值日如果只按学号轮，可能和请假、社团冲突。", mastery=MASTERY_CONCEPT),
    node(N(12), "计划：表要满足的条件", 2, [N(11)], ["plan", "ch-duty"], "能列出值日表约束：每天人数、每人每周次数、不能连续两天等。", mastery=MASTERY_CONCEPT),
    node(N(13), "实施：排出一周", 3, [N(12)], ["do", "ch-duty"], "能排出一张一周值日草表，并逐条检查约束。"),
    node(N(14), "实施：调整冲突", 3, [N(13)], ["do", "ch-duty"], "能在有人不能值日时调整，尽量少改动其他天。"),
    node(N(15), "交流：表公不公平", 3, [N(14)], ["share", "ch-duty"], "能用每人次数说明表是否公平，并提出一条改进。", mastery=MASTERY_CONCEPT),
    node(N(16), "约束思想合练", 4, [N(10), N(15)], ["mixed", "ch-end"], "能说明午餐、路线、值日都是「在限制条件下找更好的安排」。", mastery=MASTERY_GATE),
    node(N(17), "时间冲突表", 3, [N(15)], ["duty", "ch-duty"], "能用简单的时间格子标出社团与值日冲突，提前避开。", unlock=SOFT),
    node(N(18), "如果人数变了", 3, [N(16)], ["plan", "ch-end"], "能假设多一人或少一人，说明哪张表或哪盘搭配要重做。", mastery=MASTERY_CONCEPT),
    node(N(19), "写成给食堂或班级的建议", 3, [N(18)], ["share", "ch-end"], "能把项目结论写成三条可执行建议。"),
    node(N(20), "路演与答辩", 3, [N(19)], ["share", "ch-end"], "能回答「为什么不选另一个方案」，用约束和数据说话。"),
    node(N(21), "四年级实践合练", 4, [N(20)], ["mixed", "ch-end"], "能抽签完成约束类项目的完整四步。", mastery=MASTERY_GATE),
    node(N(22), "四年级实践通关", 4, [N(21)], ["mixed", "ch-end", "boss-gate"], "能独立在限制条件下给出可检查的方案并解释取舍。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(12), "type": "related", "note": "午餐约束和值日约束都要先写成可打勾的句子。"},
    {"from": N(3), "to": N(4), "type": "easily_confused", "note": "第一个可行方案不一定最好；还要在可行里比较。"},
    {"from": N(7), "to": N(10), "type": "easily_confused", "note": "指标不同，推荐的路可能不同；要声明比的是什么。"},
    {"from": N(13), "to": N(14), "type": "application", "note": "排出草表后，冲突靠局部调整，不必整周推倒。"},
    {"from": N(15), "to": N(17), "type": "application", "note": "公平讨论之后，可以用时间格子把冲突可视化。"},
]


QUESTS = [
    q(N(1), "explain", "互相卡住的要求", "列出午餐里至少三条会互相限制的要求。", "要求要能检查，不要只说「要营养」。"),
    q(N(2), "explain", "写成可打勾的约束", "把要求改成 3–5 条约束清单。", "每条都能用是/否回答。"),
    q(N(3), "practice", "配一盘并核对", "给出一盘搭配，用清单逐条打勾。", "有一条不满足就改。", items=1),
    q(N(4), "practice", "再给一个方案", "给出第二盘，比较份数或类别是否更均衡。", "两个方案都要先可行。", items=2),
    q(N(5), "explain", "放宽一条会怎样", "假设把总量上限放宽，说明可选方案会变多还是变少。", "约束越松，可行方案通常越多。"),
    q(N(5), "mini_quiz", "约束项目小测", "判断方案是否可行，指出缺了哪条约束。", "先可行，再谈更好。", items=8),
    q(N(5), "boss", "关主：约束搭配师", "击败关主：①写出约束 ②给出两个可行方案并比较 ③说明改一条约束后的影响。", "没有约束就没有优化。", xp=80, items=10, qid=f"{P}-boss-constraint"),
    q(N(6), "explain", "提出路线问题", "画出起点终点，指出至少两条路。", "路要真实能走。"),
    q(N(7), "explain", "选定指标", "选定主比的一样（时间/拐弯/门的个数），说明为什么这次不混着比。", "一次主比一样，结论才清楚。"),
    q(N(8), "practice", "画路线简图", "画出两条路并标上准备记录的数的位置。", "图要能让别人按着走。", items=2),
    q(N(9), "practice", "实地记录", "走两条路，记录时间或步数。", "出发条件尽量相同。", items=2),
    q(N(10), "explain", "推荐并留余地", "推荐一条路，并写「如果下雨/人多，另一条可能更好」。", "推荐要绑定指标。"),
    q(N(11), "explain", "值日撞车", "举一个值日冲突的例子，说明只按学号轮的问题。", "冲突要具体到人和天。"),
    q(N(12), "explain", "列出值日约束", "写出至少四条值日约束。", "包括每天人数和每人次数。"),
    q(N(13), "practice", "排出一周草表", "做一张一周值日表并逐条检查。", "先满足每天人数。", items=1),
    q(N(14), "practice", "局部调整", "假设两人某天不能来，调整表并标明改了哪几格。", "尽量少改。", items=1),
    q(N(15), "explain", "用次数谈公平", "统计每人值日次数，说明是否公平，给一条改进。", "公平要看次数，不只看感觉。"),
    q(N(16), "explain", "三种限制", "用一句话概括午餐、路线、值日的共同点。", "都是限制条件下的安排。"),
    q(N(17), "practice", "画出冲突格", "用星期×时段的格子标出两个人的冲突。", "冲突格不能排值日。", items=1),
    q(N(18), "explain", "人数变化", "假设多一名同学，说明值日表或午餐份数哪一条要改。", "输入变了，方案要重算。"),
    q(N(19), "explain", "三条建议", "写成给班级的三条建议，每条都能照着做。", "不要空话。"),
    q(N(20), "practice", "答辩一句", "准备回答「为什么不选另一方案」，用约束或数据。", "不说「我觉得」，说限制和记录。", items=1),
    q(N(21), "practice", "抽签走四步", "抽午餐/路线/值日之一完整做完。", "方案必须可检查。", items=1),
    q(N(22), "practice", "通关综合练", "独立给出一个受限方案，比较过备选，能答辩。", "可行、可比较、可解释。", items=1),
    q(N(22), "boss", "关主：四年级实践通关试炼", "最终关主：在给定约束下给出两个方案并推荐一个，说明指标和取舍。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g4-practice",
    "title": "四年级 · 综合与实践",
    "subject": "数学",
    "stage": "小学",
    "grade": 4,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "午餐盘约束为主线（关主 1）；校园路线与值日表可并行，在 n016 汇合。时间冲突表（n017）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-constraint", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：约束搭配师、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "小学四年级「综合与实践」地图：数量约束搭配、路线比较、值日安排。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g4-practice", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
