"""Build Grade 3 Statistics map JSON from a single source of truth.

Run: python3 scripts/_build_grade3_statistics.py

Pedagogical spine (课标第二学段前段，自撰短描述，非教材页原文):
  有目的地收集整理、单式表巩固
  → 复式统计表
  → 条形统计图（1格代表1、2、5）
  → 可能性入门：列出所有可能结果。
「两种标准交叉分类」为软锁支线。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-3-statistics"
G = 3
STRAND = "统计与概率"
P = "pm-g3-stat"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "先把问题问清楚", 1, [], ["collect", "ch-table"], "能把调查目的说成一句清楚的问题，并预想需要哪些类别。", mastery=MASTERY_CONCEPT),
    node(N(2), "设计记录格子", 2, [N(1)], ["collect", "ch-table"], "能设计简单记录表：类别预先写好，避免事后再发明类别。", mastery=MASTERY_CONCEPT),
    node(N(3), "按计划收集", 2, [N(2)], ["collect", "ch-table"], "能按记录表收集数据，不重复、不遗漏，类别不中途改名。"),
    node(N(4), "单式表复习", 2, [N(3)], ["table", "ch-table"], "能把收集结果整理成单式统计表，并检查合计。"),
    node(N(5), "从表里作比较", 2, [N(4)], ["table", "ch-table", "compare"], "能用单式表比较两类相差多少，说明「多几、少几」。"),
    node(N(6), "根据问题选数据", 3, [N(5)], ["table", "ch-table"], "能根据问题只取表中需要的几格，不把无关数字全加起来。"),
    node(N(7), "单式表综合", 3, [N(6)], ["table", "ch-table", "boss-gate"], "能独立完成有目的的收集，并用单式表回答三个问题。", mastery=MASTERY_GATE),
    node(N(8), "两种标准一起看", 2, [N(7)], ["compound", "ch-compound"], "知道有时既要看「喜欢什么」，又要看「男生女生」，一张表要放下两个标准。", mastery=MASTERY_CONCEPT),
    node(N(9), "复式表的表头", 3, [N(8)], ["compound", "ch-compound"], "能认复式统计表的表头：一个方向是一种标准，另一个方向是另一种标准。", mastery=MASTERY_CONCEPT),
    node(N(10), "读复式表一格", 3, [N(9)], ["compound", "ch-compound", "read"], "能读出复式表中某一格的意义，例如「女生里喜欢跳绳的有几人」。"),
    node(N(11), "读复式表合计", 3, [N(10)], ["compound", "ch-compound"], "能读行合计、列合计，并核对这些合计是否对得上。"),
    node(N(12), "填写复式表", 4, [N(11)], ["compound", "ch-compound"], "能把原始记录填进复式表，每一人只进一格。", mastery=MASTERY_GATE),
    node(N(13), "用复式表讲差别", 3, [N(12)], ["compound", "ch-compound"], "能根据复式表说出两组之间的不同，不把两组混成一组说。", mastery=MASTERY_CONCEPT),
    node(N(14), "复式表综合", 4, [N(13)], ["compound", "ch-compound", "boss-gate"], "能读、填、解释一张复式统计表，并发现合计错误。", mastery=MASTERY_GATE),
    node(N(15), "条形图1格代表1", 2, [N(7)], ["bar", "ch-bar"], "能读、画 1 格代表 1 的条形统计图。", mastery=MASTERY_CONCEPT),
    node(N(16), "1格代表2或5", 3, [N(15)], ["bar", "ch-bar", "scale"], "当数量较大时，能用 1 格代表 2 或 5，并按刻度读数。", mastery=MASTERY_CONCEPT),
    node(N(17), "读准直条高度", 3, [N(16)], ["bar", "ch-bar"], "能读出直条顶端对准的刻度，包括落在两格之间的大约数。"),
    node(N(18), "根据表画条形图", 3, [N(12), N(17)], ["bar", "ch-bar", "draw"], "能选择合适的 1 格代表几，根据表画出条形图。"),
    node(N(19), "条形图和表互译", 3, [N(18)], ["bar", "ch-bar"], "能把条形图还原成统计表，或把表画成条形图，数量一致。"),
    node(N(20), "看图提出并回答", 3, [N(19)], ["bar", "ch-bar"], "能根据条形图提出「相差、一共、哪一类」问题并解答。"),
    node(N(21), "条形图综合", 4, [N(14), N(20)], ["bar", "ch-bar", "boss-gate"], "能结合复式表或单式表，选择刻度并完成读图、画图。", mastery=MASTERY_GATE),
    node(N(22), "可能发生的所有结果", 2, [N(7)], ["chance", "ch-chance"], "能列出简单随机现象的所有可能结果，如硬币正反、盒子里三种颜色。", mastery=MASTERY_CONCEPT),
    node(N(23), "哪一种更容易发生", 3, [N(22)], ["chance", "ch-chance"], "能根据「结果是不是一样多」口头比较可能性大小。", mastery=MASTERY_CONCEPT),
    node(N(24), "转盘和摸棋", 3, [N(23)], ["chance", "ch-chance"], "能看转盘扇区或棋子组成，说出更可能停在哪一区、摸到哪一色。"),
    node(N(25), "数据与可能性合练", 4, [N(21), N(24)], ["mixed", "ch-end"], "能先用表或条形图整理，再列出可能结果并比较可能性。", mastery=MASTERY_GATE),
    node(N(26), "两种标准交叉分类", 3, [N(14)], ["compound", "ch-compound"], "能自己设计「是否戴眼镜 × 座位组」这类交叉分类并填复式表。", unlock=SOFT),
    node(N(27), "三年级统计合练", 4, [N(25)], ["mixed", "ch-end"], "综合复式表、条形图刻度、列出所有可能结果。", mastery=MASTERY_GATE),
    node(N(28), "三年级统计通关", 4, [N(27)], ["mixed", "ch-end", "boss-gate"], "能独立完成第二学段入门的统计与可能性收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(5), "to": N(8), "type": "related", "note": "单式表只有一个标准；再加一个标准就走向复式表。"},
    {"from": N(9), "to": N(10), "type": "easily_confused", "note": "一格是「某一行且某一列」的交叉，不是整行的合计。"},
    {"from": N(11), "to": N(12), "type": "easily_confused", "note": "行合计加起来应等于列合计加起来，都等于总人数。"},
    {"from": N(15), "to": N(16), "type": "easily_confused", "note": "格数不是数量，要乘「1格代表几」。"},
    {"from": N(7), "to": N(15), "type": "application", "note": "单式表里的数可以直接变成直条高度。"},
    {"from": N(22), "to": N(23), "type": "easily_confused", "note": "列出所有结果，不等于每种结果一样容易发生。"},
    {"from": N(8), "to": N(26), "type": "application", "note": "交叉分类就是把两个标准同时用到同一群人。"},
]


QUESTS = [
    q(N(1), "explain", "问句要能调查", "把「同学们的课余爱好」改写成一句能收集个数的问题，并列出 3–4 个类别。", "避免「开不开心」这种没法计数的问法。"),
    q(N(2), "explain", "先画格子", "设计一张记录表：表头、类别、打勾栏。解释为什么不边问边发明新类。", "类别事先约定，收集才不乱。"),
    q(N(3), "practice", "收集 12 人", "按记录表询问 12 人，每人只进一类，完成后核对总人数。", "总人数必须等于 12。", items=12),
    q(N(4), "practice", "整理成单式表", "把记录合并成统计表，写出合计，并检查合计是否等于总人数。", "合计是验算用的。", items=1),
    q(N(5), "practice", "相差多少", "用表计算三类两两相差，共 6 问。", "大的减小的，写明是谁比谁多。", items=6),
    q(N(6), "practice", "只取有用的格", "问题只涉及表中两列，避免把第三列加进去。做 5 题。", "先圈出问题提到的类别。", items=5),
    q(N(7), "practice", "收集小闭环", "自定问题，收集不少于 10 人，填表并回答三个问题。", "目的、类别、合计三件都要齐。", items=1),
    q(N(7), "mini_quiz", "单式表小测", "读表、算相差、找合计错误。", "合计不对，表就不能用。", items=8),
    q(N(7), "boss", "关主：有目的的收集", "击败关主：①写清调查问题 ②填单式表并核对合计 ③只取需要的数据答题。", "先问目的，再动笔。", xp=80, items=12, qid=f"{P}-boss-table"),
    q(N(8), "explain", "两个问题一张表", "说明：只问「爱看什么书」不够，还想比较男生女生时，为什么一张单式表不够用。", "两个标准交叉，格子会变多。"),
    q(N(9), "explain", "指表头", "指着复式表说明哪一侧是性别、哪一侧是爱好，交叉格表示什么。", "先读两个方向的表头，再读格子。"),
    q(N(10), "practice", "读一格的意思", "10 问：读出「某行某列」是什么意思、是多少人。", "用手指划十字定位。", items=10),
    q(N(11), "practice", "核对合计", "给带错误合计的复式表，找出错的行或列并改正。", "行总和应等于列总和。", items=4),
    q(N(12), "practice", "把人填进格", "20 条原始记录（姓名已隐去，只留两个标准），填进复式表。", "一人只占一格。", items=20),
    q(N(13), "explain", "两组有什么不同", "根据复式表说两句：男生里最多的是什么，女生里最多的是什么，二者是否相同。", "不要把两组加在一起再比「最多」。"),
    q(N(14), "practice", "复式表闯关", "读格、改合计、解释差别，共 8 问。", "十字定位 + 合计验算。", items=8),
    q(N(14), "mini_quiz", "复式表小测", "混合读格、填表、合计。夹「把行合计当成一格」的陷阱。", "合计不是交叉格。", items=10),
    q(N(14), "boss", "关主：复式表解读员", "击败关主：①读交叉格 ②核对合计 ③根据表比较两组。", "两个表头都要读到。", xp=80, items=12, qid=f"{P}-boss-compound"),
    q(N(15), "explain", "一格一人", "根据 1 格代表 1 的条形图读出三类数量。", "从 0 开始数格。"),
    q(N(16), "practice", "换刻度读数", "1 格代表 2 或 5 的图各两张，读出数量并比较。", "格数×每格代表的数。", items=8),
    q(N(17), "practice", "读到半格", "直条停在两刻度中间时，说出大约数，并说明为什么不是随便猜。", "先看相邻两个刻度，再估计中间。", items=6),
    q(N(18), "practice", "选刻度再画", "数据在 20 左右，选择 1 格代表 2 或 5，画出条形图。", "刻度太大图太矮，太小画不下。", items=1),
    q(N(19), "practice", "图和表对换", "图还原成表，表画成图，各一次，核对每个数。", "对换后数量必须一字不差。", items=2),
    q(N(20), "explain", "看图出题", "给条形图出三道题并作答，其中一道必须是相差。", "题目要用到图上至少两个数。"),
    q(N(21), "practice", "表图联动", "一张复式表取其中一组画条形图，并回答两组差异。", "先决定画哪一组，再选刻度。", items=1),
    q(N(21), "mini_quiz", "条形图小测", "读刻度、画直条、图与表互译。", "先找 1 格代表几。", items=10),
    q(N(22), "explain", "列出所有结果", "硬币正反；袋子里红黄蓝各一颗摸一颗。分别列出所有可能结果。", "不重复、不遗漏，先不管哪一种更容易。"),
    q(N(23), "explain", "一样多才同样可能", "公平硬币两种结果同样可能；盒子 5 红 1 蓝则摸到红更容易。用自己的话说区别。", "结果种类和每类有几个，不是一回事。"),
    q(N(24), "practice", "看转盘说话", "6 个转盘或盒子，选更可能停在哪、摸到哪，并列出全部结果。", "扇区更大或棋子更多，通常更可能。", items=6),
    q(N(25), "practice", "先整理再判断", "先把摸棋记录填表，再说明下一次更可能摸到什么，同时列出所有颜色。", "数据说明「更可能」，列表说明「有哪些可能」。", items=4),
    q(N(26), "practice", "交叉分类小调查", "选两个标准调查至少 12 人，填复式表并核对合计。", "两个标准都要事先写好。", items=1),
    q(N(27), "practice", "合练卷", "复式表+条形刻度+列出可能结果。", "三种题型先分类再做。", items=12),
    q(N(28), "practice", "通关综合练", "读复式表、按刻度读条形图、列出摸棋的所有结果并比较可能性。", "表头、刻度、全部结果，三件都要齐。", items=12),
    q(N(28), "boss", "关主：三年级统计通关试炼", "最终关主：①复式表读格与合计 ②按 1 格代表几读/画条形图 ③列出所有可能结果并比较可能性。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g3-statistics",
    "title": "三年级 · 统计与概率",
    "subject": "数学",
    "stage": "小学",
    "grade": 3,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "有目的收集与单式表 → 复式统计表 → 条形图刻度；可能性（列出全部结果）可与条形图并行，在 n025 汇合。两种标准交叉分类（n026）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-table", f"{P}-boss-compound", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：有目的的收集、复式表解读员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "小学三年级「统计与概率」地图：复式统计表、条形图与可能性入门。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g3-statistics", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
