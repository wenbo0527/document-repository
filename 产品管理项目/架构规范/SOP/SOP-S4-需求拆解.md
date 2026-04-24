# SOP-S4: 需求拆解

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 草稿

---

## 1. 概述

### 1.1 目标

将需求拆解为 Epic → Feature → Story → FP

### 1.2 触发时机

- S3 需求分析完成
- 需求确认

### 1.3 输入

- 需求理解报告（9项信息）
- 需求补充文档

### 1.4 输出

- Epic 列表
- Feature 列表
- Story 列表
- FP 列表
- Neo4j 节点创建

---

## 2. 处理流程

### 步骤 1: Epic 识别

**操作**：
1. 分析需求，确定 Epic 数量
2. 确定每个 Epic 的边界
3. 命名 Epic

**Epic 识别原则**：
- 一个 Epic 完成一个业务目标
- Epic 粒度：1-5 个/需求
- Epic 命名：`EPIC-{域}-{模块}-{名称}`

**示例**：
```
Epic 1: EPIC-COM-PORTAL-首页重构
Epic 2: EPIC-COM-SEARCH-搜索优化
```

---

### 步骤 2: Feature 拆解

**操作**：
1. 每个 Epic 拆解为 3-10 个 Feature
2. 确定 Feature 优先级
3. 确定 Feature 之间的依赖

**Feature 拆解原则**：
- 一个 Feature 完成一个功能模块
- Feature 粒度：3-10 个/Epic
- Feature 命名：`FEAT-{域}-{模块}-{特性}`

**示例**：
```
Epic: EPIC-COM-PORTAL-首页重构
  ├── FEAT-COM-PORTAL-首页布局
  ├── FEAT-COM-PORTAL-快速入口
  ├── FEAT-COM-PORTAL-通知公告
  └── FEAT-COM-PORTAL-数据统计
```

---

### 步骤 3: Story 拆解

**操作**：
1. 每个 Feature 拆解为 3-10 个 Story
2. 使用 UDD（User-Demand-Documentation）格式
3. 确定 Story 验收标准

**Story 格式**：
```
作为 [角色]，在 [场景] 时，需要 [需求]，以便 [价值]
```

**Story 验收标准（4项必填）**：
| 验收类型 | 说明 |
|:---|:---|
| 功能验收 | 功能是否完整 |
| 操作验收 | 操作流程是否正确 |
| 数据验收 | 数据是否准确 |
| 交互验收 | 界面交互是否友好 |

---

### 步骤 4: FP 拆解

**操作**：
1. 每个 Story 拆解为 5-15 个 FP
2. 确定 FP 类型（页面/接口/数据）
3. 确定 FP 验收标准

**FP 类型**：
| 类型 | 说明 |
|:---|:---|
| 页面 | 页面组件、布局、交互 |
| 接口 | API 定义、参数、返回值 |
| 数据 | 数据处理、计算、存储 |

**示例**：
```
Story: 首页布局配置
  ├── FP-001: 顶部导航栏组件
  ├── FP-002: 快捷入口网格组件
  ├── FP-003: 通知公告轮播组件
  └── FP-004: 数据统计卡片组件
```

---

### 步骤 5: 同步到 Neo4j

**Skill 调用**：`requirement-breakdown`

**操作**：
```cypher
// 创建 Epic
CREATE (e:Epic {
  id: "EPIC-XX-XXX",
  name: "{Epic名称}",
  status: "DRAFT",
  created_at: datetime()
})

// 创建 Feature
CREATE (f:Feature {
  id: "FEAT-XX-XXX",
  name: "{Feature名称}",
  priority: "P1",
  status: "DRAFT",
  created_at: datetime()
})

// 创建 Story
CREATE (s:Story {
  id: "STORY-XX-XXX",
  name: "{Story名称}",
  priority: "P1",
  status: "DRAFT",
  created_at: datetime()
})

// 创建 FP
CREATE (fp:FP {
  id: "FP-XX-XXX",
  name: "{FP名称}",
  type: "页面",
  priority: "P1",
  status: "DRAFT",
  created_at: datetime()
})

// 创建关系
MATCH (e:Epic {id: "EPIC-XX-XXX"})
MATCH (f:Feature {id: "FEAT-XX-XXX"})
MATCH (s:Story {id: "STORY-XX-XXX"})
MATCH (fp:FP {id: "FP-XX-XXX"})

CREATE (f)-[:BELONGS_TO]->(e)
CREATE (s)-[:BELONGS_TO]->(f)
CREATE (fp)-[:BELONGS_TO]->(s)
```

---

## 3. 拆解规范速查

| 层级 | 数量建议 | 命名格式 |
|:---|:---:|:---|
| Epic | 1-5 个 | `EPIC-{域}-{模块}-{名称}` |
| Feature | 3-10 个/Epic | `FEAT-{域}-{模块}-{特性}` |
| Story | 3-10 个/Feature | `STORY-{域}-{模块}-{用户故事}` |
| FP | 5-15 个/Story | `FP-{域}-{模块}-{功能点}` |

---

## 4. 验收检查清单

- [ ] Epic 数量在 1-5 个
- [ ] 每个 Epic 有 3-10 个 Feature
- [ ] 每个 Feature 有 3-10 个 Story
- [ ] 每个 Story 有 5-15 个 FP
- [ ] 所有 Story 有 4 项验收标准
- [ ] Neo4j 节点已创建
- [ ] 关系已建立

---

## 5. 关联 Skill

| Skill | 用途 | 调用时机 |
|:---|:---|:---|
| `requirement-breakdown` | 需求拆解到 Neo4j | 步骤5 同步数据 |
| `product-breakdown` | 产品结构拆解 | 整体流程 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
