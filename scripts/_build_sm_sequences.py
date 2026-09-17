"""Build senior-math 数列 map.

Run: python3 scripts/_build_sm_sequences.py

Pedagogical spine: 数列概念 → 等差 → 等比 → 求和与实际（利息）。
裂项、错位相减入门、无穷等比直觉、归纳法萌芽为软锁。未并入 functions 图。grade=11。
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

OUT = ROOT / "maps" / "senior-math" / "sequences"
G = 11
STRAND = "数与代数"
P = "sm-seq"
MAP_ID = "sm-sequences"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "数列的概念", 1, [], ["seq", "ch-seq"], "能说明数列是按正整数顺序排成的一列数，每一项有编号。本图从数列讲起。", mastery=MASTERY_CONCEPT),
    node(N(2), "通项公式", 2, [N(1)], ["seq", "ch-seq"], "能由通项求指定项，也能由若干项猜测简单通项。", mastery=MASTERY_CONCEPT),
    node(N(3), "递推关系入门", 3, [N(2)], ["seq", "ch-seq"], "能由 a_{n+1} 与 a_n 的关系及首项，逐步算出前几项。"),
    node(N(4), "数列与函数对照", 2, [N(2)], ["seq", "ch-seq"], "能说明数列可看成定义在正整数上的函数，图象是孤立点。", mastery=MASTERY_CONCEPT),
    node(N(5), "等差数列定义", 2, [N(3)], ["arith", "ch-arith"], "能说明从第二项起每一项与前一项的差为同一个常数，叫做公差。", mastery=MASTERY_CONCEPT),
    node(N(6), "等差通项", 3, [N(5)], ["arith", "ch-arith"], "能使用 a_n=a_1+(n-1)d 求项、求 n、求 d。", mastery=MASTERY_GATE),
    node(N(7), "等差中项", 3, [N(6)], ["arith", "ch-arith"], "能用 2b=a+c 判断 a、b、c 成等差。"),
    node(N(8), "等差求和推导", 3, [N(6)], ["arith", "ch-arith"], "能说明倒序相加：首尾配对，每一对和相等。", mastery=MASTERY_CONCEPT),
    node(N(9), "等差求和公式", 4, [N(8), N(7)], ["arith", "ch-arith"], "能使用 S_n=n(a_1+a_n)/2 或 S_n=n a_1+n(n-1)d/2。", mastery=MASTERY_GATE),
    node(N(10), "等差性质", 3, [N(9)], ["arith", "ch-arith", "boss-gate"], "能使用下标和相等则项和相等一类性质，解决简单问题。", mastery=MASTERY_GATE),
    node(N(11), "等比数列定义", 2, [N(5)], ["geo", "ch-geo"], "能说明从第二项起每一项与前一项的比为同一个非零常数，叫做公比。", mastery=MASTERY_CONCEPT),
    node(N(12), "等比通项", 3, [N(11), N(6)], ["geo", "ch-geo"], "能使用 a_n=a_1 q^{n-1}（a_1≠0, q≠0）。", mastery=MASTERY_GATE),
    node(N(13), "等比中项", 3, [N(12)], ["geo", "ch-geo"], "能用 b²=ac（同号）判断等比中项。"),
    node(N(14), "公比为 1", 2, [N(12)], ["geo", "ch-geo"], "能指出 q=1 时等比数列是常数列，求和就是 n 倍首项。"),
    node(N(15), "等比求和推导", 3, [N(12)], ["geo", "ch-geo"], "能说明用 q S_n 错位减去 S_n 得到求和公式的思路。", mastery=MASTERY_CONCEPT),
    node(N(16), "等比求和公式", 4, [N(15), N(14), N(13)], ["geo", "ch-geo"], "能分 q=1 与 q≠1 使用公式求前 n 项和。", mastery=MASTERY_GATE),
    node(N(17), "等比性质", 3, [N(16)], ["geo", "ch-geo", "boss-gate"], "能使用下标和相等则积相等一类性质（各项为正时更稳妥）。", mastery=MASTERY_GATE),
    node(N(18), "等差还是等比", 3, [N(10), N(17)], ["seq", "ch-mix"], "能根据差为常数还是比为常数选择模型，并处理简单实际数据。", mastery=MASTERY_GATE),
    node(N(19), "由 S_n 求 a_n", 3, [N(9), N(16)], ["seq", "ch-mix"], "能用 a_n=S_n-S_{n-1}（n≥2）以及 a_1=S_1 还原通项。"),
    node(N(20), "利息与增长率", 4, [N(18)], ["seq", "ch-app"], "能把单利近似看成等差、复利看成等比，并计算几年后的本利。", mastery=MASTERY_GATE),
    node(N(21), "数列合练", 4, [N(19), N(20), N(4)], ["mixed", "ch-end"], "能在等差等比、通项与和、实际增长之间切换。", mastery=MASTERY_GATE),
    node(N(22), "数列通关", 5, [N(21)], ["mixed", "ch-end", "boss-gate"], "能独立完成本图收束检查。", mastery=MASTERY_GATE),
    node(N(23), "裂项相消入门", 3, [N(9)], ["seq", "ch-mix"], "能把 1/(n(n+1)) 拆成差，使中间项抵消。", unlock=SOFT),
    node(N(24), "错位相减入门", 4, [N(16)], ["geo", "ch-geo"], "能对「等差×等比」型简单求和模仿错位一步（入门）。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(25), "无穷等比直觉", 3, [N(16)], ["geo", "ch-geo"], "能说明 |q|<1 时前 n 项和会靠近一个数，|q|≥1 时一般不收敛。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(26), "数学归纳法萌芽", 3, [N(3)], ["seq", "ch-seq"], "能对一个简单通项命题走「验证 n=1，假设 n=k 推 n=k+1」的两步骨架。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(27), "单利复利对照", 3, [N(20)], ["seq", "ch-app"], "能用同一本金对照只加固定利息与「利滚利」的差别。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(28), "等和等比混合", 4, [N(18)], ["seq", "ch-mix"], "能处理「奇数项成等差、偶数项成等比」一类结构的入门题。", unlock=SOFT),
    node(N(29), "数列图象是点", 2, [N(4)], ["seq", "ch-seq"], "能在坐标系里描出前若干项，强调不要连成连续曲线当真。", unlock=SOFT, mastery=MASTERY_CONCEPT),
]


EXTRA_EDGES = [
    {"from": N(5), "to": N(11), "type": "easily_confused", "note": "等差看差，等比看比；公比不能为 0。"},
    {"from": N(6), "to": N(12), "type": "related", "note": "通项都是首项加（乘）若干个公差（公比）。"},
    {"from": N(9), "to": N(16), "type": "easily_confused", "note": "等差求和常配对；等比求和常错位，还要单独处理 q=1。"},
    {"from": N(8), "to": N(15), "type": "related", "note": "两种求和推导都是「再写一次，换个顺序减或加」。"},
    {"from": N(20), "to": N(27), "type": "application", "note": "会套公式之后，对照单利复利的实际差别。"},
    {"from": N(4), "to": N(29), "type": "application", "note": "对照函数之后，更要强调图象是点。"},
    {"from": N(3), "to": N(26), "type": "related", "note": "递推是「下一项怎么来」，归纳法把这种步骤写成证明骨架。"},
]


QUESTS = [
    q(N(1), "explain", "什么是数列", "举一个有穷数列和一个无穷数列，指出第 3 项是哪个。", "有顺序，可以重复。"),
    q(N(2), "practice", "用通项求项", "给定通项求 8 个指定项，或由项猜 2 个简单通项。", "把 n 换成编号。", items=8),
    q(N(3), "practice", "按递推往下写", "给定首项和递推，写出前 6 项，共 2 组。", "一项一项往下。", items=2),
    q(N(4), "explain", "像函数又不连续", "说明为什么数列图象不该随便连成线。", "自变量只取正整数。"),
    q(N(5), "practice", "判断等差", "8 列数判断是否等差，并求出公差。", "每一差都要相等。", items=8),
    q(N(6), "practice", "等差通项计算", "8 道求 a_n、n 或 d。", "a_n=a_1+(n-1)d。", items=8),
    q(N(7), "practice", "等差中项", "6 道用 2b=a+c 判断或求未知数。", "中间一项的两倍等于两边之和。", items=6),
    q(N(8), "explain", "倒序相加", "用自己的话说明为什么首尾配对后每一对和相等。", "公差一正一负抵消。"),
    q(N(9), "practice", "等差求和", "8 道求 S_n。", "项数乘以首尾和的一半。", items=8),
    q(N(10), "practice", "等差性质", "4 道用下标和相等。", "下标和一样，项和一样。", items=4),
    q(N(10), "mini_quiz", "等差小测", "定义、通项、中项、求和。夹一道项数算错。", "n 是项数不是末项。", items=8),
    q(N(10), "boss", "关主：等差数列测绘员", "击败关主：①判断等差 ②通项 ③求和。", "公差和项数两处最容易漏。", xp=80, items=12, qid=f"{P}-boss-arith"),
    q(N(11), "practice", "判断等比", "8 列数判断是否等比，并求出公比，含出现 0 的警示。", "公比不能为 0；中间不能冒出 0 除非全是 0（通常不讨论）。", items=8),
    q(N(12), "practice", "等比通项计算", "8 道求 a_n、n 或 q。", "指数是 n-1。", items=8),
    q(N(13), "practice", "等比中项", "6 道用 b²=ac。", "注意符号：平方会丢负号信息。", items=6),
    q(N(14), "explain", "q=1 为什么要分开", "说明套 q≠1 的求和公式时分母为 0。", "常数列单独加。"),
    q(N(15), "explain", "错位减去", "写出 S 与 qS，说明大部分项能消掉。", "只留下首项和最后多出来的项。"),
    q(N(16), "practice", "等比求和", "8 道，含 q=1 至少 1 道。", "先看 q 是不是 1。", items=8),
    q(N(17), "practice", "等比性质", "4 道下标和相等则积相等（各项为正）。", "对应等差的「和」。", items=4),
    q(N(17), "mini_quiz", "等比小测", "定义、通项、求和、q=1。夹一道公比为负。", "公比为负会正负交错。", items=8),
    q(N(17), "boss", "关主：等比数列航海士", "击败关主：①判断等比 ②通项 ③求和（含说明 q=1）。", "公比和指数两处最容易错。", xp=80, items=12, qid=f"{P}-boss-geo"),
    q(N(18), "practice", "选模型", "6 组数据或文字判断等差、等比或都不是。", "先看差，再看比。", items=6),
    q(N(19), "practice", "由和求项", "4 道已知 S_n 求 a_n。", "n=1 单独，后面做差。", items=4),
    q(N(20), "practice", "利息短题", "2 个：一年一结的复利，求几年后本利和。", "本金乘 (1+r)^n。", items=2),
    q(N(21), "practice", "合练卷", "等差、等比、由和求项、利息各几题。", "先辨等差还是等比。", items=12),
    q(N(22), "practice", "通关综合练", "独立完成：等差求和、等比通项、一个实际增长。", "公式要对应模型。", items=12),
    q(N(22), "boss", "关主：数列通关试炼", "最终关主：①等差 ②等比 ③由 S_n 求 a_n 或一个利息问题。", "通关后记入已通关列表。", xp=100, items=16, qid=f"{P}-boss-map"),
    q(N(23), "practice", "拆成差再加", "把 3 个简单分数项拆差分并求和。", "中间项消掉。", items=3),
    q(N(24), "explain", "再错位一次", "对 1+2q+3q² 这类写出错位的第一步（不必算完）。", "乘 q 后对齐项。"),
    q(N(25), "explain", "越加越靠近吗", "用 |q|<1 和 |q|>1 各举一个和的变化趋势。", "公比绝对值小于 1 才会「加不动了」。"),
    q(N(26), "practice", "走两步骨架", "对一个简单命题写 n=1 验证和 k→k+1 的递推。", "两步都要写，缺一不可。", items=1),
    q(N(27), "practice", "同一本金对照", "本金与年利率相同，算单利 5 年与复利 5 年。", "复利每次把利息并入本金。", items=1),
    q(N(28), "practice", "两种规律夹杂", "1 道：奇数项等差、偶数项等比，求指定项。", "先拆成两个数列。", items=1),
    q(N(29), "practice", "描点不连线", "描出一个等差或等比的前 6 项，并写一句「为什么不连成曲线」。", "点才是数列。", items=1),
]


META = {
    "id": MAP_ID,
    "title": "高中 · 数列",
    "subject": "数学",
    "stage": "高中",
    "grade": G,
    "strand": STRAND,
    "module": "数列",
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "数列概念 → 等差（关主 1）→ 等比（关主 2）→ 选模型、由和求项、利息后收束。裂项（n023）、错位入门（n024）、无穷等比（n025）、归纳萌芽（n026）、单利复利（n027）、混合结构（n028）、描点（n029）为软锁。未并入函数图。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-arith", f"{P}-boss-geo", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败三名关主：等差数列测绘员、等比数列航海士、地图通关试炼。",
    },
    "content_disclaimer": "知识点与任务为普通高中数学课标（2017/2020）目录风格的原创教学大纲与自编提示语，不是任何版本教科书正文或高考试题的摘录。",
    "description": "高中选必「数列」地图：概念 → 等差 → 等比 → 求和与增长模型。独立通关。grade=11。",
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
