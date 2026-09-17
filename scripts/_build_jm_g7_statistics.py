"""Build Grade 7 Statistics map JSON (七年级 · 统计与概率).

Run: python3 scripts/_build_jm_g7_statistics.py

Pedagogical spine: 数据收集整理深化 → 统计图表进阶 → 平均数众数中位数复习 → 频数 → 简单随机事件。
本图自洽，不引用小学统计节点 id。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _junior_common import (
    MASTERY_CONCEPT,
    MASTERY_GATE,
    ROOT,
    SOFT,
    node as _node,
    q,
    sample_progress,
    write_map,
)

OUT = ROOT / "maps" / "junior-math" / "grade-7-statistics"
G = 7
STRAND = "统计与概率"
P = "jm-g7-stat"
MAP_ID = "jm-g7-statistics"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "先把问题问清楚", 1, [], ["data", "ch-data"], "能把模糊兴趣改写成可以收集数据的问题，并说明调查对象是谁。", mastery=MASTERY_CONCEPT),
    node(N(2), "数据从哪来", 2, [N(1)], ["data", "ch-data"], "能区分自己测量、询问、公开记录三种来源，并写下来源说明。", mastery=MASTERY_CONCEPT),
    node(N(3), "全面调查与抽样入门", 2, [N(2)], ["data", "ch-data"], "能说明什么时候可以问所有人，什么时候只能问一部分，并指出样本要尽量有代表性。", mastery=MASTERY_CONCEPT),
    node(N(4), "记录表怎么设计", 3, [N(3)], ["data", "ch-data"], "能设计简单记录表：项目、单位、时间、记录人，避免事后补不回来。"),
    node(N(5), "整理：分类与计数", 3, [N(4)], ["data", "ch-data"], "能把原始记录分类划记，得到各类的个数。"),
    node(N(6), "频数是什么", 2, [N(5)], ["freq", "ch-freq"], "能把某一类出现的次数叫做频数，并说明频数要对应明确的类。", mastery=MASTERY_CONCEPT),
    node(N(7), "频率与百分数", 3, [N(6)], ["freq", "ch-freq"], "能用频数除以总数得到频率，并改写成百分数，核对合计是否接近 1。", mastery=MASTERY_GATE),
    node(N(8), "条形图深化", 3, [N(7)], ["chart", "ch-chart"], "能读复式条形图：比较同一项目在两组中的高低，并读出刻度。"),
    node(N(9), "折线图看变化", 3, [N(8)], ["chart", "ch-chart"], "能说明折线图适合看随时间（或顺序）的升降，而不是看各部分占整体。", mastery=MASTERY_CONCEPT),
    node(N(10), "扇形图看结构", 3, [N(7)], ["chart", "ch-chart"], "能读扇形图中各部分占总体的多少，并说明它不适合描述趋势。", mastery=MASTERY_CONCEPT),
    node(N(11), "选择统计图", 4, [N(9), N(10)], ["chart", "ch-chart", "boss-gate"], "能按问题选择条形、折线或扇形，并说明理由。", mastery=MASTERY_GATE),
    node(N(12), "平均数复习", 2, [N(5)], ["avg", "ch-avg"], "能计算一组数据的平均数，并说明它表示「拉齐」后每份一样多。", mastery=MASTERY_CONCEPT),
    node(N(13), "众数复习", 2, [N(5)], ["avg", "ch-avg"], "能找出出现次数最多的数，并说明一组数据可能没有众数或有多个众数。"),
    node(N(14), "中位数复习", 3, [N(12)], ["avg", "ch-avg"], "能把数据排序后找中位数，区分奇数个与偶数个。"),
    node(N(15), "三种统计量对照", 4, [N(13), N(14)], ["avg", "ch-avg"], "能对同一组数据求平均、众数、中位数，各用一句话说用途。", mastery=MASTERY_GATE),
    node(N(16), "极端值会拉动平均", 3, [N(15)], ["avg", "ch-avg"], "能发现特别大或特别小的数会拉动平均数，中位数往往更稳。", mastery=MASTERY_CONCEPT),
    node(N(17), "读图写结论", 3, [N(11), N(16)], ["chart", "ch-end"], "能根据图表写一句不超过数据范围的结论，避免「所有人一定」。"),
    node(N(18), "简单随机事件", 2, [N(11)], ["prob", "ch-prob"], "能说明有些事情在相同条件下可能发生也可能不发生，叫做随机事件。", mastery=MASTERY_CONCEPT),
    node(N(19), "必然、不可能、随机", 3, [N(18)], ["prob", "ch-prob"], "能给事件分类：必然发生、不可能发生、随机发生。"),
    node(N(20), "同样可能吗", 3, [N(19)], ["prob", "ch-prob"], "能判断一个简单试验里各结果是否可以当作同样可能。", mastery=MASTERY_CONCEPT),
    node(N(21), "列出全部结果", 3, [N(20)], ["prob", "ch-prob"], "能列出简单试验的全部结果，作为以后算可能性的分母。"),
    node(N(22), "用几分之几描述", 4, [N(21)], ["prob", "ch-prob"], "能在等可能前提下，用有利结果数除以全部结果数表示可能性。", mastery=MASTERY_GATE),
    node(N(23), "频率与可能性对照", 3, [N(7), N(22)], ["prob", "ch-prob"], "能把试验得到的频率和理论上的几分之几对照，说明次数少时会对不齐。", mastery=MASTERY_CONCEPT),
    node(N(24), "统计与可能性合练", 4, [N(17), N(23)], ["mixed", "ch-end"], "能在同一课题里整理频数、选图、选统计量，并描述一个简单随机事件。", mastery=MASTERY_GATE),
    node(N(25), "七年级统计通关", 5, [N(24)], ["mixed", "ch-end", "boss-gate"], "能独立完成七年级统计与概率线的收束检查。", mastery=MASTERY_GATE),
    node(N(26), "问卷题目别诱导", 3, [N(4)], ["data", "ch-data"], "能改写带暗示的问句，使选项中立，并说明诱导会让数据偏向。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "刻度截断会骗人", 3, [N(8)], ["chart", "ch-chart"], "能指出纵轴没有从 0 开始时，高低差看起来会被放大。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "校园小调查报告", 3, [N(24)], ["mixed", "ch-end"], "能围绕一个校园问题写出：对象、表或图、一个统计量、一句谨慎结论。", unlock=SOFT),
]


EXTRA_EDGES = [
    {"from": N(6), "to": N(7), "type": "easily_confused", "note": "频数是次数，频率是占总数的几分之几。"},
    {"from": N(9), "to": N(10), "type": "easily_confused", "note": "折线看变化，扇形看结构，不要拿错图。"},
    {"from": N(12), "to": N(13), "type": "related", "note": "平均数拉齐，众数看最常见，回答的问题不同。"},
    {"from": N(14), "to": N(16), "type": "related", "note": "中位数看位置，所以不太怕极端值。"},
    {"from": N(20), "to": N(22), "type": "easily_confused", "note": "不是等可能时，不能直接用「结果种数」当分数分母。"},
    {"from": N(8), "to": N(27), "type": "application", "note": "会读条形图之后，还要会识破截轴。"},
    {"from": N(4), "to": N(26), "type": "application", "note": "表设计好了，问题本身还不能带暗示。"},
]


QUESTS = [
    q(N(1), "explain", "改写成可调查的问题", "把「大家是不是很喜欢运动」改成可以计数的问题，并写清调查谁。", "问题要能用数据回答。"),
    q(N(2), "explain", "注明来源", "为三组数各写来源：自己量的、问来的、从公示栏抄的。", "没有来源的数，后面结论站不住。"),
    q(N(3), "explain", "问全部还是问一部分", "举一个适合普查、一个适合抽样的校园例子，并说明抽样要避免只问某一类人。", "样本要尽量像总体。"),
    q(N(4), "practice", "设计一张记录表", "为「课间饮水量」设计表头，至少含项目、单位、时间。", "表头决定你事后还能不能解释这批数。", items=1),
    q(N(5), "practice", "划记分类", "把一段原始名单分类划记，得到各类人数。", "先定类，再计数，类与类不要重叠。", items=1),
    q(N(6), "practice", "读出频数", "从整理表中读出指定类的频数，共 6 题。", "频数对应明确的一类。", items=6),
    q(N(7), "practice", "频数变频率", "计算频率和百分数，并检查合计。", "频率合计应接近 1。", items=6),
    q(N(8), "practice", "读复式条形图", "比较两组在同一项目上的高低，读刻度，共 6 题。", "先看图例区分两组。", items=6),
    q(N(9), "explain", "什么时候用折线", "说明「一周气温」为什么适合折线，不适合扇形。", "折线保留顺序和升降。"),
    q(N(10), "practice", "读扇形结构", "读出最多的一类及约占几成，共 4 题。", "整个圆是总体。", items=4),
    q(N(11), "practice", "按问题选图", "8 个问题选择条形 / 折线 / 扇形。", "比多少、看变化、看结构。", items=8),
    q(N(11), "mini_quiz", "图表小测", "混合读图与选图，夹一道用扇形表示气温变化的错例。", "先问问题要什么。", items=8),
    q(N(11), "boss", "关主：图表翻译官", "击败关主：①读频数频率 ②读一种统计图 ③为三个情境选对图。", "图是给问题服务的。", xp=80, items=12, qid=f"{P}-boss-chart"),
    q(N(12), "practice", "求平均数", "计算 6 组数据的平均数。", "总和除以个数。", items=6),
    q(N(13), "practice", "找众数", "6 组数据找众数，含没有众数和两个众数。", "出现次数最多的那个（些）。", items=6),
    q(N(14), "practice", "找中位数", "奇数个、偶数个各 4 组。", "先排序；偶数个取中间两个的平均。", items=8),
    q(N(15), "practice", "三个量都算", "4 组数据分别求平均、众数、中位数，并各写一句用途。", "三种量可以同时存在。", items=4),
    q(N(16), "practice", "加入一个极端值", "同一组数据加入一个特别大的数，观察三个统计量怎么变。", "平均会被拽走。", items=3),
    q(N(17), "explain", "一句谨慎结论", "根据给定图表写结论，划掉「所有」「一定」等越界词。", "结论里的对象要和数据对象一致。"),
    q(N(18), "explain", "什么叫随机", "举一个随机事件、一个必然事件，说明「随机」不是「没原因」，而是事先不能确定哪一种。", "条件相同，结果仍可能不同。"),
    q(N(19), "practice", "给事件分类", "10 个事件分成必然 / 不可能 / 随机。", "先问：在所说条件下会不会一定发生。", items=10),
    q(N(20), "explain", "公平还是动手脚", "对比公平骰子和被做了手脚的骰子，说明什么叫同样可能。", "没有理由偏袒某一面时，才当等可能。"),
    q(N(21), "practice", "列全部分母", "4 个试验列出全部等可能结果。", "不重复、不遗漏。", items=4),
    q(N(22), "practice", "写成分数", "8 个简单等可能事件写成几分之几。", "有利个数 / 全部个数。", items=8),
    q(N(22), "mini_quiz", "可能性小测", "分类事件、判断等可能、写分数。", "不是等可能就不要硬写分数。", items=8),
    q(N(22), "boss", "关主：随机事件讲解员", "击败关主：①给事件分类 ②列出全部结果 ③用分数表示一个等可能事件。", "先列全，再数有利的。", xp=80, items=10, qid=f"{P}-boss-chance"),
    q(N(23), "explain", "频率会对齐吗", "理论上 1/2，试验 10 次可能 7 次。说明次数少会晃。", "模型是分数，试验是频率。"),
    q(N(24), "practice", "课题两手抓", "整理一组校园数据：选图、选一个统计量、再写一个等可能事件的分数。", "统计描述已有数据，可能性描述尚未发生的结果。", items=1),
    q(N(25), "practice", "通关综合练", "频数频率、选图、三个统计量、简单概率分数。", "先辨：这是在整理数据还是在谈可能性。", items=12),
    q(N(25), "boss", "关主：七年级统计通关试炼", "最终关主：①整理频数并选图 ②对照三个统计量 ③描述一个简单随机事件。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(26), "practice", "改掉诱导问句", "改写 4 句带暗示的问卷题。", "选项中立，不替对方做判断。", items=4),
    q(N(27), "practice", "给截轴图找茬", "指出 3 张纵轴截断的图会让人产生什么错觉。", "看刻度从几开始。", items=3),
    q(N(28), "practice", "四句话报告", "写对象、图或表、统计量、谨慎结论。", "四句都要指着数据。", items=1),
]


META = {
    "id": MAP_ID,
    "title": "七年级 · 统计与概率",
    "subject": "数学",
    "stage": "初中",
    "grade": 7,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "收集整理与频数主线（关主 1）；平均数等统计量从整理后并行；简单随机事件在选图后并行（关主 2）。问卷诱导（n026）、截轴（n027）、小报告（n028）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-chart", f"{P}-boss-chance", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：图表翻译官、随机事件讲解员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中七年级「统计与概率」地图：数据收集整理、统计图深化、三个统计量、频数与简单随机事件。独立通关。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress(MAP_ID, N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-explain"),
    )


if __name__ == "__main__":
    main()
