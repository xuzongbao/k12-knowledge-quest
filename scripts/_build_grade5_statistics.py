"""Build Grade 5 Statistics map JSON from a single source of truth.

Run: python3 scripts/_build_grade5_statistics.py

Pedagogical spine (课标第三学段，自撰短描述，非教材页原文):
  折线统计图（读变化、画图、单式与复式）
  → 众数；平均数对照
  → 简单随机试验与数据分析意识。
「复式折线」深入为软锁支线。中位数放六年级图。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-5-statistics"
G = 5
STRAND = "统计与概率"
P = "pm-g5-stat"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "数据会随时间变", 1, [], ["line", "ch-line"], "能举出气温、身高、每日阅读页数等随时间变化的例子，说明需要看变化而不是只看一次。", mastery=MASTERY_CONCEPT),
    node(N(2), "折线统计图长什么样", 2, [N(1)], ["line", "ch-line"], "能指出折线统计图用点表示数量、用线连接表示变化。", mastery=MASTERY_CONCEPT),
    node(N(3), "读一个点", 2, [N(2)], ["line", "ch-line"], "能读出折线图上某一点对应的时间和数量。"),
    node(N(4), "读上升下降", 2, [N(3)], ["line", "ch-line", "trend"], "能根据折线的上升、下降、走平，说出这段时间数量如何变化。", mastery=MASTERY_CONCEPT),
    node(N(5), "读最快变化", 3, [N(4)], ["line", "ch-line"], "能找出上升或下降最陡的一段，说明这段变化最大。"),
    node(N(6), "最高点和最低点", 2, [N(3)], ["line", "ch-line"], "能找出折线图的最高点、最低点及其对应时间。"),
    node(N(7), "根据表画折线", 3, [N(5), N(6)], ["line", "ch-line", "draw"], "能根据按时间排列的表描点、连线，画出折线统计图。"),
    node(N(8), "折线与条形什么时候用", 3, [N(7)], ["line", "ch-line", "choose"], "能说明：比多少常用条形图，看变化常用折线图。", mastery=MASTERY_CONCEPT),
    node(N(9), "复式折线图图例", 3, [N(8)], ["line", "ch-line", "compound"], "能根据图例区分两条折线代表哪一组。", mastery=MASTERY_CONCEPT),
    node(N(10), "读复式折线比较", 3, [N(9)], ["line", "ch-line"], "能比较同一时间两组谁高，以及哪一组变化更明显。"),
    node(N(11), "看折线做简单预测", 3, [N(10)], ["line", "ch-line"], "能根据近期趋势做一句谨慎预测，并说明预测可能不准。", mastery=MASTERY_CONCEPT),
    node(N(12), "折线图综合", 4, [N(11)], ["line", "ch-line", "boss-gate"], "能读、画单式折线，并读复式折线的图例与趋势。", mastery=MASTERY_GATE),
    node(N(13), "一组数里谁出现最多", 2, [N(1)], ["mode", "ch-mode"], "能在一组数中找出出现次数最多的数，知道这叫众数。", mastery=MASTERY_CONCEPT),
    node(N(14), "众数可以不止一个", 3, [N(13)], ["mode", "ch-mode"], "当两个数出现次数一样多且最多时，能说出有两个众数。", mastery=MASTERY_CONCEPT),
    node(N(15), "没有明显众数", 3, [N(14)], ["mode", "ch-mode"], "当每个数都只出现一次时，能说明这组数据没有明显众数。", mastery=MASTERY_CONCEPT),
    node(N(16), "众数解决什么问题", 3, [N(15)], ["mode", "ch-mode"], "能举例：订校服最常见的尺码用众数更合适，不必用平均尺码。", mastery=MASTERY_CONCEPT),
    node(N(17), "众数和平均数对照", 4, [N(16)], ["mode", "ch-mode", "average"], "能对同一组数据既求众数也求平均数，并说明它们回答的问题不同。", mastery=MASTERY_GATE),
    node(N(18), "众数综合", 4, [N(12), N(17)], ["mode", "ch-mode", "boss-gate"], "能在折线或调查数据中选用众数或平均，并说明理由。", mastery=MASTERY_GATE),
    node(N(19), "随机现象是什么", 2, [N(12)], ["random", "ch-random"], "能举出事先不能确定结果、但可以列出可能结果的现象。", mastery=MASTERY_CONCEPT),
    node(N(20), "简单随机试验", 3, [N(19)], ["random", "ch-random"], "能设计摸棋、抛硬币、转盘等小试验，事先写下可能结果。"),
    node(N(21), "重复试验做记录", 3, [N(20)], ["random", "ch-random"], "能重复试验并制成次数表，观察哪一种出现得多。"),
    node(N(22), "次数多不等于下一次一定", 3, [N(21)], ["random", "ch-random"], "能说明：即使红棋出现得多，下一次仍可能摸到别的颜色。", mastery=MASTERY_CONCEPT),
    node(N(23), "样本很小要小心", 4, [N(22)], ["random", "ch-data"], "能比较「只试 5 次」和「试 40 次」的稳定程度，建立「数据太少不可靠」的意识。", mastery=MASTERY_CONCEPT),
    node(N(24), "结论要对应问题", 3, [N(18), N(23)], ["data", "ch-data"], "能检查别人的结论是否超出了数据能说的范围。", mastery=MASTERY_GATE),
    node(N(25), "调查对象是谁", 3, [N(24)], ["data", "ch-data"], "能说明只问本班，不能直接代表全校；对象变了，结论要改口。", mastery=MASTERY_CONCEPT),
    node(N(26), "数据分析意识合练", 4, [N(25)], ["data", "ch-data", "boss-gate"], "能读折线、选统计量，并对随机试验和小样本作出谨慎判断。", mastery=MASTERY_GATE),
    node(N(27), "复式折线自己画", 4, [N(12)], ["line", "ch-line", "compound"], "能根据两组按时间排列的数据画出复式折线图，图例和纵轴清楚。", unlock=SOFT),
    node(N(28), "折线被截断的纵轴", 3, [N(12)], ["line", "ch-data"], "能发现纵轴不从 0 开始时，变化看起来会被放大，读图要看刻度。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(29), "订购与众数", 3, [N(18)], ["mode", "ch-mode"], "能在「订多少件某号」的情境中坚持用众数，而不是用平均数凑一个不存在的尺码。", unlock=SOFT),
    node(N(30), "五年级统计合练", 4, [N(26)], ["mixed", "ch-end"], "综合折线趋势、众数与平均、简单随机试验。", mastery=MASTERY_GATE),
    node(N(31), "五年级统计通关", 5, [N(30)], ["mixed", "ch-end", "boss-gate"], "能独立完成折线图、众数和随机试验意识的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(8), "type": "easily_confused", "note": "折线强调变化，条形强调比多少；不是谁更高级。"},
    {"from": N(4), "to": N(11), "type": "easily_confused", "note": "趋势可以提示可能怎样，但不能当成一定会发生。"},
    {"from": N(13), "to": N(16), "type": "related", "note": "众数回答「哪一个最常见」，平均数回答「拉齐后的水平」。"},
    {"from": N(13), "to": N(17), "type": "easily_confused", "note": "最常见的数和拉齐后的数常常不是同一个。"},
    {"from": N(21), "to": N(22), "type": "easily_confused", "note": "过去出现得多，只说明更常见，不保证下一次。"},
    {"from": N(23), "to": N(25), "type": "related", "note": "次数少和对象不对，都会让结论不稳。"},
    {"from": N(9), "to": N(27), "type": "application", "note": "会读复式折线之后，可以试着自己画。"},
]


QUESTS = [
    q(N(1), "explain", "举一个会变的量", "说出两种「过几天再量会不同」的量，并说明只记一个数不够。", "和时间挂钩的量，适合看变化。"),
    q(N(2), "explain", "点和线", "指着折线图说明：点表示某一天的数量，线表示从这天到那天怎么变。", "没有点就没有线，线不是随便画的弧。"),
    q(N(3), "practice", "读点", "8 个点：读出时间和数量。", "先看横轴再看纵轴。", items=8),
    q(N(4), "practice", "升还是降", "标出 6 段折线是上升、下降还是走平。", "后一点比前一点高就是上升。", items=6),
    q(N(5), "practice", "最陡的一段", "3 张图找出上升最陡、下降最陡的一段时间。", "同样时间内，竖着变化越大越陡。", items=3),
    q(N(6), "practice", "峰和谷", "找出最高、最低点及对应时间，共 4 张图。", "最高不一定在最后一天。", items=4),
    q(N(7), "practice", "描点连线", "根据 7 天的表画折线图，描点、标数、连线。", "点要落在刻度上，线连相邻的点。", items=1),
    q(N(8), "explain", "什么时候用折线", "给四个情境，选择条形图或折线图，并说明理由。", "问「哪类多」用条形；问「怎么变」用折线。"),
    q(N(9), "explain", "两条线的图例", "把两条折线和图例连起来，读出某一天两组各是多少。", "先看图例颜色或虚实。"),
    q(N(10), "practice", "比较两条折线", "4 张复式折线：同一时间谁高；哪一组波动更大。", "波动看上下晃得厉不厉害。", items=8),
    q(N(11), "explain", "谨慎预测", "根据近几天上升的折线，写一句预测，并补一句「如果天气突变就不一定」。", "预测要留余地。"),
    q(N(12), "practice", "折线闯关", "读趋势、画单式折线、读复式图例。", "点、趋势、图例三件齐。", items=6),
    q(N(12), "mini_quiz", "折线小测", "混合读点、最陡段、选图种、复式比较。", "先判断这张图在问变化还是比多少。", items=10),
    q(N(12), "boss", "关主：折线气象员", "击败关主：①读上升下降和最值 ②根据表画折线 ③读复式折线并做一句谨慎预测。", "看变化先看相邻两点。", xp=80, items=12, qid=f"{P}-boss-line"),
    q(N(13), "practice", "找出出现最多的", "8 组数据找出众数。", "先数每个数出现几次。", items=8),
    q(N(14), "practice", "两个众数", "4 组有两个众数的数据，把它们都写出来。", "并列第一就要都写。", items=4),
    q(N(15), "explain", "没有明显众数", "一组 1–8 各出现一次，说明为什么不宜说众数是几。", "没有「最常见」时不要硬找。"),
    q(N(16), "explain", "尺码听谁的", "订购最常见鞋码，解释为什么看众数而不是把鞋码加起来平均。", "尺码不能做成 36.5 这种「平均码」去订货。"),
    q(N(17), "practice", "两个统计量", "同一组数据求众数和平均数，各写一句「它适合回答什么」。", "常见用众数，拉齐用平均。", items=4),
    q(N(18), "practice", "选众数还是平均", "6 个情境选择更合适的统计量。", "问最常见选众数，问整体水平选平均。", items=6),
    q(N(18), "mini_quiz", "众数小测", "求众数、双众数、无众数、与平均对照。", "先数次数。", items=10),
    q(N(18), "boss", "关主：众数采购员", "击败关主：①求众数 ②处理两个众数或没有众数 ③在订购情境说明为何不用平均。", "最常见，不是拉齐。", xp=80, items=12, qid=f"{P}-boss-mode"),
    q(N(19), "explain", "事先说不准", "举两个随机现象，列出可能结果，说明做之前不知道哪一个会出现。", "随机不是「毫无规律」，而是事先不确定。"),
    q(N(20), "explain", "设计一个小试验", "设计摸棋或转盘：写出盒子里有什么、做多少次、记录表长什么样。", "试验前先写清可能结果。"),
    q(N(21), "practice", "做 20 次记录", "重复试验 20 次，制成次数表，指出出现最多的结果。", "每次条件要一样。", items=20),
    q(N(22), "explain", "下一次仍不确定", "即使记录里红很多，说明为什么下一次仍可能摸到蓝。", "记录描述过去，下一次仍是随机。"),
    q(N(23), "practice", "5 次和 40 次", "比较两组模拟记录：5 次波动大，40 次更靠近棋子组成。写两句观察。", "数据越多，偶然的晃动相对越小。", items=2),
    q(N(24), "practice", "结论越界了吗", "4 段根据小调查写出的结论，判断有没有说得太满，并改成谨慎说法。", "数据没覆盖的对象，不要被写进结论。", items=4),
    q(N(25), "explain", "问了谁", "只调查本班喜欢的运动，能不能说「全国小朋友都喜欢……」？说明理由。", "结论的范围不能大于调查对象。"),
    q(N(26), "practice", "意识合练", "读折线趋势、选众数或平均、评价一句过满的结论。", "先分清：变化、最常见、还是随机。", items=6),
    q(N(26), "mini_quiz", "数据意识小测", "混合折线、众数、小样本、对象范围。", "谨慎比「算对」更难得。", items=8),
    q(N(27), "practice", "画两条折线", "两组 7 天数据，画复式折线图，写清图例。", "两条线用不同线型或颜色。", items=1),
    q(N(28), "explain", "纵轴被截断", "同一组数据，纵轴从 0 和从 80 开始各画示意，说明哪张看起来「跳得更猛」。", "看变化幅度要读刻度，不要只看线条陡。"),
    q(N(29), "practice", "按众数订购", "根据尺码调查表决定订购哪几个码、大约各多少，避免用平均码。", "先找出现最多的码。", items=1),
    q(N(30), "practice", "合练卷", "折线+众数+随机试验记录。", "三种题型先分类。", items=12),
    q(N(31), "practice", "通关综合练", "画或读折线、求众数并对照平均、评价随机试验结论。", "趋势、最常见、别说太满。", items=12),
    q(N(31), "boss", "关主：五年级统计通关试炼", "最终关主：①折线读趋势并谨慎预测 ②众数与平均选用 ③根据试验记录作出不超过数据的判断。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g5-statistics",
    "title": "五年级 · 统计与概率",
    "subject": "数学",
    "stage": "小学",
    "grade": 5,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "折线统计图主线与众数支线可并行，在 n018 汇合；再进入简单随机试验与数据分析意识。复式折线自己画（n027）、截断纵轴（n028）、订购与众数（n029）为软锁，不挡终章关主，通关前仍须点亮。中位数见六年级图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-line", f"{P}-boss-mode", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：折线气象员、众数采购员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "小学五年级「统计与概率」地图：折线统计图、众数、简单随机与数据分析意识。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g5-statistics", N(1), f"{N(1)}-explain", N(2), N(13), f"{N(13)}-practice"),
    )


if __name__ == "__main__":
    main()
