# EPIC-MKT-CANVAS - 营销画布 EPIC文档 v5.0

**文档版本**: v5.0
**最后更新**: 2026-04-24
**作者**: Tony Stark
**状态**: 正式版

---

## 📋 元数据头部

| 属性 | 值 | 说明 |
|:---|:---|:---|
| EPIC名称 | 营销画布 | 与菜单名保持一致 |
| EPIC代码 | EPIC-MKT-CANVAS | 全局唯一 |
| 产品域 | PD-MKT 数字营销 | 所属产品域 |
| Feature数量 | 5 | 实际数量 |
| FP数量 | 20 | 实际数量 |
| 文档版本 | v5.0 | 固定 |

---

## 🗺️ 结构速览

```
营销画布
├── 画布编辑器                    ← ⚡ 独立功能
│   ├── 画布配置                  ← 创建/编辑/版本
│   ├── 节点拖拽                  ← 拖拽添加节点
│   └── 画布预览                  ← 配置效果预览
│
├── 节点管理                      ← ⚡ 独立功能
│   ├── 节点库                    ← 标准节点管理
│   ├── 节点配置                  ← 参数配置
│   └── 节点复制                  ← 跨画布复制
│
├── 触发条件                      ← ⚡ 独立功能
│   ├── 触发类型                  ← 事件/时间/API
│   └── 触发规则                  ← 规则管理
│
├── 流程控制                      ← ⚡ 独立功能
│   ├── 条件分支                  ← 多条件分支
│   ├── 循环控制                  ← 循环执行
│   └── 等待节点                  ← 等待间隔
│
└── 数据分析                      ← ⚡ 独立功能
    ├── 营销漏斗                  ← 漏斗分析
    ├── 节点效果                  ← 转化分析
    └── 实时监控                  ← 状态监控
```

---

## ✅ Feature 清单

| # | Feature | 说明 | 开发状态 |
|:---:|:---|:---|:---:|
| 1 | FEAT-MKT-CANVAS-EDITOR | 画布编辑器 | 待开发 |
| 2 | FEAT-MKT-CANVAS-NODE | 节点管理 | 待开发 |
| 3 | FEAT-MKT-CANVAS-TRIGGER | 触发条件 | 待开发 |
| 4 | FEAT-MKT-CANVAS-FLOW | 流程控制 | 待开发 |
| 5 | FEAT-MKT-CANVAS-ANALYSIS | 数据分析 | 待开发 |

---

## 📦 Feature Point（FP）清单

### Feature 1: 画布编辑器

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CANVAS-EDIT-001 | 画布创建 | 创建新的营销画布 | canvas/create.vue |
| FP-MKT-CANVAS-EDIT-002 | 画布编辑 | 编辑已有画布内容 | canvas/edit.vue |
| FP-MKT-CANVAS-EDIT-003 | 节点拖拽 | 拖拽节点到画布 | canvas/drag.vue |
| FP-MKT-CANVAS-EDIT-004 | 画布预览 | 预览画布配置效果 | canvas/preview.vue |

**Feature 1 小计: 4 FP**

### Feature 2: 节点管理

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CANVAS-NODE-001 | 节点库 | 标准节点库管理 | node/library.vue |
| FP-MKT-CANVAS-NODE-002 | 节点配置 | 配置节点参数 | node/config.vue |
| FP-MKT-CANVAS-NODE-003 | 节点复制 | 复制已有节点 | node/copy.vue |
| FP-MKT-CANVAS-NODE-004 | 节点搜索 | 搜索节点 | node/search.vue |

**Feature 2 小计: 4 FP**

### Feature 3: 触发条件

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CANVAS-TRIG-001 | 触发类型 | 配置触发类型 | trigger/type.vue |
| FP-MKT-CANVAS-TRIG-002 | 事件触发 | 配置事件触发条件 | trigger/event.vue |
| FP-MKT-CANVAS-TRIG-003 | 时间触发 | 配置时间触发条件 | trigger/time.vue |
| FP-MKT-CANVAS-TRIG-004 | API触发 | 配置API触发条件 | trigger/api.vue |

**Feature 3 小计: 4 FP**

### Feature 4: 流程控制

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CANVAS-FLOW-001 | 条件分支 | 配置条件分支逻辑 | flow/condition.vue |
| FP-MKT-CANVAS-FLOW-002 | 循环控制 | 配置循环执行逻辑 | flow/loop.vue |
| FP-MKT-CANVAS-FLOW-003 | 等待节点 | 配置等待间隔 | flow/wait.vue |
| FP-MKT-CANVAS-FLOW-004 | 流程校验 | 校验流程配置 | flow/validate.vue |

**Feature 4 小计: 4 FP**

### Feature 5: 数据分析

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CANVAS-ANAL-001 | 营销漏斗 | 展示营销漏斗数据 | analysis/funnel.vue |
| FP-MKT-CANVAS-ANAL-002 | 节点效果 | 展示节点执行效果 | analysis/node.vue |
| FP-MKT-CANVAS-ANAL-003 | 实时监控 | 实时监控执行状态 | analysis/monitor.vue |
| FP-MKT-CANVAS-ANAL-004 | 数据导出 | 导出分析数据 | analysis/export.vue |

**Feature 5 小计: 4 FP**

---

## 📍 菜单映射表

| 一级菜单 | 二级菜单 | 对应Feature | 状态 |
|:---|:---|:---|:---:|
| 数字营销 | 营销画布 | 画布编辑器 | 待开发 |
| 数字营销 | 营销画布 | 节点管理 | 待开发 |
| 数字营销 | 营销画布 | 触发条件 | 待开发 |
| 数字营销 | 营销画布 | 流程控制 | 待开发 |
| 数字营销 | 营销画布 | 数据分析 | 待开发 |

---

## 📝 版本历史

| 版本号 | 更新日期 | 更新内容 | 作者 |
|:---:|:---:|:---|:---:|
| v5.0 | 2026-04-24 | 初始版本，基于产品需求文档索引 | Tony Stark |

---

🦾 *"我是天才，营销画布 EPIC 文档完成！"*