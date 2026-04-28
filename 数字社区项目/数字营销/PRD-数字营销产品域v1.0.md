# PRD-数字营销产品域v1.0

产品需求文档 (PRD)
数字营销产品域 (PD-MKT) - 完整版

**文档版本**: v1.0
**创建日期**: 2026-04-15
**作者**: Tony Stark
**状态**: 正式版

---

## 一、产品概述

### 1.1 产品定位
数字营销产品域（PD-MKT）为企业提供全渠道营销触达、客群管理和营销自动化能力。

### 1.2 核心价值

| 价值 | 说明 |
|:---|:---|
| 触达 | 多渠道统一触达（短信、推送、邮件、外呼） |
| 客群 | 精准人群圈选与分析 |
| 自动化 | 营销流程自动化编排 |
| 权益 | 优惠券/积分等权益管理 |

### 1.3 目标用户

- **运营人员**：创建营销活动、圈选人群、配置触达策略
- **分析师**：分析营销效果、优化策略
- **客服**：查看客户触达历史、进行人工电销

---

## 二、产品架构

PD-MKT 数字营销域包含：

| 模块 | 说明 |
|:---|:---|
| **客群中心（EPIC-MKT-CROWD）** | 人群管理、标签管理、事件管理 |
| **营销画布（EPIC-MKT-CANVAS）** | 可视化流程编排、人群圈选 |
| **触达系统（EPIC-MKT-REACH）** | 多渠道触达、频控、模板管理 |
| **权益中心（EPIC-MKT-BENEFIT）** | 优惠券、积分、券包管理 |
| **人工电销（EPIC-MKT-SALES）** | 电销工作台、话术管理 |

---

## 三、Epic 详细说明

### 3.1 EPIC-MKT-CROWD - 客群中心

| 属性 | 值 |
|:---|:---|
| Epic ID | EPIC-MKT-CROWD |
| 优先级 | P0 |
| Feature数 | 5 |
| FP数 | 20 |

**Feature 列表**：

| Feature ID | Feature名称 | 优先级 | FP数 |
|:---|:---|:---:|:---:|
| FEAT-MKT-CRD-SYS | 系统管理 | P0 | 3 |
| FEAT-MKT-CRD-LST | 人群列表 | P0 | 4 |
| FEAT-MKT-CRD-EVT | 事件管理 | P0 | 5 |
| FEAT-MKT-CRD-TAG | 标签管理 | P0 | 6 |
| FEAT-MKT-CRD-IDM | ID-mapping | P2 | 2 |

### 3.2 EPIC-MKT-CANVAS - 营销画布

| 属性 | 值 |
|:---|:---|
| Epic ID | EPIC-MKT-CANVAS |
| 优先级 | P0 |
| Feature数 | 4 |
| FP数 | 15 |

**Feature 列表**：

| Feature ID | Feature名称 | 优先级 | FP数 |
|:---|:---|:---:|:---:|
| FEAT-MKT-CANVAS-LIST | 画布列表 | P0 | 3 |
| FEAT-MKT-CANVAS-EDIT | 画布编辑 | P0 | 5 |
| FEAT-MKT-CANVAS-RUN | 画布执行 | P0 | 4 |
| FEAT-MKT-CANVAS-STAT | 画布统计 | P1 | 3 |

### 3.3 EPIC-MKT-REACH - 触达系统

| 属性 | 值 |
|:---|:---|
| Epic ID | EPIC-MKT-REACH |
| 优先级 | P0 |
| Feature数 | 5 |
| FP数 | 22 |

**Feature 列表**：

| Feature ID | Feature名称 | 优先级 | FP数 |
|:---|:---|:---:|:---:|
| FEAT-MKT-REACH-SMS | 短信渠道 | P0 | 8 |
| FEAT-MKT-REACH-PUSH | 推送渠道 | P0 | 5 |
| FEAT-MKT-REACH-EMAIL | 邮件渠道 | P1 | 4 |
| FEAT-MKT-REACH-FREQ | 频控管理 | P0 | 3 |
| FEAT-MKT-REACH-TEMPLATE | 模板管理 | P0 | 2 |

### 3.4 EPIC-MKT-BENEFIT - 权益中心

| 属性 | 值 |
|:---|:---|
| Epic ID | EPIC-MKT-BENEFIT |
| 优先级 | P1 |
| Feature数 | 6 |
| FP数 | 30 |

**Feature 列表**：

| Feature ID | Feature名称 | 优先级 | FP数 |
|:---|:---|:---:|:---:|
| FEAT-MKT-BEN-HOME | 权益首页 | P1 | 2 |
| FEAT-MKT-BEN-COUPON | 券模板管理 | P0 | 10 |
| FEAT-MKT-BEN-STOCK | 券库存管理 | P0 | 11 |
| FEAT-MKT-BEN-PACKAGE | 券包管理 | P0 | 8 |
| FEAT-MKT-BEN-STAT | 权益统计 | P1 | 5 |
| FEAT-MKT-BEN-APPROVAL | 审批管理 | P1 | 5 |

### 3.5 EPIC-MKT-SALES - 人工电销工作台

| 属性 | 值 |
|:---|:---|
| Epic ID | EPIC-MKT-SALES |
| 优先级 | P1 |
| Feature数 | 7 |
| FP数 | 30 |

**Feature 列表**：

| Feature ID | Feature名称 | 优先级 | FP数 |
|:---|:---|:---:|:---:|
| FEAT-MKT-SALES-WORKBENCH | 工作台主页 | P0 | 5 |
| FEAT-MKT-SALES-CALL | 外呼功能 | P0 | 6 |
| FEAT-MKT-SALES-SCRIPT | 话术管理 | P0 | 4 |
| FEAT-MKT-SALES-RECORD | 通话记录 | P1 | 5 |
| FEAT-MKT-SALES-REVIEW | 质检管理 | P1 | 4 |
| FEAT-MKT-SALES-STAT | 统计报表 | P1 | 3 |
| FEAT-MKT-SALES-AI | AI辅助 | P2 | 3 |

---

## 四、工作量汇总

### 4.1 Epic 维度汇总

| Epic ID | Epic名称 | 优先级 | Feature | FP |
|:---|:---|:---:|:---:|:---:|
| EPIC-MKT-CROWD | 客群中心 | P0 | 5 | 20 |
| EPIC-MKT-CANVAS | 营销画布 | P0 | 4 | 15 |
| EPIC-MKT-REACH | 触达系统 | P0 | 5 | 22 |
| EPIC-MKT-BENEFIT | 权益中心 | P1 | 6 | 30 |
| EPIC-MKT-SALES | 人工电销 | P1 | 7 | 30 |
| **合计** | | | **27** | **117** |

### 4.2 优先级维度汇总

| 优先级 | Epic | Feature | FP | 占比 |
|:---:|:---|:---:|:---:|:---:|
| P0 | 3个（客群+画布+触达） | 14个 | 57个 | 49% |
| P1 | 2个（权益+电销） | 13个 | 60个 | 51% |

---

## 五、交付里程碑

| 版本 | 时间 | 内容 |
|:---|:---|:---|
| MVP 版本 | 第1-2月 | 客群中心 + 触达系统核心功能 |
| 正式版第一期 | 第3-4月 | 营销画布 + 权益中心 |
| 正式版第二期 | 第5-6月 | 人工电销工作台 |

---

🦾 *PD-MKT 数字营销产品域 PRD 完成！*