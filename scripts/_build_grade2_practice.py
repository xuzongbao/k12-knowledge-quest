"""Build Grade 2 Comprehensive Practice map JSON.

Run: python3 scripts/_build_grade2_practice.py

原创活动骨架：量一量课桌与脚步、自制纸条尺、课间十分钟小调查。
「公平转盘小制作」为软锁。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-2-practice"
G = 2
STRAND = "综合与实践"
P = "pm-g2-prac"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：课桌有多长", 1, [], ["find", "ch-measure"], "能提出「课桌有多长、和门谁更长」这类需要测量的问题。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：用什么量", 2, [N(1)], ["plan", "ch-measure"], "能在脚步、铅笔、纸条、尺之间做选择，并说明量的时候要从同一端开始。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：量课桌和门", 2, [N(2)], ["do", "ch-measure"], "能量两次并记录，两次相差太大时重测。"),
    node(N(4), "交流：量的结果", 2, [N(3)], ["share", "ch-measure"], "能汇报用了什么工具、大约多少、和同学结果差多少。", mastery=MASTERY_CONCEPT),
    node(N(5), "发现：尺子不够用", 2, [N(4)], ["find", "ch-tool"], "能发现没有长尺时，需要把短纸条接起来或做一把自己的尺。", mastery=MASTERY_CONCEPT),
    node(N(6), "计划：纸条尺怎么做", 2, [N(5)], ["plan", "ch-tool"], "能设计纸条尺：同样长的一段重复画记号，并约定每一段叫「一格」。", mastery=MASTERY_CONCEPT),
    node(N(7), "实施：做出纸条尺", 3, [N(6)], ["do", "ch-tool"], "能做出带等分记号的纸条尺，格大致一样长。"),
    node(N(8), "用自制尺再量一次", 3, [N(7)], ["do", "ch-tool"], "能用自制尺量课桌，并与第一次结果比较。"),
    node(N(9), "交流：尺公平不公平", 3, [N(8)], ["share", "ch-tool", "boss-gate"], "能讨论格不均会让测量不公平，并提出改进。", mastery=MASTERY_GATE),
    node(N(10), "发现：课间大家都在干什么", 2, [N(4)], ["find", "ch-survey"], "能提出调查课间活动的问题，并预想几种类别。", mastery=MASTERY_CONCEPT),
    node(N(11), "计划：怎么问怎么记", 2, [N(10)], ["plan", "ch-survey"], "能设计简短问法和记录表，约定每人只选一类。", mastery=MASTERY_CONCEPT),
    node(N(12), "实施：问一问", 2, [N(11)], ["do", "ch-survey"], "能调查不少于 8 人并记录，不重复问同一个人。"),
    node(N(13), "整理成表或图", 3, [N(12)], ["do", "ch-survey"], "能把记录整理成简单表或象形图。"),
    node(N(14), "交流：课间发现", 3, [N(13)], ["share", "ch-survey"], "能用数据说一句课间发现，不把「我们班」说成「所有小朋友」。", mastery=MASTERY_CONCEPT),
    node(N(15), "测量与调查合练", 3, [N(9), N(14)], ["mixed", "ch-end"], "能说明测量活动和调查活动都要先有计划再动手。", mastery=MASTERY_GATE),
    node(N(16), "公平转盘小制作", 3, [N(9)], ["make", "ch-tool"], "能用纸盘画成几块差不多大的扇区，讨论怎样才算转得比较公平。", unlock=SOFT),
    node(N(17), "给下一组的建议", 2, [N(15)], ["share", "ch-end"], "能给下一组同学写出两条建议：测量时注意什么、调查时注意什么。", mastery=MASTERY_CONCEPT),
    node(N(18), "二年级实践合练", 3, [N(17)], ["mixed", "ch-end"], "能抽签完成测量或调查中的一个完整四步。", mastery=MASTERY_GATE),
    node(N(19), "二年级实践通关", 3, [N(18)], ["mixed", "ch-end", "boss-gate"], "能独立完成测量或调查小项目的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(6), "type": "related", "note": "选现成工具和自制尺子，都要先约定「一格有多长」。"},
    {"from": N(3), "to": N(8), "type": "easily_confused", "note": "两次测量结果不同，可能是工具变了，不一定是课桌变了。"},
    {"from": N(11), "to": N(12), "type": "easily_confused", "note": "问法中途改口，类别就会乱。"},
    {"from": N(14), "to": N(17), "type": "application", "note": "交流时说过的注意事项，可以写成给下一组的建议。"},
    {"from": N(6), "to": N(16), "type": "application", "note": "等分格子和等分转盘，都在追求公平。"},
]


QUESTS = [
    q(N(1), "explain", "提出测量问题", "写出一个关于长度的问题，指出要比的两样东西。", "问题要能量，不要问「漂不漂亮」。"),
    q(N(2), "explain", "选定工具", "选定一种测量办法，说明从哪一端开始、为什么中途不换工具。", "同一把「尺子」量到底。"),
    q(N(3), "practice", "量两次", "量课桌长两次，记录并计算大约相差多少（用格或脚步）。", "相差很大就重测。", items=2),
    q(N(4), "explain", "汇报测量", "说出工具、结果、和邻座差多少。", "差异可能来自起点没对齐。"),
    q(N(5), "explain", "发现工具不够", "说明短尺量长桌时会遇到什么麻烦。", "需要接起来或做更长的尺。"),
    q(N(6), "explain", "设计纸条尺", "画出纸条尺草图：每一格差不多长，并写上从 0 开始的记号。", "格子不均，尺就不公平。"),
    q(N(7), "practice", "做一把尺", "制作纸条尺，至少 8 格，目测格子是否均匀。", "先折或先量一段，再复制。", items=1),
    q(N(8), "practice", "再用新尺量", "用自制尺量课桌，和第一次比较，解释可能的差别。", "单位不同，数字不同，长短仍应差不多。", items=1),
    q(N(9), "explain", "怎样更公平", "指出自己尺上最不均的一格，提出改进办法。", "公平来自格子一样长。"),
    q(N(9), "mini_quiz", "测量项目小测", "找测量活动的缺步和不公平做法。", "计划、对齐、记录、重测。", items=6),
    q(N(9), "boss", "关主：测量小工匠", "击败关主：①提出测量问题 ②用自制或选定工具量两次 ③说明怎样让测量更公平。", "对齐和等格是关键。", xp=80, items=10, qid=f"{P}-boss-measure"),
    q(N(10), "explain", "提出调查问题", "写出课间调查问句和 3–4 个类别。", "类别要能覆盖大多数人。"),
    q(N(11), "explain", "设计记录表", "画出问法+记录表，注明每人只选一类。", "表头先写好。"),
    q(N(12), "practice", "调查八人", "询问至少 8 人并记录。", "不重复、不漏记。", items=8),
    q(N(13), "practice", "整理呈现", "做成简单表或象形图。", "数字要和记录对上。", items=1),
    q(N(14), "explain", "用数据说话", "用一句带数字的话汇报，并写明「这是我们问到的同学」。", "不扩大范围。"),
    q(N(15), "practice", "对照两种活动", "列出测量和调查各自的四步，找一个共同点、一个不同点。", "都要先计划；一个对物，一个对人。", items=1),
    q(N(16), "practice", "做转盘", "把纸盘分成几块尽量均匀的区域，转 10 次看是否某块特别爱停。", "块太不均匀就不公平。", items=1),
    q(N(17), "explain", "两条建议", "给下一组写测量建议和调查建议各一条。", "建议要具体能照做。"),
    q(N(18), "practice", "抽签走四步", "抽测量或调查，完整走四步并展示。", "缺步就补。", items=1),
    q(N(19), "practice", "通关综合练", "独立完成一个小项目：问题、计划、数据或测量、交流。", "别人要能听懂你的办法。", items=1),
    q(N(19), "boss", "关主：二年级实践通关试炼", "最终关主：完整演示测量或调查四步，并回答「怎样才公平」。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g2-practice",
    "title": "二年级 · 综合与实践",
    "subject": "数学",
    "stage": "小学",
    "grade": 2,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "测量课桌与自制尺为主线（关主 1），课间调查可与后半段并行，在 n015 汇合。公平转盘小制作（n016）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-measure", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：测量小工匠、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "小学二年级「综合与实践」地图：测量活动、自制尺子、生活小调查。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g2-practice", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
