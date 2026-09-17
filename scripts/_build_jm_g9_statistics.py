"""Build Grade 9 Statistics map JSON (九年级 · 统计与概率).

Run: python3 scripts/_build_jm_g9_statistics.py

Pedagogical spine: 随机抽样 → 用样本估计总体 → 频率估计概率 → 列表树状图深化与古典概型综合。
本图自洽。
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

OUT = ROOT / "maps" / "junior-math" / "grade-9-statistics"
G = 9
STRAND = "统计与概率"
P = "jm-g9-stat"
MAP_ID = "jm-g9-statistics"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "总体与样本", 1, [], ["sample", "ch-sample"], "能区分总体、个体、样本，并说明为什么常常不能调查总体里的每一个。", mastery=MASTERY_CONCEPT),
    node(N(2), "简单随机抽样", 3, [N(1)], ["sample", "ch-sample"], "能说明简单随机抽样：总体中每个个体被抽到的机会相同。", mastery=MASTERY_CONCEPT),
    node(N(3), "抽样要有代表性", 3, [N(2)], ["sample", "ch-sample"], "能指出只在某一类人里抽样会让样本不像总体。"),
    node(N(4), "样本容量", 3, [N(3)], ["sample", "ch-sample"], "能说明样本太小会更不稳定，但样本大不等于方法正确。", mastery=MASTERY_CONCEPT),
    node(N(5), "用样本平均数估计总体", 3, [N(4)], ["sample", "ch-est"], "能用样本平均数作为总体平均数的估计，并说明这是估计不是精确值。", mastery=MASTERY_GATE),
    node(N(6), "用样本频率估计总体比例", 3, [N(5)], ["sample", "ch-est"], "能用样本中某类所占比例估计总体中该类比例。"),
    node(N(7), "估计要写范围意识", 3, [N(6)], ["sample", "ch-est"], "能在结论里写「大约」「估计」，避免把样本结果说成全体确定事实。"),
    node(N(8), "抽样与估计综合", 4, [N(7)], ["sample", "ch-sample", "boss-gate"], "能设计一个简单抽样方案并用样本估计总体的一个数量。", mastery=MASTERY_GATE),
    node(N(9), "频率与概率再对照", 2, [N(8)], ["prob", "ch-prob"], "能说明大量重复试验中频率稳定在某一值附近，这个值可以当作概率的估计。", mastery=MASTERY_CONCEPT),
    node(N(10), "用频率估计概率", 3, [N(9)], ["prob", "ch-prob"], "能根据试验记录计算频率，并把它当作概率的估计。", mastery=MASTERY_GATE),
    node(N(11), "试验次数的影响", 3, [N(10)], ["prob", "ch-prob"], "能比较次数少和次数多时频率的波动，说明次数多更稳。"),
    node(N(12), "古典概型再整理", 3, [N(10)], ["prob", "ch-prob"], "能重述古典概型条件：结果有限、等可能，概率=有利数/全部数。", mastery=MASTERY_CONCEPT),
    node(N(13), "列表法深化", 3, [N(12)], ["prob", "ch-prob"], "能列出两个或三个简单试验的结果表，注意是否等可能。"),
    node(N(14), "树状图深化", 4, [N(12)], ["prob", "ch-prob"], "能画分步树状图，包括「不放回」时第二步分支不同。", mastery=MASTERY_GATE),
    node(N(15), "放回与不放回", 4, [N(13), N(14)], ["prob", "ch-prob"], "能说明放回使各步情况相同，不放回会改变后面的个数。", mastery=MASTERY_CONCEPT),
    node(N(16), "古典概型综合", 4, [N(15)], ["prob", "ch-prob", "boss-gate"], "能选择列表或树状图求较规范的古典概型问题。", mastery=MASTERY_GATE),
    node(N(17), "估计与古典对照", 3, [N(11), N(16)], ["prob", "ch-end"], "能说明：能等可能列举时用古典概型，否则可用频率估计。", mastery=MASTERY_CONCEPT),
    node(N(18), "统计决策入门", 3, [N(8), N(17)], ["mixed", "ch-end"], "能根据样本估计或概率比较，做出一个谨慎的选择建议。"),
    node(N(19), "九年级统计合练", 4, [N(18)], ["mixed", "ch-end"], "能完成抽样估计与概率计算的混合检查。", mastery=MASTERY_GATE),
    node(N(20), "九年级统计通关", 5, [N(19)], ["mixed", "ch-end", "boss-gate"], "能独立完成九年级统计与概率线的收束检查。", mastery=MASTERY_GATE),
    node(N(21), "方便样本的陷阱", 3, [N(3)], ["sample", "ch-sample"], "能指出只问身边朋友、只看自愿填表，会得到方便样本，估计容易偏。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(22), "把估计说过头", 3, [N(7)], ["sample", "ch-est"], "能改写越界结论，例如把「本班样本」说成「全市一定」。", unlock=SOFT),
    node(N(23), "树状图漏枝", 3, [N(14)], ["prob", "ch-prob"], "能检查树状图是否漏掉某一分支，并说明漏枝会让概率加不起来。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(24), "用样本方差意识", 3, [N(5)], ["sample", "ch-est"], "能说明样本很散时，用平均数代表总体要更谨慎（不必计算复杂公式）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(3), "type": "easily_confused", "note": "机会相同不等于已经有代表性：抽样框本身可能缺了一类人。"},
    {"from": N(5), "to": N(6), "type": "related", "note": "估计平均数和估计比例，都是用样本推断总体。"},
    {"from": N(9), "to": N(12), "type": "easily_confused", "note": "频率估计用于不好列举或不等可能；古典概型用于等可能列举。"},
    {"from": N(14), "to": N(15), "type": "related", "note": "不放回时，第二层树枝的分母会变。"},
    {"from": N(3), "to": N(21), "type": "application", "note": "没有代表性的极端情况就是方便样本。"},
    {"from": N(7), "to": N(22), "type": "application", "note": "写过「大约」，还要检查对象有没有被夸大。"},
]


QUESTS = [
    q(N(1), "explain", "谁是总体谁是样本", "在「想了解全年级课间运动时间」里指出总体、个体、样本。", "样本是抽出来的那一部分。"),
    q(N(2), "explain", "机会相同", "用抽签或随机数说明简单随机抽样。", "事先不能偏向某一个人。"),
    q(N(3), "practice", "指出偏了的抽样", "4 个方案指出缺了哪一类人。", "抽样框要覆盖各类。", items=4),
    q(N(4), "explain", "不是越大就越对", "说明样本很大但只来自一个班级，仍然可能偏。", "方法正确比盲目加大更重要。"),
    q(N(5), "practice", "用样本平均估计", "根据样本数据估计总体平均，并写「估计」。", "不要写成全体确定值。", items=4),
    q(N(6), "practice", "用样本比例估计", "估计总体中某类所占比例，共 4 题。", "样本频率当作总体比例的估计。", items=4),
    q(N(7), "practice", "改写结论", "把 4 句说过头的结论改谨慎。", "对象范围和「估计」都要留下。", items=4),
    q(N(8), "practice", "设计并估计", "写一个抽样方案并用假设样本做一次估计。", "方案里要写怎么保证机会尽量相同。", items=1),
    q(N(8), "mini_quiz", "抽样小测", "总体样本、代表性、估计用语。", "估计不是精确普查。", items=8),
    q(N(8), "boss", "关主：抽样估计员", "击败关主：①区分总体与样本 ②指出一个有偏抽样 ③用样本估计总体并写谨慎结论。", "代表性先于计算。", xp=80, items=10, qid=f"{P}-boss-sample"),
    q(N(9), "explain", "频率稳定", "用自己的话说明大量重复时频率靠近一个数。", "那个数可以当作概率。"),
    q(N(10), "practice", "用频率估计概率", "根据试验表计算频率作为概率估计，共 4 题。", "频率=发生次数/试验次数。", items=4),
    q(N(11), "explain", "次数少会晃", "对比 10 次和 200 次的频率波动。", "次数多更稳，仍不必次次相等。"),
    q(N(12), "explain", "古典概型条件", "重述两个条件：有限、等可能。", "缺一条就不能硬除。"),
    q(N(13), "practice", "列表深化", "列出较完整的结果表并求概率，共 3 题。", "每格是否等可能先确认。", items=3),
    q(N(14), "practice", "树状图深化", "画不放回或分步树状图 3 题。", "第二步的个数可能变。", items=3),
    q(N(15), "practice", "放回对照", "同一摸球问题，放回与不放回各求一次概率。", "不放回会改变后面的分母。", items=2),
    q(N(16), "practice", "选工具求概率", "混合列表与树状图 4 题。", "分步不明时优先树状图。", items=4),
    q(N(16), "mini_quiz", "概型小测", "频率估计、古典条件、放回不放回。", "先问能不能等可能列举。", items=8),
    q(N(16), "boss", "关主：古典概型绘图员", "击败关主：①用频率估计一个概率 ②用列表或树状图求一个古典概率 ③说明放回与不放回的差别。", "工具要匹配假设。", xp=80, items=10, qid=f"{P}-boss-classical"),
    q(N(17), "explain", "两种求法何时用", "各举一例：适合古典概型、适合频率估计。", "能列举且等可能就除；否则做试验。"),
    q(N(18), "practice", "给一个谨慎建议", "根据估计或概率比较，写一句建议并写局限。", "建议不超过数据所能支撑的范围。", items=1),
    q(N(19), "practice", "合练卷", "抽样估计 + 树状图或列表求概率。", "先辨：推断总体还是计算模型概率。", items=8),
    q(N(20), "practice", "通关综合练", "设计抽样意识、样本估计、古典概型计算。", "代表性、谨慎用语、等可能，三件抓手。", items=10),
    q(N(20), "boss", "关主：九年级统计通关试炼", "最终关主：①说明样本与总体 ②用样本估计并写谨慎结论 ③用列表或树状图求概率。", "通关后记入已通关列表。", xp=100, items=14, qid=f"{P}-boss-map"),
    q(N(21), "explain", "方便样本", "指出只问朋友或只看自愿填表的问题。", "自愿的人往往更有观点。"),
    q(N(22), "practice", "缩小对象", "改写 3 句把本班说成全市的结论。", "结论对象≤样本能代表的对象。", items=3),
    q(N(23), "practice", "给树状图补枝", "找出漏掉的分支并改正概率。", "所有路径概率和应为 1（在等可能或加权正确时）。", items=2),
    q(N(24), "explain", "样本很散时", "说明样本方差大时，用平均代表总体要更小心。", "中心和波动仍要一起看。"),
]


META = {
    "id": MAP_ID,
    "title": "九年级 · 统计与概率",
    "subject": "数学",
    "stage": "初中",
    "grade": 9,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "抽样与用样本估计总体（关主 1）→ 频率估计概率与古典概型深化（关主 2）。方便样本、越界结论、漏枝、样本很散（n021–n024）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-sample", f"{P}-boss-classical", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：抽样估计员、古典概型绘图员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为课标/教材目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或习题的摘录。",
    "description": "初中九年级「统计与概率」地图：随机抽样、用样本估计总体、频率估计概率、列表树状图与古典概型。独立通关。",
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
