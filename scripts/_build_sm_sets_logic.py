"""Build senior-math 集合与常用逻辑用语 map (预备知识).

Run: python3 scripts/_build_sm_sets_logic.py

Pedagogical spine (课标 2017/2020 必修预备知识脉络，自撰短描述，非教材页原文):
  集合 → 常用逻辑用语 → 相等关系与不等关系（含从函数观点看方程/不等式）。
区间表示、德摩根律直觉、反证法萌芽为软锁。本图自洽，不引用小学/初中或其他高中地图节点。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _senior_common import (
    MASTERY_CONCEPT,
    MASTERY_GATE,
    ROOT,
    SOFT,
    node as _node,
    q,
    sample_progress,
    write_map,
)

OUT = ROOT / "maps" / "senior-math" / "sets-logic"
G = 10
STRAND = "数与代数"
P = "sm-set"
MAP_ID = "sm-sets-logic"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    # A. 集合
    node(N(1), "集合的含义", 1, [], ["set", "ch-set"], "能把具有共同属性的对象看成一个整体，并说明集合由元素确定。本图从这里进入预备知识。", mastery=MASTERY_CONCEPT),
    node(N(2), "元素与属于", 2, [N(1)], ["set", "ch-set"], "能判断对象是否属于给定集合，并用 ∈、∉ 书写。", mastery=MASTERY_CONCEPT),
    node(N(3), "列举法", 2, [N(2)], ["set", "ch-set"], "能用花括号把有限个元素一一列出，注意不重复、不遗漏、与顺序无关。"),
    node(N(4), "描述法", 2, [N(2)], ["set", "ch-set"], "能用「满足某条件的对象」描述集合，并与列举法互译简单例子。", mastery=MASTERY_CONCEPT),
    node(N(5), "有限集与无限集", 2, [N(3), N(4)], ["set", "ch-set"], "能区分元素个数有限与无限，并各举一例（如小于 5 的正整数、全体整数）。"),
    node(N(6), "空集", 2, [N(5)], ["set", "ch-set"], "能说明没有元素的集合叫做空集，记作 ∅，它是任何集合的子集。", mastery=MASTERY_CONCEPT),
    node(N(7), "子集", 3, [N(6)], ["set", "ch-set"], "能用 ⊆ 判断 A 是否为 B 的子集：A 的每个元素都属于 B。", mastery=MASTERY_CONCEPT),
    node(N(8), "真子集", 3, [N(7)], ["set", "ch-set"], "能区分 ⊂ 与 ⊆：真子集是子集但不相等。"),
    node(N(9), "集合相等", 3, [N(8)], ["set", "ch-set"], "能用「互相包含」判断两集合相等，而不只看写法是否一样。"),
    node(N(10), "全集", 2, [N(7)], ["set", "ch-set"], "能在讨论补集之前先声明全集：当前问题里所有对象构成的集合。", mastery=MASTERY_CONCEPT),
    node(N(11), "补集", 3, [N(10)], ["set", "ch-set"], "能求集合在全集中的补集：属于全集但不属于该集合的元素。"),
    node(N(12), "交集", 3, [N(7)], ["set", "ch-set"], "能求两集合的交集：同时属于两者的元素。"),
    node(N(13), "并集", 3, [N(12)], ["set", "ch-set"], "能求两集合的并集：至少属于其中之一的元素。"),
    node(N(14), "集合运算综合", 4, [N(9), N(11), N(13)], ["set", "ch-set", "boss-gate"], "能在文氏图或符号式里完成交、并、补的混合，并说明空集、全集的角色。", mastery=MASTERY_GATE),
    # B. 常用逻辑用语
    node(N(15), "命题与真假", 2, [N(14)], ["logic", "ch-logic"], "能识别可以判断真假的陈述叫做命题，并各举一真一假。", mastery=MASTERY_CONCEPT),
    node(N(16), "且、或、非", 3, [N(15)], ["logic", "ch-logic"], "能用且、或、非连接命题，并说明何时为真：且要都真，或要有一真，非要反过来。", mastery=MASTERY_GATE),
    node(N(17), "全称量词", 3, [N(16)], ["logic", "ch-logic"], "能读写「任意 / 所有」语句，并知道举一个反例就能否定全称命题。", mastery=MASTERY_CONCEPT),
    node(N(18), "存在量词", 3, [N(17)], ["logic", "ch-logic"], "能读写「存在 / 至少有一个」语句，并知道要否定它需要说明一个都没有。"),
    node(N(19), "充分条件", 3, [N(16)], ["logic", "ch-logic"], "能说明「若 p 则 q」中 p 是 q 的充分条件：有 p 就一定有 q。", mastery=MASTERY_CONCEPT),
    node(N(20), "必要条件", 3, [N(19)], ["logic", "ch-logic"], "能说明 q 是 p 的必要条件：没有 q 就没有 p；可与充分对照。"),
    node(N(21), "充要条件", 3, [N(20)], ["logic", "ch-logic"], "能判断 p 与 q 是否等价：既充分又必要，可写成当且仅当。", mastery=MASTERY_GATE),
    node(N(22), "四种命题", 3, [N(19)], ["logic", "ch-logic"], "能由原命题写出逆、否、逆否，并说明它们真假不必相同。"),
    node(N(23), "逆否命题", 4, [N(22), N(21)], ["logic", "ch-logic"], "能说明原命题与逆否命题等价，逆命题与否命题等价。", mastery=MASTERY_GATE),
    node(N(24), "逻辑用语综合", 4, [N(18), N(23)], ["logic", "ch-logic", "boss-gate"], "能在集合语句里正确使用量词、且或非、充分必要，不把「有一个」说成「所有」。", mastery=MASTERY_GATE),
    # C. 相等与不等
    node(N(25), "等式与不等式性质", 3, [N(14)], ["ineq", "ch-ineq"], "能回顾等式两边同做一件事仍相等；不等式两边同乘负数要变向。", mastery=MASTERY_CONCEPT),
    node(N(26), "从函数观点看方程", 3, [N(25)], ["ineq", "ch-ineq"], "能把方程 f(x)=0 看成函数图象与 x 轴交点，而不是另一套孤立技巧。", mastery=MASTERY_CONCEPT),
    node(N(27), "一元二次不等式", 4, [N(26)], ["ineq", "ch-ineq"], "能结合二次函数开口与零点，写出一元二次不等式的解集。", mastery=MASTERY_GATE),
    node(N(28), "解集写成集合", 3, [N(27), N(13)], ["ineq", "ch-ineq"], "能把不等式解集写成集合或简单区间形式，并与数轴对照。"),
    node(N(29), "预备知识合练", 4, [N(24), N(28)], ["mixed", "ch-end"], "能在集合运算、逻辑用语、不等式解集之间切换，不混用符号。", mastery=MASTERY_GATE),
    node(N(30), "预备知识通关", 5, [N(29)], ["mixed", "ch-end", "boss-gate"], "能独立完成集合、逻辑用语、从函数观点看不等关系的收束检查。", mastery=MASTERY_GATE),
    # 软锁
    node(N(31), "区间表示", 3, [N(28)], ["set", "ch-ineq"], "能在数轴、不等式、区间三种写法之间互译，注意端点开闭。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(32), "德摩根律直觉", 3, [N(16), N(11)], ["logic", "ch-logic"], "能用文氏图说明「补集的交并会翻转」：非(A 且 B) 相当于 非A 或 非B。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(33), "文氏图复杂情形", 3, [N(14)], ["set", "ch-set"], "能画出三个集合的文氏图，标出「只在两个里出现」的区域。", unlock=SOFT),
    node(N(34), "反证法萌芽", 3, [N(23)], ["logic", "ch-logic"], "能用「先假设结论反面，推出矛盾」说明一个简单全称命题，不要求完整格式证明。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(7), "to": N(9), "type": "easily_confused", "note": "子集允许相等；真子集不允许。写法多一个等号，意思差一层。"},
    {"from": N(12), "to": N(13), "type": "easily_confused", "note": "交是重叠部分，并是合在一起；口头「和」容易说成并却画成交。"},
    {"from": N(17), "to": N(18), "type": "easily_confused", "note": "否定全称用存在反例；否定存在要用「一个都没有」。"},
    {"from": N(19), "to": N(20), "type": "easily_confused", "note": "充分是「有它就够」；必要是「缺它不行」。方向说反最常见。"},
    {"from": N(22), "to": N(23), "type": "related", "note": "四种命题里，只有逆否与原命题永远同真同假。"},
    {"from": N(26), "to": N(27), "type": "application", "note": "先看二次函数图象过不过 x 轴，再写不等式解集。"},
    {"from": N(11), "to": N(32), "type": "related", "note": "补集是德摩根律的几何直觉来源。"},
    {"from": N(14), "to": N(33), "type": "application", "note": "运算综合之后，三个圈的区域才能对上符号。"},
]


QUESTS = [
    q(N(1), "explain", "什么是集合", "用自己的话说明集合是什么，并举一个「是集合」和一个「不宜称作集合」的例子。", "属性要能判断谁在里面、谁不在。"),
    q(N(2), "practice", "属于还是不属于", "对 8 个「对象与集合」判断 ∈ 或 ∉。", "先看集合是用什么属性规定的。", items=8),
    q(N(3), "practice", "用列举法写", "把 6 个集合用列举法写出，检查有没有重复或漏元。", "顺序可变，元素不能重复。", items=6),
    q(N(4), "practice", "列举与描述互译", "6 组：列举改描述，或描述改列举。", "描述法要写清代表元和条件。", items=6),
    q(N(5), "explain", "有限还是无限", "各举两个有限集、无限集，说明你怎么判断。", "数不清个数就是无限，不是「很大」。"),
    q(N(6), "practice", "空集辨认", "从 8 个写法里挑出空集，指出哪些只是看起来像空。", "∅ 没有元素；{∅} 有一个元素。", items=8),
    q(N(7), "practice", "判断子集", "8 组判断 A⊆B 是否成立，含空集。", "逐个检查 A 的元素是否都在 B 里。", items=8),
    q(N(8), "practice", "真子集对照", "6 组区分 ⊆ 与 ⊂，指出相等的那对为什么不是真子集。", "相等时仍是子集，但不是真子集。", items=6),
    q(N(9), "practice", "集合是否相等", "6 组用互相包含判断相等，含写法不同但元素相同。", "元素一样就相等，与列出顺序无关。", items=6),
    q(N(10), "explain", "先声明全集", "给一个「补集」问题，先写出你选定的全集，并说明为什么必须先写。", "全集变了，补集就变了。"),
    q(N(11), "practice", "求补集", "在给定全集下求 6 个集合的补集。", "补集是全集里去掉该集合。", items=6),
    q(N(12), "practice", "求交集", "求 8 对集合的交集，含不相交得到空集。", "两个都要属于才进交集。", items=8),
    q(N(13), "practice", "求并集", "求 8 对集合的并集，注意不要把交当成并。", "来自任何一方的元素都算。", items=8),
    q(N(14), "practice", "交并补混合", "6 道混合运算，可画文氏图辅助。", "由内层括号向外，补集相对谁要看清。", items=6),
    q(N(14), "mini_quiz", "集合小测", "子集、交并补、空集与 {∅} 对照。夹一道把并画成交。", "先元素，再符号。", items=10),
    q(N(14), "boss", "关主：集合运算官", "击败关主：①判断属于与子集 ②完成交并补 ③用文氏图解释一步混合运算。", "符号和区域要能对上。", xp=80, items=12, qid=f"{P}-boss-set"),
    q(N(15), "explain", "这是不是命题", "从若干句子里挑出命题，并判断真假；指出疑问句为什么不是。", "命题必须能判真假。"),
    q(N(16), "practice", "且或非真值", "8 组复合命题判断真假，含「非」只作用一部分。", "且要全真；或要有一真；非是翻转。", items=8),
    q(N(17), "practice", "否定全称", "6 个全称命题，写出否定，并各给一个反例或说明找不到。", "否定「所有」只要存在一个反例。", items=6),
    q(N(18), "practice", "否定存在", "6 个存在命题，写出否定。", "否定「存在」等于「全部都没有」。", items=6),
    q(N(19), "practice", "谁是充分", "8 组「若 p 则 q」，指出谁是谁的充分条件。", "箭头尾巴是充分。", items=8),
    q(N(20), "practice", "谁是必要", "8 组指出必要条件，并与上一节点对照方向。", "没有它就不行，是必要。", items=8),
    q(N(21), "practice", "充要判断", "6 组判断是否充要，把单向的改成正确说法。", "两个方向都要成立才叫充要。", items=6),
    q(N(22), "practice", "写出四种命题", "4 个原命题，写出逆、否、逆否，并标真假（可给简单数例）。", "换位是逆，两边都非是否。", items=4),
    q(N(23), "explain", "为什么看逆否", "用自己的话说明：证明原命题有时改证逆否，因为它们同真同假。", "等价才能换着证。"),
    q(N(24), "practice", "逻辑套集合", "6 道把「所有交于…」「存在属于…」改成符号或反过来。", "量词管的是元素，不是集合名称本身。", items=6),
    q(N(24), "mini_quiz", "逻辑用语小测", "且或非、量词否定、充分必要、逆否。夹一道把充分说反。", "先画箭头，再开口。", items=10),
    q(N(24), "boss", "关主：逻辑用语审查员", "击败关主：①判断复合命题真假 ②否定一个全称或存在 ③指出充分/必要/充要。", "方向和量词两处最容易反。", xp=80, items=12, qid=f"{P}-boss-logic"),
    q(N(25), "explain", "变向还是不变", "对照等式与不等式：两边同乘 -2 之后，等号、不等号各怎样。", "不等式乘负数要变向。"),
    q(N(26), "explain", "方程就是交点", "用二次函数草图说明 x²-1=0 的解是图象与 x 轴的交点。", "解方程可以看成看图象。"),
    q(N(27), "practice", "解一元二次不等式", "解 8 道一元二次不等式，先开口后零点。", "大于 0 看图象在 x 轴上方的部分。", items=8),
    q(N(28), "practice", "写成集合", "把 6 个解集写成集合，并在数轴上标出来。", "端点取不取得到看原不等号。", items=6),
    q(N(29), "practice", "合练卷", "集合运算、逻辑用语、二次不等式解集各几题。", "先辨题型，再选符号。", items=12),
    q(N(30), "practice", "通关综合练", "独立完成：交并补、量词否定、充要判断、二次不等式解集。", "符号、方向、开口，三处最容易漏。", items=12),
    q(N(30), "boss", "关主：预备知识通关试炼", "最终关主：①集合交并补 ②充分必要与量词否定 ③用函数观点解一个二次不等式。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(31), "practice", "三种写法互译", "不等式、区间、数轴各 4 组互译。", "圆括号不含端点，方括号含端点。", items=4),
    q(N(32), "explain", "非且变或", "用两个圈说明：不在重叠里，等于在某个圈外面。", "非(且)变成(或)，圈要画对。"),
    q(N(33), "practice", "三个圈", "在三个集合的文氏图上标出指定区域，如「恰属于两个」。", "先数属于几个集合。", items=4),
    q(N(34), "explain", "先假设反面", "选一个简单全称句，假设存在反例，推出与已知矛盾。", "矛盾来自与已知事实冲突，不是空骂一句。"),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 集合与常用逻辑用语",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "预备知识",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "集合运算（关主 1）→ 常用逻辑用语（关主 2）→ 从函数观点看方程与一元二次不等式后收束。区间（n031）、德摩根律（n032）、三圈文氏图（n033）、反证法萌芽（n034）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-set", f"{P}-boss-logic", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：集合运算官、逻辑用语审查员、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中必修「预备知识」地图：集合 → 常用逻辑用语 → 相等与不等关系。独立通关，不引用跨图节点。grade=10 表示必修学段带。",
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
