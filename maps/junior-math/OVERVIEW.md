# 初中数学地图总览

> 这里列 **七年级–九年级 × 四大领域** 的题目级路线，并链到已做成的可通关地图。  
> **小学数学四大领域 1–6 已完成**，见 [../primary-math/OVERVIEW.md](../primary-math/OVERVIEW.md)。  
> **初中数学四大领域 7–9 已完成**（12 张可通关地图）：
>
> **数与代数 7–9**  
> - [七年级 · 数与代数](grade-7-algebra/)  
> - [八年级 · 数与代数](grade-8-algebra/)  
> - [九年级 · 数与代数](grade-9-algebra/)  
>
> **图形与几何 7–9**  
> - [七年级 · 图形与几何](grade-7-geometry/)  
> - [八年级 · 图形与几何](grade-8-geometry/)  
> - [九年级 · 图形与几何](grade-9-geometry/)  
>
> **统计与概率 7–9**  
> - [七年级 · 统计与概率](grade-7-statistics/)  
> - [八年级 · 统计与概率](grade-8-statistics/)  
> - [九年级 · 统计与概率](grade-9-statistics/)  
>
> **综合与实践 7–9**  
> - [七年级 · 综合与实践](grade-7-practice/)  
> - [八年级 · 综合与实践](grade-8-practice/)  
> - [九年级 · 综合与实践](grade-9-practice/)  

知识点来自义务教育数学课标第四学段（7–9 年级）的**公开教学脉络**，**不是**某版教科书正文或练习题的转载。  
JSON 形状与小学地图相同，共用 `schema/` 与 `scripts/validate_map.py`。

图例：✅ 已有可通关地图

---

## 七年级

| 领域 | 单元题目（占位） | 状态 |
| --- | --- | --- |
| 数与代数 | 有理数；整式加减；一元一次方程；不等式入门 | ✅ `grade-7-algebra`（科学记数法、近似计算为软锁） |
| 图形与几何 | 几何语言；相交线与平行线；三角形初步；生活中的立体图形 | ✅ `grade-7-geometry`（余角补角、作垂线、平移与平行、分类总表为软锁） |
| 统计与概率 | 数据收集整理深化；统计图；平均数众数中位数；频数；简单随机事件 | ✅ `grade-7-statistics`（问卷诱导、截轴、小报告为软锁） |
| 综合与实践 | 正负记账小账本；教室过道布置 | ✅ `grade-7-practice`（规则冲突、尺子不准为软锁） |

## 八年级

| 领域 | 单元题目（占位） | 状态 |
| --- | --- | --- |
| 数与代数 | 二元一次方程组；整式乘除与因式分解；分式；一次函数 | ✅ `grade-8-algebra`（十字相乘、分式方程增根、反比例对照为软锁） |
| 图形与几何 | 全等三角形；轴对称；勾股定理；平行四边形 | ✅ `grade-8-geometry`（SSA 不能判定、等腰隐藏条件、梯形中位线、网格勾股、对角线条件对照为软锁） |
| 统计与概率 | 加权平均；极差与方差入门；直方图；概率定义与列表树状图 | ✅ `grade-8-statistics`（权的误解、组距提醒、不等可能警示为软锁） |
| 综合与实践 | 公平分组；取水最短路径 | ✅ `grade-8-practice`（另类公平定义、弯曲河岸为软锁） |

## 九年级

| 领域 | 单元题目（占位） | 状态 |
| --- | --- | --- |
| 数与代数 | 二次根式（含实数入门）；一元二次方程；二次函数 | ✅ `grade-9-algebra`（韦达入门、判别式与开口对照、有意义条件、配方对照为软锁） |
| 图形与几何 | 相似；锐角三角函数；圆；投影与视图 | ✅ `grade-9-geometry`（面积比、互余、同弧警示、切线长为软锁） |
| 统计与概率 | 随机抽样；用样本估计总体；频率估计概率；古典概型深化 | ✅ `grade-9-statistics`（方便样本、越界结论、树状图漏枝、样本很散为软锁） |
| 综合与实践 | 用样本估计偏好；无障碍坡道坡度 | ✅ `grade-9-practice`（志愿者偏差、坡度限制来源为软锁） |

**锐角三角比放在哪里：** 课标里锐角三角函数既连着直角三角形（图形），也连着比（代数）。本仓库把锐角正弦、余弦、正切和解直角三角形放进**九年级图形图**，代数图专做二次根式、一元二次方程、二次函数。请不要在代数图 `prerequisites` 里写 `jm-g9-geo-*`。

**反比例函数放在哪里：** 人教版常见放在一次函数之后。八年级代数图把「反比例函数对照」做成**软锁支线**，主线仍是方程组、整式乘除与因式分解、分式、一次函数。

---

## 年级之间怎么衔接（先只写在这里）

### 数与代数线

七年级终章的有理数运算、整式加减、一元一次方程 / 不等式，和八年级起点「二元一次方程」在教学上是接着的（多一个未知数、多一个方程）。  
八年级的一次函数、因式分解、分式，和九年级起点「算术平方根」、后半段二次函数在教学上也是接着的（从一次关系到二次关系；分解可用于解一元二次方程）。  
各图从本年级起点重新铺垫，**不要**在较高年级节点的 `prerequisites` 里写较低年级的 `jm-g*-alg-*`。

### 图形与几何线

七年级的平行线、三角形初步、几何语言，和八年级全等、轴对称、平行四边形在教学上是接着的。  
八年级的勾股与直角三角形，和九年级解直角三角形、锐角三角比在教学上是接着的。  
九年级圆、相似、投影视图从本图比例线段 / 圆的概念重新讲起，**不**把八年级全等节点写成前置。

### 统计与概率线

七年级的频数、三个统计量、简单等可能分数，和八年级加权平均、方差、直方图、概率定义在教学上是接着的。  
八年级的概率与波动，和九年级抽样估计、频率估计概率、不放回树状图在教学上是接着的。  
九年级从「总体与样本」重新铺垫，**不**把八年级直方图节点写成前置。

### 综合与实践线

七年级的正负约定与平面约束，和八年级「把公平 / 最短写成可计算目标」在教学上是接着的。  
八年级的模型假设，和九年级抽样估计、坡度限制下的计算在教学上是接着的。  
各图课题骨架原创，**不**抄教材课题长文，也**不**引用其他实践图节点。

### 与小学地图、以及四大领域之间（只写在这里）

小学六年级的负数初步、扇形与简单概率、展开图，和七年级有理数、统计图深化、立体直观在概念上衔接。  
一次函数会用到平面直角坐标系意识；坡道会用到锐角三角比或坡度比；抽样会用到频数。这些是**概念上的互助**，不是解锁条件。

**不要**在初中任一图的 `prerequisites` 里写 `pm-*`（小学）或其他 `jm-*` 地图的节点。  
**不要**在统计图或实践图里写代数 / 图形节点前置，也不要反过来写。

**现在各张地图各自独立通关**：校验器只认本目录里的节点 id。跨地图进度以后再做。

以后若做多图进度，可以：

- 用 `cleared_map_ids` 记录「小学图或低年级图已通关」，再推荐打开下一张图
- 或加 `related` 边说明概念衔接（仍不要写跨图 `prerequisites`）

---

补新地图时：复制已有 `grade-*-algebra/` 等四个 JSON，改 `map.meta.json` 的 `id` / `title` / `start_node_ids`，跑：

```bash
python3 scripts/validate_map.py maps/junior-math/<新目录>
```

已有地图（初中数学四大领域 7–9 线，共 12 张）：

```bash
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
