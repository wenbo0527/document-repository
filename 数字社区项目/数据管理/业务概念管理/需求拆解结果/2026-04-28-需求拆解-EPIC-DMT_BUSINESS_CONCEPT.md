# 需求拆解结果 - EPIC-DMT_BUSINESS_CONCEPT 业务概念管理

> 文档版本：v1.0
> 创建日期：2026-04-28
> 拆解人：Tony Stark
> Epic：EPIC-DMT_BUSINESS_CONCEPT

---

## 一、Epic 信息

| 属性 | 值 |
|:---|:---|
| Epic ID | EPIC-DMT_BUSINESS_CONCEPT |
| Epic 名称 | 业务概念管理 |
| 产品域 | PD-DMT 数据管理 |
| Epic URI | `Epic:DMT:EPIC-DMT_BUSINESS_CONCEPT` |
| 状态 | completed（功能已上线） |
| 描述 | 建立业务与技术之间的桥梁，通过业务域、业务实体、业务图谱三个维度，实现业务概念的可视化管理和业务数据的全链路追踪 |

---

## 二、Feature 拆解

| # | Feature ID | Feature 名称 | 优先级 | 状态 | Story 数 |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | FEAT-DMT-BC-DOMAIN | 业务域管理 | P0 | completed | 5 |
| 2 | FEAT-DMT-BC-ENTITY | 业务实体管理 | P0 | completed | 5 |
| 3 | FEAT-DMT-BC-GRAPH | 业务图谱 | P0 | completed | 6 |

**Feature URI 规范**：`Feature:DMT:FEAT-DMT-BC-*`

---

## 三、Story 拆解

### Feature 1：业务域管理（FEAT-DMT-BC-DOMAIN）

| Story ID | Story 名称 | 优先级 | 状态 | 验收标准 |
|:---|:---|:---:|:---:|:---|
| Story:DMT:BC-DOMAIN-001 | 业务域卡片网格展示 | P0 | completed | 响应式网格布局（24/12/8/6列），域编码带颜色标签 |
| Story:DMT:BC-DOMAIN-002 | 业务域颜色分类 | P0 | completed | 根据域名称关键词自动匹配颜色（蓝/红/橙/青/绿） |
| Story:DMT:BC-DOMAIN-003 | 业务域信息展示 | P0 | completed | 展示域编码、名称、负责人Icon、描述、覆盖率 |
| Story:DMT:BC-DOMAIN-004 | 业务域统计计数 | P0 | completed | 实时显示"共 X 个业务域" |
| Story:DMT:BC-DOMAIN-005 | 业务域详情预览 | P1 | completed | IconEye触发，提示`查看业务域: {name}` |

### Feature 2：业务实体管理（FEAT-DMT-BC-ENTITY）

| Story ID | Story 名称 | 优先级 | 状态 | 验收标准 |
|:---|:---|:---:|:---:|:---|
| Story:DMT:BC-ENTITY-001 | 业务域树导航 | P0 | completed | 左侧树形结构，包含"全部"选项，点击联动筛选 |
| Story:DMT:BC-ENTITY-002 | 实体表格展示 | P0 | completed | 表格列：实体编码、名称、描述、核心关系标签、操作 |
| Story:DMT:BC-ENTITY-003 | 实体搜索功能 | P0 | completed | 顶部输入框支持实体名称搜索 |
| Story:DMT:BC-ENTITY-004 | 实体详情抽屉 | P0 | completed | 展示基础信息、属性定义、关联数据要素、底层物理表 |
| Story:DMT:BC-ENTITY-005 | 数据要素类型展示 | P0 | completed | metric蓝色/variable橙色/dimension待定义标签 |

### Feature 3：业务图谱（FEAT-DMT-BC-GRAPH）

| Story ID | Story 名称 | 优先级 | 状态 | 验收标准 |
|:---|:---|:---:|:---:|:---|
| Story:DMT:BC-GRAPH-001 | 列表/图谱视图切换 | P0 | completed | Radio button切换，展示列表视图和X6图谱视图 |
| Story:DMT:BC-GRAPH-002 | 图谱工具栏 | P0 | completed | 层级筛选、中心实体选择、刷新、放大、缩小、自适应 |
| Story:DMT:BC-GRAPH-003 | X6图形交互 | P0 | completed | 节点渲染、边渲染、Dagre布局、滚轮缩放、拖拽平移 |
| Story:DMT:BC-GRAPH-004 | 节点层级映射 | P0 | completed | client层蓝色/account层绿色/business层橙色 |
| Story:DMT:BC-GRAPH-005 | 新建关系弹窗 | P0 | completed | 表单字段：关系名称、源实体、关系类型、目标实体 |
| Story:DMT:BC-GRAPH-006 | 关系类型筛选 | P1 | completed | 支持按组成/关联/继承类型筛选关系 |

---

## 四、Story 汇总

| Feature | Story 数 | P0 | P1 | P2 |
|:---|:---:|:---:|:---:|:---:|
| 业务域管理 | 5 | 4 | 1 | 0 |
| 业务实体管理 | 5 | 5 | 0 | 0 |
| 业务图谱 | 6 | 5 | 1 | 0 |
| **合计** | **16** | **14** | **2** | **0** |

---

## 五、Neo4j 写入语句

```cypher
// 创建 Epic
MERGE (e:Epic {uri: 'Epic:DMT:EPIC-DMT_BUSINESS_CONCEPT'})
SET e.label = '业务概念管理',
    e.status = 'completed',
    e.updatedAt = datetime()

// 建立 Epic → ProductDomain 关系
MATCH (pd:ProductDomain {uri: 'Domain:DMT:PD-DMT'})
MATCH (e:Epic {uri: 'Epic:DMT:EPIC-DMT_BUSINESS_CONCEPT'})
MERGE (pd)-[:CONTAINS]->(e)

// 创建 Feature
MERGE (f1:Feature {uri: 'Feature:DMT:FEAT-DMT-BC-DOMAIN'})
SET f1.label = '业务域管理', f1.status = 'completed'
MERGE (f2:Feature {uri: 'Feature:DMT:FEAT-DMT-BC-ENTITY'})
SET f2.label = '业务实体管理', f2.status = 'completed'
MERGE (f3:Feature {uri: 'Feature:DMT:FEAT-DMT-BC-GRAPH'})
SET f3.label = '业务图谱', f3.status = 'completed'

// 建立 Epic → Feature 关系
MATCH (e:Epic {uri: 'Epic:DMT:EPIC-DMT_BUSINESS_CONCEPT'})
MATCH (f:Feature) WHERE f.uri IN ['Feature:DMT:FEAT-DMT-BC-DOMAIN', 'Feature:DMT:FEAT-DMT-BC-ENTITY', 'Feature:DMT:FEAT-DMT-BC-GRAPH']
MERGE (e)-[:CONTAINS]->(f)

// 创建 Story（业务域管理）
...
```

---

## 六、PRD 关联

| 文档 | 路径 |
|:---|:---|
| 产品 PRD | `数字社区项目/数据管理/业务概念管理/产品PRD/PRD-PD-DMT-BC-业务概念管理-v1.0.md` |
| 业务需求 | `数字社区项目/数据管理/业务概念管理/业务需求入口/2026-04-28-业务需求-业务数据管理功能清单.md` |

---

*拆解时间：2026-04-28*
