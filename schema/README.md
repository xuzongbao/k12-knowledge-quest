# 数据模式说明

本目录用 [JSON Schema](https://json-schema.org/)（Draft 2020-12）描述「点亮知识点」地图的四种核心对象。  
地图内容在 `maps/`，校验脚本在 `scripts/validate_map.py`。

**知识点是课标/教材目录风格的教学大纲，不是教材 PDF 原文，也不是习题册扫描。**

## 四个文件

| 文件 | 管什么 |
| --- | --- |
| `knowledge-node.schema.json` | 一个知识点：学段、年级、领域、难度、前置、解锁规则、掌握标准 |
| `knowledge-edge.schema.json` | 两点之间的有向关系 |
| `quest.schema.json` | 绑在某个节点上的任务（讲清楚 / 练习 / 小测 / Boss） |
| `player-progress.schema.json` | 玩家存档：节点状态、经验、已通关地图 |

## 节点 `id`

英文短横线风格，方便程序和后续 Agent Skill 引用：

- `pm` = primary math（小学数学）
- `g1` = 一年级
- `n001` / `geo-n001` / `stat-n001` / `prac-n001` = 领域内节点序号

例：`pm-g1-n001`（数与运算）、`pm-g1-geo-n001`（图形与几何）、`pm-g1-stat-n001`（统计与概率）、`pm-g1-prac-n001`（综合与实践）。

## 边的四种 `type`

| type | 是否影响解锁 | 含义 |
| --- | --- | --- |
| `prerequisite` | 是 | `from` 应先于 `to`。构成 DAG，禁止环 |
| `related` | 否 | 兄弟知识点，可横跳复习 |
| `easily_confused` | 否 | 容易搞混的一对（如「9 加几」与「十几减 9」） |
| `application` | 否 | 把已学技能用到实际问题 |

`nodes.json` 里每个节点的 `prerequisites` 必须和「指向该节点的 prerequisite 边」一致。校验脚本会检查这一点。

## 解锁规则 `unlock_rule.type`

- `hard_all_prereqs`：前置全部为 `lit` 才把本节点变成 `available`（硬前置）。
- `soft_recommended`：建议按边走，但允许提前进入（软锁）。UI 用虚线锁表示。

## 任务 `quest.type`

- `explain`：用自己的话或学具说清楚
- `practice`：短练习
- `mini_quiz`：混合小测
- `boss`：章节关主；一张地图建议 2–3 个

## 进度状态

`locked` → `available` → `learning` → `lit`，之后可能变成 `needs_review`。  
详见 [docs/gameplay.md](../docs/gameplay.md)。

## 以后多学科

Phase 1 的 `strand` 枚举按小学数学四大领域来。语文、英语等学科扩展时：

1. 为该学科增加 `strand` 枚举或改为「学科 + 领域」两级字段
2. 新建 `maps/<subject>/` 目录，复用同一套节点/边/任务/进度模式
3. `subject` 枚举里已预留语文、英语等
