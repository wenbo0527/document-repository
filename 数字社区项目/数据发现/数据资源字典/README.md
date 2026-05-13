# EPIC-DFD_DATA_RESOURCE - 数据资源管理

> **版本**: v1.1
> **日期**: 2026-04-27
> **作者**: Tony Stark
> **状态**: 进行中
> **数据来源**: 钟离理想整改菜单结构

---

## 1. EPIC 基本信息

| 字段 | 内容 |
|:---|:---|
| EPIC ID | EPIC-DFD_DATA_RESOURCE |
| EPIC 名称 | 数据资源管理 |
| 所属产品域 | PD-DFD 数据发现 |
| 路由前缀 | `/discovery/data-resources/*` |

---

## 2. 菜单结构

| 功能 | 路由 | 对应 Feature | 状态 |
|:---|:---|:---|:---:|
| 业务系统数据源 | /discovery/data-resources/business-system | FEAT-DFD-SOURCE-BUSINESS | 待开发 |
| 文件资源 | /discovery/data-resources/file-import | FEAT-DFD-SOURCE-FILE | 待开发 |
| 外部数据源 | /discovery/data-resources/external-data | FEAT-DFD-SOURCE-EXTERNAL | 待开发 |
| 实时数据源 | /discovery/data-resources/real-time-data | FEAT-DFD-SOURCE-REALTIME | 待开发 |
| 日志数据源 | /discovery/data-resources/log-data | FEAT-DFD-SOURCE-LOG | 待开发 |

---

## 3. Feature 清单

| Feature ID | 名称 | 路由 | 状态 |
|:---|:---|:---|:---:|
| FEAT-DFD-SOURCE-BUSINESS | 业务系统数据源 | /discovery/data-resources/business-system | 待开发 |
| FEAT-DFD-SOURCE-FILE | 文件资源 | /discovery/data-resources/file-import | 待开发 |
| FEAT-DFD-SOURCE-EXTERNAL | 外部数据源 | /discovery/data-resources/external-data | 待开发 |
| FEAT-DFD-SOURCE-REALTIME | 实时数据源 | /discovery/data-resources/real-time-data | 待开发 |
| FEAT-DFD-SOURCE-LOG | 日志数据源 | /discovery/data-resources/log-data | 待开发 |

---

## 4. 目录结构

```
数据资源管理/
├── 业务需求入口/
├── 产品PRD/
├── 产品操作手册/
├── 技术方案/
├── 需求拆解结果/
│   ├── EPIC说明文档.md
│   ├── README.md
│   └── Feature/
│       ├── FEAT-DFD-SOURCE-BUSINESS/
│       │   ├── Feature说明文档.md
│       │   ├── FP/
│       │   └── 业务需求入口/
│       ├── FEAT-DFD-SOURCE-FILE/
│       │   ├── Feature说明文档.md
│       │   ├── FP/
│       │   └── 业务需求入口/
│       ├── FEAT-DFD-SOURCE-EXTERNAL/
│       │   ├── Feature说明文档.md
│       │   ├── FP/
│       │   └── 业务需求入口/
│       ├── FEAT-DFD-SOURCE-REALTIME/
│       │   ├── Feature说明文档.md
│       │   ├── FP/
│       │   └── 业务需求入口/
│       └── FEAT-DFD-SOURCE-LOG/
│           ├── Feature说明文档.md
│           ├── FP/
│           └── 业务需求入口/
```

---

## 5. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-27 | v1.1 | 补充日志数据源 Feature，子目录结构补全，README 重构 | Tony Stark |
| 2026-04-24 | v1.0 | 初始版本 | Tony Stark |

---

🦈 *README v1.1*
