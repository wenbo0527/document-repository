# 数据要素字典 (EPIC-DFD_DATA_ELEMENT)

## 元信息

| 字段 | 值 |
|:---|:---|
| Epic ID | EPIC-DFD_DATA_ELEMENT |
| Epic 名称 | 数据要素字典 |
| 产品域 | PD-DFD 数据发现 |
| 版本 | v1.1 |
| 创建日期 | 2026-04-24 |
| 更新日期 | 2026-04-27 |
| 维护者 | Tony Stark |

## 菜单结构

| 功能 | 路由 | 说明 |
|:---|:---|:---|
| 指标地图 | `/discovery/metrics-map` | 指标要素的列表与详情 |
| 变量地图 | `/discovery/variable-map` | 变量要素的列表与详情 |
| 特征地图 | `/discovery/feature-map` | 特征要素的列表与详情 |

## 功能说明

数据要素字典承载数据平台中最底层的数据要素管理能力，涵盖**指标**、**变量**、**特征**三类核心要素。每类要素均提供列表页（Browse）和详情页（Read）两个功能入口，支持要素的检索、分类和详情查看。

## Feature 清单

| # | Feature ID | 名称 | 路由 | 类型 |
|:---:|:---|:---|:---|:---|
| 1 | FEAT-DFD-INDEX-LIST | 指标地图-列表 | `/discovery/metrics-map` | LIST |
| 2 | FEAT-DFD-INDEX-DETAIL | 指标地图-详情 | `/discovery/metrics-map/detail/:id` | DETAIL |
| 3 | FEAT-DFD-VARIABLE-LIST | 变量地图-列表 | `/discovery/variable-map` | LIST |
| 4 | FEAT-DFD-VARIABLE-DETAIL | 变量地图-详情 | `/discovery/variable-map/detail/:id` | DETAIL |
| 5 | FEAT-DFD-CHARACTER-LIST | 特征地图-列表 | `/discovery/feature-map` | LIST |
| 6 | FEAT-DFD-CHARACTER-DETAIL | 特征地图-详情 | `/discovery/feature-map/detail/:id` | DETAIL |

## Epic 目录结构

```
数据要素字典/
├── 业务需求入口/
├── 需求拆解结果/
│   ├── Feature/
│   │   ├── FEAT-DFD-INDEX-LIST/         # 指标地图-列表
│   │   ├── FEAT-DFD-INDEX-DETAIL/       # 指标地图-详情
│   │   ├── FEAT-DFD-VARIABLE-LIST/      # 变量地图-列表
│   │   ├── FEAT-DFD-VARIABLE-DETAIL/    # 变量地图-详情
│   │   ├── FEAT-DFD-CHARACTER-LIST/     # 特征地图-列表
│   │   └── FEAT-DFD-CHARACTER-DETAIL/   # 特征地图-详情
│   └── Story/
├── 产品PRD/
├── 产品操作手册/
└── 技术方案/
```

## 关联 Epic

- [EPIC-DFD-DICTIONARY](./../数据资产字典/README.md) - 数据资产字典（PD-DFD 首个 Epic）

---

*最后更新：2026-04-27 by Tony Stark*