# 需求拆解完整工作流（SOP v2.0）

## 一、流程概览（8步）

```
Step 1: 读需求文档（产品说明文档 / PRD）
Step 2: 查 Neo4j 存量（Epic → Feature → Story，确认已有内容）
Step 3: 扫描 Demo 代码路径（找到实现组件，验证功能覆盖）
Step 4: 对比分析（存量 vs 文档 vs Demo，找出真实缺口）
Step 5: 结构化拆解（存量不动，仅补充缺失 Story）
Step 6: 写入飞书确认表（重建表结构，对齐客户360格式）
Step 7: 用户审核 → Neo4j 写入
Step 8: health_check 验证
```

**⚠️ 核心原则：存量数据是基准，文档是补充来源，Demo 代码是验证手段。绝不能闭门造车。**

---

## 二、Step 1 ~ Step 4（摸底阶段）

### Step 1: 需求文档收集

文档路径：
```
/Users/wenbo/Documents/project/data_community/docs/key-project-docs/
```

读完后明确：
- 几个功能模块
- 每个模块的核心能力
- 技术实现要求

### Step 2: 查 Neo4j 存量（必须先做）

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password123"))

with driver.session() as tx:
    result = tx.run("""
        MATCH (e:Epic {uri: 'Epic:EPIC-MKT_CROWD_CENTER'})
        OPTIONAL MATCH (e)-[:CONTAINS]->(f:Feature)
        OPTIONAL MATCH (f)-[:CONTAINS]->(s:Story)
        RETURN f.uri as feature_uri, f.label as feature_label,
               s.uri as story_uri, s.label as story_label,
               s.priority, s.status
        ORDER BY f.uri, s.uri
    """)
    rows = list(result)
    
    features = {}
    for r in rows:
        fid = r['feature_uri']
        if fid not in features:
            features[fid] = {'label': r['feature_label'], 'stories': []}
        if r['story_uri']:
            features[fid]['stories'].append(r['story_label'])
    
    for fid, v in features.items():
        print(f"【Feature】{fid} ({v['label']})")
        for s in v['stories']:
            print(f"  - {s}")
        if not v['stories']:
            print(f"  (无 Story) ← 重点缺口")
```

### Step 3: 扫描 Demo 代码

```bash
find /Users/wenbo/Documents/project/data_community/src -type f -name "*.vue" \
  | grep -i "customer-center\|tag-system\|audience\|event-center"
```

Demo 作用：验证功能是否有前端实现。**Demo 存在 ≠ 功能已上线**，仅作为 Story 的参考路径备注。

### Step 4: 对比分析（关键决策点）

制作对照表：

| 文档功能模块 | 存量 Feature | Demo 路径 | 存量 Story | 缺口 |
|:---|:---|:---|:---:|:---|
| 标签系统 | FEAT-MKT-CUSTOMER-TAGREG | tag-system/ | 0 | ❌ 无 Story |
| 人群圈选 | FEAT-MKT-CUSTOMER-IDCONV | audience-system/ | 2 | ⚠️ 部分完成 |
| 事件中心 | FEAT-MKT-CUSTOMER-EVENTREG | event-center/ | 3 | ✅ 已完成 |

**拆解原则**：
- 存量 Story 不动（已完成/开发中/待规划均保持原样）
- 只补充**文档有功能描述但 Neo4j 完全没有 Story** 的 Feature
- Story ID 基于存量命名规范推断，不能凭空捏造

---

## 三、Step 5: 结构化拆解

### 新增 Story 命名规范（基于存量数据）

```
STORY-{域}-{Feature简称}-{序号:001..}
示例: STORY-MKT-CUSTOMER-TAGREG-001
```

**不能使用 FEAT-MKT-CROWD-* 等不存在的 ID 前缀**，必须基于 Neo4j 存量 Feature ID。

### 存量 Story ID 前缀参考（客群中心）

| Feature | ID 前缀 |
|:---|:---|
| 标签表注册 | STORY-MKT-CUSTOMER-TAGREG-* |
| 一次性建群算 | STORY-MKT-CUSTOMER-ONESHOOT-* |
| 客群剔除 | STORY-MKT-CUSTOMER-EXCLUDE-* |
| ID-mapping主表 | STORY-MKT-MANUAL_ID_MAPPING-* |
| ID转化服务 | STORY-COM-NOTICE_CROWD-* |
| 人群删除审批流 | STORY-COM-NOTICE_CROWD-* |
| 事件注册 | STORY-COM-NOTICE_EVENT-* |
| 事件测试功能 | STORY-COM-NOTICE_EVENT-* |
| 事件圈客 | STORY-COM-NOTICE_EVENT-* |

### 验收标准模板（4条，`|` 分隔，绕过飞书多行文本 bug）

```
{功能名}功能可正常使用 | 相关操作正常 | 数据准确完整 | 交互符合预期
```

### Story 备注格式

```
Demo: pages/exploration/customer-center/tag-system/table-registration.vue
```

---

## 四、Step 6: 飞书确认表

### 表结构（对齐客户360格式）

**飞书 App**: `ANhxbU3MDabWsysyeI8c4t0mnfe`

字段列表：
| 字段名 | type | 说明 |
|:---|:---:|:---|
| 序号 | 1 | 单行文本 |
| 层级 | 3 | 单选：Epic / Feature / Story |
| ID | 1 | 单行文本 |
| 名称 | 1 | 单行文本 |
| 描述/验收标准 | 1 | 单行文本，` \| ` 分隔多行 |
| 优先级 | 3 | 单选：P0 / P1 / P2 / P3 |
| 所属Feature | 1 | 单行文本 |
| 所属Epic | 1 | 单行文本 |
| 建议操作 | 3 | 单选：新增 / 更新 / 跳过 |
| 关联Story数 | 2 | 数字 |
| Demo路径 | 1 | 单行文本 |
| 备注 | 1 | 单行文本 |
| 状态 | 3 | 单选：已完成 / 待开发 / 待规划 / 开发测试中 |

### 重建表流程

每次拆解前先删旧表建新表，确保字段结构正确：

```python
# 删表
token = get_token()
requests.delete(
    f'https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{OLD_TABLE}',
    headers={'Authorization': f'Bearer {token}'}
)

# 建新表（获取新 TABLE_ID）
resp = requests.post(
    f'https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables',
    headers=headers, json=payload, timeout=30
)
new_id = resp.json()['data']['table_id']
```

### 批量写入

- 每批 ≤20 条
- 每批间隔 0.3s
- token 每次重新获取
- 使用中文字段名，不接受 fldXXX 字段 ID

---

## 五、Step 7: Neo4j 执行写入

**前置条件：用户确认飞书拆解表**

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password123"))

with driver.session() as tx:
    # 写入 Story（建议操作=新增的才写入）
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

---

## 六、Step 8: health_check 验证

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

---

## 七、数据质量常见问题修复

| 问题 | 修复方法 |
|:---|:---|
| 捏造 Story ID（与存量不一致）| 删重建，基于存量 ID 规范推断 |
| 存量 Story 不动原则被违反 | 恢复存量 Story，增量补充缺失部分 |
| 飞书多行文本字段无法保存 | 使用 type=1 单行文本，` \| ` 分隔多行 |
| Feature 无 Story | 结合文档 + Demo 代码补充，不凭空捏造 |

---

## 八、完整案例：客群中心（2026-04-09）

**需求文档**: 客群中心平台项目说明文档.md
**Epic**: EPIC-MKT_CROWD_CENTER（客群中心）
**存量 Feature**: 9 个（含 3 个无 Story）
**存量 Story**: 14 条
**新增 Story**: 7 条（补充 3 个无 Story 的 Feature）

| Feature | 存量 Story | 新增 Story | 状态 |
|:---|:---:|:---:|:---|
| 标签表注册 | 0 | +3 | 新增 |
| 一次性建群算 | 0 | +3 | 新增 |
| 客群剔除 | 0 | +1 | 新增 |
| ID-mapping主表 | 3 | 0 | 开发中 |
| ID转化服务 | 2 | 0 | 已完成 |
| 人群删除审批流 | 2 | 0 | 待规划 |
| 事件注册 | 3 | 0 | 已完成 |
| 事件测试功能 | 2 | 0 | 待规划 |
| 事件圈客 | 2 | 0 | 待规划 |

**飞书确认表**: https://mcn2qsv100fk.feishu.cn/bitable/ANhxbU3MDabWsysyeI8c4t0mnfe/tbltPK5MUVbaZhle

**Demo 代码路径**（扫描自 `/Users/wenbo/Documents/project/data_community/src/pages/exploration/customer-center/`）：
- tag-system/: tag-management.vue / tag-create.vue / tag-detail.vue / table-registration.vue / attribute-management.vue
- audience-system/: audience-management.vue / audience-create.vue / audience-detail.vue
- event-center/: event-management.vue / event-sample-stats.vue / kafka-datasource.vue / virtual-events.vue

---

## 九、全部 Epic 盘点（截至 2026-04-09）

| # | Epic ID | 名称 | Story数 |
|:---:|:---|:---|:---:|
| 1 | EPIC-DEX_METRIC_DASHBOARD | 指标看板 | 35 |
| 2 | EPIC-DEX_UNIFIED_ANALYSIS_WORKBENCH | 统一分析工作台 | 21 |
| 3 | EPIC-DFD_ASSET_OPERATE_TOOL | 资产运营工具 | 11 |
| 4 | EPIC-DFD_DATA_ASSET | 数据资产 | 15 |
| 5 | EPIC-MKT_MANUAL_SALES_DESK | 人工销售工作台 | 41 |
| 6 | EPIC-DMT_BIZ_CONCEPT_MANAGE | 业务概念管理 | 27 |
| 7 | EPIC-DMT_DATA_SERVICE | 数据服务 | 24 |
| 8 | EPIC-DMT_DATA_STD | 数据标准 | 15 |
| 9 | EPIC-DMT_METADATA_MANAGE | 元数据管理 | 11 |
| 10 | EPIC-DFD_DATA_ELEMENT | 数据元 | 13 |
| 11 | EPIC-DFD_DATA_RESOURCE | 数据资源 | 22 |
| 12 | EPIC-MKT_REACH_SYSTEM | 触达系统 | 14 |
| 13 | EPIC-MKT_MARKETING_CANVAS | 营销画布 | 11 |
| 14 | EPIC-MKT_BENEFIT_CENTER | 权益中心 | 6 |
| 15 | EPIC-MKT_CROWD_CENTER | 客群中心 | 22 |

**总计：15 Epic / 264+ Story / 4 产品域（PD-DEX / PD-DFD / PD-MKT / PD-DMT）**
