# 产品管理系统 - Neo4j Schema 定义 v1.0

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 正式发布

---

## 1. 概述

本文档定义 Neo4j 图数据库的 Schema 结构，基于产品管理系统的本体论设计。

---

## 2. 节点类型

### 2.1 ProductDomain（产品域）

**标签**: `ProductDomain`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键，如 "PD-MKT" |
| uri | string | 完整 URI，如 "ProductDomain:PD-MKT" |
| label | string | 显示名称，如 "数字营销" |
| code | string | 编码，如 "PD-MKT" |
| description | string | 描述 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.2 Epic（史诗）

**标签**: `Epic`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键，如 "EPIC-MKT-CANVAS" |
| uri | string | 完整 URI |
| label | string | 显示名称 |
| code | string | 编码 |
| description | string | 描述 |
| status | string | 状态：DRAFT/IN_PROGRESS/DONE |
| priority | string | 优先级：P0/P1/P2/P3 |
| completionRate | float | 完成度 0-1 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.3 Feature（功能特性）

**标签**: `Feature`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键，如 "FEAT-MKT-CANVAS-001" |
| uri | string | 完整 URI |
| label | string | 显示名称 |
| code | string | 编码 |
| description | string | 描述 |
| status | string | 状态 |
| priority | string | 优先级 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.4 Story（用户故事）

**标签**: `Story`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键 |
| uri | string | 完整 URI |
| label | string | 显示名称 |
| code | string | 编码 |
| asA | string | 作为... |
| iWant | string | 我想要... |
| soThat | string | 以便... |
| acceptanceCriteria | map | 验收标准 |
| status | string | 状态 |
| priority | string | 优先级 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.5 FP（功能点）

**标签**: `FP`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键 |
| uri | string | 完整 URI |
| label | string | 显示名称 |
| code | string | 编码 |
| type | string | 类型：新增/修改/删除 |
| module | string | 模块 |
| description | string | 描述 |
| codePath | string | 代码路径 |
| status | string | 状态 |
| createdAt | datetime | 创建时间 |
| updatedAt | datetime | 更新时间 |

### 2.6 OKR（目标与关键成果）

**标签**: `OKR`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键 |
| label | string | 目标 |
| year | int | 年份 |
| quarter | string | 季度 |
| status | string | 状态 |

### 2.7 Milestone（里程碑）

**标签**: `Milestone`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键 |
| label | string | 名称 |
| dueDate | date | 截止日期 |
| status | string | 状态 |

### 2.8 Project（项目）

**标签**: `Project`

**属性**：
| 属性 | 类型 | 说明 |
|:---|:---|:---|
| id | string | 主键 |
| label | string | 项目名称 |
| description | string | 描述 |
| status | string | 状态 |

---

## 3. 关系类型

### 3.1 BELONGS_TO（归属关系）

| 起点 | 关系 | 终点 | 说明 |
|:---|:---|:---|:---|
| Epic | BELONGS_TO | ProductDomain | Epic 属于产品域 |
| Feature | BELONGS_TO | Epic | Feature 属于 Epic |
| Story | BELONGS_TO | Feature | Story 属于 Feature |
| FP | BELONGS_TO | Feature | FP 属于 Feature |

### 3.2 CONTAINS（包含关系）

| 起点 | 关系 | 终点 | 说明 |
|:---|:---|:---|:---|
| ProductDomain | CONTAINS | Epic | 产品域包含 Epic |
| Epic | CONTAINS | Feature | Epic 包含 Feature |
| Feature | CONTAINS | Story | Feature 包含 Story |
| Feature | CONTAINS | FP | Feature 包含 FP |

### 3.3 SUPPORTS（支撑关系）

| 起点 | 关系 | 终点 | 说明 |
|:---|:---|:---|:---|
| Story | SUPPORTS | Epic | Story 支撑 Epic 完成 |

### 3.4 DEPENDS_ON（依赖关系）

| 起点 | 关系 | 终点 | 说明 |
|:---|:---|:---|:---|
| Feature | DEPENDS_ON | Feature | Feature 之间的依赖 |

### 3.5 HAS_MILESTONE（里程碑关系）

| 起点 | 关系 | 终点 | 说明 |
|:---|:---|:---|:---|
| Epic | HAS_MILESTONE | Milestone | Epic 有里程碑 |

---

## 4. 层级结构

```
ProductDomain (6)
    │
    ├── CONTAINS
    │       │
    │       └──► Epic (22)
    │               │
    │               ├── BELONGS_TO ◄──┐
    │               │                │
    │               ├── CONTAINS     │
    │               │    │          │
    │               │    └──► Feature (157)
    │               │                │
    │               │                ├── BELONGS_TO ◄──┐
    │               │                │                │
    │               │                ├── CONTAINS     │
    │               │                │    │          │
    │               │                │    ├──► Story (42)
    │               │                │    │          │
    │               │                │    └──► FP (xxx)
    │               │                │                │
    │               │                │                └── BELONGS_TO ◄──┘
    │               │                │
    │               │                └── HAS_MILESTONE
    │               │                     │
    │               │                     └──► Milestone
    │               │
    │               └── SUPPORTS
    │                    │
    │                    └──► OKR
    │
    └── HAS_MILESTONE
             │
             └──► Milestone
```

---

## 5. 统计信息

### 5.1 节点统计

| 标签 | 数量 |
|:---|---:|
| ProductDomain | 6 |
| Epic | 22 |
| Feature | 157 |
| Story | 42 |
| FP | ~800+ |
| OKR | 7 |
| Milestone | 6 |
| Project | 2 |

### 5.2 关系统计

| 关系类型 | 数量 |
|:---|---:|
| BELONGS_TO | 678 |
| CONTAINS | 171 |
| SUPPORTS | 11 |
| DEPENDS_ON | 5 |
| HAS_MILESTONE | 1 |

---

## 6. Cypher 示例

### 6.1 查询产品域及其 Epic

```cypher
MATCH (pd:ProductDomain {code: 'PD-MKT'})-[:CONTAINS]->(e:Epic)
RETURN pd, e
```

### 6.2 查询 Epic 及其 Feature

```cypher
MATCH (e:Epic {code: 'EPIC-MKT-CANVAS'})-[:CONTAINS]->(f:Feature)
RETURN e, f
```

### 6.3 查询完整层级

```cypher
MATCH (pd:ProductDomain)-[:CONTAINS]->(e:Epic)
       -[:CONTAINS]->(f:Feature)
       -[:CONTAINS]->(s:Story)
WHERE pd.code = 'PD-MKT'
RETURN pd, e, f, s
```

### 6.4 查询 Feature 的 Story 和 FP

```cypher
MATCH (f:Feature {code: 'FEAT-MKT-CANVAS-001'})-[:CONTAINS]->(child)
RETURN f, child
```

---

## 7. 约束与索引

### 7.1 唯一约束

```cypher
CREATE CONSTRAINT FOR (pd:ProductDomain) REQUIRE pd.uri IS UNIQUE;
CREATE CONSTRAINT FOR (e:Epic) REQUIRE e.uri IS UNIQUE;
CREATE CONSTRAINT FOR (f:Feature) REQUIRE f.uri IS UNIQUE;
CREATE CONSTRAINT FOR (s:Story) REQUIRE s.uri IS UNIQUE;
CREATE CONSTRAINT FOR (fp:FP) REQUIRE fp.uri IS UNIQUE;
```

### 7.2 索引

```cypher
CREATE INDEX FOR (pd:ProductDomain) ON (pd.code);
CREATE INDEX FOR (e:Epic) ON (e.code);
CREATE INDEX FOR (f:Feature) ON (f.code);
CREATE INDEX FOR (s:Story) ON (s.code);
CREATE INDEX FOR (fp:FP) ON (fp.code);
```

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark