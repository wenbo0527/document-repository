---
neo4j:
  epic: "EPIC-RISK-EXTERNAL"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "EPIC-RISK-EXTERNAL外数生命周期-Epic说明文档"
  version: "v1.0"
  type: "Epic说明文档"
  productDomain: "PD-RISK"
  epicKey: "EPIC-RISK-EXTERNAL"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# EPIC-RISK-EXTERNAL - 外数生命周期

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Epic ID | EPIC-RISK-EXTERNAL |
| Epic 名称 | 外数生命周期 |
| 所属产品域 | PD-RISK 数字风险 |

## 2. 概述

外数生命周期是外部数据产品的完整管理流程，覆盖从数据引入、技术档案完善、上线运营、评估分析到归档下线的完整生命周期。

## 3. Feature 清单

| Feature ID | Feature 名称 | FP数 |
|:---|:---|:---:|
| FEAT-RISK-EX-LIFECYCLE | 外数生命周期首页 | 8 |
| FEAT-RISK-EX-ARCHIVE | 外数档案管理 | 15 |
| FEAT-RISK-EX-EVALUATION | 外数评估中心 | 5 |
| FEAT-RISK-EX-SERVICE | 外数数据服务（含陪跑计划） | 18 |
| FEAT-RISK-EX-MONITOR | 外数监控中心 | 8 |
| FEAT-RISK-EX-SUPPLIER | 供应商管理 | 15 |
| FEAT-RISK-EX-PRICING | 供应商定价档案 | 10 |

## 4. 状态说明

| 状态值 | 显示文本 | 标签颜色 |
|:---|:---|:---|
| importing | 引入中 | warning |
| pending_tech_profile | 待完善技术档案 | warning |
| online | 已上线 | success |
| pending_evaluation | 待评估 | warning |
| archived | 已归档 | default |

## 5. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - 外数生命周期*