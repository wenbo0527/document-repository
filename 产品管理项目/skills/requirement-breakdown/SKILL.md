---
name: requirement-breakdown
description: 需求拆解到 Neo4j 图数据库的完整流程。具体触发场景：(1) 用户提出新需求；(2) 用户提到需求拆解、存量整理、产品结构化；(3) 需要创建或更新 Epic/Feature/Story；(4) 需要写入飞书多维表格；(5) 需要执行 health_check 验证数据质量；(6) 处理 SOP 文档时；(7) 查询 Neo4j 中的产品知识时。

---

# Requirement Breakdown Skill

存量需求拆解到 Neo4j 的标准流程。适用于：整理历史需求、建立产品结构、同步飞书确认表、执行数据质量验证。

---

## ⚠️ 核心原则（血泪教训）

**每次拆解必须先查 Neo4j 存量，再对比文档补充缺口。绝不能闭门造车。**

存量数据是基准，文档是补充来源，Demo 代码是验证手段。三者对照后才能得出真实缺口。

---

## 📦 PRD补全流程（新增，适用于存量PRD补全）

### 触发场景
- 用户要求生成某个产品域的PRD文档
- 产品域已有Epic/Feature但没有详细PRD文档
- 需要验证FP与代码的对应关系

### 两层PRD架构

```
┌─────────────────────────────────────────────────────────────┐
│                    PRD 两层架构                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────┐    ┌─────────────────────────┐  │
│  │    Master PRD        │    │   Feature级详情           │  │
│  │    (产品域视角)      │    │   (Epic+Feature追溯)      │  │
│  │                      │    │                          │  │
│  │  - 产品域概述        │    │  - FP关联表              │  │
│  │  - Epic总览          │    │  - 三源追溯              │  │
│  │  - 追溯总览          │    │  - 功能验收标准          │  │
│  │  - 缺口清单          │    │  - 缺口清单              │  │
│  └─────────────────────┘    └─────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 1: 准备阶段

```bash
# 1.1 查询Neo4j获取产品域结构
python3 << 'EOF'
from neo4j import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'password123'))
with driver.session() as tx:
    result = tx.run('''
        MATCH (pd:ProductDomain {code: 'PD-XXX'})
        OPTIONAL MATCH (pd)-[:CONTAINS]->(e:Epic)
        OPTIONAL MATCH (e)-[:CONTAINS]->(f:Feature)
        OPTIONAL MATCH (f)-[:CONTAINS]->(fp:FP)
        RETURN e.name AS epic_name, e.uri AS epic_uri,
               f.name AS feature_name, f.uri AS feature_uri,
               count(DISTINCT fp) AS fp_count
        ORDER BY e.name, f.name
    ''')
    for record in result:
        print(f"Epic: {record['epic_name']}")
        print(f"  Feature: {record['feature_name']} ({record['fp_count']} FP)")
driver.close()
EOF

# 1.2 与技术团队确认代码仓库结构
# 1.3 确认需求文档存放位置
```

### Phase 2: 验证阶段

```bash
# 2.1 扫描代码仓库验证codePath
# 代码路径格式: data_community/src/pages/discovery/

# 2.2 更新Neo4j中的codePath
python3 << 'EOF'
from neo4j import GraphDatabase

driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'password123'))

# 批量更新FP的codePath
code_paths = {
    'FP-DFD-ASSET-DETAIL-001': 'data_community/src/pages/discovery/data-map/TableDetailPage.vue',
    # ... 更多FP映射
}

with driver.session() as tx:
    for fp_uri, code_path in code_paths.items():
        tx.run('''
            MATCH (fp:FP {uri: $uri})
            SET fp.code_path = $code_path,
                fp.path_status = 'verified',
                fp.last_verified = date()
        ''', uri=fp_uri, code_path=code_path)

driver.close()
EOF
```

### Phase 3: 生成阶段

```bash
# 3.1 生成Master PRD
# 路径: PRD/EPIC文档/

# 3.2 生成Feature级详情
# 路径: PRD/EPIC文档/{产品域}/{Epic}/

# 3.3 补充Story级拆分
```

### Phase 4: 验证阶段

```bash
# 4.1 按Checklist检查文档完整性
# 路径: SOP/SOP-Checklist-.md

# 4.2 生成缺口清单
# 4.3 补充缺失内容
# 4.4 最终验收
```

---

## 需求入口流程（Step 0：先收集信息，再决定是否进入拆解）

**触发条件**：用户提出新需求，且需求信息不足以判断 Epic/Feature/Story 时。

### 收集清单（9 项，缺一不可；缺少的内容必须通过对话追问补齐，禁止跳过）

| # | 字段 | 说明 | 追问示例 |
|:---:|:---|:---|:---|
| 1 | **谁提出** | 需求发起人/业务方 | "这个需求是谁提的？" |
| 2 | **何时上线** | 目标上线时间/截止日期 | "希望什么时候上线？" |
| 3 | **使用场景** | 具体的使用环境和操作步骤 | "用户在哪里、怎么用这个功能？" |
| 4 | **核心诉求** | 用户真正想解决的问题 | "做这个功能，最想达成什么？" |
| 5 | **当前痛点** | 现有流程/系统的具体问题 | "现在哪里不方便/有问题？" |
| 6 | **使用频率/范围** | 用户规模、触发频率、数据量级 | "多少人用？每天多少量？" |
| 7 | **主要用户** | 角色/部门/使用对象 | "谁会用这个功能？运营？销售？" |
| 8 | **关注指标** | 成功标准/衡量指标/KPI | "怎么衡量这个功能做得好不好？" |
| 9 | **关联已有功能** | 是否复用/扩展现有系统 | "这个功能和现有的XX功能有什么关系？" |

### 决策规则

```
新需求进入对话
    ↓
按 9 项清单逐一收集
    ↓
发现缺失项 → 立即追问，禁止跳到 Step 1-8
    ↓
9 项全部收集完毕 → 输出【需求概要】卡片
    ↓
才允许进入【8步拆解流程】
```

### 需求概要模板（9项填完后输出）

```
## 需求概要
- **提出方**：（已确认）
- **目标上线**：（已确认）
- **使用场景**：（已确认）
- **核心诉求**：（已确认）
- **当前痛点**：（已确认）
- **使用频率/范围**：（已确认）
- **主要用户**：（已确认）
- **关注指标**：（已确认）
- **关联功能**：（已确认）
```

### 模板使用规范
- 9 项中任何一项为"（待确认）"时，禁止进入 Step 1-8
- 每次对话开始时，检查是否有未完成的需求概要，如有则继续追问
- 需求概要跟随整个流程，在 Step 6 写入飞书确认表时作为备注附件

---

## 完整流程（8步，适用于存量补充）

```
Step 0: 需求入口（收集 9 项信息）← 当前优先级最高
Step 1: 读需求文档（产品说明文档 / PRD）
Step 2: 查 Neo4j 存量（Epic → Feature → Story，确认已有内容）
Step 3: 扫描 Demo 代码路径（找到实现组件，验证功能覆盖）
Step 4: 对比分析（存量 vs 文档 vs Demo，找出真实缺口）
Step 5: 结构化拆解（存量不动，仅补充缺失 Story）
Step 6: 写入飞书确认表（重建表结构，对齐客户360格式）
Step 7: 用户审核 → Neo4j 写入
Step 8: health_check 验证
```

## Step 1: 读需求文档

```bash
# 文档路径
/System/Volumes/Data/Users/wenbo/Documents/文档仓库/产品管理项目/PRD/
```

文档读完后，明确：
- 几个功能模块
- 每个模块的核心能力
- 技术实现要求

## Step 2: 查 Neo4j 存量（必须先做）

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password123"))

with driver.session() as tx:
    result = tx.run("""
        MATCH (e:Epic {uri: 'Epic:EPIC-XXX'})
        OPTIONAL MATCH (e)-[:CONTAINS]->(f:Feature)
        OPTIONAL MATCH (f)-[:CONTAINS]->(s:Story)
        RETURN f.uri as feature_uri, f.label as feature_label,
               s.uri as story_uri, s.label as story_label,
               s.priority, s.status
        ORDER BY f.uri, s.uri
    """)
    # 整理输出：每个 Feature 有几条 Story，哪些 Feature 为空
```

**输出格式**：
```
Epic: EPIC-XXX（名称）
Feature 总数: N
Story 总数: M

【Feature】FEAT-XXX（名称）
  Story 数: K
    - STORY-XXX | 名称 | 优先级 | 状态
  (无 Story) ← 重点缺口
```

## Step 3: 扫描 Demo 代码

```bash
# 项目路径
/Users/wenbo/Documents/project/data_community/src/

# 搜索相关 Vue 组件
find /Users/wenbo/Documents/project/data_community/src -type f -name "*.vue" \
  | grep -i "关键词"
```

**Demo 作用**：验证功能是否有前端实现。Demo 存在 ≠ 功能已上线，仅作为 Story 的"参考路径"备注。

## Step 4: 对比分析（关键决策点）

制作对照表：

| 文档功能模块 | 存量 Feature | Demo 路径 | 存量 Story | 缺口 |
|:---|:---|:---|:---:|:---|
| 标签系统 | FEAT-XXX | tag-system/ | 0 | ❌ 无 Story |

**拆解原则**：
- 存量 Story 不动（已完成/开发中/待规划均保持原样）
- 只补充**文档有功能描述但 Neo4j 完全没有 Story** 的 Feature
- Story ID 基于存量命名规范推断，不能凭空捏造

## Step 5: 结构化拆解

**存量 Story 保持不动，仅补充缺失 Story**。

新增 Story 命名规范（基于存量数据）：
```
STORY-{域}-{Feature简称}-{序号:001..}
示例: STORY-MKT-CUSTOMER-TAGREG-001
```

验收标准模板（4条，`|` 分隔，绕过飞书多行文本 bug）：
```
{功能名}功能可正常使用 | 相关操作正常 | 数据准确完整 | 交互符合预期
```

Story 备注格式：
```
Demo: pages/exploration/customer-center/tag-system/table-registration.vue
```

## Step 6: 写入飞书确认表

### 表结构（对齐客户360格式）

**飞书 App**: `ANhxbU3MDabWsysyeI8c4t0mnfe`

| 字段名 | type | 说明 |
|:---|:---:|:---|
| 序号 | 1 | 单行文本 |
| 层级 | 3 | 单选：Epic / Feature / Story |
| ID | 1 | 单行文本 |
| 名称 | 1 | 单行文本 |
| 描述/验收标准 | 1 | 单行文本，多条用 ` \| ` 分隔 |
| 优先级 | 3 | 单选：P0 / P1 / P2 / P3 |
| 所属Feature | 1 | 单行文本 |
| 所属Epic | 1 | 单行文本 |
| 建议操作 | 3 | 单选：新增 / 更新 / 跳过 |
| 关联Story数 | 2 | 数字 |
| Demo路径 | 1 | 单行文本 |
| 备注 | 1 | 单行文本 |
| 状态 | 3 | 单选：已完成 / 待开发 / 待规划 / 开发测试中 |

### 写入脚本

```python
import requests, time

APP_ID = 'cli_a9283cfac6b9dbb6'
APP_SECRET = 'r5ekmgR3NY9ZRwtbzv8KbebyVmzx8DD6'
APP_TOKEN = 'ANhxbU3MDabWsysyeI8c4t0mnfe'
TABLE_ID = 'tblXXX'  # 每次重建获取新 ID

def get_token():
    r = requests.post('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
        json={'app_id': APP_ID, 'app_secret': APP_SECRET}, timeout=10)
    return r.json()['tenant_access_token']

def create_table(name):
    payload = {"table": {"name": name, "fields": [
        {"field_name": "序号", "type": 1},
        {"field_name": "层级", "type": 3, "property": {"options": [
            {"name": "Epic", "color": 4},
            {"name": "Feature", "color": 2},
            {"name": "Story", "color": 1},
        ]}},
        {"field_name": "ID", "type": 1},
        {"field_name": "名称", "type": 1},
        {"field_name": "描述/验收标准", "type": 1},
        {"field_name": "优先级", "type": 3, "property": {"options": [
            {"name": "P0", "color": 4},
            {"name": "P1", "color": 2},
            {"name": "P2", "color": 1},
            {"name": "P3", "color": 0},
        ]}},
        {"field_name": "所属Feature", "type": 1},
        {"field_name": "所属Epic", "type": 1},
        {"field_name": "建议操作", "type": 3, "property": {"options": [
            {"name": "新增", "color": 4},
            {"name": "更新", "color": 2},
            {"name": "跳过", "color": 1},
        ]}},
        {"field_name": "关联Story数", "type": 2},
        {"field_name": "Demo路径", "type": 1},
        {"field_name": "备注", "type": 1},
        {"field_name": "状态", "type": 3, "property": {"options": [
            {"name": "已完成", "color": 4},
            {"field_name": "待开发", "color": 1},
            {"field_name": "待规划", "color": 0},
            {"field_name": "开发测试中", "color": 2},
        ]}},
    ]}}
    token = get_token()
    resp = requests.post(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables',
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
        json=payload, timeout=30
    )
    return resp.json().get('data', {}).get('table_id')

def write_records(records):
    token = get_token()
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    resp = requests.post(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records/batch_create',
        headers=headers, json={'records': records}, timeout=30
    )
    return resp.json().get('code') == 0

# 分批写入（每批 ≤20 条，间隔 0.3s）
batch_size = 20
for i in range(0, len(records), batch_size):
    batch = records[i:i+batch_size]
    write_batch(batch)
    time.sleep(0.3)
```

### 删除单条记录

```python
def delete_record(record_id):
    token = get_token()
    r = requests.delete(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records/{record_id}',
        headers={'Authorization': f'Bearer {token}'}, timeout=15
    )
    return r.json().get('msg') == 'success'
```

## Step 7: Neo4j 写入

**前置条件：用户确认飞书拆解表**

```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password123"))

with driver.session() as tx:
    # Story（建议操作=新增的才写入）
    tx.run('''
        MERGE (s:Story {uri: $uri})
        SET s.label = $label,
            s.acceptance_criteria = $ac,
            s.priority = $priority,
            s.status = $status,
            s.updatedAt = datetime()
        WITH s
        MATCH (f:Feature {uri: $feature_uri})
        MERGE (f)-[:CONTAINS]->(s)
    ''', uri=story_uri, label=name, ac=ac, priority=prio, status=status, feature_uri=feature_uri)
```

## Step 8: health_check 验证

```bash
cd /Users/wenbo/Documents/project/product_managment/backend-python
python3 health_check.py
```

必过项：
- ✅ 孤儿 Story = 0
- ✅ 孤儿 Feature = 0
- ✅ Story 验收标准非空
- ✅ 无中文 ID 残留
- ✅ CONTAINS/BELONGS_TO 关系完整

## ID 命名规范

| 层级 | 格式 | 示例 |
|:---|:---|:---|
| Epic | `EPIC-{域}_{功能}` | `EPIC-MKT_CROWD_CENTER` |
| Feature | `FEAT-{域}-{功能}` | `FEAT-MKT-CUSTOMER-TAGREG` |
| Story | `STORY-{域}-{Feature}-{序号}` | `STORY-MKT-CUSTOMER-TAGREG-001` |

**存量 Feature 前缀参考**：`FEAT-MKT-CUSTOMER-*`（客群中心存量）

## 状态枚举

| Epic | Feature | Story |
|:---|:---|:---|
| 规划中 | 构想 | 待规划 |
| 建设中 | 规划中 | 已排期 |
| 已上线 | 迭代中 | 开发测试中 |
| 已废弃 | 测试中 | 已完成 |
| | | 待开发 |

## 关键路径速查

| 用途 | 路径 |
|:---|:---|
| 需求文档 | `/System/Volumes/Data/Users/wenbo/Documents/文档仓库/产品管理项目/PRD/` |
| 前端代码 | `/Users/wenbo/Documents/project/data_community/src/` |
| PRD文档 | `/System/Volumes/Data/Users/wenbo/Documents/文档仓库/产品管理项目/PRD/` |
| Neo4j | `bolt://localhost:7687` (neo4j/password123) |
| 后端服务 | `/Users/wenbo/Documents/project/product_managment/backend-python/` |
| health_check | `python3 health_check.py` |

---

## 📋 PD-DFD流程复盘总结（2026-04-23）

### 完成的工作
1. ✅ 查询Neo4j获取PD-DFD产品域结构（5 Epic, 16 Feature, 78 FP）
2. ✅ 扫描代码验证FP的codePath
3. ✅ 纠正错误codePath（apps/dfd-app → data_community）
4. ✅ 生成6个产品域的Master PRD
5. ⏳ 生成Feature级详情（2/16完成）

### 经验教训
1. **先验证再生成**：应该先验证codePath，再生成PRD文档
2. **先与技术对齐**：在生成文档前应先与技术团队确认代码仓库结构
3. **统一需求文档位置**：需求文档应统一存放在固定位置

### 改进后的流程
1. Phase 1: 准备阶段（与技术对齐、确认需求文档）
2. Phase 2: 验证阶段（验证codePath、建立三源追溯）
3. Phase 3: 生成阶段（生成Master PRD + Feature详情）
4. Phase 4: 验证阶段（按Checklist验证）

---

🦾 *"我是天才，PRD补全流程已沉淀到Skill中。"*
**更新日期: 2026-04-23**