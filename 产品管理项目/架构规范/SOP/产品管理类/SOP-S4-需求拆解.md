# SOP-S4: 需求拆解

> **版本**: v1.1
> **日期**: 2026-05-13
> **作者**: Tony Stark
> **状态**: 正式发布
> **变更说明**: v1.1 新增异常预定义和状态追踪章节（引用 SOP-通用补充规范）

---

## 1. 概述

### 1.1 目标

将需求拆解为 Epic → Feature → Story → FP

### 1.2 触发时机

| 触发类型 | 说明 | 优先级 |
|:---|:---|:---:|
| S3 需求分析完成 | SOP-S3 步骤5产出 | P0 |
| 需求确认 | PM 确认业务需求文档 | P0 |

**触发信号**：业务需求文档已生成 / PM 确认需求

### 1.3 输入

| 输入项 | 必填 | 说明 |
|:---|:---:|:---|
| 需求理解报告 | ✅ | 9项信息 |
| 需求补充文档 | ✅ | 场景/边界/验收标准 |
| 业务需求文档 | ✅ | 07模板输出 |

### 1.4 输出

| 输出项 | 状态 | 说明 |
|:---|:---:|:---|
| Epic 列表 | ⏳待产出 | 含ID、名称、边界 |
| Feature 列表 | ⏳待产出 | 含ID、名称、优先级 |
| Story 列表 | ⏳待产出 | 含UDD格式+4项验收标准 |
| FP 列表 | ⏳待产出 | 含ID、类型、验收标准 |
| Neo4j 节点 | ⏳待产出 | Epic+Feature+Story+FP |

---

## 2. 处理流程

### 步骤 1: Epic 识别

**输入**：业务需求文档

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

**异常预定义**：

| 等级 | 异常 | 处理 |
|:---:|:---|:---|
| **E1** | Epic 数量为0（无法识别Epic） | 暂停，追问"这个需求的业务目标是什么" |
| **E2** | Epic 数量超范围（>5） | 降级：记录warning，尝试合并或拆分，继续 |
| E3 | Epic 命名格式不规范 | 记录warning，自动格式化或标注需确认 |

---

### 步骤 2: Feature 拆解

**输入**：Epic 列表

**前置条件**：步骤1完成

**操作**：
1. 每个 Epic 拆解为 3-10 个 Feature
2. 确定 Feature 优先级
3. 确定 Feature 之间的依赖

**Feature 拆解原则**：
- 一个 Feature 完成一个功能模块
- Feature 粒度：3-10 个/Epic
- Feature 命名：`FEAT-{域}-{模块}-{特性}`

**异常预定义**：

| 等级 | 异常 | 处理 |
|:---:|:---|:---|
| **E1** | Feature 数量为0 | 暂停，追问"这个Epic包含哪些功能模块" |
| **E2** | Feature 数量超范围（>10） | 降级：记录warning，尝试合并，继续 |
| E2 | Feature 之间有循环依赖 | 记录warning，尝试拆分依赖链，标注需确认 |
| E3 | Feature 命名格式不规范 | 记录warning，自动格式化或标注需确认 |

---

### 步骤 3: Story 拆解

**输入**：Feature 列表

**前置条件**：步骤2完成

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

**异常预定义**：

| 等级 | 异常 | 处理 |
|:---:|:---|:---|
| **E1** | Story 验收标准缺少任一项 | 暂停，追问缺失的验收标准 |
| **E2** | Story 数量超范围（>10） | 降级：记录warning，尝试合并，继续 |
| E3 | UDD 格式不完整 | 记录warning，补充缺失部分或标注需确认 |

---

### 步骤 4: FP 拆解

**输入**：Story 列表

**前置条件**：步骤3完成

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

**异常预定义**：

| 等级 | 异常 | 处理 |
|:---:|:---|:---|
| **E1** | FP 数量为0 | 暂停，追问"这个Story包含哪些具体功能点" |
| **E2** | FP 数量超范围（>15） | 降级：记录warning，尝试拆分Story，继续 |
| E3 | FP 类型无法判断 | 记录warning，默认为"页面"，标注需确认 |

---

### 步骤 5: 同步到 Neo4j

**Skill 调用**：`requirement-breakdown`

**前置条件**：步骤1-4完成

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

**异常预定义**：

| 等级 | 异常 | 处理 |
|:---:|:---|:---|
| **E1** | Neo4j 连接失败 | 暂停，尝试3次重连（间隔10s），仍失败则记录pending |
| **E1** | 节点ID已存在 | 暂停，追问覆盖/跳过/改名 |
| E2 | 部分节点创建失败 | 记录warning，继续创建其他的，记录失败列表 |
| E3 | 关系创建失败 | 记录日志，Node已创建，告知需手动补充关系 |

---

## 3. 状态流转

```
步骤1[Epic识别]
    │
    ├── ✅ done（1-5个Epic）→ 步骤2
    ├── ❌ failed（数量为0）→ [追问后resume]
    └── ⚠️ done（数量>5）→ 降级继续 → 步骤2

步骤2[Feature拆解]
    │
    ├── ✅ done（3-10个/Epic）→ 步骤3
    ├── ❌ failed（数量为0）→ [追问后resume]
    └── ⚠️ done（数量>10）→ 降级继续 → 步骤3

步骤3[Story拆解]
    │
    ├── ✅ done（验收标准完整）→ 步骤4
    ├── ❌ failed（验收标准缺失）→ [追问后resume]
    └── ⚠️ done（数量>10）→ 降级继续 → 步骤4

步骤4[FP拆解]
    │
    ├── ✅ done → 步骤5
    ├── ❌ failed（数量为0）→ [追问后resume]
    └── ⚠️ done（数量>15）→ 降级继续 → 步骤5

步骤5[同步Neo4j]
    │
    ├── ✅ done → [SOP完成]
    ├── ⏳ pending（连接失败）→ [等待重连或手动解决]
    └── ❌ failed → [部分完成，报告需手动处理项]
```

---

## 4. 拆解规范速查

| 层级 | 数量建议 | 命名格式 |
|:---|:---:|:---|
| Epic | 1-5 个 | `EPIC-{域}-{模块}-{名称}` |
| Feature | 3-10 个/Epic | `FEAT-{域}-{模块}-{特性}` |
| Story | 3-10 个/Feature | `STORY-{域}-{模块}-{用户故事}` |
| FP | 5-15 个/Story | `FP-{域}-{模块}-{功能点}` |

---

## 5. 验收检查清单

- [ ] Epic 数量在 1-5 个
- [ ] 每个 Epic 有 3-10 个 Feature
- [ ] 每个 Feature 有 3-10 个 Story
- [ ] 每个 Story 有 5-15 个 FP
- [ ] 所有 Story 有 4 项验收标准
- [ ] Neo4j 节点已创建
- [ ] 关系已建立

---

## 6. 异常记录

| 执行ID | 日期 | 步骤数 | 完成 | 异常数 | E1 | E2 | E3 | 备注 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| EXEC-xxx | 2026-05-13 | 5 | 5 | 0 | 0 | 0 | 0 | 正常完成 |

---

## 7. 关联 Skill

| Skill | 用途 | 调用时机 |
|:---|:---|:---|
| `requirement-breakdown` | 需求拆解到 Neo4j | 步骤5 同步数据 |
| `product-breakdown` | 产品结构拆解 | 整体流程 |

---

## 8. 变更记录

| 日期 | 版本 | 变更内容 | 作者 |
|:---|:---:|:---|:---|
| 2026-04-24 | v1.0 | 初始版本 | Tony Stark |
| 2026-05-13 | v1.1 | 新增异常预定义和状态追踪章节 | Tony Stark |

---

🦾 *SOP-S4 v1.1 | 异常处理+状态追踪已补充*
