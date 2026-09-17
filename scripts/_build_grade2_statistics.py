"""Build Grade 2 Statistics map JSON from a single source of truth.

Run: python3 scripts/_build_grade2_statistics.py

Pedagogical spine (课标第一学段，自撰短描述，非教材页原文):
  提出小问题并收集整理数据
  → 单式统计表、象形图（一图表示1或2）、条形图入门
  → 更可能 / 同样可能等口头描述。
「一周天气小记录」为软锁支线。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-2-statistics"
G = 2
STRAND = "统计与概率"
P = "pm-g2-stat"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "我们想知道什么", 1, [], ["collect", "ch-collect"], "能把好奇写成一个能调查的问题，例如「课间大家最爱玩什么」。", mastery=MASTERY_CONCEPT),
    node(N(2), "用正字或画圈记录", 1, [N(1)], ["collect", "ch-collect", "tally"], "能用画正字或画圈的办法，边问边记，不错记漏记。"),
    node(N(3), "问一问记下来", 2, [N(2)], ["collect", "ch-collect", "survey"], "能向同学收集答案，每人只记一次，并保持类别名称一致。"),
    node(N(4), "整理乱糟糟的记录", 2, [N(3)], ["collect", "ch-collect"], "能把散乱的记号按类别合并，得到每一类的个数。"),
    node(N(5), "单式统计表", 2, [N(4)], ["table", "ch-collect"], "能把类别和个数填进单式统计表，表头写清楚。", mastery=MASTERY_CONCEPT),
    node(N(6), "从表里读信息", 2, [N(5)], ["table", "ch-collect", "read"], "能从表中读出最多、最少、一共，并回答「某一类有几个」。"),
    node(N(7), "收集整理综合", 3, [N(6)], ["collect", "ch-collect", "boss-gate"], "能独立完成「提问—记录—填表—读表」这一小圈。", mastery=MASTERY_GATE),
    node(N(8), "象形图一图表示1", 2, [N(7)], ["pictograph", "ch-chart"], "能画、能读「一个图代表1」的象形图，图与个数一致。", mastery=MASTERY_CONCEPT),
    node(N(9), "象形图一图表示2", 3, [N(8)], ["pictograph", "ch-chart", "scale"], "知道有时一个图可以代表2（或几个），半个图代表一半的数量。", mastery=MASTERY_CONCEPT),
    node(N(10), "象形图别数错", 3, [N(9)], ["pictograph", "ch-chart"], "能根据图例算出真实数量，不把「图的个数」直接当成人数。", mastery=MASTERY_GATE),
    node(N(11), "条形图长什么样", 2, [N(7)], ["bar", "ch-chart"], "能指出条形统计图：直条的高低表示数量多少。", mastery=MASTERY_CONCEPT),
    node(N(12), "横轴类别纵轴数量", 2, [N(11)], ["bar", "ch-chart"], "能说出横轴上是类别、纵轴上是数量，并读出一个直条表示的数。", mastery=MASTERY_CONCEPT),
    node(N(13), "读条形图比多少", 3, [N(12)], ["bar", "ch-chart", "compare"], "能根据条形图比较两类相差多少，找出最多最少。"),
    node(N(14), "根据表画条形图", 3, [N(6), N(13)], ["bar", "ch-chart", "draw"], "能根据统计表画出简单条形图，直条对齐、高低与数量对应。"),
    node(N(15), "看图提出问题", 3, [N(10), N(13)], ["chart", "ch-chart"], "能看着图表自己提出「谁比谁多几个」「一共多少」等问题。", mastery=MASTERY_CONCEPT),
    node(N(16), "图表综合", 4, [N(14), N(15)], ["chart", "ch-chart", "boss-gate"], "能在表、象形图、条形图之间翻译同一组数据。", mastery=MASTERY_GATE),
    node(N(17), "更可能和更不可能", 2, [N(7)], ["chance", "ch-chance"], "能根据哪一类数量更多，口头说「更可能摸到哪一种」。", mastery=MASTERY_CONCEPT),
    node(N(18), "同样可能", 2, [N(17)], ["chance", "ch-chance"], "当两类一样多时，能说「摸到它们的可能性差不多」。", mastery=MASTERY_CONCEPT),
    node(N(19), "用摸棋说可能性", 3, [N(18)], ["chance", "ch-chance"], "能看盒子里的棋子组成，用更可能、同样可能、几乎不可能说话。"),
    node(N(20), "数据帮我判断", 3, [N(16), N(19)], ["mixed", "ch-end"], "能先读调查数据，再对「下一次更可能怎样」做一句有根据的猜测。", mastery=MASTERY_GATE),
    node(N(21), "一周天气小记录", 3, [N(5)], ["collect", "ch-collect", "weather"], "能连续记录几天阴晴雨，整理成表，不要求画复杂图。", unlock=SOFT),
    node(N(22), "调查课间爱玩什么", 3, [N(16)], ["collect", "ch-chart", "project"], "能完成一次小型调查：提问、记录、填表、画简单条形图。", unlock=SOFT),
    node(N(23), "二年级统计合练", 4, [N(20)], ["mixed", "ch-end"], "综合收集、读图、一图表示几个、口头可能性。", mastery=MASTERY_GATE),
    node(N(24), "二年级统计通关", 4, [N(23)], ["mixed", "ch-end", "boss-gate"], "能独立完成收集整理与读图说话的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(8), "to": N(11), "type": "related", "note": "象形图和条形图都在比多少，一个数图、一个看高低。"},
    {"from": N(8), "to": N(9), "type": "easily_confused", "note": "图的个数不等于数量，要先看图例「一个图代表几」。"},
    {"from": N(12), "to": N(14), "type": "easily_confused", "note": "直条要一样宽，比的是高矮，不是画得粗不粗。"},
    {"from": N(6), "to": N(14), "type": "application", "note": "表里的数就是条形图直条的高度。"},
    {"from": N(17), "to": N(18), "type": "easily_confused", "note": "多的一类更可能，不是一定；一样多才说差不多。"},
    {"from": N(3), "to": N(22), "type": "application", "note": "课间调查就是把收集步骤用到真实问题。"},
]


QUESTS = [
    q(N(1), "explain", "写出一个问题", "把「我想知道……」写成一句能问同学的话，并列出准备分的几类。", "问题要能用个数回答，不要问「好不好玩」。"),
    q(N(2), "practice", "正字记录", "听 12 次报类（如苹果/香蕉），用正字记下，核对每类个数。", "五个一横是一个正字，不要写成一串竖线对不齐。", items=12),
    q(N(3), "practice", "每人记一次", "向 8 位同学问同一问题，确保每人只出现一次，类别名称不临时改口。", "先把类别写在纸顶上，再往下打记号。", items=8),
    q(N(4), "practice", "合并记号", "把一张乱序记录按类别圈在一起，写出每类个数。", "先数记号，再填数，不要边数边改类别。", items=1),
    q(N(5), "explain", "填一张单式表", "画出类别、人数两列表头，把整理好的数填进去。", "表头先写，数字对齐。"),
    q(N(6), "practice", "读表六问", "给统计表，回答最多、最少、一共、某类有几个、多几个、少几个。", "「一共」是各类相加。", items=6),
    q(N(7), "practice", "走完一小圈", "自定问题，记录 10 人，填表，读出最多的一类。", "步骤不要跳：问→记→合→表。", items=1),
    q(N(7), "mini_quiz", "收集小测", "看别人的记录找错：漏记、重复记、类别改名。再补填一张表。", "每人只能进表一次。", items=8),
    q(N(7), "boss", "关主：小调查员", "击败关主：①提出能调查的问题 ②用正字记录 ③填表并读出最多最少。", "记录前先约定类别。", xp=80, items=12, qid=f"{P}-boss-collect"),
    q(N(8), "explain", "一图对一人", "把表上的人数画成象形图，一个笑脸代表一人，对齐排列。", "图要一样大，底对齐。"),
    q(N(9), "explain", "一图代表两个", "图例写「一个圆片=2人」。解释 3 个圆片和半个圆片各表示多少人。", "先看图例，再数图、再乘法。"),
    q(N(10), "practice", "按图例算人数", "6 张象形图带不同图例（1 或 2），算出每类真实数量并比较。", "不要数完图就当答案。", items=6),
    q(N(11), "explain", "指出条形图", "在几张图里指出哪张是条形统计图，并说明直条高低表示数量。", "条形图用直条，不是用小星星排队。"),
    q(N(12), "explain", "两个轴", "指着一张条形图说出：横轴写的是什么，纵轴上的刻度表示什么。", "横轴是「谁」，纵轴是「多少」。"),
    q(N(13), "practice", "读条形比多少", "读 4 张条形图，找最多最少，算相差。刻度有 1 格代表 1 或 2。", "先读刻度，再读直条顶到哪。", items=8),
    q(N(14), "practice", "表生条形图", "根据一张 4 类的表画条形图，标上类别和数量。", "直条等宽，从 0 开始长高。", items=1),
    q(N(15), "explain", "我来提问", "看着一张条形图，提出三个不同的数学问题并自己作答。", "问题要能用图上的数回答。"),
    q(N(16), "practice", "三种图互译", "同一组数据：表 ↔ 象形图（一图=2）↔ 条形图，互相检查。", "三种样子里每一类的真实数量必须相同。", items=3),
    q(N(16), "mini_quiz", "图表小测", "混合读表、按图例读象形图、读条形图。夹「忘看图例」的陷阱。", "看见图先找图例。", items=10),
    q(N(16), "boss", "关主：图表翻译官", "击败关主：①按图例读象形图 ②读条形图比多少 ③根据表画出直条。", "翻译时始终核对真实数量。", xp=80, items=12, qid=f"{P}-boss-chart"),
    q(N(17), "explain", "哪一种更常摸到", "盒中 6 红 2 蓝。说明为什么说更可能摸到红，但不能说一定摸到红。", "多只是更常发生，不是每次都发生。"),
    q(N(18), "explain", "一样多就差不多", "盒中 4 红 4 黄。说明为什么说摸到两种的可能性差不多。", "数量一样，没有哪一类占便宜。"),
    q(N(19), "practice", "看盒子选词", "8 个盒子组成不同，选用更可能 / 同样可能 / 几乎不可能。", "先数各类，再选词。", items=8),
    q(N(20), "practice", "有根据的猜测", "先读一张课间活动调查表，再说「下一次抽查更可能看到谁在玩什么」，并引用表中的数。", "猜测要指着数据说话。", items=4),
    q(N(20), "mini_quiz", "数据与可能性小测", "读表+选可能性词语。不要把最多的一类说成一定。", "数据支持「更可能」，很少支持「一定」。", items=8),
    q(N(21), "practice", "记五天天气", "连续记录 5 天阴、晴或雨，填成统计表，说出哪一种最多。", "每天只记一次，类别事先写好。", items=5),
    q(N(22), "practice", "课间小调查", "调查至少 10 人课间爱玩什么，填表并画简单条形图，用一句话汇报。", "类别不要临时增加到没法画。", items=1),
    q(N(23), "practice", "合练卷", "收集步骤改错、按图例读图、画直条、选可能性词。", "按灯的顺序回想。", items=12),
    q(N(24), "practice", "通关综合练", "独立完成：读表、读两种图、根据数据选更可能。", "先找图例和表头。", items=12),
    q(N(24), "boss", "关主：二年级统计通关试炼", "最终关主：①正字记录并填表 ②按图例读图 ③根据数据用更可能说话。全部通过即通关。", "通关后记入已通关列表；图例和「更可能≠一定」要常复习。", xp=100, items=16, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g2-statistics",
    "title": "二年级 · 统计与概率",
    "subject": "数学",
    "stage": "小学",
    "grade": 2,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "从「我们想知道什么」进入：收集整理与单式表 → 象形图（含一图表示几个）与条形图入门 → 更可能/同样可能。一周天气小记录（n021）与课间调查（n022）为软锁，不挡终章关主，通关前仍须点亮。可能性支线可与图表并行，在 n020 汇合。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-collect", f"{P}-boss-chart", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：小调查员、图表翻译官、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "小学二年级「统计与概率」地图：数据收集整理 → 象形图与条形图入门 → 可能性口头比较。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g2-statistics", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
