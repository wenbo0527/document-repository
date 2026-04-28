# EPIC-DFD_UNIFIED_SEARCH - 统一搜索

> **版本**: v1.1
> **日期**: 2026-04-27
> **作者**: Tony Stark
> **状态**: 已上线
> **路由**: `/discovery/data-map`（数据地图）

---

## 1. EPIC 基本信息

| 字段 | 内容 |
|:---|:---|
| EPIC ID | EPIC-DFD_UNIFIED_SEARCH |
| EPIC 名称 | 统一搜索 |
| 所属产品域 | PD-DFD 数据发现 |
| 路由 | `/discovery/data-map`（数据地图） |
| 上线日期 | 已上线 |

---

## 2. 菜单结构（钟离理想菜单）

### 数据地图

| 功能 | 操作 |
|:---|:---|
| 数据地图 | 查看 / 搜索 / 筛选 |

---

## 3. Feature 清单

| Feature ID | 名称 | 状态 | 说明 |
|:---|:---|:---:|:---|
| FEAT-DFD-SEARCH-QUERY | 全局搜索 | active | 支持跨库关键词搜索 |
| FEAT-DFD-SEARCH-HISTORY | 搜索历史 | active | 记录用户搜索行为 |
| FEAT-DFD-SEARCH-NAVIGATION | 搜索导航页 | active | 搜索入口与分类导航 |
| FEAT-DFD-SEARCH-RESULT | 搜索结果展示 | active | 结果列表与详情展示 |

---

## 4. 目录结构

```
统一搜索/
├── 业务需求入口/
├── 产品PRD/
├── 产品操作手册/
├── 技术方案/
└── 需求拆解结果/
    ├── EPIC说明文档.md
    └── Feature/
        ├── FEAT-DFD-SEARCH-QUERY/
        │   ├── FP/
        │   └── 业务需求入口/
        ├── FEAT-DFD-SEARCH-HISTORY/
        │   ├── FP/
        │   └── 业务需求入口/
        ├── FEAT-DFD-SEARCH-NAVIGATION/
        │   ├── FP/
        │   └── 业务需求入口/
        └── FEAT-DFD-SEARCH-RESULT/
            ├── FP/
            └── 业务需求入口/
```

---

## 5. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-24 | v2.0 | 基于 Neo4j 交叉核验后重建 | Tony Stark |
| 2026-04-27 | v1.1 | 补充完整 README，标准化 Feature 子目录 | Tony Stark |

---

🦾 *统一搜索 EPIC README v1.1*
