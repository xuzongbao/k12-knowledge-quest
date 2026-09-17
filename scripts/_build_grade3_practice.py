"""Build Grade 3 Comprehensive Practice map JSON.

Run: python3 scripts/_build_grade3_practice.py

原创活动骨架：储物柜/座位编码、搭配计数、步测操场。
「密码规则小改进」为软锁。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-3-practice"
G = 3
STRAND = "综合与实践"
P = "pm-g3-prac"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：东西不好对号", 1, [], ["find", "ch-code"], "能发现座位、储物柜、图书如果没有编号，就很难快速对上人。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：编码里要有什么", 2, [N(1)], ["plan", "ch-code"], "能设计编码规则：哪几位表示组、哪几位表示序号，并举例。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：给柜子编号", 2, [N(2)], ["do", "ch-code"], "能按规则给 12 个位置编码，保证不重复、能反查。"),
    node(N(4), "实施：看编码找位置", 3, [N(3)], ["do", "ch-code"], "能根据编码快速找到对应位置，解释每一位的意思。"),
    node(N(5), "交流：规则别人能用吗", 3, [N(4)], ["share", "ch-code", "boss-gate"], "能让没参加设计的人按说明书编码，看是否仍不冲突。", mastery=MASTERY_GATE),
    node(N(6), "发现：搭配有多少种", 2, [N(5)], ["find", "ch-combo"], "能提出「上衣和裤子、主食和配菜」有多少种搭配的问题。", mastery=MASTERY_CONCEPT),
    node(N(7), "计划：用表或连线", 2, [N(6)], ["plan", "ch-combo"], "能选择用连线、表格或树状图把搭配列全。", mastery=MASTERY_CONCEPT),
    node(N(8), "实施：有序列出", 3, [N(7)], ["do", "ch-combo"], "能不重复、不遗漏地列出所有搭配，并核对总数。"),
    node(N(9), "实施：加一个条件", 3, [N(8)], ["do", "ch-combo"], "能加上「不能同色」等条件，从全部搭配里圈出符合的。"),
    node(N(10), "交流：怎样保证没漏", 3, [N(9)], ["share", "ch-combo"], "能向别人演示自己的列出顺序，说明怎样防止遗漏。", mastery=MASTERY_CONCEPT),
    node(N(11), "发现：操场有多长", 2, [N(5)], ["find", "ch-step"], "能提出用脚步或绳段估计一段路有多长的问题。", mastery=MASTERY_CONCEPT),
    node(N(12), "计划：步测怎么走", 2, [N(11)], ["plan", "ch-step"], "能约定正常步、数步数、走直线，并准备记录表。", mastery=MASTERY_CONCEPT),
    node(N(13), "实施：走两遍", 3, [N(12)], ["do", "ch-step"], "能步测同一段路两遍，记录步数并讨论为什么会不同。"),
    node(N(14), "交流：估计与改进", 3, [N(13)], ["share", "ch-step"], "能用两次结果给出一个估计，并提出怎样走得更稳。", mastery=MASTERY_CONCEPT),
    node(N(15), "编码与搭配合练", 3, [N(10), N(14)], ["mixed", "ch-end"], "能说明编码和搭配都在「按规则把情况列清楚」。", mastery=MASTERY_GATE),
    node(N(16), "密码规则小改进", 3, [N(5)], ["code", "ch-code"], "能给编码加一位「奇偶校验」或颜色标记，减少抄错。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(17), "给新生的说明书", 2, [N(15)], ["share", "ch-end"], "能把编码规则或步测办法写成另一班能看懂的短说明书。", mastery=MASTERY_CONCEPT),
    node(N(18), "项目路演", 3, [N(17)], ["share", "ch-end"], "能在三分钟内讲清问题、规则、结果、还想改什么。"),
    node(N(19), "三年级实践合练", 3, [N(18)], ["mixed", "ch-end"], "能抽签完成编码、搭配、步测中的一个完整项目。", mastery=MASTERY_GATE),
    node(N(20), "三年级实践通关", 4, [N(19)], ["mixed", "ch-end", "boss-gate"], "能独立完成一个「规则清晰、结果可检查」的小项目。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(2), "to": N(7), "type": "related", "note": "编码规则和搭配列表都要事先说清符号的意思。"},
    {"from": N(3), "to": N(4), "type": "easily_confused", "note": "会写编码不等于会读编码；两位要都能练。"},
    {"from": N(8), "to": N(9), "type": "easily_confused", "note": "先列全，再加条件筛选；不要一开始就漏。"},
    {"from": N(12), "to": N(13), "type": "easily_confused", "note": "步子忽大忽小，两次步数就会差很多。"},
    {"from": N(5), "to": N(16), "type": "application", "note": "规则能用之后，才谈得上防抄错的小改进。"},
]


QUESTS = [
    q(N(1), "explain", "对不上号的麻烦", "描述一次「找柜子/找座位」浪费时间的经历，说明缺编号会怎样。", "问题要具体。"),
    q(N(2), "explain", "写出规则", "设计一种编码：至少包含组和序号，举例三个合法编码、一个非法编码。", "规则要能判断对错。"),
    q(N(3), "practice", "编十二个号", "给 12 个位置编码，检查无重复，并解释其中两个号。", "每个位置恰好一个号。", items=12),
    q(N(4), "practice", "看号找位置", "抽 6 个编码反查位置，说每一位代表什么。", "从左到右解码。", items=6),
    q(N(5), "practice", "别人来用", "只给说明书，让同伴编 4 个新号，看是否冲突。", "说明书含糊，别人就会编重。", items=4),
    q(N(5), "mini_quiz", "编码项目小测", "判断编码是否合法、是否冲突、说明书缺了哪一步。", "合法、唯一、可反查。", items=8),
    q(N(5), "boss", "关主：编码设计师", "击败关主：①说明问题 ②写出规则并编码 ③让别人按说明书使用。", "别人能用，规则才算成。", xp=80, items=10, qid=f"{P}-boss-code"),
    q(N(6), "explain", "提出搭配问题", "写出一个「A 种与 B 种」的搭配问题，并给出 A、B 的清单。", "清单要短，能列完。"),
    q(N(7), "explain", "选择列出办法", "在连线、表格、树状图中选一种，说明怎样保证不漏。", "固定一个顺序最不容易漏。"),
    q(N(8), "practice", "列全核对", "列出全部搭配并写出总数，与「每项配每项」的想法核对。", "有序列出。", items=1),
    q(N(9), "practice", "加条件筛选", "加上一个简单条件，圈出符合的搭配并计数。", "从完整清单里筛，不要重列一套。", items=1),
    q(N(10), "explain", "演示防漏", "向同伴演示你的顺序列法，请对方找有没有漏。", "能被检查的列表才可信。"),
    q(N(11), "explain", "提出估计问题", "写出要估计哪一段路，为什么不方便直接用尺一次量完。", "路太长就要分段或步测。"),
    q(N(12), "explain", "约定走法", "写下：怎样的步子、谁数、怎么记录、走直线还是绕。", "约定越清楚，两次越接近。"),
    q(N(13), "practice", "步测两遍", "同一段路走两遍，记录步数，计算相差。", "相差大就检查是否忽大忽小。", items=2),
    q(N(14), "explain", "给出估计", "用两次步数给一个估计，并提出一条改进。", "可以取两次接近的值，不要随意丢掉一次。"),
    q(N(15), "explain", "两种规则", "比较编码和搭配：都要按规则列清，一种给位置命名，一种把组合数完。", "规则让结果可以检查。"),
    q(N(16), "practice", "加一个防错标记", "给编码加一种容易检查的标记（如组和序号奇偶），用 4 个例子演示怎样发现抄错。", "标记要简单能算。", items=4),
    q(N(17), "explain", "写说明书", "用不超过六句话写给新生：如何编码或如何步测。", "不在现场的人也要能做。"),
    q(N(18), "practice", "三分钟路演", "按问题—规则—结果—改进讲完，让听的人能复述规则。", "先讲规则，再讲数字。", items=1),
    q(N(19), "practice", "抽签完整项目", "抽编码/搭配/步测之一，走完四步。", "结果必须可检查。", items=1),
    q(N(20), "practice", "通关综合练", "独立完成一个规则清晰的小项目并接受提问。", "问不倒规则，才算通。", items=1),
    q(N(20), "boss", "关主：三年级实践通关试炼", "最终关主：现场完成编码或搭配或步测项目，规则可让别人执行，结果可核对。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g3-practice",
    "title": "三年级 · 综合与实践",
    "subject": "数学",
    "stage": "小学",
    "grade": 3,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "先完成编码小项目（关主 1）；搭配与步测可并行，在 n015 汇合。密码规则小改进（n016）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-code", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：编码设计师、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "小学三年级「综合与实践」地图：位置编码、搭配列举、步测估计。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g3-practice", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
