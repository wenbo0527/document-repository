# Neo4j 产品域修复 Skill

## 能做什么

根据 PRD 文档，逐个 Epic 修复产品域的层级结构，补全节点元数据，同步到 Neo4j 图数据库。

## 核心能力

1. **PRD 文档分析** - 读取 EPIC 文档（v5.0），提取 Feature/FP 结构
2. **Neo4j 状态检查** - 查询 Epic/Feature/FeaturePoint 节点和关系
3. **层级修复** - 修复 ProductDomain→Epic→Feature→FeaturePoint 层级
4. **元数据补全** - 补充 name/status/fp_count/code_path/doc_version/author
5. **关系建立** - 建立 CONTAINS 关系连接各层级
6. **验证确认** - 验证层级结构和孤立节点

## 激活条件

- 用户要求修复（"修复产品域"、"同步 Neo4j"）
- PRD 更新后需要同步
- 健康检查发现数据异常

## 标准工作流程

### Step 1: 读取 PRD 文档

读取产品域的 EPIC 文档，提取：
- Epic 元数据（name/code/FP数量/版本）
- Feature 清单（URI/名称/代码路径）
- FP 清单（ID/功能点/说明）

### Step 2: 分析 Neo4j 现状

```python
# 查询当前 Epic 状态
MATCH (e:Epic {uri: 'Epic:EPIC-xxx'})
RETURN e.uri, e.name, properties(e)

# 查询 Feature 状态
MATCH (e:Epic {uri: 'Epic:EPIC-xxx'})-[:CONTAINS]->(f:Feature)
RETURN f.uri, f.name, labels(f)

# 检查孤立节点
MATCH (f:Feature) WHERE f.uri STARTS WITH 'Epic:EPIC-xxx'
RETURN count(f) as orphan
```

### Step 3: 修复层级关系

```cypher
-- 建立 ProductDomain -> Epic 关系
MATCH (d:ProductDomain {uri: 'ProductDomain:PD-MKT'})
MATCH (e:Epic {uri: 'Epic:EPIC-MKT-REACH'})
MERGE (d)-[:CONTAINS]->(e)

-- 删除旧 Feature 节点（URI 如 Epic:EPIC-MKT-REACH-FEAT-01）
MATCH (f) WHERE f.uri = 'Epic:EPIC-MKT-REACH-FEAT-01'
DETACH DELETE f

-- 创建新 Feature 节点
CREATE (f:Feature {
    uri: 'Feature:FEAT-MKT-REACH-01',
    name: '触达首页',
    code_path: 'touch/index.vue',
    domain: 'PD-MKT',
    epic: 'EPIC-MKT-REACH',
    status: 'completed',
    updated_at: datetime()
})

-- 重建 Epic -> Feature 关系
MATCH (e:Epic {uri: 'Epic:EPIC-MKT-REACH'})
MATCH (f:Feature {uri: 'Feature:FEAT-MKT-REACH-01'})
MERGE (e)-[:CONTAINS]->(f)
```

### Step 4: 补充 Epic 元数据

```cypher
MATCH (e:Epic {uri: 'Epic:EPIC-MKT-REACH'})
SET e.name = '触达系统',
    e.status = 'completed',
    e.fp_count = 22,
    e.doc_version = 'v5.0',
    e.author = 'Tony Stark',
    e.domain = 'PD-MKT',
    e.updated_at = datetime()
```

### Step 5: 补充 Feature 元数据

```cypher
MATCH (f:Feature {uri: 'Feature:FEAT-MKT-REACH-01'})
SET f.name = '触达首页',
    f.code_path = 'touch/index.vue',
    f.status = 'completed',
    f.fp_count = 3,
    f.epic = 'EPIC-MKT-REACH',
    f.domain = 'PD-MKT',
    f.updated_at = datetime()
```

### Step 6: 建立 Feature → FeaturePoint 关系

按 FP ID 前缀映射：
| 前缀 | Feature |
|:---|:---|
| IDX | FEAT-MKT-REACH-01 |
| SYS | FEAT-MKT-REACH-02 |
| POL | FEAT-MKT-REACH-03 |
| CH | FEAT-MKT-REACH-04 |
| QRY | FEAT-MKT-REACH-05 |

```cypher
MATCH (f:Feature {uri: 'Feature:FEAT-MKT-REACH-01'})
MATCH (fp:FeaturePoint)
WHERE fp.uri STARTS WITH 'FP-MKT-REACH-IDX'
MERGE (f)-[:CONTAINS]->(fp)
```

### Step 7: 验证结果

```cypher
-- 验证层级结构
MATCH (d:ProductDomain)-[:CONTAINS]->(e:Epic)-[:CONTAINS]->(f:Feature)-[:CONTAINS]->(fp:FeaturePoint)
WHERE e.uri = 'Epic:EPIC-MKT-REACH'
RETURN e.name, collect(DISTINCT f.name) as features, count(DISTINCT fp) as total_fp

-- 验证无孤立节点
MATCH (fp:FeaturePoint)
WHERE fp.uri STARTS WITH 'FP-MKT-REACH'
AND NOT (fp)<-[:CONTAINS]-(:Feature)
RETURN count(fp) as orphan_count
```

### Step 8: 代码交叉验证

检查代码目录是否存在，交叉验证 PRD 中的 code_path：

```python
import os

base_paths = {
    'touch': '/Users/wenbo/Documents/project/data_community/data_community/apps/touch/src/pages/touch',
    'sales': '/Users/wenbo/Documents/project/telemarketing-workbench/src/features',
    'campaign': '/path/to/campaign/code',
    'crowd': '/path/to/crowd/code',
    'benefit': '/path/to/benefit/code',
}

# 验证 Feature 代码路径
feature_code_paths = {
    'FEAT-MKT-REACH-01': 'touch/index.vue',
    'FEAT-MKT-REACH-02': 'touch/system/',
    'FEAT-MKT-SALES-01': 'organization',
    'FEAT-MKT-SALES-02': 'outbound',
}

for feat_uri, code_path in feature_code_paths.items():
    # 提取目录路径
    dir_path = os.path.dirname(code_path)
    full_path = os.path.join(base_path, dir_path)
    exists = os.path.exists(full_path)
    print(f'{feat_uri}: {code_path} -> {"✅" if exists else "❌"}')

## 已完成 Epic

| Epic | 状态 |
|:---|:---:|
| EPIC-MKT-REACH (触达系统) | ✅ 完成 |
| EPIC-MKT-SALES (人工电销工作台) | 🔄 待处理 |
| EPIC-MKT-CROWD (客群中心) | ⏳ 待处理 |
| EPIC-MKT-BENEFIT (权益中心) | ⏳ 待处理 |
| EPIC-MKT-CANVAS (营销画布) | ⏳ 待处理 |

## 产品域目录

```
PRD 文档路径: /System/Volumes/Data/Users/wenbo/Documents/文档仓库/产品管理项目/PRD/

04-PD-MKT-数字营销/
  01-触达系统-v5.0.md      (EPIC-MKT-REACH) ✅
  02-权益中心-v5.0.md      (EPIC-MKT-BENEFIT)
  03-客群中心-v5.0.md      (EPIC-MKT-CROWD)
  04-营销画布-v5.0.md      (EPIC-MKT-CANVAS)
  05-人工电销工作台-v5.0.md (EPIC-MKT-SALES)
```

## 关键路径

| 用途 | 路径 |
|:---|:---|
| PRD 文档目录 | /System/Volumes/Data/Users/wenbo/Documents/文档仓库/产品管理项目/PRD/ |
| 本地工作目录 | /Volumes/MOVESPEED/Data/个人核心/05_AgentOutput/agent_work/产品管理方案团队/ |
| Neo4j 连接 | bolt://localhost:7687 (neo4j/password123) |

## Neo4j 连接配置

```python
from neo4j import GraphDatabase

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'password123'))

with driver.session() as session:
    result = session.run('MATCH (n) RETURN count(n)')
```

---

Version: 2.0 | For: Tony Stark | Updated: 2026-04-20