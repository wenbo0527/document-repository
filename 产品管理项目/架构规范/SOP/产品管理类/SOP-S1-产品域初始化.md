# SOP-S1: 产品域初始化

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 草稿

---

## 1. 概述

### 1.1 目标

新建产品域时，初始化完整的产品管理框架，包括文档、数据库、飞书表格。

### 1.2 触发时机

- 新建产品域
- 产品线扩展

### 1.3 输入

- 产品域基本信息（ID、名称、定位）
- 业务范围描述
- 团队成员

### 1.4 输出

- 产品域说明文档
- Epic 说明文档列表
- Neo4j 节点创建
- 飞书多维表格初始化

---

## 2. 处理流程

### 步骤 1: 创建目录结构

```
产品管理项目/
└── PRD/
    └── {产品域名称}/
        ├── 01-产品域说明.md
        ├── 02-EPIC文档/
        │   ├── 01-EPIC-XXX.md
        │   └── 02-EPIC-YYY.md
        └── 03-Feature文档/
            ├── 01-Feature-XXX.md
            └── 02-Feature-YYY.md
```

**操作**：创建目录和空文档

---

### 步骤 2: 创建产品域说明文档

**模板**：`架构规范/模板/02-产品域说明文档模板.md`

**必填字段**：
- 产品域 ID
- 产品域名称
- 英文名
- 产品定位
- 核心价值
- 团队成员

---

### 步骤 3: 创建 Epic 说明文档

**模板**：`架构规范/模板/03-EPIC说明文档.md`

**每个 Epic 需要创建**：
- Epic 说明文档
- 关联的 Feature 说明文档

---

### 步骤 4: 同步到 Neo4j

**Skill 调用**：`product-breakdown`

**操作**：
```bash
# 创建 ProductDomain 节点
CREATE (pd:ProductDomain {
  id: "PD-XX",
  name: "{产品域名称}",
  description: "{描述}",
  created_at: datetime()
})

# 创建 Epic 节点
CREATE (e:Epic {
  id: "EPIC-XX-XXX",
  name: "{Epic名称}",
  product_domain: "PD-XX",
  status: "DRAFT",
  created_at: datetime()
})

# 创建 BELONGS_TO 关系
MATCH (pd:ProductDomain {id: "PD-XX"})
MATCH (e:Epic {id: "EPIC-XX-XXX"})
CREATE (e)-[:BELONGS_TO]->(pd)
```

---

### 步骤 5: 初始化飞书多维表格

**Skill 调用**：`feishu-sync`

**操作**：
1. 创建飞书多维表格
2. 配置字段：
   - Epic ID
   - Feature ID
   - Story ID
   - FP ID
   - 状态
   - 负责人
   - 优先级
   - 完成度

---

## 3. 验收检查清单

- [ ] 目录结构创建完成
- [ ] 产品域说明文档已创建
- [ ] 所有 Epic 说明文档已创建
- [ ] Neo4j 节点已创建
- [ ] 飞书多维表格已初始化
- [ ] 团队成员已配置

---

## 4. 关联 Skill

| Skill | 用途 | 调用时机 |
|:---|:---|:---|
| `product-breakdown` | 产品结构拆解 | 同步到 Neo4j |
| `feishu-sync` | 飞书同步 | 初始化飞书表格 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
