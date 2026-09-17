"""Build Grade 6 Statistics map JSON from a single source of truth.

Run: python3 scripts/_build_grade6_statistics.py

Pedagogical spine (课标第三学段收束，自撰短描述，非教材页原文):
  扇形统计图（部分占整体）
  → 中位数；选择统计量（平均/中位/众数）与选择统计图
  → 等可能简单概率、综合数据分析。
「容易误导的图」为软锁支线。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-6-statistics"
G = 6
STRAND = "统计与概率"
P = "pm-g6-stat"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "部分占整体", 1, [], ["pie", "ch-pie"], "能说出有些问题关心的是「这一块占全部的多少」，而不只是个数本身。", mastery=MASTERY_CONCEPT),
    node(N(2), "扇形统计图长什么样", 2, [N(1)], ["pie", "ch-pie"], "能指出扇形统计图用整个圆表示总体，用扇形表示各部分。", mastery=MASTERY_CONCEPT),
    node(N(3), "读扇区对应的部分", 2, [N(2)], ["pie", "ch-pie"], "能根据图例读出某一扇区表示哪一类。"),
    node(N(4), "比较扇区大小", 2, [N(3)], ["pie", "ch-pie"], "能比较哪一部分占得最多、最少，并说明依据是扇区大小。"),
    node(N(5), "百分数与扇区", 3, [N(4)], ["pie", "ch-pie", "percent"], "能把扇区旁的百分数读成「每一百份里占几份」，并核对各部分百分数是否合起来合理。", mastery=MASTERY_CONCEPT),
    node(N(6), "由数据想到扇区", 3, [N(5)], ["pie", "ch-pie"], "能根据各类占总体的份数，说明哪一类扇区应该最大。"),
    node(N(7), "扇形图不能看变化", 3, [N(6)], ["pie", "ch-pie", "choose"], "能说明扇形图适合看结构，不适合看随时间的升降。", mastery=MASTERY_CONCEPT),
    node(N(8), "读图提问题", 3, [N(7)], ["pie", "ch-pie"], "能根据扇形图提出「哪一类最多」「大约占几成」等问题并回答。"),
    node(N(9), "扇形图综合", 4, [N(8)], ["pie", "ch-pie", "boss-gate"], "能读扇形图的图例、大小和百分数，并判断它适不适合该问题。", mastery=MASTERY_GATE),
    node(N(10), "把数据排一排队", 2, [N(1)], ["median", "ch-median"], "能把一组数从小到大排列，为找中位数做准备。"),
    node(N(11), "奇数个的中位数", 3, [N(10)], ["median", "ch-median"], "个数是奇数时，能指出最中间的那个数就是中位数。", mastery=MASTERY_CONCEPT),
    node(N(12), "偶数个的中位数", 3, [N(11)], ["median", "ch-median"], "个数是偶数时，能取最中间两个数的平均数作为中位数。"),
    node(N(13), "中位数不怕极端值", 3, [N(12)], ["median", "ch-median"], "能发现一个特别大的数会拉动平均数，但不轻易改变中位数。", mastery=MASTERY_CONCEPT),
    node(N(14), "中位数适合什么", 3, [N(13)], ["median", "ch-median"], "能举例：成绩或身高这种「中间位置」用中位数常常更稳。", mastery=MASTERY_CONCEPT),
    node(N(15), "三种统计量对照", 4, [N(9), N(14)], ["median", "ch-stat"], "能对同一组数据求平均、中位数、众数（若有），并各用一句话说它们的分工。", mastery=MASTERY_GATE),
    node(N(16), "选择合适的统计量", 4, [N(15)], ["stat", "ch-stat"], "能根据问题选择平均、中位数或众数，并说明理由。"),
    node(N(17), "选择合适的统计图", 4, [N(16)], ["stat", "ch-stat", "choose"], "能在条形、折线、扇形之间选择：比多少、看变化、看结构。", mastery=MASTERY_GATE),
    node(N(18), "一张图一个结论", 3, [N(17)], ["stat", "ch-stat"], "能根据选定的图写出一句不超过数据范围的结论。"),
    node(N(19), "统计选择综合", 4, [N(18)], ["stat", "ch-stat", "boss-gate"], "能完成「选统计量 + 选统计图 + 写谨慎结论」。", mastery=MASTERY_GATE),
    node(N(20), "等可能是什么", 2, [N(9)], ["prob", "ch-prob"], "能说明：每种结果发生的机会一样时，才适合用「几份里占几份」来描述。", mastery=MASTERY_CONCEPT),
    node(N(21), "全部结果要列全", 3, [N(20)], ["prob", "ch-prob"], "能列出等可能试验的全部结果，作为计算的分母。"),
    node(N(22), "用几分之几表示可能性", 3, [N(21)], ["prob", "ch-prob"], "能用分数表示简单等可能事件的可能性，如公平硬币正面是 1/2。"),
    node(N(23), "复合一点的计数", 4, [N(22)], ["prob", "ch-prob"], "能在「两个不同转盘」或「摸一颗不放回前先列树」的简单情形里数出有利结果。", mastery=MASTERY_GATE),
    node(N(24), "可能性大小用分数比", 3, [N(22)], ["prob", "ch-prob"], "能比较两个分数形式的可能性谁更大。"),
    node(N(25), "试验频率和分数", 3, [N(23), N(24)], ["prob", "ch-prob"], "能把试验中的频率和理论上的几分之几对照，说明次数少时会对不齐。", mastery=MASTERY_CONCEPT),
    node(N(26), "随机与数据合练", 4, [N(19), N(25)], ["mixed", "ch-end"], "能在同一课题里选图、选统计量，并用分数描述简单等可能事件。", mastery=MASTERY_GATE),
    node(N(27), "容易误导的图", 4, [N(17)], ["stat", "ch-data"], "能指出扇区没标清、立体扇形看起来一块更大、纵轴截断等误导手法。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "自己做一张结构图", 3, [N(9)], ["pie", "ch-pie"], "能把班级调查的各类占总体情况，整理成扇形图草图并标百分数（可用估算）。", unlock=SOFT),
    node(N(29), "校园数据小报告", 4, [N(26)], ["mixed", "ch-end", "project"], "能围绕一个校园问题选择图表与统计量，写出不超过数据的三句话结论。", unlock=SOFT),
    node(N(30), "小学统计常用工具箱", 4, [N(26)], ["mixed", "ch-end"], "能用一张清单说出：表、条形、折线、扇形、平均、中位、众数、简单概率各解决什么。", mastery=MASTERY_CONCEPT),
    node(N(31), "六年级统计合练", 5, [N(30)], ["mixed", "ch-end"], "综合扇形图、中位数与选择、简单概率分数。", mastery=MASTERY_GATE),
    node(N(32), "六年级统计通关", 5, [N(31)], ["mixed", "ch-end", "boss-gate"], "能独立完成小学统计与概率线的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(7), "type": "easily_confused", "note": "扇形图看结构，折线图看变化，不要拿扇形图描述「越来越高」。"},
    {"from": N(11), "to": N(12), "type": "easily_confused", "note": "奇数个取正中间；偶数个要再平均一次中间两个。"},
    {"from": N(12), "to": N(13), "type": "related", "note": "中位数看位置，平均数看总和，极端值对它们的影响不同。"},
    {"from": N(15), "to": N(16), "type": "easily_confused", "note": "三个统计量可以并存，选用取决于问题，不是谁更高级。"},
    {"from": N(7), "to": N(17), "type": "application", "note": "会判断扇形图的用途，才能在三种图里做选择。"},
    {"from": N(20), "to": N(22), "type": "easily_confused", "note": "不是等可能时，不能直接用「结果种数」当分数分母。"},
    {"from": N(17), "to": N(27), "type": "application", "note": "会选图之后，还要会识破故意画歪的图。"},
]


QUESTS = [
    q(N(1), "explain", "问结构还是问个数", "举「喜欢某项运动的人数」和「这项占全班几成」两个问法，说明后者在看部分与整体。", "占整体，才需要扇形这样的图。"),
    q(N(2), "explain", "圆是总体", "指着扇形图说明整个圆是全部，某一块扇形是其中一类。", "各块合起来应该是整个圆。"),
    q(N(3), "practice", "图例对扇区", "6 张扇形图，把类别和图例、扇区对上。", "先看图例，再看哪一块。", items=6),
    q(N(4), "practice", "哪块最大", "不看百分数，只比较扇区大小，判断最多最少，共 6 题。", "张角更大通常占得更多。", items=6),
    q(N(5), "practice", "读百分数", "核对各部分百分数是否大约合为 100%，并读出指定类占几成。", "百分数合起来应接近一百。", items=6),
    q(N(6), "explain", "数据决定哪块大", "给出四类人数，说明哪一类扇区最大、哪一类最小，不必精确画角。", "人数多的类，扇区就该更大。"),
    q(N(7), "explain", "别用扇形看趋势", "「一周体温变化」该用什么图？说明为什么扇形图不合适。", "扇形没有时间顺序。"),
    q(N(8), "practice", "看图提问作答", "给扇形图提出并回答三问：最多、约占几成、两类合起来约占多少。", "两类合起来要把百分数相加。", items=3),
    q(N(9), "practice", "扇形图闯关", "读图例、比大小、核对百分数、判断是否该用扇形图。", "先问：这是在看结构吗？", items=8),
    q(N(9), "mini_quiz", "扇形图小测", "混合读图与选择图种。夹「用扇形图表示气温变化」的错误例子。", "结构用扇形，变化用折线。", items=10),
    q(N(9), "boss", "关主：扇形结构员", "击败关主：①指出总体和部分 ②读百分数并比较 ③判断三个情境该不该用扇形图。", "整个圆是 100%。", xp=80, items=12, qid=f"{P}-boss-pie"),
    q(N(10), "practice", "从小到大排", "8 组无序数据，排成递增序列。", "先排再找中间，不要跳步。", items=8),
    q(N(11), "practice", "奇数个找中间", "6 组奇数个数据求中位数。", "排好后左右人数一样多。", items=6),
    q(N(12), "practice", "偶数个取平均", "6 组偶数个数据求中位数。", "中间两个加起来除以 2。", items=6),
    q(N(13), "practice", "拉开平均但不拉中位", "同一组数据加入一个特别大的数，分别看平均和中位数怎么变。", "平均会被拽走，中位数常常还在原处附近。", items=3),
    q(N(14), "explain", "什么时候用中位数", "在「有一个特别高的分数」的小组成绩里，说明为什么中位数更能代表中间水平。", "中间位置，不受一个极端分数左右。"),
    q(N(15), "practice", "三个数各算一遍", "4 组数据分别求平均、中位数、众数（没有则写无），并各写一句用途。", "三种量可以同时存在。", items=4),
    q(N(16), "practice", "按问题选量", "8 个问题选择平均 / 中位数 / 众数。", "最常见→众数；中间位置→中位；拉齐→平均。", items=8),
    q(N(17), "practice", "按问题选图", "8 个问题选择条形 / 折线 / 扇形。", "比多少、看变化、看结构，三把钥匙。", items=8),
    q(N(18), "explain", "一句谨慎结论", "根据给定图表写一句结论，避免「所有人」「一定」等越界词。", "结论里的对象要和图上的对象一致。"),
    q(N(19), "practice", "选择综合", "一个校园情境：选统计量、选图、写结论。", "先问问题要什么，再选工具。", items=1),
    q(N(19), "mini_quiz", "选择小测", "混合选量、选图、改越界结论。", "工具没有高低，只有合适不合适。", items=10),
    q(N(19), "boss", "关主：统计工具选配师", "击败关主：①同一组数据三种统计量 ②三个情境选对图 ③把一句说过头的结论改谨慎。", "先问问题，再选刀。", xp=80, items=12, qid=f"{P}-boss-choose"),
    q(N(20), "explain", "什么叫同样可能", "公平骰子六点同样可能；被做了手脚的骰子不是。用自己的话区分。", "没有理由偏袒某一面时，才当等可能。"),
    q(N(21), "practice", "列全部分母", "4 个试验列出全部等可能结果，作为分母。", "不重复、不遗漏。", items=4),
    q(N(22), "practice", "写成分数", "8 个简单事件写成几分之几，如「从 1–5 号球摸到偶数」。", "有利结果个数 / 全部结果个数。", items=8),
    q(N(23), "practice", "数有利结果", "两个一步试验（不同颜色棋、两枚公平硬币）列出树状或表，再写分数。", "先列全，再圈有利的。", items=4),
    q(N(24), "practice", "比两个分数", "比较可能性 1/2 和 1/3 等，共 6 题，可用画图或通分。", "分母不同时先变成一样的整体。", items=6),
    q(N(25), "explain", "频率会对齐吗", "理论上 1/2，试验 10 次可能 7 次正面。说明次数少时频率会晃，次数多了更靠近。", "分数是模型，频率是试验，二者会越来越近但不保证次次相等。"),
    q(N(26), "practice", "课题里两手抓", "给一个小课题：选图描述结构或变化，再用分数说一个等可能事件。", "统计描述已有数据，概率描述尚未发生的等可能结果。", items=1),
    q(N(27), "practice", "给误导图找茬", "4 张容易误导的图，指出问题并改写成读图注意事项。", "立体、截轴、无图例是常客。", items=4),
    q(N(28), "practice", "结构草图", "用本班四类人数（可假设合理数据）画扇形草图，标百分数，核对合计。", "百分数合计应接近 100%。", items=1),
    q(N(29), "practice", "三句话报告", "自选校园问题，写：用了什么图、什么统计量、一句不越界的结论。", "三句话都要指着数据。", items=1),
    q(N(30), "explain", "打开工具箱", "用清单说出至少六种小学统计工具各解决什么问题。", "对号入座，不堆砌术语。"),
    q(N(31), "practice", "合练卷", "扇形图+中位数+选图选量+简单概率分数。", "先辨题型。", items=12),
    q(N(32), "practice", "通关综合练", "读扇形、求中位数并对照平均、选图、写 1/2 这类分数。", "结构、中间位置、等可能，三件齐。", items=12),
    q(N(32), "boss", "关主：六年级统计通关试炼", "最终关主：①读扇形图 ②求中位数并选择统计量/统计图 ③用分数表示简单等可能事件。小学统计与概率线在此收束。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g6-statistics",
    "title": "六年级 · 统计与概率",
    "subject": "数学",
    "stage": "小学",
    "grade": 6,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "扇形统计图与中位数可并行，在 n015 汇合后选择统计量/统计图；简单等可能概率从扇形关后并行，在 n026 汇合。容易误导的图（n027）、自己做结构图（n028）、校园数据小报告（n029）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-pie", f"{P}-boss-choose", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：扇形结构员、统计工具选配师、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "小学六年级「统计与概率」地图：扇形统计图、中位数、选择统计工具、简单等可能概率。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g6-statistics", N(1), f"{N(1)}-explain", N(2), N(10), f"{N(10)}-practice"),
    )


if __name__ == "__main__":
    main()
