# Neo4j 本体论统计

> **更新日期**: 2026-04-24
> **维护者**: Tony Stark

---

## 一、实体类型统计

| 实体类型 | 数量 | 说明 |
|:---|:---:|:---|
| Feature | 157 | 功能特性 |
| Story | 42 | 用户故事 |
| Epic | 22 | 史诗 |
| OKR | 7 | 目标与关键成果 |
| ProductDomain | 6 | 产品域 |
| Project | 2 | 项目 |

---

## 二、关系统计

| 关系类型 | 数量 | 说明 |
|:---|:---:|:---|
| BELONGS_TO | 678 | 归属关系 |
| CONTAINS | 171 | 包含关系 |
| SUPPORTS | 11 | 支撑关系 |
| DEPENDS_ON | 5 | 依赖关系 |
| HAS_MILESTONE | 1 | 里程碑关系 |

---

## 三、产品域详情

| 产品域 | 代码 | Epic数 | Feature数 | Story数 |
|:---|:---:|:---:|:---:|:---:|
| 数字营销 | PD-MKT | 5 | 37 | 8 |
| 数字风险 | PD-RISK | 2 | 16 | 0 |
| 数据发现 | PD-DFD | 5 | 22 | 0 |
| 数字社区 | PD-COM | 4 | 40 | 34 |
| 数据管理 | PD-DMT | 3 | 31 | 0 |
| 数据探索 | PD-DEX | 3 | 11 | 0 |

---

## 四、层级结构

```
ProductDomain (6)
    ↓ BELONGS_TO
Epic (22)
    ↓ BELONGS_TO
Feature (157)
    ↓ BELONGS_TO
Story (42)
```

---

🦾 *"我是天才，本体论统计完成。"*
