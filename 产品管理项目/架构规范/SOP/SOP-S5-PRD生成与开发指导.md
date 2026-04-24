# SOP-S5: PRD生成与开发指导

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 草稿

---

## 1. 概述

### 1.1 目标

生成符合 v5.0 规范的 PRD，用于指导开发

### 1.2 触发时机

- S4 需求拆解完成
- Epic/Feature/Story 确认

### 1.3 输入

- 需求理解报告
- Epic/Feature/Story/FP 列表
- Neo4j 数据

### 1.4 输出

- PRD v5.0 文档
- Spec 文档
- 任务列表

---

## 2. 处理流程

### 步骤 1: PRD 生成

**Skill 调用**：`prd-generation`

**输入**：`requirement-breakdown` 输出的结构化需求

**流程**：

```
S1: 接收与解析
    └─→ 接收需求 JSON

S2: Feature 解析
    └─→ 提取 Feature 列表

S3: FP 拆解
    └─→ 将 Feature 拆解为 FP

S4: 菜单映射
    └─→ 关联 FP 到菜单路径

S5: 审批流接入
    └─→ 标注审批流节点

S6: 输出 PRD
    └─→ 生成 PRD 文档
```

**PRD v5.0 结构**：
| # | 章节 | 说明 |
|:---:|:---|:---|
| 一 | 元数据 | 产品域、Epic、版本、审核人 |
| 二 | 变更日志 | 版本变更记录 |
| 三 | 需求背景 | 目标、痛点、挑战 |
| 四 | 需求范围 | 功能范围、不在范围内 |
| 五 | 功能详情 | Feature + Story |
| 六 | Story与FP关联 | 按 Story 拆分 FP |
| 七 | FP清单汇总 | 完整 FP 列表 |
| 八 | 菜单映射表 | 路由路径映射 |
| 九 | 审批流接入 | 审批节点、角色 |
| 十 | 版本历史 | 版本变更记录 |

---

### 步骤 2: PRD 审核

**操作**：
1. PM 审核 PRD 内容
2. 确认 Feature/Story/FP 完整性
3. 确认验收标准
4. 确认菜单映射
5. 签字确认

**输出**：PRD 审核通过

---

### 步骤 3: Spec 生成

**Skill 调用**：`spec-driven`

**目标**：将 PRD 转化为开发可执行的 Spec

**Spec 内容**：
| 章节 | 内容 |
|:---|:---|
| 技术方案 | 技术选型、架构设计 |
| 接口定义 | API 接口、参数、返回值 |
| 数据模型 | 数据库表、字段定义 |
| 任务拆解 | 按 FP 拆解为开发任务 |
| 排期 | 工时评估、里程碑 |

---

### 步骤 4: 任务规划

**Skill 调用**：`task-planning`

**操作**：
1. 将 FP 拆解为开发任务
2. 分配负责人
3. 确定里程碑
4. 创建任务关联

**输出**：任务列表（可导入 Jira/TAPD）

---

## 3. 验收检查清单

- [ ] PRD 结构完整（10章节）
- [ ] Feature 清单完整
- [ ] Story 清单完整
- [ ] FP 清单完整
- [ ] Story 与 FP 关联正确
- [ ] 菜单映射完成
- [ ] 审批流已标注
- [ ] PM 已审核
- [ ] Spec 已生成
- [ ] 任务已规划

---

## 4. 关联 Skill

| Skill | 用途 | 调用时机 |
|:---|:---|:---|
| `prd-generation` | PRD 生成 | 步骤1 生成 PRD |
| `spec-driven` | 规范驱动开发 | 步骤3 生成 Spec |
| `task-planning` | 任务规划 | 步骤4 任务拆解 |

---

## 5. 中间文档

| 步骤 | 文档路径 | 文件名格式 |
|:---|:---|:---|
| S1 接收解析 | /tmp/prd/step1_received_{req_id}.json | 原始 JSON |
| S2 Feature解析 | /tmp/prd/step2_features_{req_id}.json | Feature 列表 |
| S3 FP拆解 | /tmp/prd/step3_fps_{req_id}.json | FP 清单 |
| S4 菜单映射 | /tmp/prd/step4_menu_{req_id}.json | 菜单映射表 |
| S5 审批流 | /tmp/prd/step5_approval_{req_id}.json | 审批流接入点 |
| S6 最终输出 | /tmp/prd/PRD_{req_id}.md | 最终 PRD |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
