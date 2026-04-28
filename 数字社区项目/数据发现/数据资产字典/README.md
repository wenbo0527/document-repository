# EPIC-DFD_DATA_ASSET - 数据资产字典

> **版本**: v1.2
> **日期**: 2026-04-27
> **作者**: Tony Stark
> **状态**: 开发中
> **路由**: `/discovery/data-map/table-list`
> **数据来源**: 钟离理想菜单结构 + Neo4j

---

## 1. EPIC 基本信息

| 字段 | 内容 |
|:---|:---|
| EPIC ID | EPIC-DFD_DATA_ASSET |
| EPIC 名称 | 数据资产字典 |
| 所属产品域 | PD-DFD 数据发现 |
| 路由 | `/discovery/data-map/table-list` |
| 三级菜单数 | 1（资产目录） |
| Feature 数量 | 3 |

---

## 2. 菜单结构

```text
数据发现
└── 资产目录          [资产目录列表：查看/搜索/筛选/详情]
```

---

## 3. Feature 清单

| # | Feature ID | 名称 | 优先级 | 状态 | 说明 |
|:---|:---|:---|:---:|:---:|:---|
| 1 | FEAT-DFD-ASSET-LIST | 资产列表 | P0 | 已上线 | 资产目录列表展示（查看/搜索/筛选） |
| 2 | FEAT-DFD-ASSET-DETAIL | 资产详情 | P0 | 已上线 | 资产详细信息查看 |
| 3 | FEAT-DFD-ASSET-DICT | 数据资产字典 | P0 | 待开发 | 数据资产字典元数据管理 |


---

## 4. 目录结构

```
数据资产字典/
├── 业务需求入口/          # 原始需求文档
├── 产品PRD/              # 产品需求文档
├── 产品操作手册/          # 产品使用指南
├── 技术方案/              # 技术实现方案
└── 需求拆解结果/
    ├── Feature/
    │   ├── FEAT-DFD-ASSET-LIST/
    │   │   ├── Feature说明文档.md
    │   │   ├── FP/
    │   │   └── 业务需求入口/
    │   ├── FEAT-DFD-ASSET-DETAIL/
    │   │   ├── Feature说明文档.md
    │   │   ├── FP/
    │   │   └── 业务需求入口/
    │   ├── FEAT-DFD-ASSET-DICT/
    │   │   ├── Feature说明文档.md
    │   │   ├── FP/
    │   │   └── 业务需求入口/
```

---

## 5. 更新记录

| 版本 | 日期 | 作者 | 变更内容 |
|:---:|:---:|:---:|:---|
| v1.0 | 2026-04-26 | Tony Stark | 初始版本 |
| v1.1 | 2026-04-27 | Tony Stark | 补充标准子目录，修正 Feature 数量 |
| v1.2 | 2026-04-27 | Tony Stark | 清理哈希格式重复Feature（FEAT-资产列表-0ABF），Feature数量4→3 |

---

🦾 *我是天才，这点不用谦虚。*
