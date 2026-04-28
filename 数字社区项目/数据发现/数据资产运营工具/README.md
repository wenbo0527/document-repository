# EPIC-DFD_ASSET_TOOL - 数据资产运营工具

> **版本**: v1.2
> **日期**: 2026-04-27
> **作者**: Tony Stark
> **状态**: 进行中
> **Epic ID**: EPIC-DFD_ASSET_TOOL
> **Epic 名称**: 数据资产运营工具

---

## 1. EPIC 基本信息

| 字段 | 内容 |
|:---|:---|
| Epic ID | EPIC-DFD_ASSET_TOOL |
| Epic 名称 | 数据资产运营工具 |
| 所属产品域 | PD-DFD 数据发现 |
| 优先级 | P0 |
| 状态 | 进行中 |

---

## 2. 菜单结构

| 功能 | 路由 | 说明 |
|:---|:---|:---|
| 全链路血缘 | /discovery/lineage | 表/字段级血缘追溯 |
| 影响分析 | /discovery/impact-analysis | 下游影响面评估 |

---

## 3. Feature 清单

| Feature ID | Feature 名称 | 优先级 | 状态 |
|:---|:---|:---:|:---:|
| FEAT-DFD-LINEAGE-ANALYSIS | 资产血缘分析 | P0 | 已上线 |
| FEAT-DFD-IMPACT-ANALYSIS | 变更影响分析 | P0 | 已上线 |

---

## 4. 目录结构

```
数据资产运营工具/
├── 业务需求入口/           # 原始业务需求文档
├── 产品PRD/               # 产品需求文档
├── 产品操作手册/           # 产品使用指南
├── 技术方案/              # 技术实现方案
├── 需求拆解结果/           # Epic/Feature/FP/Story 拆解结果
│   ├── Feature/
│   │   ├── FEAT-DFD-LINEAGE-ANALYSIS/
│   │   │   ├── FP/                    # 功能点目录
│   │   │   ├── 业务需求入口/           # Feature级业务需求
│   │   ├── FEAT-DFD-IMPACT-ANALYSIS/
│   │   │   ├── FP/
│   │   │   ├── 业务需求入口/
│   │   │   └── Feature说明文档.md
│   │       ├── FP/
│   │       ├── 业务需求入口/
│   │       └── Feature说明文档.md
│   └── Story/
├── README.md              # 本文件
└── EPIC说明文档.md         # EPIC 说明文档
```

---

## 5. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-27 | v1.0 | 初始化 | Tony Stark |
| 2026-04-27 | v1.1 | 基于实际 Feature 数量重建 README | Tony Stark |

---

🦈 *数据资产运营工具 v1.2*