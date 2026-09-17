# 高中数学地图总览

> 这里列 **普通高中数学课程标准（2017 年版 2020 年修订）必修 + 选择性必修核心** 的模块级路线，并链到已做成的可通关地图。  
> **小学数学四大领域 1–6 已完成**，见 [../primary-math/OVERVIEW.md](../primary-math/OVERVIEW.md)。  
> **初中数学四大领域 7–9 已完成**，见 [../junior-math/OVERVIEW.md](../junior-math/OVERVIEW.md)。  
> **高中数学核心模块已完成**（11 张可通关地图，按课标主题而不是假的高一/高二/高三文件夹）：
>
> **必修学段带（`grade: 10`）**  
> - [集合与常用逻辑用语](sets-logic/)（预备知识）  
> - [函数概念与基本初等函数](functions/)  
> - [三角函数与解三角形](trig/)  
> - [平面向量与复数](vectors-complex/)  
> - [立体几何初步](solid-geometry/)  
> - [概率与统计（必修）](probability-statistics/)  
>
> **选必学段带（`grade: 11`）**  
> - [数列](sequences/)  
> - [导数及其应用](derivatives/)  
> - [平面解析几何](analytic-geometry/)  
> - [计数原理与随机变量](counting-probability/)  
>
> **综合收束学段带（`grade: 12`）**  
> - [数学建模与综合实践](practice/)  

知识点来自课标**公开教学脉络**的原创大纲，**不是**某版教科书正文、练习册或高考原题整题转载。  
JSON 形状与小学、初中地图相同，共用 `schema/` 与 `scripts/validate_map.py`。  
`stage` 一律为 `高中`。schema 要求数字 `grade`，因此用 **10 / 11 / 12** 表示学段带；真实模块名写在地图标题和 `map.meta.json` 的 `module` 字段。  
`strand` 仍复用四大领域桶：数与代数 / 图形与几何 / 统计与概率 / 综合与实践。

图例：✅ 已有可通关地图

---

## 必修核心（约高一学段带）

| 模块 | 单元题目（占位） | 状态 |
| --- | --- | --- |
| 预备知识 | 集合；常用逻辑用语；相等关系与不等关系（含从函数观点看方程/不等式） | ✅ `sets-logic`（区间、德摩根律、三圈文氏图、反证法萌芽为软锁） |
| 函数 | 函数概念与性质；幂函数；指数函数；对数函数；函数应用 | ✅ `functions`（反函数直觉、二分法、平移伸缩、对数不等式为软锁） |
| 三角函数与解三角形 | 任意角与弧度；三角函数；图象与正弦型；和差/二倍角入门；正弦/余弦定理 | ✅ `trig`（扇形、辅助角、SSA 两解、诱导符号、最小正周期为软锁） |
| 几何与代数 | 平面向量；数量积；复数 | ✅ `vectors-complex`（单位向量、功、乘 i 旋转、零向量、中点证法为软锁） |
| 立体几何初步 | 几何体与三视图；点线面平行垂直；简单度量 | ✅ `solid-geometry`（异面棱、三垂线直觉、作图误差、球截面、割补、传递陷阱为软锁） |
| 概率与统计（必修） | 抽样与数字特征；相关与回归直觉；随机事件与古典概型 | ✅ `probability-statistics`（方便样本、回归非因果、组距、普查、互斥非对立、等可能检查为软锁） |

**解三角形放在哪里：** 课标把正弦定理、余弦定理写在「平面向量及其应用」里。本仓库为了让「三角函数与解三角形」一张图可独立通关，把解三角形并进 **trig** 图；向量图只做向量与复数，**不要**在 `prerequisites` 里写 `sm-trig-*` 或反过来写。

**数列、导数不在函数图：** 课标把数列、导数放在选必「函数」主题。本仓库单独成图 `sequences`、`derivatives`，函数图做到指数对数与简单应用为止。

## 选择性必修核心（约高二学段带）

| 模块 | 单元题目（占位） | 状态 |
| --- | --- | --- |
| 数列 | 数列概念；等差；等比；求和与增长模型 | ✅ `sequences`（裂项、错位入门、无穷等比、归纳萌芽、单利复利、混合结构、描点为软锁） |
| 导数及其应用 | 变化率；求导运算；切线；单调极值最值；优化入门 | ✅ `derivatives`（可导与连续、尖点、极值非最值、漏乘、实际定义域、割线切线、水平非极值为软锁） |
| 平面解析几何 | 直线；圆；椭圆、双曲线、抛物线入门 | ✅ `analytic-geometry`（渐近线、离心率、椭圆参数、坐标法证题、焦点弦为软锁） |
| 计数原理与随机变量 | 分类分步；排列组合；二项式入门；分布列；二项；期望；条件概率 | ✅ `counting-probability`（放回对照、独立非互斥、期望非众数、组合对称、正态直觉、混合陷阱为软锁） |

**空间向量不在立体几何初步图：** 必修立体几何用综合法；空间向量在选必，本批地图不做，以免把必修图撑成假的「高三立体」。

**条件概率不在必修概率图：** 必修停在古典概型与互斥加法；条件概率、离散型随机变量在 `counting-probability`。

## 数学建模活动（约高三收束带）

| 模块 | 原创课题骨架 | 状态 |
| --- | --- | --- |
| 数学建模活动与数学探究活动 | 流量套餐分段计费；讲座后排视线约束；综合成果卡 | ✅ `practice`（隐藏条款、测量误差、假设清单、白话讲解、二手数据为软锁） |

课题骨架原创，**不**抄教材课题长文，也**不**引用其他高中图节点。建模会用到函数分段、简单相似/正切，只在 OVERVIEW 里写概念衔接。

---

## 模块之间怎么衔接（先只写在这里）

### 预备知识 → 函数

集合与区间、逻辑用语、从函数观点看二次不等式，和函数图的定义域、零点在教学上是接着的。  
函数图从「对应关系」重新铺垫，**不要**在 `sm-func-*` 的 `prerequisites` 里写 `sm-set-*`。

### 函数 → 三角函数 / 数列 / 导数

函数的图象、单调、最值，和三角函数图象、数列（正整数上的函数）、导数（瞬时变化率）在教学上是接着的。  
各图从本模块起点重新讲起，**不要**互写节点前置。

### 向量 ↔ 解三角形 ↔ 立体几何 ↔ 解析几何

向量数量积与解三角形、线面角；解析几何用坐标重写直线圆；立体几何综合法与空间向量（本批不做）在概念上互助。  
**不要**在任一图的 `prerequisites` 里写另一张高中图的节点。

### 必修概率 → 选必计数与随机变量

古典概型、互斥加法，和排列组合、分布列、条件概率在教学上是接着的。  
选必图从分类计数重新铺垫，**不**把 `sm-stat-*` 写成前置。

### 与初中、小学地图（只写在这里）

初中二次函数、锐角三角比、勾股、抽样与古典概型，和高中函数、任意角三角函数、立体直观、概率统计在概念上衔接。  
**不要**在高中任一图的 `prerequisites` 里写 `pm-*` 或 `jm-*`。

**现在各张地图各自独立通关**：校验器只认本目录里的节点 id。跨地图进度以后再做。

以后若做多图进度，可以：

- 用 `cleared_map_ids` 记录「初中图或必修模块已通关」，再推荐打开下一张图
- 或加 `related` 边说明概念衔接（仍不要写跨图 `prerequisites`）

---

节点 id 前缀（稳定，请勿改）：

| 地图目录 | 地图 id | 节点前缀 | 关主前缀 |
| --- | --- | --- | --- |
| `sets-logic` | `sm-sets-logic` | `sm-set-n001` | `sm-set-boss-*` |
| `functions` | `sm-functions` | `sm-func-n001` | `sm-func-boss-*` |
| `trig` | `sm-trig` | `sm-trig-n001` | `sm-trig-boss-*` |
| `vectors-complex` | `sm-vectors-complex` | `sm-vec-n001` | `sm-vec-boss-*` |
| `solid-geometry` | `sm-solid-geometry` | `sm-solid-n001` | `sm-solid-boss-*` |
| `analytic-geometry` | `sm-analytic-geometry` | `sm-ag-n001` | `sm-ag-boss-*` |
| `probability-statistics` | `sm-probability-statistics` | `sm-stat-n001` | `sm-stat-boss-*` |
| `derivatives` | `sm-derivatives` | `sm-der-n001` | `sm-der-boss-*` |
| `counting-probability` | `sm-counting-probability` | `sm-count-n001` | `sm-count-boss-*` |
| `sequences` | `sm-sequences` | `sm-seq-n001` | `sm-seq-boss-*` |
| `practice` | `sm-practice` | `sm-prac-n001` | `sm-prac-boss-*` |

补新地图时：复制已有模块目录的四个 JSON，改 `map.meta.json` 的 `id` / `title` / `module` / `start_node_ids`，跑：

```bash
python3 scripts/validate_map.py maps/senior-math/<新目录>
```

已有地图（高中数学核心模块，共 11 张）：

```bash
python3 scripts/validate_map.py maps/senior-math/sets-logic
python3 scripts/validate_map.py maps/senior-math/functions
python3 scripts/validate_map.py maps/senior-math/trig
python3 scripts/validate_map.py maps/senior-math/vectors-complex
python3 scripts/validate_map.py maps/senior-math/solid-geometry
python3 scripts/validate_map.py maps/senior-math/analytic-geometry
python3 scripts/validate_map.py maps/senior-math/probability-statistics
python3 scripts/validate_map.py maps/senior-math/derivatives
python3 scripts/validate_map.py maps/senior-math/counting-probability
python3 scripts/validate_map.py maps/senior-math/sequences
python3 scripts/validate_map.py maps/senior-math/practice
python3 scripts/validate_map.py --all
```
