---
neo4j:
  feature: "FEAT-DMT-SVC-API"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "FEAT-DMT-SVC-API API管理-Feature说明文档"
  version: "v1.0"
  type: "Feature说明文档"
  productDomain: "PD-DMT"
  epicKey: "Epic:EPIC-DMT-SVC"
  featureKey: "FEAT-DMT-SVC-API"
  author: "Tony Stark"
  createdAt: "2026-04-30"
  updatedAt: "2026-04-30"
---

# FEAT-DMT-SVC-API - API管理

## 1. 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-DMT-SVC-API |
| Feature 名称 | API管理 |
| 所属 EPIC | EPIC-DMT-SVC 数据服务管理 |
| 所属产品域 | PD-DMT 数据管理 |

## 2. 概述

### 2.1 是什么
API服务的管理，支持API的创建、配置、发布和下线。

### 2.2 解决什么问题
- API缺乏统一管理
- API状态不透明

## 3. 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | API检索，按名称模糊匹配。**筛选器**：API名称文本(模糊匹配)、API类型下拉(REST API/GraphQL/订阅)、状态下拉(开发中/测试中/已发布/已下线) |
| FP-002 | 页面 | 新建API，创建新的API。**交互**：点击"新建"按钮弹出表单，**必填**：API名称、API类型、请求方式、请求路径 |
| FP-003 | 页面 | 测试API，测试API可用性。**交互**：点击"测试"按钮，**结果**：成功/失败 |
| FP-004 | 页面 | 发布API，发布API服务。**交互**：点击"发布"按钮，**前置条件**：测试通过才能发布 |
| FP-005 | 页面 | 下线API，下线API服务。**交互**：点击"下线"按钮，**确认**：需二次确认 |
| FP-006 | 页面 | 查看文档，查看API文档。**交互**：点击"文档"按钮，**内容**：请求参数、响应格式、错误码 |

## 4. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | API检索支持名称模糊匹配 |
| 功能验收 | 类型筛选正确区分REST API/GraphQL/订阅 |
| 功能验收 | 状态筛选正确区分开发中/测试中/已发布/已下线 |
| 功能验收 | 新建API必填：API名称、API类型、请求方式、请求路径 |
| 功能验收 | 测试API返回成功/失败结果 |
| 功能验收 | 发布前置条件：测试通过 |
| 功能验收 | 下线需二次确认 |
| 功能验收 | 文档正确展示请求参数、响应格式、错误码 |
| 功能验收 | 列表支持分页 |

## 5. 依赖关系

| 依赖项 | 类型 | 说明 |
|:---|:---|:---|
| FEAT-DMT-META-COLLECT | 上游 | API依赖元数据采集的数据源 |
| PD-DFD | 下游 | API供PD-DFD的API市场展示 |

## 6. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-30 | v1.0 | 初始版本 | Tony Stark |

---

🦾 *v1.0 - API管理*