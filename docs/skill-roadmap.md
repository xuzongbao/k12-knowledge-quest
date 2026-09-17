# 后续：做成 Agent Skill / 学习工具

Phase 1 只把「地图数据 + 规则」放进仓库。以后可以包成 Cursor / 其他助手里的 **Skill**，让学生或家长用自然语言玩这张图。

本文是路线，不是现在要写的代码。

## Skill 一次对话里该做的事

1. **定位**  
   读 `player-progress`，找出当前 `available` / `learning` / `needs_review` 节点。
2. **推荐下一盏灯**  
   在硬前置已满足的节点里，优先：主线（非 soft）、低难度、同一 `tags` 章节。
3. **派出任务**  
   从该节点的 `quests.json` 里选一个尚未 `cleared` 的任务；`explain` 用口语引导，`practice` 现场出同构题目（**自编**，不要去抄教材页）。
4. **讲清楚**  
   用节点 `description` 和任务 `success_hint` 做讲解提纲，再用学具或生活例子展开。
5. **判定点亮**  
   对照 `mastery_criteria` 更新存档：XP、`state`、`cleared_quest_ids`。
6. **关主**  
   前置灯都亮了才允许挑战 `boss`；失败只留在 `learning`。

输入输出都应是普通 JSON（进度）+ 中文短句（对学生说的话），方便以后接 App。

## 建议的工具接口（以后再实现）

| 工具名 | 作用 |
| --- | --- |
| `map.overview` | 返回地图标题、起点、通关条件、各层节点 |
| `map.next_nodes` | 给定存档，返回可点亮的下一节点 |
| `quest.start` | 取出某节点的下一个任务 |
| `quest.evaluate` | 学生作答后，返回是否过关、还差哪条掌握标准 |
| `progress.patch` | 合法地改节点状态和 XP |
| `review.due` | 列出 `needs_review` |

全部只读地图 JSON，不在模型里「记住一套私有大纲」。

## 多学科怎么长

- 数学：小学见 `maps/primary-math/`，初中见 `maps/junior-math/`（两套 OVERVIEW；schema 相同）
- 语文：字、词、句、段、篇；阅读策略单独成图
- 英语：把 **word-knowledge-map**（词义、搭配、主题词簇）做成另一张图，节点 id 如 `pe-g3-w012`  
  - 英语单词节点可以用 `related` 连到语文的语素或主题单元  
  - 数学应用题里的「比多比少」以后也可以 `related` 到英语 *more / fewer* 词汇节点  
- 理化生、史地：复用同一套 schema，扩展 `strand` 枚举即可

原则：**先有合法 DAG，再有讲解。** 不要先堆几千个孤立卡片。

## 讲解质量（Skill 约束）

- 对学生说中文；id、字段名保持英文短横线
- 题目必须是**同构新题**（换数量、换情境），禁止整段复述某版教科书
- 发现学生把「9 加几」和「十几减 9」搞反时，顺着 `easily_confused` 边跳转对比，不要只打「错了」
- 软锁支线（序数等）在学生问「第几是什么」时再推，不挡主线口算

## 不在 Skill 第一版做的事

- 真人语音评测、拍照批改口算本
- 排行榜、社交
- 自动爬取任何教材 PDF / 网盘资源

那些要另开 Phase，并且继续遵守：大纲自建，不搬书。
