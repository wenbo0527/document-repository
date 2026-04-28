# PD-DMT 数据管理 功能清单（钟离版）

> **版本**: v2.0
> **日期**: 2026-04-27
> **作者**: Tony Stark → 钟离
> **用途**: 技术方案评估 & 开发任务分配

---

## 一、元数据管理（EPIC-DMT_METADATA_MANAGE）

**Epic 优先级**: P0
**Story 数量**: 19
**状态**: 待开发

---

### Feature 1：元数据建模（FEAT-DMT-METADATA-MODELING）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-META-001 | 创建元数据模型 | P0 | 动态表单字段配置、字段类型映射（MySQL→标准类型）、拖拽排序 |
| Story-META-002 | 编辑元数据模型 | P0 | 版本Diff算法、变更日志表设计、类型变更告警 |
| Story-META-003 | 模型版本管理 | P0 | 历史版本存储（JSON Snapshot）、回滚事务设计、版本Diff展示 |
| Story-META-004 | 模型发布 | P1 | 审批流集成（Feishu审批）、发布锁定机制 |

---

### Feature 2：元数据采集（FEAT-DMT-METADATA-COLLECT）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-META-005 | 新建采集任务 | P0 | 多数据源连接器（MySQL/PG/Oracle/Hive/API）、密码加密存储（CBC）、Cron调度 |
| Story-META-006 | 采集任务执行 | P0 | 异步任务队列（Celery/xxl-job）、进度实时推送（WebSocket/SSE）、断点续传 |
| Story-META-007 | 采集结果查看 | P0 | 分页查询优化（游标分页 vs OFFSET）、Excel导出（流式写入） |
| Story-META-008 | 手动录入元数据 | P1 | Excel解析（openpyxl）、批量写入事务、格式校验规则引擎 |

---

### Feature 3：标签管理（FEAT-DMT-ASSET-MANAGE-TAG）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-META-009 | 标签定义 | P1 | 标签分类树设计（Nested Set 或 Closure Table）、内置标签保护 |
| Story-META-010 | 标签分配 | P1 | 多对多关系（资产-标签）、批量分配事务 |
| Story-META-011 | 标签检索 | P1 | 多标签组合过滤查询、倒排索引优化 |

---

### Feature 4：要素上下架（FEAT-DMT-ELEMENT-LISTING）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-META-012 | 要素上架申请 | P1 | 上架审批流触发（Feishu）、申请表单草稿机制 |
| Story-META-013 | 要素审批 | P1 | 审批结果回写、申请人通知（Feishu Bot） |
| Story-META-014 | 要素下架 | P1 | 下架软删除（is_deleted + 下架时间）、引用检查 |

---

### Feature 5：资产上下架（FEAT-DMT-ASSET-LISTING）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-META-015 | 资产上架申请 | P1 | 资产完整性校验（字段完整性/标签完整性） |
| Story-META-016 | 资产审批 | P1 | 同要素审批，可复用 |
| Story-META-017 | 资产下架 | P1 | 被服务引用检查、下架软删除 |

---

### Feature 6：资源上下架管理（FEAT-DMT-RESOURCE-LISTING）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-META-018 | 资源上下架管理 | P1 | 统一上下架操作抽象（要素/资产统一处理） |
| Story-META-019 | 资源状态查询 | P1 | 状态缓存（Redis）、状态变更历史记录 |

---

## 二、数据标准（EPIC-DMT_DATA_STD）

**Epic 优先级**: P0
**Story 数量**: 13
**状态**: 已上线（参考实现）

---

### Feature 1：标准字典（FEAT-DMT-STD-DICT）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-STD-001 | 字典浏览 | P1 | 分类筛选（多级分类）、分页查询 |
| Story-STD-002 | 字典搜索 | P1 | 全文搜索（Elasticsearch/数据库LIKE）、关键词高亮 |
| Story-STD-003 | 字典管理 | P1 | 唯一性约束（标准编码）、软删除 |

---

### Feature 2：标准定义（FEAT-DMT-STD-DEFINE）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-STD-004 | 创建标准定义 | P0 | 富文本编辑器（Monaco/Ace）、结构化规则表达式解析 |
| Story-STD-005 | 编辑标准定义 | P0 | 版本号自动递增（语义化版本）、草稿/已发布状态机 |
| Story-STD-006 | 标准版本管理 | P0 | 版本Diff、JSON Snapshot存储 |
| Story-STD-007 | 标准发布审批 | P1 | Feishu审批流集成 |

---

### Feature 3：标准映射（FEAT-DMT-STD-MAPPING）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-STD-008 | 创建标准映射 | P1 | 表/字段选择器（树形）、批量导入（Excel）、冲突检测算法 |
| Story-STD-009 | 映射列表管理 | P1 | 多条件筛选、列表导出 |
| Story-STD-010 | 映射冲突检测 | P1 | 冲突类型检测（一对多/多对一）、实时检测性能优化 |

---

### Feature 4：标准检查（FEAT-DMT-STD-CHECK）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-STD-011 | 执行标准检查 | P1 | 异步检查任务（大数据量）、进度推送 |
| Story-STD-012 | 检查报告查看 | P1 | 分层结果存储（汇总表/明细表）、导出性能 |
| Story-STD-013 | 检查结果整改 | P1 | 整改状态机、单独字段重新检查 |

---

## 三、数据服务（EPIC-DMT_DATA_SERVICE）

**Epic 优先级**: P0
**Story 数量**: 14（去重后）
**状态**: 已上线（参考实现）

---

### Feature 1：服务API（FEAT-DMT-SVC-API）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-SVC-001 | API创建 | P0 | API配置持久化、文档自动生成（OpenAPI/Swagger） |
| Story-SVC-002 | API配置管理 | P0 | 配置版本管理、操作日志表 |
| Story-SVC-003 | API上下线 | P0 | 上线审批流、AppKey/AppSecret生成（JWT/HS256）、密钥安全存储 |

---

### Feature 2：服务建模（FEAT-DMT-SVC-MODEL）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-SVC-004 | 模型创建 | P1 | 数据源绑定、字段映射配置 |
| Story-SVC-005 | 模型配置 | P1 | 数据源切换兼容性检查、版本管理 |

---

### Feature 3：服务查询（FEAT-DMT-SVC-QUERY）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-SVC-006 | 查询条件配置 | P1 | 动态Query Builder生成、过滤条件表达式解析 |
| Story-SVC-007 | 查询执行 | P1 | 动态SQL拼接、查询超时控制（30s）、结果集流式返回（大数据量） |

---

### Feature 4：服务监控（FEAT-DMT-SVC-MONITOR）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-SVC-008 | 监控大盘 | P1 | 指标聚合查询（调用量/响应时间/错误率）、时序数据存储（InfluxDB/TDengine） |
| Story-SVC-009 | 调用明细 | P1 | 日志存储（ES/ClickHouse）、分页查询优化 |

---

### Feature 5：服务目录（FEAT-DMT-SVC-CATALOG）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-SVC-010 | 目录浏览 | P1 | 分类树缓存（Redis）、懒加载 |
| Story-SVC-011 | 服务发现 | P1 | 全文搜索、ES聚合排序 |

---

### Feature 6：服务鉴权（FEAT-DMT-SVC-AUTH）

| Story ID | Story 名称 | 优先级 | 技术要点 |
|:---|:---|:---:|:---|
| Story-SVC-012 | API密钥管理 | P0 | AppKey生成（UUID）、AppSecret加密（bcrypt）、密钥禁用/启用状态 |
| Story-SVC-013 | 权限控制 | P0 | 白名单鉴权中间件、批量授权事务、权限变更即时生效（缓存失效） |
| Story-SVC-014 | 配额管理 | P1 | 配额计数器（Redis INCR + EXPIRE）、配额耗尽返回429、告警阈值检测 |

---

## 四、技术关注点汇总

### 高优先级技术风险

| 风险点 | Epic | 说明 | 建议 |
|:---|:---|:---|:---|
| 大数据量采集性能 | 元数据采集 | 单次采集万级表，全量遍历 | 分批采集 + 增量采集 + 异步队列 |
| 动态SQL安全 | 数据服务 | 查询条件动态拼接 | 参数化查询 + 白名单字段过滤 |
| 定时任务调度 | 元数据采集/标准检查 | 多任务并行/依赖管理 | xxl-job / Airflow |
| 服务调用限流 | 数据服务 | 配额精准计数 | Redis Token Bucket / 滑动窗口 |
| 版本Diff展示 | 元数据建模/标准定义 | JSON结构深比较 | JSON Diff算法（deepequal/jsondiff） |

### 复用组件建议

| 组件 | Epic | 说明 |
|:---|:---|:---|
| 审批流 | 全部 | Feishu审批SDK统一接入 |
| 操作日志 | 全部 | AOP拦截统一写入 |
| 通知服务 | 全部 | Feishu Bot统一通知 |
| 状态机 | 元数据上下架/标准发布/服务上下线 | 统一状态机设计 |
| Excel导入导出 | 元数据录入/检查报告 | 统一工具类 |

---

## 五、工作量估算参考

| Epic | Story数 | 预估工时 | 备注 |
|:---|:---:|---:|:---|
| 元数据管理 | 19 | 15-20人日 | 采集任务和版本管理较复杂 |
| 数据标准 | 13 | 8-10人日 | 已有参考实现，重点在检查引擎 |
| 数据服务 | 14 | 12-15人日 | 鉴权和监控有技术挑战 |
| **合计** | **48** | **35-45人日** | |

---

🦾 *PD-DMT 功能清单 v2.0 | Tony Stark → 钟离*

---

## 六、前端 Demo 优先级说明

**文博明确：只需前端 Demo，后端不关心**

### Demo 范围判定

| Demo 优先级 | 含义 | 后端处理 |
|:---:|:---|:---|
| 🔴 P0 Demo必须 | 前端 Demo 核心，必须有完整 UI/交互 | 模拟数据（JSON/Mock） |
| 🟡 P1 Demo重要 | 有完整 UI，数据可静态模拟 | 轻量 Mock（可有可无） |
| 🟢 S2 后端关注 | 前端 UI 简单或无 UI，主要看后端逻辑 | 真实后端实现 |

### 按 Epic 分类

#### 元数据管理（19 Story）

| Story | 名称 | Demo优先级 | 后端处理 | 关键UI组件 |
|:---|:---|:---:|:---:|:---|
| META-001 | 创建元数据模型 | 🔴 P0 | Mock | 模型表单+字段编辑器+拖拽排序 |
| META-002 | 编辑元数据模型 | 🔴 P0 | Mock | 已有模型编辑+版本Diff |
| META-003 | 模型版本管理 | 🔴 P0 | Mock | 版本历史列表+版本对比视图 |
| META-004 | 模型发布 | 🔴 P0 | Mock | 发布按钮+审批状态展示 |
| META-005 | 新建采集任务 | 🔴 P0 | Mock | 数据源配置表单+连接测试 |
| META-006 | 采集任务执行 | 🟡 P1 | Mock | 执行进度条+日志滚动 |
| META-007 | 采集结果查看 | 🟡 P1 | Mock | 表列表+字段详情+导出按钮 |
| META-008 | 手动录入元数据 | 🔴 P0 | Mock | Excel上传+预览表格+格式校验反馈 |
| META-009 | 标签定义 | 🔴 P0 | Mock | 标签分类树+增删改操作 |
| META-010 | 标签分配 | 🔴 P0 | Mock | 标签选择器+批量分配 |
| META-011 | 标签检索 | 🔴 P0 | Mock | 多标签筛选+结果列表 |
| META-012 | 要素上架申请 | 🟡 P1 | Mock | 上架表单+提交状态 |
| META-013 | 要素审批 | 🟡 P1 | Mock | 审批操作按钮+通过/拒绝 |
| META-014 | 要素下架 | 🟡 P1 | Mock | 下架表单+确认Dialog |
| META-015 | 资产上架申请 | 🟡 P1 | Mock | 同要素上架 |
| META-016 | 资产审批 | 🟡 P1 | Mock | 同要素审批 |
| META-017 | 资产下架 | 🟡 P1 | Mock | 同要素下架 |
| META-018 | 资源上下架管理 | 🟡 P1 | Mock | 统一操作面板 |
| META-019 | 资源状态查询 | 🟢 S2 | 无 | 状态标签展示 |

#### 数据标准（13 Story）

| Story | 名称 | Demo优先级 | 后端处理 | 关键UI组件 |
|:---|:---|:---:|:---:|:---|
| STD-001 | 字典浏览 | 🔴 P0 | Mock | 字典列表+分类筛选+分页 |
| STD-002 | 字典搜索 | 🔴 P0 | Mock | 搜索框+实时过滤+高亮 |
| STD-003 | 字典管理 | 🔴 P0 | Mock | 新增/编辑/禁用操作 |
| STD-004 | 创建标准定义 | 🔴 P0 | Mock | 标准定义表单+口径规则编辑器 |
| STD-005 | 编辑标准定义 | 🔴 P0 | Mock | 表单编辑+版本提示 |
| STD-006 | 标准版本管理 | 🔴 P0 | Mock | 版本历史+Diff对比 |
| STD-007 | 标准发布审批 | 🟡 P1 | Mock | 提交审批+审批状态 |
| STD-008 | 创建标准映射 | 🔴 P0 | Mock | 表/字段选择树+映射配置表 |
| STD-009 | 映射列表管理 | 🔴 P0 | Mock | 映射列表+筛选+导出 |
| STD-010 | 映射冲突检测 | 🟡 P1 | Mock | 冲突Warning面板 |
| STD-011 | 执行标准检查 | 🔴 P0 | Mock | 检查配置+进度条+结果Dialog |
| STD-012 | 检查报告查看 | 🔴 P0 | Mock | 报告列表+详情+导出 |
| STD-013 | 检查结果整改 | 🟡 P1 | Mock | 整改确认Dialog+重新检查 |

#### 数据服务（14 Story）

| Story | 名称 | Demo优先级 | 后端处理 | 关键UI组件 |
|:---|:---|:---:|:---:|:---|
| SVC-001 | API创建 | 🔴 P0 | Mock | API创建表单+参数配置 |
| SVC-002 | API配置管理 | 🔴 P0 | Mock | 配置详情+编辑+日志 |
| SVC-003 | API上下线 | 🔴 P0 | Mock | 上线申请+审批状态+密钥展示 |
| SVC-004 | 模型创建 | 🟡 P1 | Mock | 模型配置表单+字段映射 |
| SVC-005 | 模型配置 | 🟡 P1 | Mock | 模型编辑+版本管理 |
| SVC-006 | 查询条件配置 | 🔴 P0 | Mock | 查询字段配置+过滤方式选择 |
| SVC-007 | 查询执行 | 🔴 P0 | Mock | API调试台+请求/响应展示 |
| SVC-008 | 监控大盘 | 🔴 P0 | Mock | 指标卡片+趋势图+服务列表 |
| SVC-009 | 调用明细 | 🟡 P1 | Mock | 调用列表+详情Dialog |
| SVC-010 | 目录浏览 | 🔴 P0 | Mock | 分类树+服务卡片列表 |
| SVC-011 | 服务发现 | 🔴 P0 | Mock | 搜索框+结果列表 |
| SVC-012 | API密钥管理 | 🟡 P1 | Mock | 密钥列表+重新生成/禁用 |
| SVC-013 | 权限控制 | 🟡 P1 | Mock | 白名单配置+添加/移除 |
| SVC-014 | 配额管理 | 🟡 P1 | Mock | 配额表格+进度条+阈值配置 |

---

### 前端 Demo 技术选型建议

| 用途 | 技术 | 说明 |
|:---|:---|:---|
| 组件库 | React 18 + Ant Design 5 | 完整组件生态，表格/表单/Dialog全覆盖 |
| 拖拽排序 | @dnd-kit 或 react-beautiful-dnd | 模型字段拖拽 |
| 富文本编辑器 | @monaco-editor/react | 标准口径规则编辑 |
| 图表/趋势 | @ant-design/charts 或 Recharts | 监控大盘趋势图 |
| Mock 数据 | Mock.js 或 静态 JSON | 前端内置模拟数据 |
| 状态管理 | Zustand / React Context | 表单状态/全局状态 |
| 路由 | React Router v6 | 多页 Demo 切换 |

### Demo 可跳过项（后端关注）

以下 Story 前端工作量小但后端复杂，Demo 阶段可暂不完整：

- META-006 采集任务执行（进度实时推送需要 WebSocket，Demo 用静态进度条替代）
- SVC-009 调用明细（日志量大的查询，Demo 用静态列表替代）
- STD-011 执行标准检查（大数据量检查引擎，Demo 用模拟结果替代）

---

🦾 *前端 Demo 优先，后端 Mock 处理。钟离按 P0 排期即可。*
