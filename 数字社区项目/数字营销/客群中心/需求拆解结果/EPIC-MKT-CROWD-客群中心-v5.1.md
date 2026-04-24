# 客群中心 - EPIC文档 v5.1

**文档版本**: v5.1
**最后更新**: 2026-04-20
**作者**: Tony Stark
**状态**: ✅ 已更新

---

## 📋 元数据头部

| 属性 | 值 | 说明 |
|:---|:---|:---|
| EPIC名称 | 客群中心 | 与菜单名保持一致 |
| EPIC代码 | EPIC-MKT-CROWD | 全局唯一 |
| 产品域 | PD-MKT 数字营销 | 所属产品域 |
| Feature数量 | 5 | 实际数量 |
| FP数量 | 20 | 实际数量 |
| 文档版本 | v5.1 | 固定 |

---

## 🗺️ 结构速览

```
客群中心
├── 系统管理                      ← ⚡ 独立菜单
│   ├── 数据源管理                ← 列表页 + 详情页
│   ├── Kafka管理                 ← 列表页 + 详情页
│   └── 标签表管理                ← 列表页 + 详情页
│
├── 人群列表                      ← ⚡ 独立菜单
│   ├── 新建人群（标签群/事件圈客/剔除）
│   ├── 人群详情（画像分析）
│   └── 人群操作（编辑/复制/删除/导出）
│
├── 事件管理                      ← ⚡ 独立菜单
│   ├── 事件列表（真实事件）
│   ├── 虚拟事件列表 + 详情
│   ├── 事件圈客
│   ├── 事件测试
│   └── 一次性建群算
│
├── 标签管理                      ← ⚡ 独立菜单
│   ├── 属性列表
│   ├── 标签列表
│   ├── 标签详情
│   └── 新建标签
│
└── ID-mapping                   ← 底层能力（不在菜单）
```

---

## ✅ Feature 清单

| # | Feature | 说明 | 开发状态 |
|:---:|:---|:---|:---:|
| 1 | 系统管理 | 数据源/Kafka/标签表管理 | 已完成 |
| 2 | 人群列表 | 人群创建/圈选/详情/操作 | 已完成 |
| 3 | 事件管理 | 事件注册/圈客/测试/建群 | 已完成 |
| 4 | 标签管理 | 属性/标签的增删改查 | 已完成 |
| 5 | ID-mapping | 用户锚点ID（底层能力） | 待规划 |

---

## 📦 Feature Point（FP）清单

### Feature 1: 系统管理

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CRD-SYS-001 | 数据源管理 | 客群数据源（数据库/接口）的增删改查与连接测试 | exploration/customer-center/datasource/ |
| FP-MKT-CRD-SYS-002 | Kafka管理 | Kafka数据源的配置、Topic管理与消费者组配置 | exploration/customer-center/event-center/kafka-datasource.vue |
| FP-MKT-CRD-SYS-003 | 标签表管理 | 标签元数据表的注册与管理 | exploration/customer-center/tag-system/table-management.vue |

**Feature 1 小计: 3 FP**

### Feature 2: 人群列表

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CRD-LST-001 | 新建人群 | 支持标签群/事件圈客/剔除规则创建人群 | exploration/customer-center/audience-system/audience-create.vue |
| FP-MKT-CRD-LST-002 | 人群详情 | 人群画像分析、成员样本查看 | exploration/customer-center/audience-system/audience-detail.vue |
| FP-MKT-CRD-LST-003 | 人群操作 | 人群的编辑/复制/删除/导出/刷新操作 | exploration/customer-center/audience-system/audience-management.vue |
| FP-MKT-CRD-LST-004 | 人群列表查询 | 人群列表的筛选、分页、排序 | exploration/customer-center/audience-system/index.vue |

**Feature 2 小计: 4 FP**

### Feature 3: 事件管理

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CRD-EVT-001 | 事件列表 | 真实事件的注册、编辑，下线管理 | exploration/customer-center/event-center/event-management.vue |
| FP-MKT-CRD-EVT-002 | 虚拟事件 | 虚拟事件的创建、编辑、详情查看 | exploration/customer-center/event-center/virtual-events.vue |
| FP-MKT-CRD-EVT-003 | 事件圈客 | 基于事件条件进行人群圈选 | exploration/customer-center/event-center/event-create.vue |
| FP-MKT-CRD-EVT-004 | 事件测试 | 事件圈选条件的测试与样本验证 | exploration/customer-center/event-center/sample-stats.vue |
| FP-MKT-CRD-EVT-005 | 一次性建群 | 一次性事件建群任务的创建与结果查询 | exploration/customer-center/event-center/event-management.vue |

**Feature 3 小计: 5 FP**

### Feature 4: 标签管理

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CRD-TAG-001 | 属性列表 | 属性分类体系（基础属性/行为属性/业务属性）列表展示 | exploration/customer-center/tag-system/ |
| FP-MKT-CRD-TAG-002 | 属性详情 | 属性详细信息查看、字段映射配置 | exploration/customer-center/tag-system/ |
| FP-MKT-CRD-TAG-003 | 属性新建 | 新建属性配置（名称/类型/分类/映射规则） | exploration/customer-center/tag-system/ |
| FP-MKT-CRD-TAG-004 | 标签列表 | 标签列表展示，支持筛选、搜索 | exploration/customer-center/tag-system/ |
| FP-MKT-CRD-TAG-005 | 标签详情 | 标签详细信息查看，包含标签规则和计算配置 | exploration/customer-center/tag-system/ |
| FP-MKT-CRD-TAG-006 | 新建标签 | 创建新标签，配置IDMapping、标签规则、计算策略 | exploration/customer-center/tag-system/ |

**Feature 4 小计: 6 FP**

### Feature 5: ID-mapping

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-MKT-CRD-IDM-001 | ID关联配置 | 用户多ID（手机/邮箱/设备）的关联关系配置 | 底层能力 |
| FP-MKT-CRD-IDM-002 | 锚点ID管理 | 主键ID（Anchor ID）的配置与查询 | 底层能力 |

**Feature 5 小计: 2 FP**

---

## 📍 菜单映射表

| 一级菜单 | 二级菜单 | 对应Feature | 状态 |
|:---|:---|:---|:---:|
| 数字营销 | 客群中心 | 系统管理 | 待规划 |
| 数字营销 | 客群中心 | 人群列表 | 待规划 |
| 数字营销 | 客群中心 | 事件管理 | 待规划 |
| 数字营销 | 客群中心 | 标签管理 | 待规划 |

---

## 📌 审批流接入点

| Feature名称 | 审批场景 | 对应审批流模板 | 接入状态 |
|:---|:---|:---|:---:|
| 系统管理 | 数据源/标签表配置变更审批 | 【数据源配置审批流】 | 待接入 |
| 人群列表 | 人群发布审批（敏感人群） | 【人群发布审批流】 | 待接入 |
| 事件管理 | 虚拟事件创建审批 | 【事件创建审批流】 | 待接入 |
| 标签管理 | 标签发布审批（核心标签） | 【标签发布审批流】 | 待接入 |
| ID-mapping | 无特定审批场景 | - | 不适用 |

---

## 📝 版本历史

| 版本号 | 更新日期 | 更新内容 | 作者 |
|:---:|:---:|:---|:---:|
| v5.0 | 2026-04-17 | 按代码菜单结构重建，含完整FP和审批流接入点 | Tony Stark |
| v5.1 | 2026-04-20 | 补充标签管理Feature：属性列表/标签列表/新建标签 | Tony Stark |

---

🦾 *"我是天才，这点不用谦虚。"*