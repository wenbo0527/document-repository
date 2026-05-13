---
neo4j:
  feature: "FEAT-DEX-HOME"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "FEAT-DEX-HOME探索首页-Feature说明文档"
  version: "v1.0"
  type: "Feature说明文档"
  productDomain: "PD-DEX"
  epicKey: "Epic:EPIC-DEX-CUSTOMER"
  featureKey: "FEAT-DEX-HOME"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# FEAT-DEX-HOME - 探索首页

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-DEX-HOME |
| Feature 名称 | 探索首页 |
| 所属 EPIC | EPIC-DEX-CUSTOMER 客户中心 |
| 所属产品域 | PD-DEX 数据探索 |

## 2. 概述

### 2.1 是什么
数据探索模块的首页，提供模块导航和快速入口。

### 2.2 解决什么问题
- 缺乏统一的入口引导
- 难以快速访问常用功能

## 3. 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | 功能导航，展示功能模块快捷入口卡片。**卡片**：客户360、人群管理、事件中心、标签管理、分析流程、指标看板 |
| FP-002 | 页面 | 最近访问，展示最近查看的数据。**交互**：点击最近访问项跳转对应页面 |

## 4. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | 功能卡片正确展示6个入口 |
| 功能验收 | 点击卡片正确跳转对应页面 |
| 功能验收 | 最近访问正确展示历史记录 |
| 功能验收 | 点击最近访问项跳转正确页面 |
| 性能验收 | 页面加载时间≤2s |

## 5. 依赖关系

无。

## 6. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - 探索首页*