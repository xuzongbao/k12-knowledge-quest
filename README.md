# k12-knowledge-quest

中小学**知识图谱** + 轻量 RPG：**点亮知识点、打关升级**。

现在完成的是 **Phase 0–2（部分）**：把数据格式定下来，并做出十二张可校验、可通关的样例地图——小学一至六年级「数与运算」（一年级题为「数与运算入门」）和一至六年级「图形与几何」。**小学数与运算 1–6 线、图形与几何 1–6 线均已完成。**

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
| 2 | 补全小学数学其余领域地图（图形与几何、统计与概率、综合与实践；仍是大纲，不搬书） | 进行中：图形与几何 1–6 已完成；统计与概率、综合与实践仍占位 |
| 3 | 语文、英语等学科；英语可挂「单词知识图」 | 未开始 |
| 4 | 游戏客户端或 Agent Skill：读 JSON、改存档、出题 | 未开始 |

**Phase 1 只做小学数学。** 其它学科先在模式里留好 `subject` 枚举。

## 目录

```
schema/                              四种 JSON Schema + 短说明
maps/primary-math/OVERVIEW.md        小学数学 1–6 年级领域标题（路书）
maps/primary-math/grade-1-numbers/   一年级「数与运算」地图（四个 JSON + 演示存档）
maps/primary-math/grade-2-numbers/   二年级「数与运算」地图（同上）
maps/primary-math/grade-3-numbers/   三年级「数与运算」地图（同上）
maps/primary-math/grade-4-numbers/   四年级「数与运算」地图（同上）
maps/primary-math/grade-5-numbers/   五年级「数与运算」地图（同上）
maps/primary-math/grade-6-numbers/   六年级「数与运算」地图（同上）
maps/primary-math/grade-1-geometry/  一年级「图形与几何」地图（同上）
maps/primary-math/grade-2-geometry/  二年级「图形与几何」地图（同上）
maps/primary-math/grade-3-geometry/  三年级「图形与几何」地图（同上）
maps/primary-math/grade-4-geometry/  四年级「图形与几何」地图（同上）
maps/primary-math/grade-5-geometry/  五年级「图形与几何」地图（同上）
maps/primary-math/grade-6-geometry/  六年级「图形与几何」地图（同上）
docs/gameplay.md                     点亮、经验、关主、软锁/硬前置
docs/skill-roadmap.md                以后做成 Skill 的接口设想
scripts/validate_map.py              校验地图合法
scripts/_geo_common.py               图形地图生成共用函数
scripts/_build_grade1_numbers.py     重新生成一年级数与运算 JSON
scripts/_build_grade2_numbers.py     重新生成二年级数与运算 JSON
scripts/_build_grade3_numbers.py     重新生成三年级数与运算 JSON
scripts/_build_grade4_numbers.py     重新生成四年级数与运算 JSON
scripts/_build_grade5_numbers.py     重新生成五年级数与运算 JSON
scripts/_build_grade6_numbers.py     重新生成六年级数与运算 JSON
scripts/_build_grade1_geometry.py    重新生成一年级图形与几何 JSON
scripts/_build_grade2_geometry.py    重新生成二年级图形与几何 JSON
scripts/_build_grade3_geometry.py    重新生成三年级图形与几何 JSON
scripts/_build_grade4_geometry.py    重新生成四年级图形与几何 JSON
scripts/_build_grade5_geometry.py    重新生成五年级图形与几何 JSON
scripts/_build_grade6_geometry.py    重新生成六年级图形与几何 JSON
LICENSE                              MIT
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
- 程序 id 用英文短横线：数与运算如 `pm-g1-n001` … `pm-g6-n001`；图形与几何如 `pm-g1-geo-n001` … `pm-g6-geo-n001`（关主如 `pm-g1-geo-boss-position`）
- `nodes.json` 里的 `prerequisites` 必须和「指向它的 prerequisite 边」一致
- 只有前置边参与解锁；它们必须构成**有向无环图（DAG）**

更细的字段说明：[schema/README.md](schema/README.md)。  
怎么点亮、怎么发经验：[docs/gameplay.md](docs/gameplay.md)。

## 怎么「玩」这些样例地图

现在没有画面，按数据走即可，和以后客户端规则相同。十二张图各自通关，**还没有**跨地图进度引擎（数与运算图与图形图也不互相前置）。

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
python3 scripts/validate_map.py --all --tree
```

## 以后多学科

小学数学 1–6 年级领域标题已经列在 [maps/primary-math/OVERVIEW.md](maps/primary-math/OVERVIEW.md)，**小学数与运算 1–6 线**和**图形与几何 1–6 线**已做成可通关地图，其余领域（统计与概率、综合与实践）仍是**只占题目**。  
数与运算六张图概念上衔接（一年级 100 以内 → 二年级起点复习；二年级万以内读写与整百整千口算 → 三年级起点数位复习；三年级万以内数位与一位小数初步 → 四年级大数与小数意义；四年级小数加减与乘除入门 → 五年级小数乘除与分数；五年级分数加减与简易方程 → 六年级分数乘除与方程巩固）。  
图形与几何六张图概念上衔接（一年级立体平面 → 二年级边角与长度；二年级量长度 → 三年级周长面积；三年级面积入门 → 四年级面积公式扩展；四年级多边形面积 → 五年级组合面积与圆；五年级圆 → 六年级圆柱底面）。  
存档和校验都按图独立，跨地图进度以后再做。数与运算图与图形图之间**不要**互写节点前置。  
语文、英语将新增 `maps/<学科>/`，复用同一套 schema。英语单词知识图可以和语文语素、数学应用题用语用 `related` 边连起来（见 Skill 路线）。


## 已知缺口（下一步）

- 还没有图形界面，状态要靠读 JSON 想象
- 练习题只有提示语，没有自动出题器
- 统计与概率、综合与实践等其它领域地图尚未填写节点
- `strand` 枚举目前按数学四大领域；其他学科需要扩展字段

这些不挡 Phase 1：模式、样例 DAG、校验、许可证已经齐。
