---
neo4j:
  feature: "FEAT-DEX-C360-REALTIME"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "FEAT-DEX-C360-REALTIME实时数据-Feature说明文档"
  version: "v1.0"
  type: "Feature说明文档"
  productDomain: "PD-DEX"
  epicKey: "Epic:EPIC-DEX-CUSTOMER"
  featureKey: "FEAT-DEX-C360-REALTIME"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# FEAT-DEX-C360-REALTIME - 实时数据

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-DEX-C360-REALTIME |
| Feature 名称 | 实时数据 |
| 所属 EPIC | EPIC-DEX-CUSTOMER 客户中心 |
| 所属产品域 | PD-DEX 数据探索 |

## 2. 概述

客户实时行为数据监控和展示。

## 3. 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | 实时事件监控。**事件类型**：登录事件、浏览事件、点击事件、申请事件、查询事件 |
| FP-002 | 页面 | 事件列表展示。**字段**：事件类型、发生时间、事件内容、来源渠道，**交互**：开启/暂停监控、清空记录、导出数据 |

## 4. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | 事件类型正确区分5种类型 |
| 功能验收 | 实时监控延迟≤5秒 |
| 功能验收 | 开启/暂停监控即时生效 |
| 功能验收 | 导出数据为Excel格式 |

## 5. 依赖关系

| 依赖项 | 类型 | 说明 |
|:---|:---|:---|
| FEAT-DEX-C360-SEARCH | 上游 | 实时数据依赖客户查询结果 |
| PD-RISK | 上游 | 实时数据来源于风控系统 |

## 6. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - 实时数据*