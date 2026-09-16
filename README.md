# k12-knowledge-quest

中小学**知识图谱** + 轻量 RPG：**点亮知识点、打关升级**。

现在完成的是 **Phase 0–1**：把数据格式定下来，并做出两张可校验、可通关的样例地图——**小学一年级「数与运算入门」**和**二年级「数与运算」**。

> **内容边界（请先读）：**  
> 知识点是义务教育课标四大领域 + 常见教材**目录/教学脉络**风格的**原创大纲**，用来排学习顺序。  
> **不是**人教版或其他版本教科书 PDF 的摘录，也不是练习册扫描。仓库里不会放、也不会去爬教材正文。

许可证：[MIT](LICENSE)

---

## 这个项目要干什么

很多学生「会做这页练习」，但说不清这个点和前面哪个点连着。  
我们把小学到高中的内容拆成**一盏盏灯（知识点）**，灯和灯之间有「必须先会」「容易搞混」「用来解题」等关系。学生按图走：

1. 打开当前能学的灯  
2. 完成讲解 / 练习 / 小测  
3. 灯亮，经验增加  
4. 章节关主出现，打过就进下一章  
5. 整张地图通关，以后还可以复习（灯会闪，提醒回看）

以后可以做成 App，或做成 AI **Skill**（助手根据地图推荐「下一盏灯」并出同构新题）。Skill 设想见 [docs/skill-roadmap.md](docs/skill-roadmap.md)。

## 阶段

| 阶段 | 内容 | 状态 |
| --- | --- | --- |
| 0 | 仓库、许可证、模式（schema）、玩法文字 | ✅ 本仓库 |
| 1 | 小学数学样例：一、二年级数与运算可通关地图 + 1–6 年级标题路书 | ✅ 本仓库 |
| 2 | 补全小学数学其余年级/领域地图（仍是大纲，不搬书） | 未开始 |
| 3 | 语文、英语等学科；英语可挂「单词知识图」 | 未开始 |
| 4 | 游戏客户端或 Agent Skill：读 JSON、改存档、出题 | 未开始 |

**Phase 1 只做小学数学。** 其它学科先在模式里留好 `subject` 枚举。

## 目录

```
schema/                              四种 JSON Schema + 短说明
maps/primary-math/OVERVIEW.md        小学数学 1–6 年级领域标题（路书）
maps/primary-math/grade-1-numbers/   一年级「数与运算」地图（四个 JSON + 演示存档）
maps/primary-math/grade-2-numbers/   二年级「数与运算」地图（同上）
docs/gameplay.md                     点亮、经验、关主、软锁/硬前置
docs/skill-roadmap.md                以后做成 Skill 的接口设想
scripts/validate_map.py              校验地图合法
scripts/_build_grade1_numbers.py     重新生成一年级 JSON
scripts/_build_grade2_numbers.py     重新生成二年级 JSON
LICENSE                              MIT
docs/gameplay.md                 点亮、经验、关主、软锁/硬前置
docs/skill-roadmap.md            以后做成 Skill 的接口设想
scripts/validate_map.py          校验地图合法
LICENSE                          MIT
```

## 模式怎么工作

四种对象，分开存，用 id 互相指：

| 对象 | 文件 | 关键字段 |
| --- | --- | --- |
| 知识点 | `knowledge-node.schema.json` | `id` `title` `subject` `stage`（小学）`grade`（1–6）`strand`（数与代数 / 图形与几何 / 统计与概率 / 综合与实践）`difficulty`（1–5）`prerequisites` `tags` `unlock_rule` `mastery_criteria` `description` |
| 边 | `knowledge-edge.schema.json` | `from` `to` `type`：`prerequisite` / `related` / `easily_confused` / `application` |
| 任务 | `quest.schema.json` | 绑在一个节点上：`explain` / `practice` / `mini_quiz` / `boss` |
| 进度 | `player-progress.schema.json` | 每盏灯：`locked` / `available` / `learning` / `lit` / `needs_review`；还有 `xp_total`、`cleared_map_ids` |

约定：

- 给学生看的字用**中文**
- 程序 id 用英文短横线，如 `pm-g1-n001`、`pm-g2-n001`（primary math，年级，第几号节点）
- `nodes.json` 里的 `prerequisites` 必须和「指向它的 prerequisite 边」一致
- 只有前置边参与解锁；它们必须构成**有向无环图（DAG）**

更细的字段说明：[schema/README.md](schema/README.md)。  
怎么点亮、怎么发经验：[docs/gameplay.md](docs/gameplay.md)。

## 怎么「玩」这些样例地图

现在没有画面，按数据走即可，和以后客户端规则相同。两张图各自通关，**还没有**跨地图进度引擎。

### 一年级 · 数与运算入门

1. 打开 [`maps/primary-math/grade-1-numbers/map.meta.json`](maps/primary-math/grade-1-numbers/map.meta.json)  
   - 地图名：**一年级 · 数与运算入门**  
   - 起点：`pm-g1-n001` 数一数（10以内）  
   - 通关：点亮全部节点，并打过三名关主
2. 打开 `nodes.json`，从起点读 `description`（一句话目标）
3. 打开 `quests.json`，做该节点的任务；做完在存档里把节点标成 `lit`
4. 打开 `edges.json`，沿着 `type: "prerequisite"` 的箭头，看下一盏 `available` 的灯  
   （演示存档 [`player-progress.sample.json`](maps/primary-math/grade-1-numbers/player-progress.sample.json) 里，起点已亮，`同样多、多、少` 可学，`认识1～5` 学到一半）
5. 主线建议：10 以内 → 关主 1 → 20 以内进退位 → 关主 2 → 100 以内数与简单加减、应用题 → 关主 3  
   「第几：基数与序数」是**软锁支线**，不挡口算，但通关前仍要点亮

### 二年级 · 数与运算

1. 打开 [`maps/primary-math/grade-2-numbers/map.meta.json`](maps/primary-math/grade-2-numbers/map.meta.json)  
   - 地图名：**二年级 · 数与运算**  
   - 起点：`pm-g2-n001` 100以内数的组成复习  
   - 通关：点亮全部节点，并打过三名关主（一百以内进退位、表内乘除、地图通关试炼）
2. 演示存档里，起点已亮，`两位数加一位数（进位）` 可学，`两位数加两位数（不进位）` 学到一半
3. 主线建议：100 以内进退位 → 关主 1 → 表内乘法 → 表内除法（含有余数）→ 关主 2 → 混合运算与小括号 → 万以内数与估算 → 关主 3  
   「奇数与偶数」是**软锁支线**，不挡口诀，但通关前仍要点亮  
   万以内数认识可与加减主线并行，在「整百整千加减」处汇合

打印推荐层（从起点沿前置边展开）：

```bash
python3 scripts/validate_map.py maps/primary-math/grade-1-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-2-numbers --tree
```

## 校验命令

需要 Python 3.10+。图结构检查只用标准库。若要连 JSON Schema 一起验：

```bash
pip install -r scripts/requirements.txt
python3 scripts/validate_map.py maps/primary-math/grade-1-numbers
python3 scripts/validate_map.py maps/primary-math/grade-2-numbers
python3 scripts/validate_map.py --all
```

退出码 0 表示通过。

重新生成样例 JSON（改对应 `_build_*.py` 之后）：

```bash
python3 scripts/_build_grade1_numbers.py
python3 scripts/_build_grade2_numbers.py
python3 scripts/validate_map.py --all --tree
```

## 以后多学科

小学数学 1–6 年级领域标题已经列在 [maps/primary-math/OVERVIEW.md](maps/primary-math/OVERVIEW.md)，目前一、二年级「数与运算」已做成可通关地图，其余年级/领域仍是**只占题目**。  
两张地图概念上衔接（一年级 100 以内 → 二年级起点复习），但存档和校验都按图独立，跨地图进度以后再做。  
语文、英语将新增 `maps/<学科>/`，复用同一套 schema。英语单词知识图可以和语文语素、数学应用题用语用 `related` 边连起来（见 Skill 路线）。

## 已知缺口（下一步）

- 还没有图形界面，状态要靠读 JSON 想象
- 练习题只有提示语，没有自动出题器
- 三年级及以后、以及图形与几何等其它领域地图尚未填写节点
- `strand` 枚举目前按数学四大领域；其他学科需要扩展字段

这些不挡 Phase 1：模式、样例 DAG、校验、许可证已经齐。
