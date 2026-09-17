"""Build Grade 1 Comprehensive Practice map JSON.

Run: python3 scripts/_build_grade1_practice.py

Pedagogical spine (课标综合与实践，原创活动骨架，非教材课题原文):
  教室收纳小调查（发现问题→定标准→分类实施→交流）
  → 比一比谁更高（测量活动）
  → 学具摆图案（设计与制作）。
「积木小故事」为软锁支线。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-1-practice"
G = 1
STRAND = "综合与实践"
P = "pm-g1-prac"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "教室里的小麻烦", 1, [], ["find", "ch-tidy"], "能发现教室或书包里「乱、难找」的现象，并说出这是一个可以用分类解决的问题。", mastery=MASTERY_CONCEPT),
    node(N(2), "我们到底想弄清什么", 1, [N(1)], ["find", "ch-tidy"], "能把麻烦改写成一句清楚的问题，例如「哪些东西应该放在一起」。", mastery=MASTERY_CONCEPT),
    node(N(3), "定一个收纳标准", 2, [N(2)], ["plan", "ch-tidy"], "能商量一个分类标准（按用途或按大小），并让同伴重复一遍标准。", mastery=MASTERY_CONCEPT),
    node(N(4), "动手分一分", 2, [N(3)], ["do", "ch-tidy"], "能按商定标准把物品分成几堆，中途不偷偷换标准。"),
    node(N(5), "数一数记下来", 2, [N(4)], ["do", "ch-tidy"], "能数出每一堆有几个，用图画或数字记在纸上。"),
    node(N(6), "把收纳结果说给别人听", 2, [N(5)], ["share", "ch-tidy"], "能用「我们按……分，这一堆有……」向别人汇报。", mastery=MASTERY_CONCEPT),
    node(N(7), "收纳小项目综合", 3, [N(6)], ["share", "ch-tidy", "boss-gate"], "能把发现、标准、实施、汇报连成一次完整的小项目。", mastery=MASTERY_GATE),
    node(N(8), "发现：谁更高更长", 1, [N(7)], ["find", "ch-measure"], "能提出比较桌椅、积木塔、彩带谁更高/更长的问题。", mastery=MASTERY_CONCEPT),
    node(N(9), "计划用什么来比", 2, [N(8)], ["plan", "ch-measure"], "能选择小棒、手掌或同样长的纸条当「尺子」，并说明要同样的办法比才公平。", mastery=MASTERY_CONCEPT),
    node(N(10), "实施比一比", 2, [N(9)], ["do", "ch-measure"], "能对齐一端进行比较，并记录谁高、谁矮、差不多。"),
    node(N(11), "交流比较结果", 2, [N(10)], ["share", "ch-measure"], "能向同伴展示记录，并讨论「换一种尺子结果会不会变」。", mastery=MASTERY_CONCEPT),
    node(N(12), "发现：想摆一个图案", 1, [N(7)], ["find", "ch-make"], "能提出用学具摆小房子、小鱼等图案的愿望，并说要用哪些形状。", mastery=MASTERY_CONCEPT),
    node(N(13), "计划图案草稿", 2, [N(12)], ["plan", "ch-make"], "能先在纸上画出要用几块、大概怎么摆，再动手。", mastery=MASTERY_CONCEPT),
    node(N(14), "实施摆一摆", 2, [N(13)], ["do", "ch-make"], "能按草稿摆出图案，摆不下去时修改计划而不是乱动。"),
    node(N(15), "交流作品", 2, [N(14)], ["share", "ch-make"], "能介绍作品用了哪些图形、哪一部分最难摆。", mastery=MASTERY_CONCEPT),
    node(N(16), "积木小故事", 2, [N(11), N(15)], ["make", "ch-make"], "能用积木搭一个小场景，并用上下左右讲一句故事。", unlock=SOFT),
    node(N(17), "两个项目合练", 3, [N(11), N(15)], ["mixed", "ch-end"], "能在测量和制作里都走完「问题—计划—实施—交流」。", mastery=MASTERY_GATE),
    node(N(18), "一年级实践通关", 3, [N(17)], ["mixed", "ch-end", "boss-gate"], "能独立完成一次入门综合活动的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(3), "to": N(4), "type": "easily_confused", "note": "标准是事先商量的；实施时改标准，别人就对不上了。"},
    {"from": N(9), "to": N(10), "type": "easily_confused", "note": "一端没对齐，比出来的高矮不算数。"},
    {"from": N(8), "to": N(12), "type": "related", "note": "比高低和摆图案都可以在教室里完成，都要先有计划。"},
    {"from": N(6), "to": N(11), "type": "related", "note": "交流时都要让别人听懂你用了什么办法。"},
    {"from": N(10), "to": N(16), "type": "application", "note": "搭积木故事时正好用得上谁高谁在上面。"},
]


QUESTS = [
    q(N(1), "explain", "找出一个麻烦", "在教室或书包里指出一样「不好找/堆在一起」的东西，说明为什么这是个问题。", "问题要具体，不要只说「好乱」。"),
    q(N(2), "explain", "写成问句", "把麻烦写成一句「我们想知道……」或「我们想把……放好」。", "问句要能用行动回答。"),
    q(N(3), "explain", "商量标准", "和同伴定一个分类标准，各用一句话说给对方听，看是否一样。", "两个人说的标准必须能对上。"),
    q(N(4), "practice", "按标准分堆", "按商定标准把 12 件物品分成至少 3 堆，中途不改口。", "拿起一件先问：它属于哪一堆？", items=12),
    q(N(5), "practice", "记下每一堆", "数出每堆个数，用圆圈或数字记在纸上。", "点着数，写完再复核。", items=3),
    q(N(6), "explain", "汇报收纳", "向另一组汇报：标准是什么、分了几堆、每堆几个。", "先说标准，再说数字。"),
    q(N(7), "practice", "走完收纳圈", "换一批物品，自己走完发现—标准—分类—记录—汇报。", "缺一步就补上。", items=1),
    q(N(7), "mini_quiz", "收纳项目小测", "看别人的活动找缺步：没标准就分、没记录就汇报等。", "四步都要在。", items=6),
    q(N(7), "boss", "关主：收纳小队长", "击败关主：①找出可分类的麻烦 ②定标准并分类计数 ③向别人说清楚结果。", "没有标准，就没有公平的分堆。", xp=80, items=10, qid=f"{P}-boss-tidy"),
    q(N(8), "explain", "提出比较问题", "提出一个「谁更高/更长」的问题，指出要比较的两样东西。", "两样东西要能放在一起比。"),
    q(N(9), "explain", "选公平的办法", "在手掌、小棒、纸条里选一种，说明为什么两次要用同一种。", "办法中途更换，比出来就不公平。"),
    q(N(10), "practice", "对齐再比", "比较三样物品的高或长，记录顺序，强调一端对齐。", "先对齐，再看另一端。", items=3),
    q(N(11), "explain", "说说比的结果", "展示记录，并回答：如果改用手掌量，顺序会不会变。", "顺序通常不变，格数可能会变。"),
    q(N(12), "explain", "想摆什么", "说出想摆的图案名称，以及打算用的两种形状。", "先有目标，再动手。"),
    q(N(13), "explain", "先画草稿", "在纸上画出大约几块、哪块当屋顶或车轮。", "草稿可以很简单，但不能没有。"),
    q(N(14), "practice", "按草稿摆", "用学具摆出图案；若摆不下，在草稿上改一笔再摆。", "先改计划，再改作品。", items=1),
    q(N(15), "explain", "介绍作品", "介绍用了哪些形状、哪一步最难、你是怎么改计划的。", "让别人听得见你的想法，不只是看成品。"),
    q(N(16), "practice", "积木讲一句", "搭一个至少三层的小场景，用上、下说一句故事。", "下面先放站得稳的块。", items=1),
    q(N(17), "practice", "两项目回顾", "用四步名称，分别给测量和制作各写一行：我们做了什么。", "每行都要有问题、计划、实施、交流。", items=2),
    q(N(18), "practice", "通关综合练", "抽一项：收纳、比较或摆图案，独立走完四步并汇报。", "缺哪一步就回到那盏灯。", items=1),
    q(N(18), "boss", "关主：一年级实践通关试炼", "最终关主：当场完成一个小项目四步（收纳或比较或摆图案），能让别人听懂你的标准和结果。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g1-practice",
    "title": "一年级 · 综合与实践",
    "subject": "数学",
    "stage": "小学",
    "grade": 1,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "先完成教室收纳小项目（关主 1），再并行「比高低」与「摆图案」，在 n017 汇合。积木小故事（n016）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-tidy", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：收纳小队长、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "小学一年级「综合与实践」地图：收纳分类、比较高低、学具制作。项目式节点，独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g1-practice", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-explain"),
    )


if __name__ == "__main__":
    main()
