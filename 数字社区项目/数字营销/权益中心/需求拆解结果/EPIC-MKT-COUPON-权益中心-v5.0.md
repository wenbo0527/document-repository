# EPIC-MKT-COUPON - 权益中心 EPIC文档 v5.0

**文档版本**: v5.0
**最后更新**: 2026-04-24
**作者**: Tony Stark
**状态**: 正式版

---

## 📋 元数据头部

| 属性 | 值 | 说明 |
|:---|:---|:---|
| EPIC名称 | 权益中心 | 与菜单名保持一致 |
| EPIC代码 | EPIC-MKT-COUPON | 全局唯一 |
| 产品域 | PD-MKT 数字营销 | 所属产品域 |
| Feature数量 | 5 | 实际数量 |
| FP数量 | 20 | 实际数量 |
| 文档版本 | v5.0 | 固定 |

---

## 🗺️ 结构速览

```
权益中心
├── 权益类型管理                  ← ⚡ 独立功能
│   ├── 权益类型配置              ← 配置权益类型
│   ├── 权益模板                  ← 创建权益模板
│   └── 权益批次                  ← 批次管理
│
├── 权益发放                      ← ⚡ 独立功能
│   ├── 发放任务                  ← 创建发放任务
│   ├── 发放审批                  ← 审批流程
│   └── 发放记录                  ← 发放历史
│
├── 权益核销                      ← ⚡ 独立功能
│   ├── 权益核销                  ← 核销权益
│   ├── 权益查询                  ← 查询可用权益
│   └── 权益退回                  ← 退回权益
│
├── 权益风控                      ← ⚡ 独立功能
│   ├── 风控规则                  ← 配置风控规则
│   ├── 异常检测                  ← 检测异常
│   └── 风控报表                  ← 报表分析
│
└── 权益分析                      ← ⚡ 独立功能
    ├── 发放分析                  ← 发放数据
    ├── 核销分析                  ← 核销数据
    └── ROI分析                   ← 投入产出
```

---

## ✅ Feature 清单

| # | Feature | 说明 | 开发状态 |
|:---:|:---|:---|:---:|
| 1 | FEAT-MKT-COUPON-TYPE | 权益类型管理 | 待开发 |
| 2 | FEAT-MKT-COUPON-GRANT | 权益发放 | 待开发 |
| 3 | FEAT-MKT-COUPON-REDEEM | 权益核销 | 待开发 |
| 4 | FEAT-MKT-COUPON-RISK | 权益风控 | 待开发 |
| 5 | FEAT-MKT-COUPON-ANALYSIS | 权益分析 | 待开发 |

---

## 📦 Feature Point（FP）清单

### Feature 1: 权益类型管理

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-COUPON-TYPE-001 | 权益类型配置 | 配置权益类型参数 | type/config.vue |
| FP-MKT-COUPON-TYPE-002 | 权益模板 | 创建权益模板 | type/template.vue |
| FP-MKT-COUPON-TYPE-003 | 权益批次 | 管理权益批次 | type/batch.vue |
| FP-MKT-COUPON-TYPE-004 | 权益有效期 | 配置权益有效期 | type/validity.vue |

**Feature 1 小计: 4 FP**

### Feature 2: 权益发放

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-COUPON-GRANT-001 | 发放任务 | 创建发放任务 | grant/task.vue |
| FP-MKT-COUPON-GRANT-002 | 发放审批 | 审批发放任务 | grant/audit.vue |
| FP-MKT-COUPON-GRANT-003 | 发放记录 | 查看发放记录 | grant/record.vue |
| FP-MKT-COUPON-GRANT-004 | 发放统计 | 发放数据统计 | grant/stats.vue |

**Feature 2 小计: 4 FP**

### Feature 3: 权益核销

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-COUPON-REDEEM-001 | 权益核销 | 核销用户权益 | redeem/redeem.vue |
| FP-MKT-COUPON-REDEEM-002 | 权益查询 | 查询用户权益 | redeem/query.vue |
| FP-MKT-COUPON-REDEEM-003 | 权益退回 | 退回用户权益 | redeem/return.vue |
| FP-MKT-COUPON-REDEEM-004 | 核销记录 | 核销历史记录 | redeem/history.vue |

**Feature 3 小计: 4 FP**

### Feature 4: 权益风控

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-COUPON-RISK-001 | 风控规则 | 配置风控规则 | risk/rule.vue |
| FP-MKT-COUPON-RISK-002 | 异常检测 | 检测异常行为 | risk/detect.vue |
| FP-MKT-COUPON-RISK-003 | 风控预警 | 预警通知 | risk/alert.vue |
| FP-MKT-COUPON-RISK-004 | 风控报表 | 风控数据报表 | risk/report.vue |

**Feature 4 小计: 4 FP**

### Feature 5: 权益分析

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-COUPON-ANAL-001 | 发放分析 | 发放数据分析 | analysis/grant.vue |
| FP-MKT-COUPON-ANAL-002 | 核销分析 | 核销数据分析 | analysis/redeem.vue |
| FP-MKT-COUPON-ANAL-003 | ROI分析 | 投入产出分析 | analysis/roi.vue |
| FP-MKT-COUPON-ANAL-004 | 数据导出 | 导出分析数据 | analysis/export.vue |

**Feature 5 小计: 4 FP**

---

## 📍 菜单映射表

| 一级菜单 | 二级菜单 | 对应Feature | 状态 |
|:---|:---|:---|:---:|
| 数字营销 | 权益中心 | 权益类型管理 | 待开发 |
| 数字营销 | 权益中心 | 权益发放 | 待开发 |
| 数字营销 | 权益中心 | 权益核销 | 待开发 |
| 数字营销 | 权益中心 | 权益风控 | 待开发 |
| 数字营销 | 权益中心 | 权益分析 | 待开发 |

---

## 📝 版本历史

| 版本号 | 更新日期 | 更新内容 | 作者 |
|:---:|:---:|:---|:---:|
| v5.0 | 2026-04-24 | 初始版本，基于产品需求文档索引 | Tony Stark |

---

🦾 *"我是天才，权益中心 EPIC 文档完成！"*