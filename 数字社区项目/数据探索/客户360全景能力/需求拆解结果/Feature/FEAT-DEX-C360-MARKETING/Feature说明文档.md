---
neo4j:
  epic: "Epic:EPIC-DEX-CUSTOMER_360"
  feature: "FEAT-DEX-C360-MARKETING"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "营销记录 Feature说明文档"
  version: "v1.0"
  status: "backlog"
  productDomain: "PD-DEX"
  epicKey: "EPIC-DEX-CUSTOMER_360"
  author: "Tony Stark"
  createdAt: "2026-04-29"
  updatedAt: "2026-04-29"
---

# FEAT-DEX-C360-MARKETING - 营销记录

> **版本**: v1.0
> **日期**: 2026-04-29
> **作者**: Tony Stark
> **状态**: backlog

---

## 1. Feature 基本信息

| 字段 | 内容 |
|:---|:---|
| Feature ID | FEAT-DEX-C360-MARKETING |
| Feature URI | Feature:FEAT-DEX-C360-MARKETING |
| Feature 名称 | 营销记录 |
| 所属 Epic | EPIC-DEX-CUSTOMER_360 客户360全景能力 |
| 所属产品域 | PD-DEX 数据探索 |
| 负责人 | Tony Stark |
| Story数 | 3 |

---

## 2. Feature 概述

### 2.1 是什么
营销记录模块展示客户的营销触达历史、权益发放记录、营销效果分析。

### 2.2 解决什么问题
- 功能模块开发中，待补充具体痛点

### 2.3 用户场景

| 场景 | 用户 | 描述 |
|:---|:---|:---|
| 场景1 | 业务人员 | 查看客户触达记录（触达渠道、活动名称、触达结果）了解营销历史 |
| 场景2 | 业务人员 | 查看权益发放记录（积分、优惠券等），确认客户权益领取情况 |
| 场景3 | 管理人员 | 查看营销效果分析（转化率、ROI、客户终身价值）评估营销ROI |

---

## 3. 系统模块图（页面/组件结构）

```mermaid
flowchart TB
    subgraph 页面["营销记录"]
        P_MAIN["主页面"]
    end

    subgraph 组件["公共组件"]
        C_TABLE["Table表格"]
    end

    P_MAIN --> C_TABLE
```

### 3.1 页面说明

| 页面 | 路由 | 组件 | 说明 |
|:---|:---|:---|:---|
| 营销记录 | /discovery/customer360/detail | 营销记录Page | 主功能页 |

### 3.2 组件说明

| 组件 | 类型 | 说明 |
|:---|:---|:---|
| Table | 公共 | 通用表格组件 |

---

## 4. 功能说明

### 4.1 功能清单

| 功能点 | 类型 | 描述 |
|:---|:---|:---|
| FP-001 | 页面 | 触达记录 |
| FP-002 | 页面 | 权益发放记录 |
| FP-003 | 页面 | 营销效果分析 |


### 4.2 用户流程

```mermaid
flowchart LR
    A["用户进入"] --> B["查看列表"]
    B --> C["操作详情"]
    C --> D["完成"]
```

---

## 5. 验收标准

| 验收项 | 标准 |
|:---|:---|
| 功能验收 | 功能正常展示和操作 |
| 交互验收 | 交互符合预期 |
| 性能验收 | 页面加载2秒以内 |

---

## 6. 依赖关系

| 依赖项 | 类型 | 说明 |
|:---|:---|:---|
| 触达系统（REACH） | 数据依赖 | 触达记录（渠道、活动、结果）来自 EPIC-MKT-REACH |
| 权益中心（BENEFIT） | 数据依赖 | 权益发放记录（类型、名称、状态）来自 EPIC-MKT-BENEFIT |
| 营销分析平台 | 数据依赖 | 营销效果分析（ROI、转化率）来自营销数据分析模块 |

---

## 7. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-29 | v1.0 | 新建，基于功能清单同步 | Tony Stark |

---

🦈 *Feature 说明文档 v1.0 - 2026-04-29*
