# Product Breakdown Skill - 基于本体论的智能需求拆解

## 概述

基于产品管理本体论 (Ontology) 进行智能需求拆解，将用户需求转换为规范的 Epic → Feature → Story 结构。

**适用场景**: 当用户需要将原始需求拆解为产品结构时使用。

**触发词**: "拆解"、"分解"、"breakdown"、"创建需求"

---

## 本体论约束

### 节点类型

| 层级 | 节点类型 | 说明 | ID 格式 |
|:---:|:---|:---|:---|
| L0 | Vision | 产品愿景 | - |
| L1 | Goal | 目标 | `GOAL-{code}` |
| L2 | OKR | 关键结果 | `OKR-{code}` |
| L3 | Project | 项目 | `PROJ-{nnn}` |
| L4 | ProductDomain | 产品域 | `PD-{code}` |
| L5 | Epic | 史诗 | `EPIC-{域}-{模块}` |
| L6 | Feature | 特性 | `FEAT-{域}-{Epic}-{特性}` |
| L7 | Story | 用户故事 | `STORY-{域}-{Epic}-{特性}-{nnn}` |

### 关系类型

| 关系 | 说明 | 示例 |
|:---|:---|:---|
| `CONTAINS` | 包含关系 | `Epic CONTAINS Feature` |
| `PART_OF` | 归属关系 | `Feature PART_OF Epic` |
| `DEPENDS_ON` | 依赖关系 | `Feature DEPENDS_ON Feature` |
| `SUPPORTS` | 支持关系 | `Epic SUPPORTS OKR` |

### 属性规范

#### Epic 属性
```yaml
uri: "Epic:EPIC-{域}-{模块}"
label: string           # 显示名称
localName: string       # 本地名称
description: string     # 详细描述
status: planning|active|completed|archived
priority: P0|P1|P2      # P0=核心 P1=重要 P2=辅助
productDomain: string   # 所属产品域 URI
acceptCriteria: [string] # 验收标准
```

#### Feature 属性
```yaml
uri: "Feature:FEAT-{域}-{Epic}-{特性}"
label: string
status: planning|in_progress|completed|archived
priority: P0|P1|P2
description: string
acceptanceCriteria: [string]
epic: string           # 所属 Epic URI
```

#### Story 属性
```yaml
uri: "Story:STORY-{域}-{Epic}-{特性}-{nnn}"
label: string
title: string           # 用户故事标题 "作为...我希望...以便..."
status: backlog|todo|in_progress|done|archived
storyPoints: number    # 故事点
acceptanceCriteria: [string]
feature: string         # 所属 Feature URI
assignee: string        # 负责人
```

---

## 拆解流程

### Step 1: 解析需求意图

```
用户输入: "我希望有一个用户中心，包含注册登录、个人资料、账号安全"
```

1. 识别产品域 (ProductDomain)
2. 识别功能模块 (Epic)
3. 识别核心功能 (Feature)
4. 拆解用户故事 (Story)

### Step 2: 生成 ID

遵循 ID 命名规范:

```
Epic:   EPIC-{产品域简称}-{模块简称}
        例: EPIC-COM-USER (数据社区-用户中心)

Feature: FEAT-{产品域}-{Epic简称}-{特性}
        例: FEAT-COM-USER-AUTH (数据社区-用户-认证)

Story:  STORY-{产品域}-{Epic简称}-{特性简称}-{序号}
        例: STORY-COM-USER-AUTH-REG-001
```

### Step 3: 构建图结构

```
ProductDomain:PD-COM
       │
       └── CONTAINS ──→ Epic:EPIC-COM-USER
                            │
                            ├── CONTAINS ──→ Feature:FEAT-COM-USER-AUTH
                            │                      │
                            │                      └── CONTAINS ──→ Story:STORY-COM-USER-AUTH-REG-001
                            │                                    └──→ Story:STORY-COM-USER-AUTH-LOGIN-001
                            │
                            ├── CONTAINS ──→ Feature:FEAT-COM-USER-PROFILE
                            │                      │
                            │                      └── CONTAINS ──→ ...
                            │
                            └── CONTAINS ──→ Feature:FEAT-COM-USER-SECURITY
                                           │
                                           └── CONTAINS ──→ ...
```

### Step 4: 输出确认

输出 Markdown 格式的拆解结果，包含:
- Epic 详情
- Feature 列表
- Story 列表
- 完整的关系结构

**在用户确认前不写入数据库。**

### Step 5: 用户确认后写入

用户确认后，执行 Cypher 写入:

```cypher
// 创建 Epic
CREATE (e:Epic {
  uri: $epicUri,
  label: $label,
  description: $description,
  status: 'planning',
  priority: $priority,
  createdAt: datetime()
})

// 创建关系
MATCH (d:ProductDomain {uri: $domainUri})
CREATE (d)-[:CONTAINS]->(e)

// 创建 Feature 和 Story (类似结构)
...
```

---

## 输出格式

### 拆解结果预览

```markdown
## 📦 Epic 拆解结果

### Epic
| 属性 | 值 |
|:---|:---|
| URI | Epic:EPIC-COM-USER |
| 名称 | 用户中心 |
| 产品域 | PD-COM (数据社区) |
| 优先级 | P0 |
| 描述 | 用户中心系统... |

### Feature 列表
| Feature | 名称 | 优先级 | Story 数 |
|:---|:---|:---:|:---:|
| FEAT-COM-USER-AUTH | 用户认证 | P0 | 3 |
| FEAT-COM-USER-PROFILE | 个人资料 | P1 | 2 |
| FEAT-COM-USER-SECURITY | 账号安全 | P1 | 3 |

### Story 列表
| Story | 标题 | 验收标准 |
|:---|:---|:---|
| STORY-COM-USER-AUTH-REG-001 | 注册账号 | 1. 填写表单... |
| STORY-COM-USER-AUTH-LOGIN-001 | 登录账号 | 1. 输入账号... |
```

### Neo4j 预览 (关系图)

```
PD-COM
  └── [CONTAINS] → EPIC-COM-USER (P0)
                      ├── [CONTAINS] → FEAT-COM-USER-AUTH (P0)
                      │                 ├── STORY-COM-USER-AUTH-REG-001
                      │                 ├── STORY-COM-USER-AUTH-LOGIN-001
                      │                 └── STORY-COM-USER-AUTH-PWD-001
                      ├── [CONTAINS] → FEAT-COM-USER-PROFILE (P1)
                      │                 ├── STORY-COM-USER-PROFILE-VIEW-001
                      │                 └── STORY-COM-USER-PROFILE-EDIT-001
                      └── [CONTAINS] → FEAT-COM-USER-SECURITY (P1)
                                        ├── STORY-COM-USER-SEC-CHG-001
                                        ├── STORY-COM-USER-SEC-BIND-001
                                        └── STORY-COM-USER-SEC-TFA-001
```

---

## 技术实现

### 依赖工具

- `exec` - 执行 Python/Cypher
- `read` / `write` - 文件读写
- Neo4j HTTP API - 图数据库操作

### Neo4j 连接

```python
NEO4J_URL = "http://localhost:7474/db/neo4j/tx/commit"
NEO4J_AUTH = ("neo4j", "password123")
```

### 拆解器类

```python
class OntologyBreakdown:
    """基于本体论的拆解器"""
    
    PRODUCT_DOMAINS = {
        "COM": "ProductDomain:PD-COM",  # 数据社区
        "RISK": "ProductDomain:PD-RISK", # 数字风险
        "DEX": "ProductDomain:PD-DEX",   # 数据探索
        "DFD": "ProductDomain:PD-DFD",   # 数据发现
        "DMT": "ProductDomain:PD-DMT",  # 数据管理
        "MKT": "ProductDomain:PD-MKT",   # 数字营销
    }
    
    def breakdown(self, requirement: str, domain: str = "COM") -> BreakdownPlan:
        """执行拆解"""
        ...
    
    def preview(self, plan: BreakdownPlan) -> str:
        """输出预览"""
        ...
    
    def to_cypher(self, plan: BreakdownPlan) -> List[str]:
        """生成 Cypher 语句"""
        ...
    
    def execute(self, plan: BreakdownPlan) -> Dict:
        """执行写入"""
        ...
```

---

## 使用示例

### 用户对话

```
用户: 帮我拆解用户中心需求
Tony: 请描述你的需求...
用户: 我希望有注册登录、个人资料、账号安全功能
Tony: [执行拆解，输出预览]
Tony: 确认后我将写入数据库，输入"确认写入"即可
用户: 确认写入
Tony: [写入 Neo4j，返回结果]
```

### 确认流程

1. **拆解**: 分析需求 → 生成结构
2. **预览**: 显示 Markdown + 图结构
3. **确认**: 用户确认
4. **写入**: 执行 Cypher，存入数据库

---

## 约束规则

1. **ID 唯一性**: 创建前检查 URI 是否已存在
2. **层级完整**: Epic → Feature → Story 必须完整
3. **关系方向**: CONTAINS 从父指向子
4. **状态初始化**: 新建实体状态为 `planning` / `backlog`
5. **确认写入**: 不自动写入，必须用户确认

---

*Version: 1.0 | For: Tony Stark | Based: Product Management Ontology v3.0*
