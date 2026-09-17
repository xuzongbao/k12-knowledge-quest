"""Build Grade 6 Comprehensive Practice map JSON.

Run: python3 scripts/_build_grade6_practice.py

原创活动骨架：抽屉里一定有相同的发现、跨领域校园小课题、小学数学成果展。
「反例与边界」为软锁。本图自洽，不引用跨图节点。
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

OUT = ROOT / "maps" / "primary-math" / "grade-6-practice"
G = 6
STRAND = "综合与实践"
P = "pm-g6-prac"


def node(nid, title, difficulty, prereqs, tags, description, *, unlock=None, mastery=None):
    return _node(
        nid, title, G, STRAND, difficulty, prereqs, tags, description, unlock=unlock, mastery=mastery
    )


def N(k: int) -> str:
    return f"{P}-n{k:03d}"


NODES = [
    node(N(1), "发现：多出来的一定挤在一起", 1, [], ["find", "ch-pigeon"], "能从「抽屉、袜子、生日月份」等情境感到：东西比格子多时，至少有一格会多于一个。", mastery=MASTERY_CONCEPT),
    node(N(2), "计划：格子和东西", 2, [N(1)], ["plan", "ch-pigeon"], "能明确什么当格子、什么当放进去的东西，先数清两类。", mastery=MASTERY_CONCEPT),
    node(N(3), "实施：最均匀也还会多", 3, [N(2)], ["do", "ch-pigeon"], "能用「尽量放均匀」说明：东西比格子多 1 时，至少一格有 2 个。"),
    node(N(4), "实施：想保证某一格有 3 个", 3, [N(3)], ["do", "ch-pigeon"], "能思考要放多少才能保证至少一格有 3 个（在简单数字里）。"),
    node(N(5), "实施：举生活例子", 3, [N(4)], ["do", "ch-pigeon"], "能自编一个生活例子，并指出格子、东西、保证的那句话。"),
    node(N(6), "交流：这不是碰巧", 3, [N(5)], ["share", "ch-pigeon", "boss-gate"], "能说明结论在「最不巧、最均匀」时仍然成立，所以不是碰巧。", mastery=MASTERY_GATE),
    node(N(7), "发现：校园里的综合问题", 2, [N(6)], ["find", "ch-project"], "能提出一个要用到测量或统计或编码中至少两样的校园问题。", mastery=MASTERY_CONCEPT),
    node(N(8), "计划：课题说明书", 2, [N(7)], ["plan", "ch-project"], "能写课题说明书：问题、需要的数据、步骤、可能用到的图或模型。", mastery=MASTERY_CONCEPT),
    node(N(9), "实施：收集与测量", 3, [N(8)], ["do", "ch-project"], "能按说明书收集或测量，记录来源和时间。"),
    node(N(10), "实施：选择数学工具", 3, [N(9)], ["do", "ch-project"], "能选择表、图、平均/中位/众数、简单模型中至少两种处理数据。"),
    node(N(11), "实施：得出不超过数据的结论", 3, [N(10)], ["do", "ch-project"], "能写出结论，并写清对象范围和局限。"),
    node(N(12), "交流：课题答辩", 4, [N(11)], ["share", "ch-project"], "能回答数据从哪来、为什么选这个图或这个统计量。", mastery=MASTERY_GATE),
    node(N(13), "发现：六年要留下什么", 2, [N(6)], ["find", "ch-exhibit"], "能提出为小学数学做一次成果展：选哪些作品、给谁看。", mastery=MASTERY_CONCEPT),
    node(N(14), "计划：展览结构", 2, [N(13)], ["plan", "ch-exhibit"], "能把展览分成「会算、会量、会调查、会建模」等几块，每块有代表作。", mastery=MASTERY_CONCEPT),
    node(N(15), "实施：整理作品说明卡", 3, [N(14)], ["do", "ch-exhibit"], "能为每件作品写说明卡：问题、方法、结果、我还想改什么。"),
    node(N(16), "实施：参观路线", 3, [N(15)], ["do", "ch-exhibit"], "能设计参观顺序，让没学过的低年级也能先看简单的。"),
    node(N(17), "交流：讲解与提问", 3, [N(12), N(16)], ["share", "ch-exhibit"], "能给参观者讲 2 分钟，并准备两个常问问题的回答。", mastery=MASTERY_CONCEPT),
    node(N(18), "小学实践工具箱", 4, [N(17)], ["mixed", "ch-end"], "能列出综合与实践常用步骤：发现、计划、实施、交流，以及证据从哪来。", mastery=MASTERY_CONCEPT),
    node(N(19), "反例与边界", 3, [N(6)], ["pigeon", "ch-pigeon"], "能举出「格子和东西一样多时不能保证有一格有两个」的反例，从而看清边界。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(20), "如果数据不可靠", 3, [N(12)], ["project", "ch-project"], "能假设一批数据漏记或对象不对，说明结论要怎样降级。", unlock=SOFT, mastery=MASTERY_CONCEPT),
    node(N(21), "给五年级的一封信", 3, [N(18)], ["share", "ch-end"], "能写信告诉低一年级：做一个综合项目最容易漏的三步。", mastery=MASTERY_CONCEPT),
    node(N(22), "跨领域对照", 3, [N(18)], ["mixed", "ch-end"], "能指出本次课题用了哪些领域的思想（数、图、统计、实践），但不必引用其他地图节点。", mastery=MASTERY_CONCEPT),
    node(N(23), "成果展彩排", 4, [N(21), N(22)], ["share", "ch-end"], "能按时间把讲解压缩到规定时长，数字来源仍说得清。"),
    node(N(24), "六年级实践合练", 4, [N(23)], ["mixed", "ch-end"], "能抽签完成抽屉发现、校园课题或成果展说明卡中的完整流程。", mastery=MASTERY_GATE),
    node(N(25), "小学实践收束", 4, [N(24)], ["mixed", "ch-end"], "能用一个项目证明自己会走完四步，并说明局限。", mastery=MASTERY_GATE),
    node(N(26), "六年级实践通关", 5, [N(25)], ["mixed", "ch-end", "boss-gate"], "能独立完成小学综合与实践线的收束检查。", mastery=MASTERY_GATE),
]


EXTRA_EDGES = [
    {"from": N(3), "to": N(4), "type": "related", "note": "保证有 2 个和保证有 3 个，只是「最均匀仍会多出来」的不同程度。"},
    {"from": N(3), "to": N(19), "type": "easily_confused", "note": "东西不比格子多时，不能保证某一格有两个。"},
    {"from": N(8), "to": N(10), "type": "application", "note": "说明书里预告的工具，实施时要对着数据真正选一次。"},
    {"from": N(11), "to": N(20), "type": "application", "note": "写过局限，才容易设想数据变差时结论如何降级。"},
    {"from": N(15), "to": N(17), "type": "related", "note": "说明卡上的四句，就是口头讲解的骨架。"},
    {"from": N(6), "to": N(22), "type": "related", "note": "抽屉发现也是一种建模：格子与东西的对应。"},
]


QUESTS = [
    q(N(1), "explain", "说出现象", "用抽屉或袜子举例，说出「多出来的会挤在同一类」的感觉。", "先有感觉，再数格子。"),
    q(N(2), "explain", "谁是格子谁是东西", "在自选情境里标明格子和东西各是什么、各有几个。", "两类都要数清。"),
    q(N(3), "practice", "最均匀仍多 1", "若干组「格子 n、东西 n+1」，说明为什么至少一格有 2 个。", "先均匀分，再看多出来的 1。", items=4),
    q(N(4), "practice", "保证有 3 个", "在小数字里计算：要保证至少一格有 3 个，至少要放几件。", "先让每格都有 2 个，再多 1 件。", items=4),
    q(N(5), "explain", "自编例子", "自编生活例子，写清格子、东西、保证句。", "保证句里要有「至少」。"),
    q(N(6), "explain", "不是碰巧", "解释为什么看「最均匀」的放法就够了。", "最不巧都成立，其他情况更成立。"),
    q(N(6), "mini_quiz", "抽屉发现小测", "判断保证句对不对，指出格子和东西是否搞反。", "先对齐两类再保证。", items=8),
    q(N(6), "boss", "关主：抽屉发现者", "击败关主：①分清格子与东西 ②说明多 1 件时的保证 ③自编一个生活例子。", "最均匀仍然多，就不是碰巧。", xp=80, items=10, qid=f"{P}-boss-pigeon"),
    q(N(7), "explain", "提出综合问题", "写出一个校园问题，并标明会用到的至少两种办法（量、问、画、编码等）。", "一种办法不够，才叫综合。"),
    q(N(8), "explain", "课题说明书", "写问题、数据、步骤、预备工具。", "别人按说明书能开工。"),
    q(N(9), "practice", "留下来源", "收集或测量一组数据，每条注明来源和时间。", "没有来源的数以后答辩会垮。", items=1),
    q(N(10), "practice", "选用两种工具", "对同一批数据用两种工具处理（如表+折线，或平均+中位）。", "说明为什么选它们。", items=2),
    q(N(11), "explain", "写结论和局限", "结论不超过三句，局限至少一句。", "对象范围要写进结论。"),
    q(N(12), "practice", "课题答辩", "回答三个问题：数据从哪来、为何选这个图、结论不能代表谁。", "答不出就回到说明书。", items=3),
    q(N(12), "mini_quiz", "课题质量小测", "给几份模拟课题找缺：无来源、图选错、结论越界。", "证据链要完整。", items=6),
    q(N(13), "explain", "展览给谁看", "确定观众（低年级、家长或本班），说明因此要选哪些作品。", "观众不同，讲解深度不同。"),
    q(N(14), "explain", "分块", "把展览分成至少三块，每块举一件代表作。", "块的名字要让外行人懂。"),
    q(N(15), "practice", "写说明卡", "为两件作品各写四句说明卡。", "问题、方法、结果、改进。", items=2),
    q(N(16), "practice", "设计路线", "画出参观顺序，把最容易的放在前面。", "路线也是一种优化。", items=1),
    q(N(17), "practice", "两分钟讲解", "讲解一件作品，并准备两个提问的回答。", "超时就删细节，不删来源。", items=1),
    q(N(18), "explain", "打开实践工具箱", "说出四步名称，以及每一步需要留下什么证据。", "没有证据的交流只是讲故事。"),
    q(N(19), "explain", "看清边界", "举出格子和东西一样多时的反例，说明此时不能保证。", "边界让保证句更精确。"),
    q(N(20), "explain", "数据变差", "假设漏记一半，说明结论应改成更谨慎的说法。", "证据弱，结论就要降级。"),
    q(N(21), "explain", "三句提醒", "给五年级写最容易漏的三步。", "例如：没约定就动手、没有来源、结论越界。"),
    q(N(22), "explain", "用到哪些思想", "列出本次课题用到的领域思想，不写其他地图的节点 id。", "综合是思想合用，不是把图锁在一起。"),
    q(N(23), "practice", "压缩彩排", "把讲解压到规定时长，请同伴计时并提问来源。", "短，但来源还在。", items=1),
    q(N(24), "practice", "抽签走流程", "抽抽屉发现 / 校园课题 / 说明卡讲解之一完整做完。", "四步和证据都要齐。", items=1),
    q(N(25), "practice", "收束项目", "自选一个项目证明会走四步，并主动说出一个局限。", "能说局限，才像真做完。", items=1),
    q(N(26), "practice", "通关综合练", "独立完成小学综合实践收束：规则或模型、数据或例子、交流与局限。", "发现—计划—实施—交流。", items=1),
    q(N(26), "boss", "关主：六年级实践通关试炼", "最终关主：①讲清一个「一定有相同」的保证例子 ②展示一个带证据的校园小课题或说明卡 ③说出局限。小学综合与实践线在此收束。", "通关后记入已通关列表。", xp=100, items=8, qid=f"{P}-boss-map"),
]


META = {
    "id": "pm-g6-practice",
    "title": "六年级 · 综合与实践",
    "subject": "数学",
    "stage": "小学",
    "grade": 6,
    "strand": STRAND,
    "version": "0.1.0",
    "locale": "zh-CN",
    "start_node_ids": [N(1)],
    "recommended_path_note": "抽屉发现为主线（关主 1）；校园综合课题与成果展可并行，在 n017 汇合。反例与边界（n019）、数据不可靠（n020）为软锁，不挡终章关主，通关前仍须点亮。",
    "win_condition": {
        "type": "light_all_nodes_and_bosses",
        "required_node_ids": "all",
        "required_boss_quest_ids": [f"{P}-boss-pigeon", f"{P}-boss-map"],
        "summary": "点亮全部知识点，并击败两名关主：抽屉发现者、地图通关试炼。",
    },
    "content_disclaimer": "活动骨架为课标综合与实践风格的原创设计，不是教材课题或练习页的摘录。",
    "description": "小学六年级「综合与实践」地图：抽屉原理发现、跨领域小课题、小学成果展。独立通关，不引用跨图节点。",
}


def main() -> None:
    write_map(
        OUT, META, NODES, EXTRA_EDGES, QUESTS,
        sample_progress("pm-g6-practice", N(1), f"{N(1)}-explain", N(2), N(3), f"{N(3)}-practice"),
    )


if __name__ == "__main__":
    main()
