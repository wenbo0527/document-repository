# PD-MKT 数字营销 - 参考结构

## Epic 列表（5个）

| Epic Code | Epic Name | Feature Count | FP Count |
|:---|:---|:---:|:---:|
| EPIC-MKT-REACH | 触达系统 | 5 | 22 |
| EPIC-MKT-BENEFIT | 权益中心 | 4 | 9 |
| EPIC-MKT-CROWD | 客群中心 | 4 | 14 |
| EPIC-MKT-CANVAS | 营销画布 | 2 | 8 |
| EPIC-MKT-SALES | 人工电销工作台 | 7 | 30 |

**合计**: 5 Epic, 22 Feature, 83 FP

---

## EPIC-MKT-REACH 触达系统

### Feature 清单

| Feature Code | Feature Name | Code Path |
|:---|:---|:---|
| FEAT-MKT-REACH-IDX | 触达首页 | touch/index.vue |
| FEAT-MKT-REACH-SYS | 系统管理 | touch/system/ |
| FEAT-MKT-REACH-POL | 策略管理 | touch/policy/ |
| FEAT-MKT-REACH-CH | 渠道管理 | touch/channel/ |
| FEAT-MKT-REACH-QRY | 触达查询 | touch/query/ |

### FP 清单（22个）

#### FEAT-MKT-REACH-IDX 触达首页

| FP ID | 功能点 | Code Path |
|:---|:---|:---|
| FP-MKT-REACH-IDX-001 | 任务明细展示 | touch/index.vue |
| FP-MKT-REACH-IDX-002 | 数据概览 | touch/index.vue |
| FP-MKT-REACH-IDX-003 | 快捷入口 | touch/index.vue |

#### FEAT-MKT-REACH-SYS 系统管理

| FP ID | 功能点 | Code Path |
|:---|:---|:---|
| FP-MKT-REACH-SYS-001 | 系统概览 | touch/system/index.vue |
| FP-MKT-REACH-SYS-002 | 字段管理 | touch/system/dictionary.vue |

#### FEAT-MKT-REACH-POL 策略管理

| FP ID | 功能点 | Code Path |
|:---|:---|:---|
| FP-MKT-REACH-POL-001 | 策略模板 | touch/policy/template/ |
| FP-MKT-REACH-POL-002 | 数据概览 | touch/policy/overview.vue |

#### FEAT-MKT-REACH-CH 渠道管理

| FP ID | 功能点 | Code Path |
|:---|:---|:---|
| FP-MKT-REACH-CH-001 | 人工外呼模板 | touch/channel/manual-call-template.vue |
| FP-MKT-REACH-CH-002 | 短信模板 | touch/channel/sms-template.vue |
| FP-MKT-REACH-CH-003 | AI外呼模板 | touch/channel/ai-call-template.vue |
| FP-MKT-REACH-CH-004 | 预警管理 | touch/channel/alert.vue |
| FP-MKT-REACH-CH-005 | 全局频控 | touch/channel/rate-limit.vue |
| FP-MKT-REACH-CH-006 | 黑名单管理 | touch/channel/blacklist.vue |
| FP-MKT-REACH-CH-007 | AI供应商 | touch/channel/vendors/ai.vue |
| FP-MKT-REACH-CH-008 | 短信供应商 | touch/channel/vendors/sms.vue |

#### FEAT-MKT-REACH-QRY 触达查询

| FP ID | 功能点 | Code Path |
|:---|:---|:---|
| FP-MKT-REACH-QRY-001 | 触达明细查询 | touch/query/detail.vue |
| FP-MKT-REACH-QRY-002 | 短信发送记录 | touch/query/sms-records.vue |
| FP-MKT-REACH-QRY-003 | AI外呼记录 | touch/query/ai-call-records.vue |
| FP-MKT-REACH-QRY-004 | AI厂商短信记录 | touch/query/ai-sms-vendor-records.vue |
| FP-MKT-REACH-QRY-005 | 人工外呼记录 | touch/query/manual-call-records.vue |
| FP-MKT-REACH-QRY-006 | 人工厂商短信记录 | touch/query/manual-sms-vendor-records.vue |
| FP-MKT-REACH-QRY-007 | 营销记录查询 | touch/query/marketing-search.vue |

---

## EPIC-MKT-BENEFIT 权益中心

### Feature 清单

| Feature Code | Feature Name |
|:---|:---|
| FEAT-MKT-BENEFIT-IDX | 权益首页 |
| FEAT-MKT-BENEFIT-CONFIG | 权益配置 |
| FEAT-MKT-BENEFIT-STATS | 权益统计 |
| FEAT-MKT-BENEFIT-GLOBAL | 全局管理 |

### FP 清单（9个）

| FP ID | Feature | 功能点 |
|:---|:---|:---|
| FP-MKT-BENEFIT-IDX-001 | 权益首页 | 权益汇总数据展示 |
| FP-MKT-BENEFIT-CONFIG-001 | 权益配置 | 券模板管理 |
| FP-MKT-BENEFIT-CONFIG-002 | 权益配置 | 券库存管理 |
| FP-MKT-BENEFIT-CONFIG-003 | 权益配置 | 券包管理 |
| FP-MKT-BENEFIT-STATS-001 | 权益统计 | 权益日志 |
| FP-MKT-BENEFIT-STATS-002 | 权益统计 | 库存查询 |
| FP-MKT-BENEFIT-GLOBAL-001 | 全局管理 | 全局规则 |
| FP-MKT-BENEFIT-GLOBAL-002 | 全局管理 | 预警管理 |

---

## EPIC-MKT-CROWD 客群中心

### Feature 清单

| Feature Code | Feature Name |
|:---|:---|
| FEAT-MKT-CROWD-SYS | 系统管理 |
| FEAT-MKT-CROWD-LIST | 人群列表 |
| FEAT-MKT-CROWD-EVENT | 事件管理 |
| FEAT-MKT-CROWD-IDMAP | ID-mapping |

### FP 清单（14个）

| FP ID | Feature | 功能点 |
|:---|:---|:---|
| FP-MKT-CROWD-SYS-001 | 系统管理 | 数据源管理 |
| FP-MKT-CROWD-SYS-002 | 系统管理 | Kafka管理 |
| FP-MKT-CROWD-SYS-003 | 系统管理 | 标签表管理 |
| FP-MKT-CROWD-LIST-001 | 人群列表 | 新建人群 |
| FP-MKT-CROWD-LIST-002 | 人群列表 | 人群详情 |
| FP-MKT-CROWD-LIST-003 | 人群列表 | 人群操作 |
| FP-MKT-CROWD-EVENT-001 | 事件管理 | 事件列表 |
| FP-MKT-CROWD-EVENT-002 | 事件管理 | 虚拟事件 |
| FP-MKT-CROWD-EVENT-003 | 事件管理 | 事件圈客 |
| FP-MKT-CROWD-EVENT-004 | 事件管理 | 事件测试 |
| FP-MKT-CROWD-EVENT-005 | 事件管理 | 一次性建群算 |
| FP-MKT-CROWD-IDMAP-001 | ID-mapping | ID映射服务 |

---

## EPIC-MKT-CANVAS 营销画布

### Feature 清单

| Feature Code | Feature Name |
|:---|:---|
| FEAT-MKT-CANVAS-LIST | 画布列表 |
| FEAT-MKT-CANVAS-DETAIL | 画布详情 |

### FP 清单（8个）

| FP ID | Feature | 功能点 |
|:---|:---|:---|
| FP-MKT-CANVAS-LIST-001 | 画布列表 | 列表展示 |
| FP-MKT-CANVAS-LIST-002 | 画布列表 | 新建画布 |
| FP-MKT-CANVAS-DETAIL-001 | 画布详情 | 编辑Tab |
| FP-MKT-CANVAS-DETAIL-002 | 画布详情 | 统计Tab |
| FP-MKT-CANVAS-DETAIL-003 | 画布详情 | 版本Tab |
| FP-MKT-CANVAS-DETAIL-004 | 画布详情 | 节点配置 |
| FP-MKT-CANVAS-DETAIL-005 | 画布详情 | 交互优化 |
| FP-MKT-CANVAS-DETAIL-006 | 画布详情 | 发布校验 |

---

## EPIC-MKT-SALES 人工电销工作台

### Feature 清单

| Feature Code | Feature Name |
|:---|:---|
| FEAT-MKT-SALES-ORG | 组织管理 |
| FEAT-MKT-SALES-TASK | 任务管理 |
| FEAT-MKT-SALES-WORKBENCH | 客户工作台 |
| FEAT-MKT-SALES-QC | 质量管理 |
| FEAT-MKT-SALES-COST | 费用管理 |
| FEAT-MKT-SALES-SYS | 系统管理 |
| FEAT-MKT-SALES-DASHBOARD | 数据看板 |

### FP 清单（30个）

| FP ID | Feature | 功能点 |
|:---|:---|:---|
| FP-MKT-SALES-ORG-001 | 组织管理 | 小组管理 |
| FP-MKT-SALES-ORG-002 | 组织管理 | 团队管理 |
| FP-MKT-SALES-ORG-003 | 组织管理 | 坐席管理 |
| FP-MKT-SALES-ORG-004 | 组织管理 | 角色管理 |
| FP-MKT-SALES-TASK-001 | 任务管理 | 外呼任务管理 |
| FP-MKT-SALES-TASK-002 | 任务管理 | 新建外呼任务 |
| FP-MKT-SALES-TASK-003 | 任务管理 | 智能外呼配置 |
| FP-MKT-SALES-TASK-004 | 任务管理 | 任务详情 |
| FP-MKT-SALES-TASK-005 | 任务管理 | 任务排班 |
| FP-MKT-SALES-TASK-006 | 任务管理 | 回访管理 |
| FP-MKT-SALES-WORKBENCH-001 | 客户工作台 | 目标潜客工作台 |
| FP-MKT-SALES-WORKBENCH-002 | 客户工作台 | 客户列表 |
| FP-MKT-SALES-WORKBENCH-003 | 客户工作台 | 客户详情 |
| FP-MKT-SALES-WORKBENCH-004 | 客户工作台 | 拨打功能 |
| FP-MKT-SALES-WORKBENCH-005 | 客户工作台 | 跟进记录 |
| FP-MKT-SALES-WORKBENCH-006 | 客户工作台 | 通话记录查询 |
| FP-MKT-SALES-QC-001 | 质量管理 | 评分模板管理 |
| FP-MKT-SALES-QC-002 | 质量管理 | 质检检查 |
| FP-MKT-SALES-QC-003 | 质量管理 | 质检结果详情 |
| FP-MKT-SALES-COST-001 | 费用管理 | 费用规则配置 |
| FP-MKT-SALES-COST-002 | 费用管理 | 费用明细 |
| FP-MKT-SALES-SYS-001 | 系统管理 | 规则池配置 |
| FP-MKT-SALES-SYS-002 | 系统管理 | 外部数据管理 |
| FP-MKT-SALES-SYS-003 | 系统管理 | 用户日志查询 |
| FP-MKT-SALES-DASHBOARD-001 | 数据看板 | 绩效概览 |
| FP-MKT-SALES-DASHBOARD-002 | 数据看板 | 坐席监控 |
| FP-MKT-SALES-DASHBOARD-003 | 数据看板 | 坐席绩效 |
| FP-MKT-SALES-DASHBOARD-004 | 数据看板 | 数据概览 |

---

## 审批流接入点

| Feature | 审批场景 | 审批流模板 |
|:---|:---|:---|
| 策略管理 | 触达策略发布前审批 | 【触达策略审批流】 |
| 渠道管理 | 渠道配置变更审批 | 【渠道配置审批流】 |
