"""Build Grade 1 Statistics map JSON from a single source of truth.

Run: python3 scripts/_build_grade1_statistics.py
The generated JSON under maps/primary-math/grade-1-statistics/ is the published content.

Pedagogical spine (课标第一学段脉络，自撰短描述，非教材页原文):
  分类（颜色、形状、大小与自定标准）
  → 简单象形图与条形高低入门、简单统计表
  → 可能性口头描述（一定、可能、不可能）。
「做一张我的象形图」为软锁支线。本图自洽，不引用数与运算或图形节点 id。
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

OUT = ROOT / "maps" / "primary-math" / "grade-1-statistics"
G = 1
STRAND = "统计与概率"
P = "pm-g1-stat"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(
        N(1),
        "东西有相同和不同",
        1,
        [],
        ["classify", "ch-sort"],
        "能指出两件物品哪里一样、哪里不一样，为后面按标准分类做准备。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(2),
        "按颜色分一分",
        1,
        [N(1)],
        ["classify", "ch-sort", "color"],
        "能按颜色把一堆学具分成几堆，并说出每一堆是什么颜色。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(3),
        "按形状分一分",
        1,
        [N(1)],
        ["classify", "ch-sort", "shape"],
        "能按形状把物品分成几堆，不把颜色不同但形状相同的东西拆开。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(4),
        "按大小分一分",
        1,
        [N(1)],
        ["classify", "ch-sort", "size"],
        "能按大、中、小把物品分成几堆，并说明自己是怎么比的。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(5),
        "自己定一个标准",
        2,
        [N(2), N(3), N(4)],
        ["classify", "ch-sort", "criterion"],
        "能自己选定一个标准（如能不能滚动）给物品分类，并让别人听懂这个标准。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(6),
        "每一类有几个",
        2,
        [N(5)],
        ["classify", "ch-sort", "count"],
        "分类之后能数出每一类有几个，并用手指点着数，不多数也不漏数。",
    ),
    node(
        N(7),
        "分类结果说一说",
        2,
        [N(6)],
        ["classify", "ch-sort", "talk"],
        "能用「按……分，这一类有……个」把分类结果讲给同伴听。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(8),
        "分类综合",
        3,
        [N(7)],
        ["classify", "ch-sort", "boss-gate"],
        "能换一个标准重新分类，并比较两次结果有什么不同。",
        mastery=MASTERY_GATE,
    ),
    node(
        N(9),
        "把同类排成一列",
        2,
        [N(8)],
        ["pictograph", "ch-chart"],
        "能把同一类物品对齐排成一列，方便一眼看出哪一列更长。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(10),
        "一个图代表一个",
        2,
        [N(9)],
        ["pictograph", "ch-chart"],
        "知道象形统计图里，一个小图通常代表一件东西，图的个数和数量一样多。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(11),
        "象形图谁多谁少",
        2,
        [N(10)],
        ["pictograph", "ch-chart", "compare"],
        "能看着象形图说出哪一类最多、哪一类最少，并能指出多几个。",
    ),
    node(
        N(12),
        "把象形图补完整",
        3,
        [N(11)],
        ["pictograph", "ch-chart"],
        "能根据「还缺几个图」把象形图补画完整，使图的个数和数量一致。",
    ),
    node(
        N(13),
        "用高矮比数量",
        2,
        [N(9)],
        ["bar", "ch-chart"],
        "能用叠方块或涂格子的高低比较数量，知道更高通常表示更多。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(14),
        "简单统计表",
        2,
        [N(11), N(13)],
        ["table", "ch-chart"],
        "能认简单统计表：左边是类别，右边是个数，并从表里读出一个数。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(15),
        "看图表回答问题",
        3,
        [N(12), N(14)],
        ["chart", "ch-chart", "read"],
        "能根据象形图或简单表回答「最多、最少、一共、多几个」这类问题。",
    ),
    node(
        N(16),
        "读图综合",
        3,
        [N(15)],
        ["chart", "ch-chart", "boss-gate"],
        "能把同一组数据在「排队的实物、象形图、简单表」之间对上号。",
        mastery=MASTERY_GATE,
    ),
    node(
        N(17),
        "一定、可能、不可能",
        2,
        [N(16)],
        ["chance", "ch-chance"],
        "能用「一定、可能、不可能」口头描述简单事情会不会发生。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(18),
        "生活里碰碰运气",
        2,
        [N(17)],
        ["chance", "ch-chance"],
        "能对摸棋子、看天气、猜盒子里是什么等事，选用合适的可能性词语。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(19),
        "把可能性说清楚",
        3,
        [N(18)],
        ["chance", "ch-chance"],
        "能说明自己为什么说「一定」或「不可能」，不把「还没发生」都说成不可能。",
        mastery=MASTERY_CONCEPT,
    ),
    node(
        N(20),
        "分类图表和可能性",
        4,
        [N(19)],
        ["mixed", "ch-end"],
        "能在同一情境里先分类计数，再读简单图，最后用可能性词语说一句话。",
        mastery=MASTERY_GATE,
    ),
    node(
        N(21),
        "做一张我的象形图",
        3,
        [N(16)],
        ["pictograph", "ch-chart", "make"],
        "能自己调查身边几类物品，画一张「一个图代表一个」的象形图并配上类别名。",
        unlock=SOFT,
    ),
    node(
        N(22),
        "一年级统计通关",
        4,
        [N(20)],
        ["mixed", "ch-end", "boss-gate"],
        "综合分类、简单图表和口头可能性，能独立完成入门地图的收束检查。",
        mastery=MASTERY_GATE,
    ),
]


EXTRA_EDGES = [
    {
        "from": N(2),
        "to": N(3),
        "type": "related",
        "note": "颜色和形状是两种常见标准，宜对照着用。",
    },
    {
        "from": N(2),
        "to": N(5),
        "type": "easily_confused",
        "note": "标准变了，同一件物品可能换堆；不是物品自己变了。",
    },
    {
        "from": N(10),
        "to": N(13),
        "type": "related",
        "note": "象形图用个数比多少，叠高用高低比多少。",
    },
    {
        "from": N(10),
        "to": N(13),
        "type": "easily_confused",
        "note": "图多不一定画得更大；要比的是个数或格子数，不是图画尺寸。",
    },
    {
        "from": N(6),
        "to": N(14),
        "type": "application",
        "note": "每一类的个数填进表，就是简单统计表。",
    },
    {
        "from": N(17),
        "to": N(18),
        "type": "easily_confused",
        "note": "「可能」不是「一定」，也不是「不可能」；中间那档最容易说滑。",
    },
    {
        "from": N(11),
        "to": N(21),
        "type": "application",
        "note": "会读象形图之后，可以试着自己画一张。",
    },
]


QUESTS = [
    q(N(1), "explain", "找相同找不同", "拿出橡皮、铅笔、尺子。说出两件物品的一个相同点和一个不同点。", "先看能摸到的：颜色、长短、能不能写字。"),
    q(N(2), "explain", "颜色分家", "把 10 件彩色积木按颜色分成几堆，说出每一堆的颜色。", "一次只看颜色，先别管形状。"),
    q(N(2), "practice", "再分一次颜色", "换一袋学具，按颜色分堆，至少分成 3 堆，并核对没有混色。", "拿起一件先问：它是什么颜色？", items=8),
    q(N(3), "explain", "形状分家", "按圆形、方形、长条把物品分堆，即使颜色不同也要放在同一形状堆。", "标准是形状，不是颜色。"),
    q(N(4), "explain", "大小分家", "把扣子或纸片分成大、小两堆，并说明你是怎么比的。", "并排放在一起比，比轮流拿在手里感觉。"),
    q(N(5), "explain", "我的分类标准", "自己定一个标准给文具分类（如「能放进笔袋」），讲给同伴听，让对方按你的标准再分一次。", "标准要一句话说完，别人才能照做。"),
    q(N(6), "practice", "数一数每一类", "分类后数出每一类的个数，写在纸上。三类都要数对。", "点一个记一个，数完再从头复核一遍。", items=6),
    q(N(7), "explain", "汇报分类", "用句式「我按……分，这一类有……个」连说三类。", "先说标准，再说每一类的名称和个数。"),
    q(N(8), "practice", "换标准再分", "同一堆物品先按颜色分，再按能否滚动分，比较两张结果有什么不同。", "物品没变，标准变了，堆就会变。", items=8),
    q(N(8), "mini_quiz", "分类小测", "听口令分类 + 自己定标准 + 数出每类个数。正确率达到掌握标准才过关。", "每一题先确认标准是什么。", items=10),
    q(
        N(8),
        "boss",
        "关主：分类小能手",
        "击败关主：①按给定标准分类 ②自己定一个别人能听懂的标准 ③换标准后再数一数。",
        "先把标准说清楚，再动手。",
        xp=80,
        items=12,
        qid=f"{P}-boss-sort",
    ),
    q(N(9), "explain", "排成一列比长短", "把红黄蓝三类积木各排成一列，对齐底部，指出哪一列最长。", "底对齐，才能用长短比多少。"),
    q(N(10), "explain", "一个图就是一个", "看一张用小星星画的图，说明一颗星代表一个人或一件物，不能随便代表好几个。", "现在先约定：一图对一件。"),
    q(N(11), "practice", "谁多谁少", "读 4 张象形图，分别说出最多、最少，以及最多比最少多几个。", "先数每一类的图，再相减。", items=8),
    q(N(12), "practice", "补上缺的图", "给出「喜欢猫的有 6 人，图上只画了 4 只猫」，把图补完整。再做 3 题类似的。", "缺几个就补几个，不要把图画得更大来充数。", items=4),
    q(N(13), "explain", "叠高比多少", "用方块给三类数量叠高，说明更高表示更多，并指出最高的一类。", "每一层一个方块，不要有的层叠两块。"),
    q(N(14), "explain", "表上有类别和个数", "看一张两列表：类别 | 个数。读出其中一类有几个。", "先找类别名字，再读右边的数。"),
    q(N(14), "practice", "从表里读数", "给 6 张简单表，读出指定类别的个数，并找出最多的一类。", "用手指指着横着读，避免串行。", items=6),
    q(N(15), "practice", "看图回答", "根据象形图或表回答：最多、最少、一共、多几个。共 8 问。", "问「一共」要把各类加起来。", items=8),
    q(N(16), "practice", "三种样子对对碰", "同一组数据分别是实物列、象形图、表。把三种表示连起来。", "先核对每一类的个数是否相同。", items=6),
    q(N(16), "mini_quiz", "读图小测", "混合：读象形图、读表、比较多少。夹一道「图画得大但个数少」的干扰题。", "比的是个数，不是图的大小。", items=10),
    q(
        N(16),
        "boss",
        "关主：读图小侦探",
        "击败关主：①读象形图比多少 ②从表里找数 ③指出「图大不等于数量多」的例子。",
        "先数个数，再下结论。",
        xp=80,
        items=12,
        qid=f"{P}-boss-chart",
    ),
    q(N(17), "explain", "三个词怎么用", "用「太阳从东边升起」「明天可能下雨」「人用手走路」各配一个：一定 / 可能 / 不可能，并说明理由。", "一定是每次都会；不可能是不会发生；可能是说不准。"),
    q(N(18), "practice", "给事情配词", "8 件生活小事，选用一定、可能、不可能。包含摸口袋里的棋子、看窗外是否在下雨。", "先想这件事会不会换结果。", items=8),
    q(N(19), "explain", "为什么这样说", "解释：盒子里只有红棋，摸出红棋为什么说「一定」；盒子是空的为什么说「不可能摸出棋」。", "先看盒子里到底有什么，再选词。"),
    q(N(20), "practice", "先分类再猜猜", "先把棋子分类计数，再闭眼摸一颗：根据哪一类更多，用可能/更常摸到来说一句话。", "数量多的一类，更常被摸到，但仍不是「一定」。", items=6),
    q(N(20), "mini_quiz", "合练小测", "混合：分类计数、读简单图、选可能性词语。", "分类和读图用数，可能性用词，不要混成一道算术。", items=10),
    q(N(21), "practice", "我来画象形图", "调查桌上四类文具的个数，画象形图：一类一行，一个图代表一个，写下标题。", "图要一样大、对齐，类别名称写在旁边。", items=1),
    q(N(22), "practice", "入门地图综合练", "题型混合：换标准分类、读象形图、读表、选一定/可能/不可能。", "不会时回到对应那盏灯再看一眼。", items=12),
    q(
        N(22),
        "boss",
        "关主：一年级统计通关试炼",
        "最终关主：①按两种标准分类并计数 ②读图比多少 ③给三件事选可能性词语。全部通过即通关本地图。",
        "通关后记入已通关列表；分类标准和「图大≠更多」最容易回生。",
        xp=100,
        items=16,
        qid=f"{P}-boss-map",
    ),
]


META = {
    "id": "pm-g1-statistics",
    "title": "一年级 · 统计与概率",
    "subject": "数学",
    "stage": "小学",
    "grade": 1,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "从「东西有相同和不同」进入：先打通分类，再简单象形图/条形高低与统计表，最后口头说可能性。做一张我的象形图（n021）为软锁支线，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-sort", f"{P}-boss-chart", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：分类小能手、读图小侦探、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "小学一年级「统计与概率」地图：分类 → 简单象形/条形入门 → 可能性口头描述。与其他领域地图各自独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT,
        META,
        NODES,
        EXTRA_EDGES,
        QUESTS,
        sample_progress("pm-g1-statistics", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-explain"),
    )


if __name__ == "__main__":
    main()
