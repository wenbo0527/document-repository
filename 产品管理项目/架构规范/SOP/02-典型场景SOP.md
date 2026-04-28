# 产品管理典型场景 SOP v1.0

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 正式发布

---

## 1. 概述

本文档梳理产品管理系统的典型场景，每个场景定义其目标、流程、输入输出和关联 Skill。

---

## 2. 典型场景总览

| 场景 ID | 场景名称 | 触发时机 | 关联 Skill |
|:---:|:---|:---|:---|
| S1 | **产品域初始化** | 新建产品域时 | product-breakdown, requirement-understanding |
| S2 | **产品域-EPIC 重建** | 补齐缺失文档、对齐数据库、对齐代码 | neo4j-product-domain-repair, requirement-breakdown |
| S3 | **需求分析** | 收到新业务需求时 | requirement-understanding, requirement-supplement |
| S4 | **需求拆解** | 需求确认后 | requirement-breakdown, prd-generation |
| S5 | **PRD 生成与开发指导** | 需求拆解完成后 | prd-generation, spec-driven, task-planning |
| S6 | **Epic 交付开发** | PRD 确认后 | tony-zhongli-collaboration, git-workflow |
| S7 | **文档维护** | 日常维护 | wiki-maintenance, feishu-sync, health-check |

---

## 3. 场景详解

### S1: 产品域初始化

**目标**：新建产品域时，初始化完整的产品管理框架

**流程**：
```
1. 创建产品域目录结构
2. 初始化产品域说明文档
3. 创建 Epic 说明文档
4. 创建 Feature 说明文档
5. 同步到 Neo4j
6. 初始化飞书多维表格
```

**输入**：
- 产品域基本信息（ID、名称、定位）
- 业务范围描述

**输出**：
- 产品域说明文档
- Epic 说明文档列表
- Neo4j 节点创建
- 飞书多维表格初始化

**关联 Skill**：
- `product-breakdown` - 产品域结构拆解
- `requirement-understanding` - 需求理解

**状态**：待补充

---

### S2: 产品域-EPIC 重建

**目标**：补齐缺失文档，对齐数据库（Neo4j），对齐代码库

**触发时机**：
- 发现文档缺失
- Neo4j 数据与实际不符
- 代码库与文档不一致

**流程**：
```
1. 健康检查（发现问题）
   └─→ health-check

2. 诊断问题
   ├─→ 缺失文档 → 创建/补齐
   ├─→ Neo4j 不一致 → 修复图数据
   └─→ 代码不一致 → 记录差异

3. 补齐文档
   ├─→ 产品域说明文档
   ├─→ EPIC 说明文档
   ├─→ Feature 说明文档
   └─→ PRD 文档

4. 对齐 Neo4j
   └─→ neo4j-product-domain-repair

5. 同步到飞书
   └─→ feishu-sync
```

**输入**：
- 产品域 ID
- 待修复项清单

**输出**：
- 补齐的文档
- 更新的 Neo4j 数据
- 问题修复报告

**关联 Skill**：
- `health-check` - 健康检查
- `neo4j-product-domain-repair` - Neo4j 数据修复
- `requirement-breakdown` - 需求拆解
- `feishu-sync` - 飞书同步

**文档补齐清单**：
| 文档类型 | 状态检查 | 补齐操作 |
|:---|:---:|:---|
| 产品域说明文档 | 检查是否存在、版本 | 创建/更新 |
| EPIC 说明文档 | 检查每个 EPIC 是否有文档 | 创建/更新 |
| Feature 说明文档 | 检查每个 Feature 是否有文档 | 创建/更新 |
| PRD 文档 | 检查每个 EPIC 是否有 PRD | 创建/更新 |
| FP 清单 | 检查 FP 数量、状态 | 创建/更新 |

---

### S3: 需求分析

**目标**：理解业务需求，填充需求理解的 9 项信息

**触发时机**：
- 收到新业务需求
- 产品经理提出新想法

**流程**：
```
1. 需求接收
   └─→ 原始需求文档/描述

2. 需求理解
   └─→ requirement-understanding
       └─→ 填充 9 项信息

3. 需求补充
   └─→ requirement-supplement
       └─→ 用户场景、功能边界、验收标准
```

**输入**：
- 原始需求（文字描述、会议纪要等）

**输出**：
- 需求理解报告（9项信息填充）
- 需求补充文档

**关联 Skill**：
- `requirement-understanding` - 需求理解
- `requirement-supplement` - 需求补充

**验收的 9 项信息**：
1. 需求类型
2. 需求背景
3. 用户群体
4. 用户场景
5. 功能范围
6. 非功能需求
7. 验收标准
8. 优先级
9. 依赖关系

---

### S4: 需求拆解

**目标**：将需求拆解为 Epic → Feature → Story → FP

**触发时机**：
- S3 需求分析完成
- 需求确认

**流程**：
```
1. Epic 拆解
   └─→ 识别 Epic 边界

2. Feature 拆解
   └─→ 每个 Epic 下的 Feature

3. Story 拆解
   └─→ 每个 Feature 下的用户故事

4. FP 拆解
   └─→ 每个 Story 下的功能点

5. 同步到 Neo4j
   └─→ requirement-breakdown
```

**输出**：
- Epic 列表
- Feature 列表
- Story 列表
- FP 列表
- Neo4j 节点创建

**关联 Skill**：
- `requirement-breakdown` - 需求拆解到 Neo4j
- `product-breakdown` - 产品结构拆解

**拆解规范**：
| 层级 | 数量建议 | 说明 |
|:---|:---:|:---|
| Epic | 1-5 个 | 按业务领域划分 |
| Feature | 3-10 个/Epic | 按功能模块划分 |
| Story | 3-10 个/Feature | 按用户故事划分 |
| FP | 5-15 个/Story | 按功能点划分 |

---

### S5: PRD 生成与开发指导

**目标**：生成符合 v5.0 规范的 PRD，用于指导开发

**触发时机**：
- S4 需求拆解完成
- Epic/Feature/Story 确认

**流程**：
```
1. PRD 生成
   └─→ prd-generation
       ├─→ 元数据填充
       ├─→ Feature 清单生成
       ├─→ FP 清单生成
       ├─→ 菜单映射
       └─→ 审批流接入点

2. PRD 审核
   └─→ PM 审核确认

3. Spec 生成
   └─→ spec-driven
       └─→ 将 PRD 转化为开发 Spec

4. 任务规划
   └─→ task-planning
       └─→ 拆解为可执行任务
```

**输出**：
- PRD v5.0 文档
- Spec 文档
- 任务列表

**关联 Skill**：
- `prd-generation` - PRD 生成
- `spec-driven` - 规范驱动开发
- `task-planning` - 任务规划

---

### S6: Epic 交付开发

**目标**：将 Epic 交付给开发团队，跟踪开发进度

**触发时机**：
- PRD 审核通过
- 需要启动开发

**流程**：
```
1. Epic 交付
   └─→ Tony → 钟离（IF-001）
       └─→ EPIC 文档、技术要求

2. 技术评估
   └─→ 钟离评估（IF-002）
       └─→ 可行性报告、工时评估

3. 评审与确认
   └─→ 通过/修订后重提

4. 开发阶段
   └─→ 钟离开发
       └─→ 状态: IN_PROGRESS

5. Story 验收
   └─→ Tony 验收（IF-003）
       └─→ 功能/操作/数据/交互 4项验收

6. Epic 完成
   └─→ 钟离确认（IF-004）
       └─→ 状态: COMPLETED
```

**接口定义**：
| 接口 | 方向 | 内容 | 状态 |
|:---|:---|:---|:---|
| IF-001 | Tony → 钟离 | EPIC 文档、技术要求 | PENDING |
| IF-002 | 钟离 → Tony | 可行性报告、工时 | APPROVED/NEED_REVISION |
| IF-003 | Tony → 钟离 | Story 验收 | ACCEPT/PARTIAL/REJECT |
| IF-004 | 钟离 → Tony | 完成确认 | COMPLETED |

**关联 Skill**：
- `tony-zhongli-collaboration` - Tony-钟离协作
- `git-workflow` - Git 工作流
- `code-review` - 代码审查

---

### S7: 文档维护

**目标**：日常维护文档、Neo4j、飞书的同步一致性

**触发时机**：
- 定期维护（建议每周）
- 发现数据不一致

**流程**：
```
1. 健康检查
   └─→ health-check
       ├─→ Neo4j 检查
       ├─→ 飞书检查
       └─→ Wiki 检查

2. 问题修复
   ├─→ 文档缺失 → 补齐
   ├─→ 数据不一致 → 同步
   └─→ 版本过期 → 更新

3. Wiki 维护
   └─→ wiki-maintenance
       └─→ 知识库健康检查

4. 飞书同步
   └─→ feishu-sync
       └─→ PRD 定稿后同步
```

**检查清单**：
| 检查项 | 频率 | 负责人 |
|:---|:---:|:---|
| Neo4j 数据一致性 | 每周 | Tony |
| 飞书文档同步 | 实时 | Tony |
| Wiki 知识库 | 每周 | Tony |
| 模板版本更新 | 每月 | Tony |

**关联 Skill**：
- `health-check` - 健康检查
- `wiki-maintenance` - Wiki 维护
- `feishu-sync` - 飞书同步

---

## 4. 场景关系图

```
S3 需求分析
    │
    ▼
S4 需求拆解 ───────────────────────────────────┐
    │                                            │
    ▼                                            │
S5 PRD生成 ──────────────────────────────────────┤
    │                                            │
    ▼                                            │
S6 Epic交付开发 ───────────────────────────────┤
                                                 │
                    ┌───────────────────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  S7 文档维护   │
            └───────────────┘
                    ▲
                    │
S2 产品域-EPIC重建 ─┘
                    ▲
                    │
S1 产品域初始化 ────┘
```

---

## 5. 触发条件速查

| 场景 | 触发条件 | 优先级 |
|:---|:---|:---:|
| S1 产品域初始化 | 新建产品域 | P0 |
| S2 产品域-EPIC重建 | 文档缺失、数据不一致 | P0 |
| S3 需求分析 | 收到新需求 | P0 |
| S4 需求拆解 | S3 完成 | P0 |
| S5 PRD生成 | S4 完成 | P0 |
| S6 Epic交付开发 | PRD 审核通过 | P0 |
| S7 文档维护 | 定期/发现问题 | P1 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
