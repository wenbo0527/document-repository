# SOP-S2: 产品域-EPIC重建

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 正式发布

---

## 1. 概述

### 1.1 目标

补齐缺失文档，对齐数据库（Neo4j），对齐代码库

### 1.2 触发时机

- 发现文档缺失
- Neo4j 数据与实际不符
- 代码库与文档不一致
- 健康检查发现问题

### 1.3 输入

- 产品域 ID
- 待修复项清单（健康检查报告）

### 1.4 输出

- 补齐的文档
- 更新的 Neo4j 数据
- 问题修复报告

---

## 2. 处理流程

### 步骤 1: 健康检查（发现问题）

**Skill 调用**：`health-check`

**操作**：
```bash
# 执行健康检查
python3 health_check.py --domain PD-XX
```

**检查项**：
| 检查项 | 检查内容 |
|:---|:---|
| 文档完整性 | 产品域说明、EPIC说明、Feature说明、PRD |
| Neo4j 一致性 | 节点数量、关系完整性 |
| 飞书同步 | 文档同步状态 |
| 版本一致性 | 模板版本、文档版本 |

**输出**：问题清单

---

### 步骤 2: 诊断问题类型

**问题分类**：

| 类型 | 说明 | 处理方式 |
|:---|:---|:---|
| 文档缺失 | 缺少某类文档 | 创建/补齐 |
| 数据不一致 | Neo4j 与文档不符 | 修复数据 |
| 版本过期 | 模板/文档版本过旧 | 更新版本 |
| 关系缺失 | 节点关系不完整 | 补充关系 |

---

### 步骤 3: 补齐文档

**Skill 调用**：`requirement-breakdown`

**文档补齐清单**：

| 文档类型 | 检查方法 | 补齐操作 |
|:---|:---|:---|
| 产品域说明文档 | 检查是否存在 | 使用模板创建 |
| EPIC 说明文档 | 遍历 Neo4j Epic 节点 | 使用模板创建 |
| Feature 说明文档 | 遍历 Neo4j Feature 节点 | 使用模板创建 |
| PRD 文档 | 检查每个 EPIC 是否有 PRD | 使用 PRD 模板创建 |

**操作示例**：
```bash
# 列出缺失文档
python3 check_missing_docs.py --domain PD-XX --type epic

# 批量创建缺失文档
python3 create_missing_docs.py --domain PD-XX --type epic
```

---

### 步骤 4: 修复 Neo4j 数据

**Skill 调用**：`neo4j-product-domain-repair`

**操作**：
```bash
# 检查 Neo4j 数据
python3 neo4j_check.py --domain PD-XX

# 修复数据
python3 neo4j_repair.py --domain PD-XX --fix
```

**修复内容**：
- 缺失的节点创建
- 错误的关系修复
- id 重复问题修复
- NULL id 问题修复

---

### 步骤 5: 同步到飞书

**Skill 调用**：`feishu-sync`

**操作**：
```bash
# 同步 PRD 到飞书
python3 feishu_sync.py --domain PD-XX --type prd

# 同步状态到飞书
python3 feishu_sync.py --domain PD-XX --type status
```

---

## 3. 验收检查清单

- [ ] 健康检查完成
- [ ] 问题清单已确认
- [ ] 缺失文档已补齐
- [ ] Neo4j 数据已修复
- [ ] 飞书已同步
- [ ] 修复报告已生成

---

## 4. 关联 Skill

| Skill | 用途 | 调用时机 |
|:---|:---|:---|
| `health-check` | 健康检查 | 步骤1 发现问题 |
| `requirement-breakdown` | 需求拆解/补齐文档 | 步骤3 补齐文档 |
| `neo4j-product-domain-repair` | Neo4j 数据修复 | 步骤4 修复数据 |
| `feishu-sync` | 飞书同步 | 步骤5 同步飞书 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
