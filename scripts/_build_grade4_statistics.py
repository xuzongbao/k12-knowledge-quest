"""Build Grade 4 Statistics map JSON from a single source of truth.

Run: python3 scripts/_build_grade4_statistics.py

Pedagogical spine (课标第二学段，自撰短描述，非教材页原文):
  条形图进阶（复式条形图、选择 1 格代表几）
  → 平均数的意义与计算、用平均数比较
  → 可能性大小：列出结果并定性比较。
「选择合适的单位格」为软锁支线。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-4-statistics"
G = 4
STRAND = "统计与概率"
P = "pm-g4-stat"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "读条形图复习", 1, [], ["bar", "ch-bar"], "能读单式条形图的类别、刻度和直条高度，说出最多最少。", mastery=MASTERY_CONCEPT),
    node(N(2), "1格代表几要先看", 2, [N(1)], ["bar", "ch-bar", "scale"], "读图前先确认 1 格代表几，避免把格数当成数量。", mastery=MASTERY_CONCEPT),
    node(N(3), "较大数据的条形图", 2, [N(2)], ["bar", "ch-bar"], "当数据到几十、几百时，能选用 1 格代表 5、10 等来读图。"),
    node(N(4), "复式条形图是什么", 2, [N(1)], ["bar", "ch-bar", "compound"], "能认出复式条形图：同一类别旁有两组直条，便于比较两组。", mastery=MASTERY_CONCEPT),
    node(N(5), "读复式条形图", 3, [N(3), N(4)], ["bar", "ch-bar", "compound"], "能读出某一类别两组各是多少，并比较同一类别哪组更多。"),
    node(N(6), "复式条形图的图例", 3, [N(5)], ["bar", "ch-bar"], "能根据图例区分两种直条代表哪一组，不看错颜色或花纹。", mastery=MASTERY_CONCEPT),
    node(N(7), "根据复式表画复式条形图", 4, [N(6)], ["bar", "ch-bar", "draw"], "能把复式统计表画成复式条形图，两组直条对齐、图例清楚。", mastery=MASTERY_GATE),
    node(N(8), "看图比较两组", 3, [N(7)], ["bar", "ch-bar"], "能根据复式条形图说出两组整体上有什么不同。", mastery=MASTERY_CONCEPT),
    node(N(9), "从图中发现问题", 3, [N(8)], ["bar", "ch-bar"], "能指出直条对不齐、图例缺失、刻度不是从 0 开始等不规范处。"),
    node(N(10), "条形图综合", 4, [N(9)], ["bar", "ch-bar", "boss-gate"], "能读、画、评价单式与复式条形图。", mastery=MASTERY_GATE),
    node(N(11), "平均是在拉齐", 2, [N(1)], ["average", "ch-avg"], "能用「移多补少、拉成一样长」说明平均数在讲什么。", mastery=MASTERY_CONCEPT),
    node(N(12), "平均数怎么算", 3, [N(11)], ["average", "ch-avg"], "能用「总和÷个数」求出一组简单数据的平均数。"),
    node(N(13), "除不尽的平均数", 3, [N(12)], ["average", "ch-avg"], "当除不尽时，能按要求保留整数或一位小数，并说明这是大约拉齐后的数。", mastery=MASTERY_CONCEPT),
    node(N(14), "平均数不一定是实际有的数", 3, [N(13)], ["average", "ch-avg"], "知道平均后的数可以不是原来任何一个数据，例如人均不是某一个人的个数。", mastery=MASTERY_CONCEPT),
    node(N(15), "用平均数比两组", 3, [N(14)], ["average", "ch-avg", "compare"], "能用两组的平均数比较整体水平，同时提醒人数不同时要小心。"),
    node(N(16), "一个特别大的数", 4, [N(15)], ["average", "ch-avg"], "能发现一个特别大或特别小的数会把平均数拉偏。", mastery=MASTERY_GATE),
    node(N(17), "根据总数和平均想个数", 3, [N(12)], ["average", "ch-avg"], "能用「平均数×个数=总和」解决简单问题。"),
    node(N(18), "看图估计平均", 3, [N(10), N(15)], ["average", "ch-avg", "bar"], "能根据条形图估计哪一组平均更高，再计算验证。"),
    node(N(19), "平均数解决问题", 3, [N(16), N(17)], ["average", "ch-avg", "application"], "能在「人均、平均每天」的情境中选择求平均或还原总和。"),
    node(N(20), "平均数综合", 4, [N(18), N(19)], ["average", "ch-avg", "boss-gate"], "能计算、解释并用平均数比较，同时说出它的局限。", mastery=MASTERY_GATE),
    node(N(21), "列出所有可能结果", 2, [N(10)], ["chance", "ch-chance"], "能有序列出简单随机现象的所有可能结果，不重复不遗漏。", mastery=MASTERY_CONCEPT),
    node(N(22), "等可能与不等可能", 3, [N(21)], ["chance", "ch-chance"], "能区分「结果种类一样多且公平」和「有的结果更常出现」。", mastery=MASTERY_CONCEPT),
    node(N(23), "可能性大小比较", 3, [N(22)], ["chance", "ch-chance"], "能用更大、更小、一样大描述可能性，不要求写分数。"),
    node(N(24), "转盘扇区与棋子数量", 3, [N(23)], ["chance", "ch-chance"], "能根据扇区大小或棋子数量比较可能性，并说明依据。"),
    node(N(25), "试验记录与判断", 3, [N(24)], ["chance", "ch-chance"], "能做少量摸棋记录，说明次数少时结果会晃，不能只凭两三次下结论。", mastery=MASTERY_CONCEPT),
    node(N(26), "统计与可能性合练", 4, [N(20), N(25)], ["mixed", "ch-end"], "能先用表或平均数整理数据，再对随机现象比较可能性。", mastery=MASTERY_GATE),
    node(N(27), "选择合适的单位格", 3, [N(10)], ["bar", "ch-bar", "scale"], "能为一组数据选择 1 格代表几，使图既画得下又分得出高低。", unlock=SOFT),
    node(N(28), "人均不是每人", 3, [N(20)], ["average", "ch-avg"], "能用自己的话解释：班均图书 8 本，不是每个人都恰好有 8 本。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(29), "四年级统计合练", 4, [N(26)], ["mixed", "ch-end"], "综合复式条形图、平均数、可能性大小。", mastery=MASTERY_GATE),
    node(N(30), "四年级统计通关", 4, [N(29)], ["mixed", "ch-end", "boss-gate"], "能独立完成条形图进阶、平均数与可能性的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(4), "to": N(6), "type": "easily_confused", "note": "复式条形图必须先看图例，否则两组直条会读反。"},
    {"from": N(11), "to": N(12), "type": "related", "note": "移多补少的结果，和总和除以个数，说的是同一件事。"},
    {"from": N(12), "to": N(14), "type": "easily_confused", "note": "平均数可以是「没有人恰好等于它」的数。"},
    {"from": N(15), "to": N(16), "type": "easily_confused", "note": "平均数会被极端数据拉开，不能只看平均就断定每个人。"},
    {"from": N(21), "to": N(22), "type": "easily_confused", "note": "列出四种结果，不等于四种一样可能。"},
    {"from": N(10), "to": N(18), "type": "application", "note": "条形图的高低可以帮助估计哪一组平均更大。"},
    {"from": N(2), "to": N(27), "type": "application", "note": "选单位格就是主动决定 1 格代表几。"},
]


QUESTS = [
    q(N(1), "explain", "读一张条形图", "读出类别、最多最少，并说明刻度从几开始。", "先看轴，再看直条顶端。"),
    q(N(2), "practice", "先找单位格", "6 张图的 1 格代表 1、2、5、10 不等，先写下单位再读数。", "没有单位格就不要读数。", items=6),
    q(N(3), "practice", "读较大的数", "数据在几十到一百的条形图 4 张，读准高度。", "10 格×每格 10 就是 100。", items=8),
    q(N(4), "explain", "两组直条", "指出哪张是复式条形图，说明同一类别为什么有两根直条。", "两根条是为了并排比较两组。"),
    q(N(5), "practice", "读两组", "复式条形图 4 张，读指定类别两组的数量并比较。", "先锁定类别，再读两根条。", items=8),
    q(N(6), "explain", "图例对上号", "把图例颜色和组别连线，再说一句「左边这根表示……」。", "图例是翻译器。"),
    q(N(7), "practice", "表画复式条形图", "根据 3×2 的复式表画复式条形图，补全图例和类别。", "同一类别的两根条要靠在一起。", items=1),
    q(N(8), "explain", "两组整体不同", "看着复式条形图，用两句话比较两组：哪一组整体更高，哪一类差别最大。", "不要只看一个类别。"),
    q(N(9), "practice", "给图找茬", "5 张不规范条形图（没图例、刻度不从 0、直条不等宽），指出问题。", "先检查 0 点、图例、直条宽度。", items=5),
    q(N(10), "practice", "条形图闯关", "读单式、读复式、改错图各 2 题。", "图例和单位格每次都要先看。", items=6),
    q(N(10), "mini_quiz", "条形图小测", "混合刻度、复式图例、找不规范。", "读图三步：单位、图例、直条。", items=10),
    q(N(10), "boss", "关主：条形图测绘员", "击败关主：①按单位格读图 ②读复式条形图 ③指出一张不规范图的问题。", "没有图例不要猜哪一组。", xp=80, items=12, qid=f"{P}-boss-bar"),
    q(N(11), "explain", "移多补少", "用 3 根不同长度的纸条，把长的剪一段补给短的，直到一样长，说明这就是「平均」。", "平均是拉齐后的长度，不是最长也不是最短。"),
    q(N(12), "practice", "算平均数", "8 组数据（2–6 个数）求平均数，数字控制在可口算或简算范围。", "先求和，再除以个数。", items=8),
    q(N(13), "practice", "除不尽怎么办", "4 组除不尽的数据，按题目保留整数或一位小数。", "写出「大约」或按要求取近似。", items=4),
    q(N(14), "explain", "平均可以没有人等于它", "举例：4 人分别有 1、1、1、5 支笔，平均 2 支，但没有人恰好 2 支。", "平均数描述这组，不保证是某个人的数。"),
    q(N(15), "practice", "两组比平均", "两组人数相同或不同的数据，先算平均再比较，并写一句注意。", "人数不同时，只比平均，不比总和。", items=4),
    q(N(16), "practice", "拉开的平均数", "同一组数据去掉一个特别大的数，再算平均，说说变了多少。", "极端数据会把平均拽过去。", items=3),
    q(N(17), "practice", "由平均还原", "已知平均和个数求总和，或已知总和与平均求个数。共 6 题。", "总和＝平均×个数。", items=6),
    q(N(18), "practice", "看条形估平均", "先估哪一组平均更高，再计算验证，共 3 组图。", "特别高的一根条会把平均抬起来。", items=3),
    q(N(19), "practice", "人均情境", "平均每天、人均本数等 6 个短情境，选择求平均还是还原总和。", "问整体用乘法，问水平用除法。", items=6),
    q(N(20), "practice", "平均数闯关", "计算、解释「不是每人恰好」、比较两组、指出极端值影响。", "会算还要会说它的局限。", items=8),
    q(N(20), "mini_quiz", "平均数小测", "混合计算、还原、比较、极端值。", "先看问的是总和、个数还是平均。", items=10),
    q(N(20), "boss", "关主：平均数调解员", "击败关主：①算平均 ②说明平均可以不是实际有的数 ③比较两组并指出一个极端值的影响。", "平均是拉齐，不是每个人。", xp=80, items=12, qid=f"{P}-boss-average"),
    q(N(21), "explain", "有序列出", "摸两颗不同颜色棋子的顺序（先红后黄、先黄后红等），列出全部结果。", "顺序不同算不同结果时，要写全。"),
    q(N(22), "explain", "公平和不公平", "公平硬币与「一边更重的硬币」对比：结果都是正反，可能性却不一定一样。", "有哪些结果，和是否同样可能，要分开说。"),
    q(N(23), "practice", "比可能性", "8 个情境用更大/更小/一样大描述，不写分数。", "先看是否公平，再看数量或扇区。", items=8),
    q(N(24), "practice", "转盘与盒子", "转盘扇区大小不同、盒子棋子数量不同，各 3 题比较可能性。", "更大的扇区、更多的棋子，通常可能性更大。", items=6),
    q(N(25), "explain", "试两次不够", "只摸两次都是红，能不能说「一定是红」？用自己的话说明次数少时会晃。", "次数少，偶然性大，不要急着下结论。"),
    q(N(26), "practice", "先统计再判断", "整理 20 次摸棋记录，算每种颜色的次数和平均每 5 次大约几次，再比较可能性。", "记录是数据，可能性判断要对照盒子里实际有什么。", items=1),
    q(N(27), "practice", "我来选单位格", "三组数据范围不同，为每组选择 1 格代表几并说明理由。", "图要画得下，高低还要分得清。", items=3),
    q(N(28), "explain", "班均不是每人", "班均课外书 8 本，用两三句话说清楚：有人更多、有人更少，8 是拉齐后的数。", "平均描述全班，不描述每一个人。"),
    q(N(29), "practice", "合练卷", "复式条形图、平均数、可能性大小。", "三种题型先分类。", items=12),
    q(N(30), "practice", "通关综合练", "读复式条形图、算并解释平均数、比较可能性。", "图例、除法、全部结果，三件齐。", items=12),
    q(N(30), "boss", "关主：四年级统计通关试炼", "最终关主：①复式条形图 ②平均数计算与意义 ③列出结果并比较可能性大小。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g4-statistics",
    "title": "四年级 · 统计与概率",
    "subject": "数学",
    "stage": "小学",
    "grade": 4,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "条形图进阶（含复式条形图）与平均数可并行，在 n018 汇合；再进入可能性大小。选择合适的单位格（n027）与「人均不是每人」（n028）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-bar", f"{P}-boss-average", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：条形图测绘员、平均数调解员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "小学四年级「统计与概率」地图：复式条形图、平均数入门、可能性大小。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g4-statistics", N(1), f"{N(1)}-explain", N(2), N(4), f"{N(4)}-explain"),
    )


if __name__ == "__main__":
    main()
