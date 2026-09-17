"""Build Grade 7 Comprehensive Practice map JSON (七年级 · 综合与实践).

Run: python3 scripts/_build_jm_g7_practice.py

原创课题骨架：课间小账本（正负记录）与教室通道怎么留（平面约束）。
流程：发现问题 → 建模 → 求解 → 交流。不抄教材课题长文。
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

OUT = ROOT / "maps" / "junior-math" / "grade-7-practice"
G = 7
STRAND = "综合与实践"
P = "jm-g7-prac"
MAP_ID = "jm-g7-practice"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：账对不上", 1, [], ["find", "ch-ledger"], "能从「零花钱记完对不上」感到：收入、支出、结余需要统一的正负约定。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：正负记账规则", 2, [N(1)], ["plan", "ch-ledger"], "能约定：进账为正、出账为负（或相反），0 表示清零，并写成给同学看的规则。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：记一周流水", 3, [N(2)], ["do", "ch-ledger"], "能按规则记录至少 8 笔，每笔注明日期和事由。"),
    node(N(4), "实施：求结余", 3, [N(3)], ["do", "ch-ledger"], "能把流水按有理数加法汇总，得到结余，并解释负数结余的含义。"),
    node(N(5), "实施：分类看去向", 3, [N(4)], ["do", "ch-ledger"], "能按类别合并同类支出，指出最大去向。"),
    node(N(6), "交流：账本答辩", 3, [N(5)], ["share", "ch-ledger", "boss-gate"], "能讲清规则、一笔有争议的记录如何裁定，以及结余说明什么。", mastery=MASTERY_GATE),
    node(N(7), "发现：过道总是堵", 2, [N(6)], ["find", "ch-aisle"], "能提出教室课桌摆放导致过道太窄的问题，并说明要测量什么。", mastery=MASTERY_CONCEPT),
    node(N(8), "计划：约束清单", 2, [N(7)], ["plan", "ch-aisle"], "能列出约束：过道最小宽度、桌椅数量不变、黑板要看得见。", mastery=MASTERY_CONCEPT),
    node(N(9), "实施：画平面草图", 3, [N(8)], ["do", "ch-aisle"], "能用简化矩形表示桌椅，画出当前布置，标出主要尺寸。"),
    node(N(10), "实施：提出两种方案", 3, [N(9)], ["do", "ch-aisle"], "能给出两种不减少座位的布置，并量出最窄过道。"),
    node(N(11), "实施：比较与取舍", 3, [N(10)], ["do", "ch-aisle"], "能用「最窄过道、是否挡视线」比较方案，选出一个并说明放弃另一个的原因。"),
    node(N(12), "交流：布置说明会", 4, [N(11)], ["share", "ch-aisle"], "能向假想的同学讲解方案，回答「为什么不把桌子再挪一点」。", mastery=MASTERY_GATE),
    node(N(13), "发现：两件事能合在一起吗", 2, [N(6)], ["find", "ch-mix"], "能提出一个同时用到正负记录和平面约束的小问题，例如义卖摊位收支与通道。", mastery=MASTERY_CONCEPT),
    node(N(14), "计划：课题说明书", 2, [N(13)], ["plan", "ch-mix"], "能写问题、数据或尺寸从哪来、步骤、准备交流什么。", mastery=MASTERY_CONCEPT),
    node(N(15), "实施：走完四步", 3, [N(12), N(14)], ["do", "ch-mix"], "能按说明书收集数或尺寸，算出一个结果，并写下局限。"),
    node(N(16), "交流：成果卡", 3, [N(15)], ["share", "ch-mix"], "能用四句话写成果卡：问题、模型、结果、局限。", mastery=MASTERY_CONCEPT),
    node(N(17), "实践工具箱", 3, [N(16)], ["mixed", "ch-end"], "能列出综合与实践四步，以及每一步应留下的证据。", mastery=MASTERY_CONCEPT),
    node(N(18), "七年级实践合练", 4, [N(17)], ["mixed", "ch-end"], "能抽签完成账本或通道课题中的完整流程。", mastery=MASTERY_GATE),
    node(N(19), "七年级实践通关", 5, [N(18)], ["mixed", "ch-end", "boss-gate"], "能独立完成七年级综合与实践线的收束检查。", mastery=MASTERY_GATE),
    node(N(20), "规则冲突时怎么办", 3, [N(6)], ["ledger", "ch-ledger"], "能假设一笔「同学垫付又还回来」的记录，讨论记两笔还是记一笔，并修订规则。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(21), "如果尺子不准", 3, [N(11)], ["aisle", "ch-aisle"], "能说明测量有误差时，过道宽度结论应怎样写得更谨慎。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(4), "type": "application", "note": "规则决定结余怎么加：符号约定错了，总数就会反。"},
    {"from": N(5), "to": N(20), "type": "related", "note": "分类合并之后，更容易发现一笔记录该不该拆开。"},
    {"from": N(8), "to": N(11), "type": "application", "note": "比较方案时要回到约束清单，不能只看「好看」。"},
    {"from": N(9), "to": N(10), "type": "related", "note": "草图是模型，两种方案是对模型的两次求解。"},
    {"from": N(11), "to": N(21), "type": "application", "note": "选完方案，还要承认尺子和步测都不完美。"},
]


QUESTS = [
    q(N(1), "explain", "对不上的感觉", "讲述一次账对不上的经历或假设，指出可能漏记了什么。", "先感到「需要约定」，再谈正负。"),
    q(N(2), "explain", "写出记账规则", "用不超过五句话写出正负约定，让没学过的同学也能照做。", "进账、出账、0，三件事都要写到。"),
    q(N(3), "practice", "记八笔流水", "按规则记下 8 笔（可用合理假设），每笔有日期和事由。", "没有事由的数字以后无法答辩。", items=8),
    q(N(4), "practice", "算出结余", "把流水加总，解释结余为负表示什么。", "按有理数加法，不要漏符号。", items=1),
    q(N(5), "practice", "合并类别", "把支出分成至少三类并合并，指出最大去向。", "同类才能合并。", items=1),
    q(N(6), "explain", "讲清裁定", "选一笔有争议的账，说明记还是不记、记在哪一类。", "规则要能裁定争议。"),
    q(N(6), "mini_quiz", "账本质量小测", "找三份模拟流水的问题：漏符号、无事由、结余算错。", "证据链要完整。", items=6),
    q(N(6), "boss", "关主：小账本审计员", "击败关主：①说出正负约定 ②汇总结余 ③裁定一笔争议记录。", "约定先于计算。", xp=80, items=8, qid=f"{P}-boss-ledger"),
    q(N(7), "explain", "堵在哪里", "描述教室里哪一段过道最容易堵，并列出要量的尺寸。", "问题要落到可以量的量。"),
    q(N(8), "explain", "约束写成清单", "写出至少三条不可破的约束。", "座位数量往往是硬约束。"),
    q(N(9), "practice", "画现状草图", "用矩形表示桌椅，标出两条主要过道宽度。", "草图要能让别人量出你标的数。", items=1),
    q(N(10), "practice", "两种布置", "画出两种方案，各标最窄过道。", "不减少座位。", items=2),
    q(N(11), "practice", "比较取舍", "用一张对照表比较两种方案，写出选择理由。", "理由要对应约束。", items=1),
    q(N(12), "practice", "回答质疑", "准备两个提问：为什么不继续加宽、会不会挡黑板。", "每个回答指回测量或约束。", items=2),
    q(N(12), "mini_quiz", "布置质量小测", "给几份方案找缺：无尺寸、减少座位、没比过道。", "没有尺寸的方案只是愿望。", items=6),
    q(N(13), "explain", "提出综合问题", "写出一个同时用到记账和空间约束的问题。", "两种办法都要用到，才叫综合。"),
    q(N(14), "explain", "写说明书", "写问题、数据来源、步骤、交流时展示什么。", "别人按说明书能开工。"),
    q(N(15), "practice", "留下证据", "收集数或尺寸，算出结果，写一句局限。", "局限不是谦虚，是范围。", items=1),
    q(N(16), "practice", "四句成果卡", "问题、模型、结果、局限各一句。", "模型可以是正负约定，也可以是平面草图。", items=1),
    q(N(17), "explain", "打开工具箱", "说出四步名称，以及每步留下什么证据。", "没有证据的交流只是讲故事。"),
    q(N(18), "practice", "抽签走流程", "抽账本或通道之一完整做完四步。", "发现—计划—实施—交流。", items=1),
    q(N(19), "practice", "通关综合练", "独立完成一个带规则或草图的小项目，并主动说局限。", "能说局限，才像真做完。", items=1),
    q(N(19), "boss", "关主：七年级实践通关试炼", "最终关主：①讲清一套正负记账规则并汇总 ②展示一个带尺寸的过道方案或成果卡 ③说出局限。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
    q(N(20), "explain", "修订规则", "针对垫付再还回，决定记两笔还是抵消，并改规则说明书。", "规则要覆盖新情况。"),
    q(N(21), "explain", "误差下的结论", "假设每条过道可能差 2 厘米，说明结论应怎样改口。", "证据变弱，说法要降级。"),
]


META = {
    "id": MAP_ID,
    "title": "七年级 · 综合与实践",
    "subject": "数学",
    "stage": "初中",
    "grade": 7,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "课间小账本为主线（关主 1）；教室过道布置在账本交流后展开；综合课题与成果卡收束。规则冲突（n020）、尺子不准（n021）为软锁。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-ledger", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：小账本审计员、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "初中七年级「综合与实践」地图：正负记账小账本、教室过道布置。独立通关，不引用跨图节点。",
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
