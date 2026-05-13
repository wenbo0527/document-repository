---
neo4j:
  feature: "FEAT-RISK-EX-EVALUATION"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "FEAT-RISK-EX-EVALUATION外数评估中心-Feature说明文档"
  version: "v1.0"
  type: "Feature说明文档"
  productDomain: "PD-RISK"
  epicKey: "Epic:EPIC-RISK-EXTERNAL"
  featureKey: "FEAT-RISK-EX-EVALUATION"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# FEAT-RISK-EX-EVALUATION - 外数评估中心

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-RISK-EX-EVALUATION |
| Feature 名称 | 外数评估中心 |
| 所属 EPIC | EPIC-RISK-EXTERNAL 外数生命周期 |
| 所属产品域 | PD-RISK 数字风险 |

## 2. 概述

外部数据评估报告的管理页面，支持查看和筛选各类评估报告。

## 3. 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | 评估列表检索。**筛选器**：评估类型(质量/性能/性价比/综合)、状态(草稿灰/进行中橙/已完成绿/已归档灰) |
| FP-002 | 页面 | 查询/重置。**交互**：点击"查询/重置"按钮 |
| FP-003 | 页面 | 评估报告列表。**字段**：标题、类型(质量蓝/性能绿/性价比橙/综合紫)、状态、评分(无则显示"—")、创建时间 |
| FP-004 | 页面 | 评估详情。**交互**：点击查看评估报告详情 |
| FP-005 | 页面 | 列表分页。**交互**：支持分页导航 |

## 4. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | 评估类型正确区分4种类型 |
| 功能验收 | 状态正确区分草稿/进行中/已完成/已归档 |
| 功能验收 | 评分无数据显示"—" |
| 功能验收 | 列表支持分页 |

## 5. 依赖关系

| 依赖项 | 类型 | 说明 |
|:---|:---|:---|
| FEAT-RISK-EX-ARCHIVE | 上游 | 评估对象来源于档案 |

## 6. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - 外数评估中心*