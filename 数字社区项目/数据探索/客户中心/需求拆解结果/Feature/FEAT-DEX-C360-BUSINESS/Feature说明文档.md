---
neo4j:
  feature: "FEAT-DEX-C360-BUSINESS"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "FEAT-DEX-C360-BUSINESS业务核心详情-Feature说明文档"
  version: "v1.0"
  type: "Feature说明文档"
  productDomain: "PD-DEX"
  epicKey: "Epic:EPIC-DEX-CUSTOMER"
  featureKey: "FEAT-DEX-C360-BUSINESS"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# FEAT-DEX-C360-BUSINESS - 业务核心详情

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-DEX-C360-BUSINESS |
| Feature 名称 | 业务核心详情 |
| 所属 EPIC | EPIC-DEX-CUSTOMER 客户中心 |
| 所属产品域 | PD-DEX 数据探索 |

## 2. 概述

### 2.1 是什么
客户业务数据汇总展示区域。

### 2.2 解决什么问题
- 业务数据分散，难以统一查看
- 缺乏业务指标汇总

## 3. 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | 在贷信息展示。**字段**：在贷余额(万元)、历史贷款次数(次) |
| FP-002 | 页面 | 历史借款展示。**字段**：累计借款金额(万元)、累计还款金额(万元) |
| FP-003 | 页面 | 逾期情况展示。**字段**：正常还款期数、逾期期数、最高逾期金额(万元)、累计罚息(万元) |

## 4. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | 在贷余额正确展示当前在贷总金额(万元) |
| 功能验收 | 历史贷款次数正确展示(次) |
| 功能验收 | 累计借款/还款金额正确展示(万元) |
| 功能验收 | 逾期情况正确展示期数和金额 |
| 功能验收 | 数据刷新后正确更新 |

## 5. 依赖关系

| 依赖项 | 类型 | 说明 |
|:---|:---|:---|
| FEAT-DEX-C360-SEARCH | 上游 | 业务数据依赖客户查询结果 |

## 6. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - 业务核心详情*