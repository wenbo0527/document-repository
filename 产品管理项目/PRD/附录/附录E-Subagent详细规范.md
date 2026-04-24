# 产品管理系统设计方案 v1.0 - 附录E：Subagent 详细规范

> **版本**: v1.0
> **日期**: 2026-04-18
> **作者**: Tony Stark
> **来源**: 飞书文档

---

## E.1 Subagent 标准模板

### E.1.1 基础信息

| 属性 | 值 |
|:---|:---|
| 名称 | [Agent中文名] |
| 英文名 | [AgentEnglishName] |
| 层级 | 产品/技术/执行上下文层 |
| 版本 | v1.0 |
| 作者 | Tony Stark |
| 创建日期 | 2026-04-18 |

### E.1.2 输入输出规范

| 类型 | 描述 |
|:---|:---|
| 输入 | [输入内容描述] |
| 输出 | [输出内容描述] |
| Token 消耗 | ~[X] tokens |

### E.1.3 Prompt 模板

```
# [Agent名称]

## 角色定义
你是一个专业的[领域]专家，负责[核心职责]。

## 输入格式
[输入内容示例]

## 处理流程
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 输出格式
JSON格式输出，包含 status、data、message 字段

## 注意事项
- [注意事项1]
- [注意事项2]

## 错误处理
- [错误场景1] → [处理方式]
```

---

## E.2 九个 Subagent 详细规范

### E.2.1 产品上下文层

#### 1. 需求理解 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 需求理解 Agent |
| 英文名 | ProductContextAgent |
| 层级 | 产品上下文层 |
| Token 消耗 | ~800 tokens |

**职责**：
1. 理解需求背景和目标
2. 提取关键实体和关系
3. 识别相关产品域
4. 生成结构化需求文档

**输入**：原始需求（飞书消息/文档/口头描述）
**输出**：结构化需求文档（JSON）

```json
{
  "requirement_id": "REQ-YYYYMMDD-XXX",
  "title": "需求标题",
  "background": "需求背景",
  "实体": ["实体1", "实体2"],
  "操作": ["操作1", "操作2"],
  "相关产品域": ["PD-MKT"],
  "优先级": "P0/P1/P2"
}
```

#### 2. 产品分析 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 产品分析 Agent |
| 英文名 | ProductAnalysisAgent |
| 层级 | 产品上下文层 |
| Token 消耗 | ~1,200 tokens |

**职责**：
1. 分析需求影响范围
2. 识别依赖关系
3. 评估风险和优先级
4. 提出建议

**输入**：结构化需求文档
**输出**：产品分析报告

```json
{
  "requirement_id": "REQ-XXX",
  "impact_analysis": {
    "产品域": ["PD-MKT"],
    "影响程度": "高/中/低"
  },
  "risks": [{"risk": "风险描述", "level": "高/中/低"}],
  "priority_recommendation": "P0/P1/P2"
}
```

#### 3. PRD 生成 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | PRD 生成 Agent |
| 英文名 | PRDGeneratorAgent |
| 层级 | 产品上下文层 |
| Token 消耗 | ~1,500 tokens |

**职责**：
1. 生成 Epic 结构
2. 拆解 Feature 列表
3. 拆解 Story 列表
4. 定义验收标准

**输入**：产品分析报告
**输出**：PRD 文档（Epic/Feature/Story 结构）

---

### E.2.2 技术上下文层

#### 4. 代码结构扫描 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 代码结构扫描 Agent |
| 英文名 | CodeScannerAgent |
| 层级 | 技术上下文层 |
| Token 消耗 | ~600 tokens |

**职责**：
1. 扫描代码仓库结构
2. 识别相关代码文件
3. 分析技术依赖

**输入**：Epic/Feature 描述
**输出**：代码路径清单、技术依赖分析

#### 5. 技术拆解 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 技术拆解 Agent |
| 英文名 | TechBreakdownAgent |
| 层级 | 技术上下文层 |
| Token 消耗 | ~1,000 tokens |

**职责**：
1. 将 Feature 拆解为 FP
2. 定义接口方案
3. 规划数据库变更

**输入**：Epic/Feature + 代码结构
**输出**：技术拆解结果（FP、接口、数据库）

#### 6. 技术评估 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 技术评估 Agent |
| 英文名 | TechAssessmentAgent |
| 层级 | 技术上下文层 |
| Token 消耗 | ~800 tokens |

**职责**：
1. 评估技术可行性
2. 估算开发工时
3. 识别技术风险

**输入**：技术拆解结果
**输出**：技术可行性报告

```json
{
  "feasibility": "可行/有条件可行/不可行",
  "estimated_hours": 40,
  "risks": [{"risk": "风险", "level": "高/中/低"}],
  "approval_status": "approved/need_revision/rejected"
}
```

---

### E.2.3 执行上下文层

#### 7. 数据同步 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 数据同步 Agent |
| 英文名 | DataSyncAgent |
| 层级 | 执行上下文层 |
| Token 消耗 | ~400 tokens |

**职责**：
1. 同步状态到 Neo4j
2. 更新飞书多维表格
3. 维护数据一致性

**输入**：Epic/Story 状态变更
**输出**：Neo4j 更新 + 飞书同步结果

```json
{
  "sync_result": "success/partial/failed",
  "neo4j_updated": true,
  "feishu_updated": true,
  "errors": []
}
```

#### 8. 状态跟踪 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 状态跟踪 Agent |
| 英文名 | ProgressTrackerAgent |
| 层级 | 执行上下文层 |
| Token 消耗 | ~500 tokens |

**职责**：
1. 跟踪开发进度
2. 生成进度报告
3. 预警延期风险

**输入**：Epic/Story 列表
**输出**：进度报告、预警信息

```json
{
  "progress": {
    "total": 20,
    "completed": 10,
    "completion_rate": "50%"
  },
  "risks": ["延期风险1"],
  "suggestions": ["改进建议1"]
}
```

#### 9. 周报生成 Agent

| 属性 | 值 |
|:---|:---|
| 名称 | 周报生成 Agent |
| 英文名 | WeeklyReportAgent |
| 层级 | 执行上下文层 |
| Token 消耗 | ~600 tokens |

**职责**：
1. 汇总本周完成工作
2. 生成周报文档
3. 同步到飞书

**输入**：本周工作数据
**输出**：周报文档

---

## E.3 Agent 协作示例

### 标准流程

```
用户输入 → 需求理解 → 产品分析 → PRD生成
                              ↓
                         代码结构扫描
                              ↓
                         技术拆解 → 技术评估
                              ↓
                         数据同步 → 状态跟踪 → 周报生成
```

### 简化流程（快速路径）

```
用户输入 → 需求理解 → PRD生成 → 技术评估 → 数据同步
```

---

**文档版本**: v1.0
**最后更新**: 2026-04-18
**维护者**: Tony Stark