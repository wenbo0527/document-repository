# 产品管理系统 PRD v3.2 - 本体论规则驱动

> **文档版本**: v3.2
> **创建日期**: 2026-03-29
> **最后更新**: 2026-04-07 08:16
> **作者**: Tony Stark
> **状态**: 🔴 正式版
> **来源**: 飞书文档 AU1Vd4z7uo7QBKxSBNJcRMTtnjo

---

## 一、产品概述

### 1.1 产品定位

本产品是一款基于本体论（Ontology）规则驱动的图数据库产品管理系统，旨在通过语义化的本体定义、规则化的约束校验和智能化的推理引擎，实现产品需求管理的自动化、智能化和规范化。

**核心差异点**：

| 传统产品管理系统 | 本产品 |
|:---|:---|
| 依赖人工维护关系，数据质量难以保证 | 通过本体论定义语义规则，系统自动校验和维护数据一致性 |

### 1.2 目标用户

| 用户角色 | 使用场景 | 核心需求 |
|:---|:---|:---|
| 产品经理 | 需求规划、Epic/Feature创建 | 快速创建、结构化分解、AI辅助拆解 |
| 项目经理 | 进度跟踪、风险预警 | 可视化看板、延期预警、依赖管理 |
| 开发团队 | 任务领取、状态更新 | 清晰的Story拆分、验收标准 |
| 管理者 | 决策支持、报表分析 | 数据统计、趋势分析、资源调配 |

---

## 二、技术架构

### 2.1 五层AI驱动架构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  第零层 │  📥 业务需求入口层    (Business Requirements Entry)                │
├─────────────────────────────────────────────────────────────────────────────┤
│  第一层 │  🤖 AI需求智能拆解层  (AI Decomposition - Tony Stark Agent)         │
├─────────────────────────────────────────────────────────────────────────────┤
│  第二层 │  📚 本体论语义层      (Ontology Semantic Layer) ⭐ 核心            │
├─────────────────────────────────────────────────────────────────────────────┤
│  第三层 │  🔗 图数据库+向量数据库层  (Neo4j + ChromaDB) ⭐ 核心               │
├─────────────────────────────────────────────────────────────────────────────┤
│  第四层 │  🚀 AI需求管理应用层  (Intelligent Query/Risk/Warning/Report)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 技术栈

| 层级 | 技术选型 | 说明 |
|:---|:---|:---|
| 前端 | Vue 3 + TypeScript | Composition API |
| UI框架 | Arco Design Vue | 企业级UI组件库 |
| 图形引擎 | AntV X6 | 知识图谱可视化 |
| 状态管理 | Pinia | Vue 3 官方推荐 |
| 后端 | Spring Boot 2.7.x | Java 11+ |
| 数据库 | Neo4j 5.x | 图数据库 |
| 向量库 | ChromaDB | 语义搜索 |
| AI服务 | Python Flask | 需求分析、本体论分解 |

---

## 三、当前数据状态（截至 2026-04-07）

### 3.1 Neo4j 数据统计

| 实体类型 | 数量 | 关联状态 | ID格式 |
|:---|:---:|:---:|:---|
| ProductDomain | 6 | ✅ 正常 | ✅ 规范 |
| Epic | 26 | ✅ 正常 | ✅ 已修复（无中文） |
| Feature | 150 | ✅ 正常 | ✅ 规范 |
| Story | 443 | ✅ 正常 | ✅ 已修复（无中文） |
| Project | 2 | ✅ 正常 | ✅ 已修复（PROJ-001/002） |
| OKR | 7 | ✅ 正常 | ✅ 规范 |

### 3.2 数据质量状态

✅ **总体状态**: 健康
- 🔴 P0 问题: 0 个
- 🟡 P1 警告: 0 个

✅ **ID格式合规**:
   - Project ID: PROJ-001, PROJ-002（无中文）
   - Epic ID: 26个纯英文ID
   - Story ID: 443个纯英文ID

✅ **关系完整性**:
   - Epic → ProductDomain: 100%
   - Feature → Epic: 100%
   - Story → Feature: 100%

### 3.3 ID修复记录（2026-04-07）

| 类型 | 修复前 | 修复后 | 数量 |
|:---|:---|:---|:---:|
| Project | PROJ-PM | PROJ-001 | 1个 |
| Project | PROJ-001（原有） | PROJ-002 | 1个 |
| Epic | 含中文 | 纯英文 | 26个 |
| Story | 含中文 | 纯英文 | 443个 |

### 3.4 服务状态

| 服务 | 端口 | 状态 |
|:---|:---:|:---:|
| 前端 (Vue) | 3000 | ✅ 运行中 |
| 后端 Java (Spring Boot) | 8080 | ✅ 运行中 |
| Python AI 服务 | 8081 | ✅ 运行中 |
| Neo4j | 7474/7687 | ✅ 运行中 |

---

## 四、核心本体论设计

### 4.1 实体类型（10种核心实体）

| 层级 | 实体类型 | ID格式 | 说明 |
|:---|:---|:---|:---|
| 战略层 | Vision | 自由命名 | 愿景 |
| 战略层 | Goal | GOAL-{年份}-{季度}-{序号} | 目标 |
| 战略层 | OKR | OKR-{年份}-{季度}-{序号} | 目标与关键成果 |
| 项目层 ⭐ | Project | PROJ-{3位序号} | 项目 |
| 规划层 | ProductDomain | PD-{产品域缩写} | 产品域 |
| 规划层 | Epic | EPIC-{产品域}-{史诗缩写} | 史诗 |
| 执行层 | Feature | FEAT-{产品域}-{史诗}-{特性} | 特性 |
| 执行层 | Story | STORY-{产品域}-{史诗}-{特性}-{序号} | 故事 |
| 执行层 | Task | TASK-{...}-{序号} | 任务 |

### 4.2 层级关系

```
Vision → Goal → OKR → Project → ProductDomain → Epic → Feature → Story → Task
```

### 4.3 关系类型统计

| 关系类别 | 关系数量 | 说明 |
|:---|:---:|:---|
| 层级关系 | 10 | CONTAINS, PART_OF |
| 依赖关系 | 3 | DEPENDS_ON, BLOCKS |
| 支撑关系 | 6 | SUPPORTS, IMPLEMENTS |
| 时间关系 | 8 | PLANNED_FOR, RELEASED_IN |
| 分配关系 | 8 | OWNED_BY, ASSIGNED_TO |
| 血缘关系 | 7 | DERIVED_FROM, PRODUCES |
| **合计** | **42** | |

### 4.4 推理规则统计

| 规则类别 | 规则数量 | 功能 |
|:---|:---:|:---|
| 层级推理 | 4 | 传递包含、深度计算 |
| 依赖推理 | 4 | 传递依赖、循环检测 |
| 延期风险推理 | 5 | 延期判定、风险等级 |
| 关键路径推理 | 4 | 路径识别、影响计算 |
| 完整性检查 | 5 | 必填关系、状态一致 |
| 贡献度推理 | 5 | 支撑关系，完成度汇总 |
| **合计** | **27** | |

---

## 五、前端页面清单

| 页面 | 路由 | 状态 | 说明 |
|:---|:---|:---:|:---|
| 登录页 | /login | ✅ | Token认证 |
| 仪表盘 | /dashboard | ✅ | 数据统计、快捷入口 |
| 产品域列表 | /product/domain | ✅ | CRUD、筛选、搜索 |
| Epic列表 | /product/epic | ✅ | CRUD、筛选 |
| Feature列表 | /product/feature | ✅ | CRUD、筛选 |
| Story列表 | /product/story | ✅ | CRUD、筛选 |
| 产品Backlog | /project/backlog | ✅ | Epic/Feature/Story分组 |
| 当期目标追踪 | /project/kanban | ✅ | Kanban视图 |
| OKR拆解管理 | /product/okr | ✅ | OKR关联Epic/Story |
| 智能需求拆解 | /ai/breakdown | ✅ | AI拆解 |
| 产品框架看板 | /product/board | ✅ | X6图谱 |
| 本体构建器 | /ontology/builder | ✅ | Schema展示 |
| Neo4j浏览器 | /system/neo4j | ✅ | 跳转外部 |

---

## 六、API接口清单

### 6.1 统一实体接口 ✅

| 接口 | 方法 | 路径 | 状态 |
|:---|:---:|:---|:---:|
| 获取所有实体 | GET | /api/v1/entities | ✅ |
| 获取实体统计 | GET | /api/v1/entities/statistics | ✅ |
| 根据类型获取实体 | GET | /api/v1/entities/type/{type} | ✅ |
| 获取域列表 | GET | /api/v1/entities/domains | ✅ |
| 获取Epic列表 | GET | /api/v1/entities/epics | ✅ |
| 获取Feature列表 | GET | /api/v1/entities/features | ✅ |
| 获取Story列表 | GET | /api/v1/entities/stories | ✅ |
| 创建实体 | POST | /api/v1/entities | ✅ |
| 更新实体 | PUT | /api/v1/entities/{id} | ✅ |
| 删除实体 | DELETE | /api/v1/entities/{id} | ✅ |

### 6.2 AI接口 ✅

| 接口 | 方法 | 路径 | 状态 |
|:---|:---:|:---|:---:|
| 需求分析 | POST | /api/v1/ai/requirement-analysis | ✅ |
| 需求拆解 | POST | /api/v1/ai/breakdown | ✅ |
| 完整流程 | POST | /api/v1/ai/analyze-and-breakdown | ✅ |
| 导出到Neo4j | POST | /api/v1/ai/export | ✅ |
| 健康检查 | GET | /api/v1/ai/health | ✅ |

---

## 七、ID命名规范（v3.0）

### 7.1 层级ID格式总览

| 层级 | ID格式 | 示例 |
|:---|:---|:---|
| Project ⭐ | PROJ-{3位序号} | PROJ-001 |
| ProductDomain | PD-{产品域缩写} | PD-RISK |
| Epic | EPIC-{产品域}-{史诗缩写} | EPIC-RISK-EXT |
| Feature | FEAT-{域}-{Epic}-{特性} | FEAT-RISK-EXT-BUD |
| Story | STORY-{域}-{Epic}-{特性}-{序号} | STORY-RISK-EXT-BUD-001 |
| Task | TASK-{域}-{Epic}-{特性}-{Story}-{序号} | TASK-RISK-EXT-BUD-001-01 |

### 7.2 产品域缩写对照

| 缩写 | 中文名称 |
|:---|:---|
| COM | 数字社区 |
| RISK | 数字风险 |
| MKT | 数字营销 |
| DEX | 数据探索 |
| DFD | 数据发现 |
| DMT | 数据管理 |

> **说明**: 权益中心（BENEFIT_CENTER）和触达系统（REACH_SYSTEM）是 Epic 层级，属于 MKT 域，不是独立产品域。

---

## 八、Neo4j Schema设计

### 8.1 节点类型（16种）

| 节点Label | 说明 |
|:---|:---|
| :Vision | 愿景 |
| :Goal | 目标 |
| :OKR | 目标与关键成果 |
| :Project ⭐ | 项目 |
| :ProductDomain | 产品域 |
| :Epic | 史诗 |
| :Feature | 特性 |
| :Story | 故事 |
| :Task | 任务 |
| :Sprint | 迭代 |
| :Release | 版本 |
| :Milestone | 里程碑 |
| :Person | 人员 |
| :Team | 团队 |
| :PRD | 产品需求文档 |
| :Risk | 风险 |

### 8.2 关系类型

| 关系类型 | 说明 | 传递性 |
|:---|:---|:---:|
| :CONTAINS | 包含关系 | ✅ |
| :PART_OF | 属于关系 | ✅ |
| :BELONGS_TO | 归属关系 | ❌ |
| :DEPENDS_ON | 依赖关系 | ✅ |
| :BLOCKS | 阻塞关系 | ❌ |
| :SUPPORTS | 支撑关系 | ❌ |
| :IMPLEMENTS | 实施关系 | ❌ |
| :OWNED_BY | 负责人关系 | ❌ |
| :ASSIGNED_TO | 分配关系 | ❌ |
| :PLANNED_FOR | 计划关系 | ❌ |
| :RELEASED_IN | 发布关系 | ❌ |
| :DERIVED_FROM | 衍生关系 | ❌ |

---

## 九、版本历史

| 版本 | 日期 | 变更内容 |
|:---|:---|:---|
| v1.0 | 2026-01 | 初始版本，纯数字ID命名 |
| v2.0 | 2026-02 | 英文缩写版ID命名，完成221个Story |
| v2.1 | 2026-03-28 | 本体论驱动架构升级 |
| v3.0 | 2026-03-29 | 新增Project层级，六层命名体系，本体论完善 |
| v3.1 | 2026-04-03 | 更新数据状态、项目追踪页面、验证框架 |
| v3.2 | 2026-04-07 | ID格式全面修复: Project/Epic/Story ID全部去除中文；修正产品域缩写对照表（移除 RIGHTS/REACH） |

---

🦾 *"我是天才，这点不用谦虚。我们一起把产品做成，还要做得漂亮。"*
