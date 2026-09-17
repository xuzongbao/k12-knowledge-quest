# k12-knowledge-quest

中小学**知识图谱** + 轻量 RPG：**点亮知识点、打关升级**。

现在完成的是 **Phase 0–2 以及初中数学 7–9**：把数据格式定下来，并做出可校验、可通关的样例地图——

- **小学**一至六年级四大领域，共 **24** 张（`maps/primary-math/`）
- **初中**七至九年级四大领域，共 **12** 张（`maps/junior-math/`）

小学与初中共用同一套 JSON Schema。**小学数学四大领域地图线完成；初中数学 7–9 四大领域地图线完成。**

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
| 1 | 小学数学样例：一至六年级数与运算可通关地图 + 1–6 年级标题路书 | ✅ 本仓库（数与运算 1–6 线完成） |
| 2 | 补全小学数学其余领域地图（图形与几何、统计与概率、综合与实践；仍是大纲，不搬书） | ✅ 本仓库：**小学数学四大领域地图线完成**（24 张图） |
| 2b | 初中数学 7–9 四大领域（数与代数、图形与几何、统计与概率、综合与实践；schema 与小学相同） | ✅ 本仓库：**初中数学 7–9 四大领域地图线完成**（12 张图） |
| 3 | 语文、英语等学科；英语可挂「单词知识图」 | 未开始 |
| 4 | 游戏客户端或 Agent Skill：读 JSON、改存档、出题 | 未开始 |

**Phase 1–2 做小学数学，2b 做初中数学。** 其它学科先在模式里留好 `subject` 枚举。小学 / 初中数学地图 **schema 仍共用**，只是 `stage`、`grade` 和节点 id 前缀不同。

## 目录

```
schema/                              四种 JSON Schema + 短说明（小学/初中共用）
maps/primary-math/OVERVIEW.md        小学数学 1–6 年级领域标题（路书）
maps/primary-math/grade-*-numbers/   一至六年级「数与运算」地图（四个 JSON + 演示存档）
maps/primary-math/grade-*-geometry/  一至六年级「图形与几何」地图（同上）
maps/primary-math/grade-*-statistics/一至六年级「统计与概率」地图（同上）
maps/primary-math/grade-*-practice/  一至六年级「综合与实践」地图（同上）
maps/junior-math/OVERVIEW.md         初中数学 7–9 年级领域标题（路书）
maps/junior-math/grade-7-algebra/    七年级「数与代数」地图（四个 JSON + 演示存档）
maps/junior-math/grade-7-geometry/   七年级「图形与几何」地图（同上）
maps/junior-math/grade-7-statistics/ 七年级「统计与概率」地图（同上）
maps/junior-math/grade-7-practice/   七年级「综合与实践」地图（同上）
maps/junior-math/grade-8-algebra/    八年级「数与代数」地图（同上）
maps/junior-math/grade-8-geometry/   八年级「图形与几何」地图（同上）
maps/junior-math/grade-8-statistics/ 八年级「统计与概率」地图（同上）
maps/junior-math/grade-8-practice/   八年级「综合与实践」地图（同上）
maps/junior-math/grade-9-algebra/    九年级「数与代数」地图（同上）
maps/junior-math/grade-9-geometry/   九年级「图形与几何」地图（同上）
maps/junior-math/grade-9-statistics/ 九年级「统计与概率」地图（同上）
maps/junior-math/grade-9-practice/   九年级「综合与实践」地图（同上）
docs/gameplay.md                     点亮、经验、关主、软锁/硬前置
docs/skill-roadmap.md                以后做成 Skill 的接口设想
scripts/validate_map.py              校验地图合法（`--all` 会扫描 maps/ 下所有含 map.meta.json 的目录）
scripts/_geo_common.py               图形地图生成共用函数
scripts/_map_common.py               统计/实践等地图生成共用函数（`stage` 可设小学或初中）
scripts/_junior_common.py            初中地图生成：默认 `stage=初中`
scripts/_build_grade*_*.py           重新生成小学各图 JSON
scripts/_build_jm_g7_algebra.py      重新生成七年级数与代数 JSON
scripts/_build_jm_g7_geometry.py     重新生成七年级图形与几何 JSON
scripts/_build_jm_g7_statistics.py   重新生成七年级统计与概率 JSON
scripts/_build_jm_g7_practice.py     重新生成七年级综合与实践 JSON
scripts/_build_jm_g8_algebra.py      重新生成八年级数与代数 JSON
scripts/_build_jm_g8_geometry.py     重新生成八年级图形与几何 JSON
scripts/_build_jm_g8_statistics.py   重新生成八年级统计与概率 JSON
scripts/_build_jm_g8_practice.py     重新生成八年级综合与实践 JSON
scripts/_build_jm_g9_algebra.py      重新生成九年级数与代数 JSON
scripts/_build_jm_g9_geometry.py     重新生成九年级图形与几何 JSON
scripts/_build_jm_g9_statistics.py   重新生成九年级统计与概率 JSON
scripts/_build_jm_g9_practice.py     重新生成九年级综合与实践 JSON
scripts/_build_junior_math.py        一次重新生成全部 12 张初中图
LICENSE                              MIT
```

## 模式怎么工作

四种对象，分开存，用 id 互相指：

| 对象 | 文件 | 关键字段 |
| --- | --- | --- |
| 知识点 | `knowledge-node.schema.json` | `id` `title` `subject` `stage`（小学 / 初中）`grade`（小学 1–6；初中 7–9）`strand`（数与代数 / 图形与几何 / 统计与概率 / 综合与实践）`difficulty`（1–5）`prerequisites` `tags` `unlock_rule` `mastery_criteria` `description` |
| 边 | `knowledge-edge.schema.json` | `from` `to` `type`：`prerequisite` / `related` / `easily_confused` / `application` |
| 任务 | `quest.schema.json` | 绑在一个节点上：`explain` / `practice` / `mini_quiz` / `boss` |
| 进度 | `player-progress.schema.json` | 每盏灯：`locked` / `available` / `learning` / `lit` / `needs_review`；还有 `xp_total`、`cleared_map_ids` |

约定：

- 给学生看的字用**中文**
- 程序 id 用英文短横线：小学数与运算如 `pm-g1-n001` … `pm-g6-n001`；图形与几何如 `pm-g1-geo-n001`；统计与概率如 `pm-g1-stat-n001`（关主如 `pm-g1-stat-boss-sort`）；综合与实践如 `pm-g1-prac-n001`。初中如 `jm-g7-alg-n001`、`jm-g7-geo-n001`、`jm-g7-stat-n001`、`jm-g7-prac-n001`（关主如 `jm-g7-alg-boss-rational`）
- `nodes.json` 里的 `prerequisites` 必须和「指向它的 prerequisite 边」一致
- 只有前置边参与解锁；它们必须构成**有向无环图（DAG）**

更细的字段说明：[schema/README.md](schema/README.md)。  
怎么点亮、怎么发经验：[docs/gameplay.md](docs/gameplay.md)。

## 怎么「玩」这些样例地图

现在没有画面，按数据走即可，和以后客户端规则相同。小学二十四张图、初中十二张图各自通关，**还没有**跨地图进度引擎（四大领域图也不互相前置；初中图不引用 `pm-*`）。

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

### 三年级 · 数与运算

1. 打开 [`maps/primary-math/grade-3-numbers/map.meta.json`](maps/primary-math/grade-3-numbers/map.meta.json)  
   - 地图名：**三年级 · 数与运算**  
   - 起点：`pm-g3-n001` 万以内数位与组成复习  
   - 通关：点亮全部节点，并打过三名关主（万以内加减、多位数乘除、地图通关试炼）
2. 演示存档里，起点已亮，`万以内加法（不进位）` 可学，`万以内减法（不退位）` 学到一半
3. 主线建议：万以内加减与估算 → 关主 1 → 倍的认识 → 多位数乘一位数 → 一位数除多位数（含余数）→ 关主 2 → 分数初步 → 关主 3  
   两位数乘两位数入门可与除法主线并行，在终章汇合  
   「认识一位小数」是**软锁支线**（人教版三年级下常见、课标系统学习多在四年级），不挡终章关主，但通关前仍要点亮

### 四年级 · 数与运算

1. 打开 [`maps/primary-math/grade-4-numbers/map.meta.json`](maps/primary-math/grade-4-numbers/map.meta.json)  
   - 地图名：**四年级 · 数与运算**  
   - 起点：`pm-g4-n001` 计数单位：从万到亿  
   - 通关：点亮全部节点，并打过三名关主（大数认识、乘除大闯关、地图通关试炼）
2. 演示存档里，起点已亮，`亿以内数的读法` 学到一半
3. 主线建议：大数读写改写与近似数 → 关主 1 → 三位数乘两位数 → 除数是两位数的除法（含调商）→ 关主 2 → 四则运算与运算律、简便运算 → 小数意义与加减 → 关主 3  
   除法口算可与乘法笔算并行，在「用整十数除」处汇合  
   「小数乘除入门」是**软锁支线**（人教版系统学习多在五年级），不挡终章关主，但通关前仍要点亮  
   三年级图的一位小数软锁支线与本图「小数的意义」在概念上衔接；本图从计数单位与小数意义重新讲起，**不**引用 `pm-g3-*` 节点

### 五年级 · 数与运算

1. 打开 [`maps/primary-math/grade-5-numbers/map.meta.json`](maps/primary-math/grade-5-numbers/map.meta.json)  
   - 地图名：**五年级 · 数与运算**  
   - 起点：`pm-g5-n001` 小数乘整数  
   - 通关：点亮全部节点，并打过三名关主（小数乘除、分数加减、地图通关试炼）
2. 演示存档里，起点已亮，`积的小数位数` 学到一半
3. 主线建议：小数乘除系统化（含积与商的近似值、循环小数、混合运算）→ 关主 1 → 因数倍数与质数合数 → 分数意义、约分通分 → 分数加减 → 关主 2 → 关主 3  
   运算律推广、积的近似值、乘法应用可与除法主线并行，在「小数乘除综合」处汇合  
   「简易方程」是**软锁支线**（人教版五年级上常见），不挡终章关主，但通关前仍要点亮  
   四年级图的小数乘除入门与本图「小数乘整数」在概念上衔接；本图从小数乘整数重新讲起，**不**引用 `pm-g4-*` 节点

### 六年级 · 数与运算

1. 打开 [`maps/primary-math/grade-6-numbers/map.meta.json`](maps/primary-math/grade-6-numbers/map.meta.json)  
   - 地图名：**六年级 · 数与运算**  
   - 起点：`pm-g6-n001` 分数乘法的意义  
   - 通关：点亮全部节点，并打过三名关主（分数乘除、比百分数比例、地图通关试炼）
2. 演示存档里，起点已亮，`分数乘整数` 学到一半
3. 主线建议：分数乘除 → 关主 1 → 比与按比分配、百分数（可并行）→ 比例与正反比例入门 → 关主 2 → 列方程巩固分数/百分数问题 → 关主 3  
   「认识负数」是**软锁支线**，不挡终章关主，但通关前仍要点亮  
   圆、圆柱圆锥等几何大块不在本图  
   五年级图的分数加减与简易方程与本图起点、方程巩固在概念上衔接；本图从分数乘法重新讲起，**不**引用 `pm-g5-*` 节点

### 一年级 · 图形与几何

1. 打开 [`maps/primary-math/grade-1-geometry/map.meta.json`](maps/primary-math/grade-1-geometry/map.meta.json)  
   - 地图名：**一年级 · 图形与几何**  
   - 起点：`pm-g1-geo-n001` 上和下  
   - 通关：点亮全部节点，并打过三名关主（位置小侦探、图形分拣员、地图通关试炼）
2. 主线建议：上下前后左右 → 关主 1 → 立体图形 → 平面图形 → 关主 2 → 拼组 → 关主 3  
   七巧板、对折看对称为**软锁支线**  
   与一年级数与运算图独立通关，不引用 `pm-g1-n*`

### 二年级 · 图形与几何

1. 打开 [`maps/primary-math/grade-2-geometry/map.meta.json`](maps/primary-math/grade-2-geometry/map.meta.json)  
   - 地图名：**二年级 · 图形与几何**  
   - 起点：`pm-g2-geo-n001` 比长短  
   - 通关：三名关主（长度测量员、角与观察小能手、地图通关试炼）
2. 主线建议：厘米米及分毫米千米 → 关主 1 → 角初步、长方形正方形边和角（可与观察物体并行）→ 轴对称欣赏 → 关主 2 → 关主 3  
   东南西北与路线图、平移欣赏为**软锁支线**  
   **不**引用 `pm-g1-geo-*`

### 三年级 · 图形与几何

1. 打开 [`maps/primary-math/grade-3-geometry/map.meta.json`](maps/primary-math/grade-3-geometry/map.meta.json)  
   - 地图名：**三年级 · 图形与几何**  
   - 起点：`pm-g3-geo-n001` 四边形有四条边  
   - 通关：三名关主（周长测绘员、面积铺贴员、地图通关试炼）
2. 主线建议：四边形家族 → 周长 → 关主 1 → 面积入门 → 关主 2 → 关主 3  
   平移旋转可与测量主线并行；观察物体为**软锁支线**  
   **不**引用 `pm-g2-geo-*`

### 四年级 · 图形与几何

1. 打开 [`maps/primary-math/grade-4-geometry/map.meta.json`](maps/primary-math/grade-4-geometry/map.meta.json)  
   - 地图名：**四年级 · 图形与几何**  
   - 起点：`pm-g4-geo-n001` 直线射线线段  
   - 通关：三名关主（角的度量师、三角形与四边形鉴定官、地图通关试炼）
2. 主线建议：角的度量与垂直平行 → 关主 1 → 平行四边形梯形与三角形（三角形可早早并行）→ 关主 2 → 面积公式扩展 → 关主 3  
   轴对称作图、旋转作图为**软锁支线**  
   **不**引用 `pm-g3-geo-*`

### 五年级 · 图形与几何

1. 打开 [`maps/primary-math/grade-5-geometry/map.meta.json`](maps/primary-math/grade-5-geometry/map.meta.json)  
   - 地图名：**五年级 · 图形与几何**  
   - 起点：`pm-g5-geo-n001` 面积从转化来  
   - 通关：三名关主（多边形面积工程师、圆的度量师、地图通关试炼）
2. 主线建议：多边形面积 → 关主 1；圆的认识可并行，在圆面积转化处汇合 → 关主 2 → 轴对称与旋转深入 → 关主 3  
   扇形初步、观察物体还原为**软锁支线**  
   圆放在本图（人教常见在六年级上）；长方体体积见六年级图  
   **不**引用 `pm-g4-geo-*`

### 六年级 · 图形与几何

1. 打开 [`maps/primary-math/grade-6-geometry/map.meta.json`](maps/primary-math/grade-6-geometry/map.meta.json)  
   - 地图名：**六年级 · 图形与几何**  
   - 起点：`pm-g6-geo-n001` 长方体的认识  
   - 通关：三名关主（长方体工匠、圆柱圆锥工匠、地图通关试炼）
2. 主线建议：长方体正方体展开图/表面积/体积 → 关主 1；圆柱圆锥可并行 → 关主 2；比例尺与放大缩小从起点并行 → 关主 3  
   路线图与方向为**软锁支线**  
   五年级圆与本图圆柱「底面是圆」仅概念衔接；本图从长方体重新讲起，**不**引用 `pm-g5-geo-*`

### 一年级 · 统计与概率

1. 打开 [`maps/primary-math/grade-1-statistics/map.meta.json`](maps/primary-math/grade-1-statistics/map.meta.json)  
   - 地图名：**一年级 · 统计与概率**  
   - 起点：`pm-g1-stat-n001` 东西有相同和不同  
   - 通关：三名关主（分类小能手、读图小侦探、地图通关试炼）
2. 主线建议：分类 → 关主 1 → 简单象形图/条形高低与统计表 → 关主 2 → 一定/可能/不可能 → 关主 3  
   「做一张我的象形图」为**软锁支线**  
   **不**引用数与运算或图形节点

### 二年级 · 统计与概率

1. 打开 [`maps/primary-math/grade-2-statistics/map.meta.json`](maps/primary-math/grade-2-statistics/map.meta.json)  
   - 地图名：**二年级 · 统计与概率**  
   - 起点：`pm-g2-stat-n001` 我们想知道什么  
   - 通关：三名关主（小调查员、图表翻译官、地图通关试炼）
2. 主线建议：收集整理填表 → 关主 1 → 象形图（含一图表示几个）与条形图（可并行）→ 关主 2 → 更可能/同样可能 → 关主 3  
   一周天气小记录、课间调查为**软锁支线**  
   **不**引用 `pm-g1-stat-*`

### 三年级 · 统计与概率

1. 打开 [`maps/primary-math/grade-3-statistics/map.meta.json`](maps/primary-math/grade-3-statistics/map.meta.json)  
   - 地图名：**三年级 · 统计与概率**  
   - 起点：`pm-g3-stat-n001` 先把问题问清楚  
   - 通关：三名关主（有目的的收集、复式表解读员、地图通关试炼）
2. 主线建议：单式表 → 关主 1 → 复式统计表 → 关主 2；条形图刻度与列出全部可能结果可并行 → 关主 3  
   两种标准交叉分类为**软锁支线**  
   **不**引用 `pm-g2-stat-*`

### 四年级 · 统计与概率

1. 打开 [`maps/primary-math/grade-4-statistics/map.meta.json`](maps/primary-math/grade-4-statistics/map.meta.json)  
   - 地图名：**四年级 · 统计与概率**  
   - 起点：`pm-g4-stat-n001` 读条形图复习  
   - 通关：三名关主（条形图测绘员、平均数调解员、地图通关试炼）
2. 主线建议：复式条形图与平均数可并行 → 关主 1 / 关主 2 → 可能性大小 → 关主 3  
   选择合适的单位格、人均不是每人为**软锁支线**  
   **不**引用 `pm-g3-stat-*`

### 五年级 · 统计与概率

1. 打开 [`maps/primary-math/grade-5-statistics/map.meta.json`](maps/primary-math/grade-5-statistics/map.meta.json)  
   - 地图名：**五年级 · 统计与概率**  
   - 起点：`pm-g5-stat-n001` 数据会随时间变  
   - 通关：三名关主（折线气象员、众数采购员、地图通关试炼）
2. 主线建议：折线统计图与众数可并行 → 关主 1 / 关主 2 → 简单随机试验与数据分析意识 → 关主 3  
   复式折线自画、截断纵轴、订购与众数为**软锁支线**  
   中位数见六年级图；**不**引用 `pm-g4-stat-*`

### 六年级 · 统计与概率

1. 打开 [`maps/primary-math/grade-6-statistics/map.meta.json`](maps/primary-math/grade-6-statistics/map.meta.json)  
   - 地图名：**六年级 · 统计与概率**  
   - 起点：`pm-g6-stat-n001` 部分占整体  
   - 通关：三名关主（扇形结构员、统计工具选配师、地图通关试炼）
2. 主线建议：扇形图与中位数可并行 → 选择统计量/统计图 → 关主 2；简单等可能概率可并行 → 关主 3  
   容易误导的图、自己做结构图、校园数据小报告为**软锁支线**  
   **不**引用 `pm-g5-stat-*`

### 一年级 · 综合与实践

1. 打开 [`maps/primary-math/grade-1-practice/map.meta.json`](maps/primary-math/grade-1-practice/map.meta.json)  
   - 地图名：**一年级 · 综合与实践**  
   - 起点：`pm-g1-prac-n001` 教室里的小麻烦  
   - 通关：两名关主（收纳小队长、地图通关试炼）
2. 主线建议：发现→计划→实施→交流走完收纳项目 → 关主 1；比高低与摆图案并行 → 关主 2  
   积木小故事为**软锁支线**  
   活动骨架原创，不抄教材课题原文

### 二年级 · 综合与实践

1. 打开 [`maps/primary-math/grade-2-practice/map.meta.json`](maps/primary-math/grade-2-practice/map.meta.json)  
   - 地图名：**二年级 · 综合与实践**  
   - 起点：`pm-g2-prac-n001` 发现：课桌有多长  
   - 通关：两名关主（测量小工匠、地图通关试炼）
2. 主线建议：量课桌与自制尺 → 关主 1；课间调查可并行 → 关主 2  
   公平转盘小制作为**软锁支线**  
   **不**引用 `pm-g1-prac-*`

### 三年级 · 综合与实践

1. 打开 [`maps/primary-math/grade-3-practice/map.meta.json`](maps/primary-math/grade-3-practice/map.meta.json)  
   - 地图名：**三年级 · 综合与实践**  
   - 起点：`pm-g3-prac-n001` 发现：东西不好对号  
   - 通关：两名关主（编码设计师、地图通关试炼）
2. 主线建议：储物位置编码 → 关主 1；搭配与步测可并行 → 关主 2  
   编码防错标记为**软锁支线**  
   **不**引用 `pm-g2-prac-*`

### 四年级 · 综合与实践

1. 打开 [`maps/primary-math/grade-4-practice/map.meta.json`](maps/primary-math/grade-4-practice/map.meta.json)  
   - 地图名：**四年级 · 综合与实践**  
   - 起点：`pm-g4-prac-n001` 发现：盘子装不下  
   - 通关：两名关主（约束搭配师、地图通关试炼）
2. 主线建议：午餐盘数量约束 → 关主 1；校园路线与值日表可并行 → 关主 2  
   时间冲突表为**软锁支线**  
   **不**引用 `pm-g3-prac-*`

### 五年级 · 综合与实践

1. 打开 [`maps/primary-math/grade-5-practice/map.meta.json`](maps/primary-math/grade-5-practice/map.meta.json)  
   - 地图名：**五年级 · 综合与实践**  
   - 起点：`pm-g5-prac-n001` 发现：花盆怎么摆才匀  
   - 通关：两名关主（间隔规划员、地图通关试炼）
2. 主线建议：间隔摆花模型 → 关主 1；通知传递与浪费调查可并行 → 关主 2  
   模型误差讨论为**软锁支线**  
   **不**引用 `pm-g4-prac-*`

### 六年级 · 综合与实践

1. 打开 [`maps/primary-math/grade-6-practice/map.meta.json`](maps/primary-math/grade-6-practice/map.meta.json)  
   - 地图名：**六年级 · 综合与实践**  
   - 起点：`pm-g6-prac-n001` 发现：多出来的一定挤在一起  
   - 通关：两名关主（抽屉发现者、地图通关试炼）
2. 主线建议：抽屉保证句 → 关主 1；校园综合课题与成果展可并行 → 关主 2  
   反例与边界、数据不可靠为**软锁支线**  
   **不**引用 `pm-g5-prac-*`

---

### 七年级 · 数与代数

1. 打开 [`maps/junior-math/grade-7-algebra/map.meta.json`](maps/junior-math/grade-7-algebra/map.meta.json)  
   - 地图名：**七年级 · 数与代数**　`stage`：初中　`grade`：7  
   - 起点：`jm-g7-alg-n001` 正数、负数和 0  
   - 通关：三名关主（有理数运算官、整式整理员、地图通关试炼）
2. 主线建议：有理数 → 关主 1 → 整式加减 → 关主 2 → 一元一次方程 → 不等式入门 → 关主 3  
   科学记数法、近似计算为**软锁支线**  
   **不**引用 `pm-*` 或其他 `jm-*`

### 七年级 · 图形与几何

1. 打开 [`maps/junior-math/grade-7-geometry/map.meta.json`](maps/junior-math/grade-7-geometry/map.meta.json)  
   - 地图名：**七年级 · 图形与几何**　起点：`jm-g7-geo-n001` 点、线、面、体  
   - 通关：三名关主（平行线调度员、三角形鉴定官、地图通关试炼）
2. 主线建议：几何语言 → 相交线平行线 → 关主 1；三角形可并行 → 关主 2；立体直观从起点并行  
   余角补角、作垂线等为**软锁支线**

### 七年级 · 统计与概率

1. 打开 [`maps/junior-math/grade-7-statistics/map.meta.json`](maps/junior-math/grade-7-statistics/map.meta.json)  
   - 地图名：**七年级 · 统计与概率**　起点：`jm-g7-stat-n001` 先把问题问清楚  
   - 通关：三名关主（图表翻译官、随机事件讲解员、地图通关试炼）
2. 主线建议：收集整理与频数 → 关主 1；三个统计量并行；简单随机事件 → 关主 2

### 七年级 · 综合与实践

1. 打开 [`maps/junior-math/grade-7-practice/map.meta.json`](maps/junior-math/grade-7-practice/map.meta.json)  
   - 地图名：**七年级 · 综合与实践**　起点：`jm-g7-prac-n001` 发现：账对不上  
   - 通关：两名关主（小账本审计员、地图通关试炼）
2. 主线建议：正负记账 → 关主 1；教室过道布置 → 关主 2。课题骨架原创，不抄教材长文

### 八年级 · 数与代数

1. 打开 [`maps/junior-math/grade-8-algebra/map.meta.json`](maps/junior-math/grade-8-algebra/map.meta.json)  
   - 地图名：**八年级 · 数与代数**　起点：`jm-g8-alg-n001` 二元一次方程  
   - 通关：三名关主（消元指挥官、因式分解工匠、地图通关试炼）
2. 主线建议：方程组 → 关主 1 → 整式乘除与因式分解 → 关主 2 → 分式；一次函数从方程组后并行  
   十字相乘、增根、反比例对照为**软锁支线**

### 八年级 · 图形与几何

1. 打开 [`maps/junior-math/grade-8-geometry/map.meta.json`](maps/junior-math/grade-8-geometry/map.meta.json)  
   - 地图名：**八年级 · 图形与几何**　起点：`jm-g8-geo-n001` 全等形的意义  
   - 通关：三名关主（全等判定官、勾股测量员、地图通关试炼）
2. 主线建议：全等 → 关主 1；轴对称并行；勾股 → 关主 2；平行四边形并行。SSA 不能判定为软锁警示

### 八年级 · 统计与概率

1. 打开 [`maps/junior-math/grade-8-statistics/map.meta.json`](maps/junior-math/grade-8-statistics/map.meta.json)  
   - 地图名：**八年级 · 统计与概率**　起点：`jm-g8-stat-n001` 平均数还不够  
   - 通关：三名关主（加权与波动分析员、概率绘图员、地图通关试炼）
2. 主线建议：加权平均与方差 → 关主 1；直方图并行；概率定义与列表树状图 → 关主 2

### 八年级 · 综合与实践

1. 打开 [`maps/junior-math/grade-8-practice/map.meta.json`](maps/junior-math/grade-8-practice/map.meta.json)  
   - 地图名：**八年级 · 综合与实践**　起点：`jm-g8-prac-n001` 发现：分组总被嫌不公  
   - 通关：两名关主（公平分组师、地图通关试炼）
2. 主线建议：公平分组建模 → 关主 1；轴对称最短取水路径 → 关主 2

### 九年级 · 数与代数

1. 打开 [`maps/junior-math/grade-9-algebra/map.meta.json`](maps/junior-math/grade-9-algebra/map.meta.json)  
   - 地图名：**九年级 · 数与代数**　起点：`jm-g9-alg-n001` 算术平方根  
   - 通关：三名关主（二次根式化简官、一元二次方程考官、地图通关试炼）
2. 主线建议：二次根式 → 关主 1 → 一元二次方程 → 关主 2 → 二次函数  
   锐角三角比在九年级**图形图**，本图不做

### 九年级 · 图形与几何

1. 打开 [`maps/junior-math/grade-9-geometry/map.meta.json`](maps/junior-math/grade-9-geometry/map.meta.json)  
   - 地图名：**九年级 · 图形与几何**　起点：`jm-g9-geo-n001` 比例线段  
   - 通关：三名关主（相似测绘员、解直角三角形向导、地图通关试炼）
2. 主线建议：相似 → 关主 1 → 锐角三角函数 → 关主 2；圆与投影视图可并行

### 九年级 · 统计与概率

1. 打开 [`maps/junior-math/grade-9-statistics/map.meta.json`](maps/junior-math/grade-9-statistics/map.meta.json)  
   - 地图名：**九年级 · 统计与概率**　起点：`jm-g9-stat-n001` 总体与样本  
   - 通关：三名关主（抽样估计员、古典概型绘图员、地图通关试炼）
2. 主线建议：抽样与用样本估计总体 → 关主 1 → 频率估计概率与古典概型深化 → 关主 2

### 九年级 · 综合与实践

1. 打开 [`maps/junior-math/grade-9-practice/map.meta.json`](maps/junior-math/grade-9-practice/map.meta.json)  
   - 地图名：**九年级 · 综合与实践**　起点：`jm-g9-prac-n001` 发现：全年级的口味说不清  
   - 通关：两名关主（偏好估计员、地图通关试炼）
2. 主线建议：用样本估计偏好 → 关主 1；无障碍坡道坡度 → 关主 2

打印推荐层（从起点沿前置边展开）：

```bash
python3 scripts/validate_map.py maps/primary-math/grade-1-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-2-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-3-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-4-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-5-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-6-numbers --tree
python3 scripts/validate_map.py maps/primary-math/grade-1-geometry --tree
python3 scripts/validate_map.py maps/primary-math/grade-2-geometry --tree
python3 scripts/validate_map.py maps/primary-math/grade-3-geometry --tree
python3 scripts/validate_map.py maps/primary-math/grade-4-geometry --tree
python3 scripts/validate_map.py maps/primary-math/grade-5-geometry --tree
python3 scripts/validate_map.py maps/primary-math/grade-6-geometry --tree
python3 scripts/validate_map.py maps/primary-math/grade-1-statistics --tree
python3 scripts/validate_map.py maps/primary-math/grade-2-statistics --tree
python3 scripts/validate_map.py maps/primary-math/grade-3-statistics --tree
python3 scripts/validate_map.py maps/primary-math/grade-4-statistics --tree
python3 scripts/validate_map.py maps/primary-math/grade-5-statistics --tree
python3 scripts/validate_map.py maps/primary-math/grade-6-statistics --tree
python3 scripts/validate_map.py maps/primary-math/grade-1-practice --tree
python3 scripts/validate_map.py maps/primary-math/grade-2-practice --tree
python3 scripts/validate_map.py maps/primary-math/grade-3-practice --tree
python3 scripts/validate_map.py maps/primary-math/grade-4-practice --tree
python3 scripts/validate_map.py maps/primary-math/grade-5-practice --tree
python3 scripts/validate_map.py maps/primary-math/grade-6-practice --tree
python3 scripts/validate_map.py maps/junior-math/grade-7-algebra --tree
python3 scripts/validate_map.py maps/junior-math/grade-7-geometry --tree
python3 scripts/validate_map.py maps/junior-math/grade-7-statistics --tree
python3 scripts/validate_map.py maps/junior-math/grade-7-practice --tree
python3 scripts/validate_map.py maps/junior-math/grade-8-algebra --tree
python3 scripts/validate_map.py maps/junior-math/grade-8-geometry --tree
python3 scripts/validate_map.py maps/junior-math/grade-8-statistics --tree
python3 scripts/validate_map.py maps/junior-math/grade-8-practice --tree
python3 scripts/validate_map.py maps/junior-math/grade-9-algebra --tree
python3 scripts/validate_map.py maps/junior-math/grade-9-geometry --tree
python3 scripts/validate_map.py maps/junior-math/grade-9-statistics --tree
python3 scripts/validate_map.py maps/junior-math/grade-9-practice --tree
```

## 校验命令

需要 Python 3.10+。图结构检查只用标准库。若要连 JSON Schema 一起验：

```bash
pip install -r scripts/requirements.txt
python3 scripts/validate_map.py maps/primary-math/grade-1-numbers
python3 scripts/validate_map.py maps/primary-math/grade-2-numbers
python3 scripts/validate_map.py maps/primary-math/grade-3-numbers
python3 scripts/validate_map.py maps/primary-math/grade-4-numbers
python3 scripts/validate_map.py maps/primary-math/grade-5-numbers
python3 scripts/validate_map.py maps/primary-math/grade-6-numbers
python3 scripts/validate_map.py maps/primary-math/grade-1-geometry
python3 scripts/validate_map.py maps/primary-math/grade-2-geometry
python3 scripts/validate_map.py maps/primary-math/grade-3-geometry
python3 scripts/validate_map.py maps/primary-math/grade-4-geometry
python3 scripts/validate_map.py maps/primary-math/grade-5-geometry
python3 scripts/validate_map.py maps/primary-math/grade-6-geometry
python3 scripts/validate_map.py maps/primary-math/grade-1-statistics
python3 scripts/validate_map.py maps/primary-math/grade-2-statistics
python3 scripts/validate_map.py maps/primary-math/grade-3-statistics
python3 scripts/validate_map.py maps/primary-math/grade-4-statistics
python3 scripts/validate_map.py maps/primary-math/grade-5-statistics
python3 scripts/validate_map.py maps/primary-math/grade-6-statistics
python3 scripts/validate_map.py maps/primary-math/grade-1-practice
python3 scripts/validate_map.py maps/primary-math/grade-2-practice
python3 scripts/validate_map.py maps/primary-math/grade-3-practice
python3 scripts/validate_map.py maps/primary-math/grade-4-practice
python3 scripts/validate_map.py maps/primary-math/grade-5-practice
python3 scripts/validate_map.py maps/primary-math/grade-6-practice
python3 scripts/validate_map.py maps/junior-math/grade-7-algebra
python3 scripts/validate_map.py maps/junior-math/grade-7-geometry
python3 scripts/validate_map.py maps/junior-math/grade-7-statistics
python3 scripts/validate_map.py maps/junior-math/grade-7-practice
python3 scripts/validate_map.py maps/junior-math/grade-8-algebra
python3 scripts/validate_map.py maps/junior-math/grade-8-geometry
python3 scripts/validate_map.py maps/junior-math/grade-8-statistics
python3 scripts/validate_map.py maps/junior-math/grade-8-practice
python3 scripts/validate_map.py maps/junior-math/grade-9-algebra
python3 scripts/validate_map.py maps/junior-math/grade-9-geometry
python3 scripts/validate_map.py maps/junior-math/grade-9-statistics
python3 scripts/validate_map.py maps/junior-math/grade-9-practice
python3 scripts/validate_map.py --all
```

退出码 0 表示通过。

重新生成样例 JSON（改对应 `_build_*.py` 之后）：

```bash
python3 scripts/_build_grade1_numbers.py
python3 scripts/_build_grade2_numbers.py
python3 scripts/_build_grade3_numbers.py
python3 scripts/_build_grade4_numbers.py
python3 scripts/_build_grade5_numbers.py
python3 scripts/_build_grade6_numbers.py
python3 scripts/_build_grade1_geometry.py
python3 scripts/_build_grade2_geometry.py
python3 scripts/_build_grade3_geometry.py
python3 scripts/_build_grade4_geometry.py
python3 scripts/_build_grade5_geometry.py
python3 scripts/_build_grade6_geometry.py
python3 scripts/_build_grade1_statistics.py
python3 scripts/_build_grade2_statistics.py
python3 scripts/_build_grade3_statistics.py
python3 scripts/_build_grade4_statistics.py
python3 scripts/_build_grade5_statistics.py
python3 scripts/_build_grade6_statistics.py
python3 scripts/_build_grade1_practice.py
python3 scripts/_build_grade2_practice.py
python3 scripts/_build_grade3_practice.py
python3 scripts/_build_grade4_practice.py
python3 scripts/_build_grade5_practice.py
python3 scripts/_build_grade6_practice.py
python3 scripts/_build_junior_math.py
python3 scripts/validate_map.py --all --tree
```

## 以后多学科

小学数学 1–6 年级领域标题已经列在 [maps/primary-math/OVERVIEW.md](maps/primary-math/OVERVIEW.md)，**小学数学四大领域地图线完成**（数与运算、图形与几何、统计与概率、综合与实践各 1–6，共 24 张可通关地图）。  
初中数学 7–9 年级领域标题列在 [maps/junior-math/OVERVIEW.md](maps/junior-math/OVERVIEW.md)，**初中数学四大领域地图线完成**（数与代数、图形与几何、统计与概率、综合与实践各 7–9，共 12 张可通关地图）。小学与初中 **schema 仍共用**。  
小学数与运算 / 图形 / 统计 / 实践各六张图概念上衔接，但节点 id 不跨图引用（详见小学 OVERVIEW）。  
初中数与代数 / 图形 / 统计 / 实践各三张图同样只在 OVERVIEW 里写概念衔接：**不要**在 `prerequisites` 里写 `pm-*` 或其他 `jm-*` 地图的节点。  
存档和校验都按图独立，跨地图进度以后再做。四大领域图之间**不要**互写节点前置。  
语文、英语将新增 `maps/<学科>/`，复用同一套 schema。英语单词知识图可以和语文语素、数学应用题用语用 `related` 边连起来（见 Skill 路线）。


## 已知缺口（下一步）

- 还没有图形界面，状态要靠读 JSON 想象
- 练习题只有提示语，没有自动出题器
- 小学数学四大领域 1–6、初中数学四大领域 7–9 已齐；高中数学以及其他学科地图尚未开始
- `strand` 枚举目前按数学四大领域；其他学科需要扩展字段

这些不挡 Phase 1–2b：模式、36 张样例 DAG、校验、许可证已经齐。下一阶段是游戏客户端或 Agent Skill，或高中数学 / 其他学科地图。
