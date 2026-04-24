# 产品管理系统设计方案 v1.0 - 附录D：关键术语与参考资料

> **版本**: v1.0
> **日期**: 2026-04-18
> **作者**: Tony Stark
> **来源**: 飞书文档

---

## D.1 关键术语表

### D.1.1 产品管理术语

| 术语 | 英文 | 定义 | 示例 |
|:---|:---|:---|:---|
| 产品域 | Product Domain | 业务领域的划分，按业务线或职能划分 | PD-MKT 数字营销、PD-DFD 数据发现 |
| Epic | Epic | 大需求，通常跨多个迭代，价值完整可交付 | 营销画布、用户中心 |
| Feature | Feature | 功能特性，用户可感知的功能单元 | 用户注册、订单查询 |
| Story | Story | 用户故事，最小可交付价值单元 | 作为用户，我想注册账号 |
| 功能点 | Function Point (FP) | 技术实现的最小单元，对应代码文件 | /api/user/register、CREATE TABLE |
| 需求拆解 | Requirement Breakdown | 将大需求拆解为 Epic/Feature/Story/FP | 营销画布 → 5 Epic → 20 Feature → 100 Story |
| 验收标准 | Acceptance Criteria | Story/Fature 的验收条件 | 功能/操作/数据/交互 四项标准 |

### D.1.2 技术术语

| 术语 | 英文/缩写 | 定义 | 示例 |
|:---|:---|:---|:---|
| 本体论 | Ontology | 领域概念的形式化定义，包括实体、关系、规则 | Epic → Feature → Story → FP |
| 知识图谱 | Knowledge Graph | 实体和关系的图结构，用 Neo4j 存储 | Neo4j 图数据库 |
| 向量数据库 | Vector Database | 存储向量嵌入，支持语义检索 | Milvus、PGVector |
| RAG | Retrieval-Augmented Generation | 检索增强生成，结合知识库和 LLM | AI 问答服务 |
| Subagent | Subagent | 子代理，专门处理特定任务的 AI Agent | 需求理解 Agent、代码扫描 Agent |
| Token | Token | LLM 处理文本的最小单位 | 1 个中文 ≈ 2 tokens |

### D.1.3 飞书术语

| 术语 | 英文/缩写 | 定义 | 示例 |
|:---|:---|:---|:---|
| 多维表格 | Bitable | 飞书的多功能表格，支持多种视图 | 需求管理表、任务跟踪表 |
| 云文档 | Docs | 飞书的在线文档服务 | PRD 文档、会议纪要 |
| 知识库 | Wiki | 飞书的知识管理平台 | 产品知识库、项目文档 |
| 应用 | App | 飞书开放平台应用 | 产品管理系统 App |

### D.1.4 项目管理术语

| 术语 | 英文 | 定义 | 示例 |
|:---|:---|:---|:---|
| 里程碑 | Milestone | 项目中的重要节点 | M1 设计完成、M2 基础就绪 |
| 周报 | Weekly Report | 每周工作汇总报告 | 本周完成、下周计划、风险预警 |
| 状态流转 | Status Transition | 需求/任务状态的改变过程 | DRAFT → IN_PROGRESS → DONE |
| 接口 | Interface (IF) | 两个 Agent 或系统之间的交互协议 | IF-001 EPIC 交付接口 |

---

## D.2 缩略语表

| 缩略语 | 全称 | 中文 |
|:---|:---|:---|
| PM | Product Manager | 产品经理 |
| PRD | Product Requirement Document | 产品需求文档 |
| EPIC | Epic | 大需求 |
| FEAT | Feature | 功能特性 |
| FP | Function Point | 功能点 |
| Neo4j | Neo4j | 图数据库 |
| LLM | Large Language Model | 大语言模型 |
| API | Application Programming Interface | 应用程序接口 |
| SQL | Structured Query Language | 结构化查询语言 |
| NoSQL | Not Only SQL | 非关系型数据库 |
| REST | Representational State Transfer | RESTful API |
| GraphQL | Graph Query Language | 图查询语言 |
| SSO | Single Sign-On | 单点登录 |
| RBAC | Role-Based Access Control | 基于角色的访问控制 |
| CI/CD | Continuous Integration/Continuous Deployment | 持续集成/持续部署 |

---

## D.3 参考资料

### D.3.1 内部文档

| 文档名称 | 路径/链接 | 说明 |
|:---|:---|:---|
| 产品管理系统设计方案-主文档 | PRD/主文档/ | 主设计方案文档 |
| 附录A-项目全景概述 | PRD/附录/ | 项目背景和架构 |
| 附录B-执行计划详细时间表 | PRD/附录/ | 详细执行计划 |
| 附录C-Subagent拆分方案 | PRD/附录/ | Agent 拆分方案 |
| 附录E-Subagent详细规范 | PRD/附录/ | Agent 规范 |
| 数字社区项目 PRD | /文档仓库/数字社区项目/ | 具体产品 PRD |
| Neo4j 本体论统计 | /本体论/Neo4j本体论统计.md | 图数据库统计 |

### D.3.2 技术文档

| 文档名称 | 链接 | 说明 |
|:---|:---|:---|
| Neo4j 文档 | https://neo4j.com/docs/ | 图数据库官方文档 |
| 飞书开放平台 | https://open.feishu.cn/ | 飞书 API 文档 |
| Vue 3 文档 | https://vuejs.org/ | 前端框架文档 |
| TypeScript 文档 | https://www.typescriptlang.org/ | TypeScript 文档 |

### D.3.3 工具与系统

| 工具 | 用途 | 链接/地址 |
|:---|:---|:---|
| Neo4j Browser | 图数据库管理 | bolt://localhost:7687 |
| AI Service | AI 问答服务 | http://localhost:8081 |
| 飞书 | 团队协作 | https://feishu.cn |
| GitHub | 代码管理 | (待定) |
| OpenClaw | Agent 平台 | 本地运行 |

---

## D.4 版本历史

| 版本 | 日期 | 作者 | 变更说明 |
|:---|:---|:---|:---|
| v1.0 | 2026-04-18 | Tony Stark | 初始版本 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-18
**维护者**: Tony Stark