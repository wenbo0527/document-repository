---
neo4j:
  feature: "FEAT-DMT-SVC-STATS"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "FEAT-DMT-SVC-STATS调用统计-Feature说明文档"
  version: "v1.0"
  type: "Feature说明文档"
  productDomain: "PD-DMT"
  epicKey: "Epic:EPIC-DMT-SVC"
  featureKey: "FEAT-DMT-SVC-STATS"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# FEAT-DMT-SVC-STATS - 调用统计

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-DMT-SVC-STATS |
| Feature 名称 | 调用统计 |
| 所属 EPIC | EPIC-DMT-SVC 数据服务管理 |
| 所属产品域 | PD-DMT 数据管理 |

## 2. 概述

### 2.1 是什么
数据服务调用统计分析，支持查看调用报表。

### 2.2 解决什么问题
- 调用数据难以分析
- 缺乏统计报表

## 3. 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | 调用报表，展示调用统计数据。**指标**：总调用量、成功调用量、失败调用量、平均响应时间 |
| FP-002 | 页面 | 时间筛选，按时间范围筛选。**筛选器**：时间范围选择(今天/近7天/近30天/自定义) |
| FP-003 | 页面 | 导出报表，导出调用统计报表。**交互**：点击"导出"按钮，**格式**：Excel |

## 4. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | 调用报表正确展示总调用量、成功量、失败量、平均响应时间 |
| 功能验收 | 时间筛选支持今天/近7天/近30天/自定义 |
| 功能验收 | 导出报表为Excel格式 |
| 性能验收 | 报表加载时间≤5s |

## 5. 依赖关系

| 依赖项 | 类型 | 说明 |
|:---|:---|:---|
| FEAT-DMT-SVC-MONITOR | 上游 | 统计依赖监控数据 |

## 6. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - 调用统计*