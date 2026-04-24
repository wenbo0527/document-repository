---
name: code-review
description: 多维度代码审查。适用于任何代码合并前、feature实现完成后、agent产出评估、代码重构后、bug修复后。审查覆盖五个维度：正确性、可读性、架构、安全、性能。本地项目包括：数据社区(data_community)、产品管理系统(product-*)、Agent Dashboard(agent_work/Zhongli/)。
---

# Code Review and Quality (本地定制版)

## Overview

多维度代码审查，质量门禁不可跳过。审查覆盖五个维度：正确性、可读性、架构、安全、性能。

**审批标准**：代码确实提升了整体代码健康度就批准，不需要完美。完美不存在——目标是持续改进。不要因为"不是我的写法"就拒绝。

## 本地项目特殊规则

### 项目路径

| 项目 | 路径 | 技术栈 | 审查重点 |
|------|------|--------|----------|
| 数据社区 | `~/Documents/project/data_community/` | Vue 3 + Vite + TypeScript + Arco Design | 组件规范、Arco Design 遵守 |
| 产品管理系统 | `~/Documents/project/product/` | Spring Boot + Vue 3 + Neo4j | API 契约、后端规范 |
| Agent Dashboard | `~/Documents/05_AgentOutput/agent_work/Zhongli/` | React + TypeScript + Express | 架构一致性 |

### 本地编码约束

**禁止修改**：
- `accompany.ts` — 核心业务定义文件
- `calculation.ts` — 计算公式统一使用已有方法

**必须遵守**：
- 路由更新必须同步修改侧边栏菜单配置
- 组件使用 `<script setup>` 语法
- Arco Design 组件替代（如用 `IconBarChart` 替代不存在的 `IconHistogram`）

### 变更大小规范

```
~100 行   → ✅ 良好，一次审查完
~300 行   → ⚠️ 可接受，单个逻辑变化
~500+ 行  → ❌ 太大，必须拆分
```

## The Five-Axis Review

### 1. Correctness（正确性）

- [ ] 代码行为与需求一致
- [ ] 边界情况处理（null、空值、边界值）
- [ ] 错误路径处理
- [ ] 是否修改了禁止修改的文件（`accompany.ts`、`calculation.ts`）
- [ ] 测试是否覆盖了正确行为

### 2. Readability & Simplicity（可读性）

- [ ] 命名清晰，与项目命名规范一致
- [ ] 控制流直接，无深层嵌套
- [ ] 代码逻辑分组清晰
- [ ] 无"聪明"技巧需要简化
- [ ] 死代码检查：无 `temp`、`data`、`result` 等无意义命名
- [ ] 注释仅用于非显而易见的地方

### 3. Architecture（架构）

- [ ] 遵循现有模式
- [ ] 模块边界清晰
- [ ] 无重复代码应共享
- [ ] 依赖方向正确，无循环依赖
- [ ] 抽象层级适当

### 4. Security（安全）

- [ ] 用户输入验证和清洗
- [ ] 无 secrets 在代码、日志、版本控制中
- [ ] 认证/授权检查到位
- [ ] SQL 查询参数化
- [ ] 输出编码防止 XSS
- [ ] 外部数据源（API、日志、用户内容、配置文件）视为不可信

### 5. Performance（性能）

- [ ] 无 N+1 查询模式
- [ ] 无无界循环或无约束数据获取
- [ ] 应异步的同步操作已异步
- [ ] UI 组件无不必要的重渲染
- [ ] 列表端点有分页

## 本地项目特殊检查项

### 数据社区项目

```markdown
### 数据社区审查清单
- [ ] 组件使用 Arco Design（不是原生 HTML 或其他 UI 库）
- [ ] 无使用 `IconHistogram`（替换为 `IconBarChart`）
- [ ] 侧边栏菜单配置与路由同步
- [ ] WebSocket 连接处理（远程服务器无 WebSocket 端点）
- [ ] SPA 路由使用 `-s` 参数或 `try_files` fallback
```

### 产品管理系统

```markdown
### 产品管理系统审查清单
- [ ] API 端点符合 RESTful 规范
- [ ] controller 不为空（当前为已知问题，记录但不拒绝）
- [ ] Neo4j 连接配置正确
- [ ] 无 hardcoded 密码或密钥
```

## Review Process

### Step 1: 理解上下文

```
- 这个变更要实现什么？
- 符合哪个 spec 或 task？
- 期望的行为变化是什么？
```

### Step 2: 先审查测试

```
- 测试是否存在？
- 测试行为还是实现细节？
- 边界情况覆盖？
- 测试命名描述清晰？
```

### Step 3: 审查实现

```
逐文件审查：
1. 正确性：代码行为与测试一致？
2. 可读性：不看帮助能理解？
3. 架构：符合系统设计？
4. 安全：漏洞？
5. 性能：瓶颈？
```

### Step 4: 分类发现

| 前缀 | 含义 | 作者操作 |
|------|------|----------|
| *(无前缀)* | 必要修改 | 合并前必须处理 |
| **Critical:** | 阻断合并 | 安全漏洞、数据丢失、功能破坏 |
| **Nit:** | 次要可选 | 可忽略——格式、风格偏好 |
| **Optional:** | 建议 | 值得考虑但非必须 |
| **FYI** | 信息性 | 不需要操作——为未来参考 |

### Step 5: 验证验证

```
- 运行了什么测试？
- 构建通过？
- 手动测试过？
- UI 变更有截图？
- 有前后对比？
```

## Multi-Agent 审查模式

```
Agent A 写代码
    │
    ▼
Agent B 审查（正确性 + 架构视角）
    │
    ▼
Agent A 修复问题
    │
    ▼
Human 最终确认（Checkpoint）
```

## Dead Code 检查

重构后检查孤立代码：

```
发现死代码：
- src/utils/date.ts 中的 formatLegacyDate() — 已由 formatDate() 替代
- src/components/ 中的 OldTaskCard — 已由 TaskCard 替代
- src/config.ts 中的 LEGACY_API_URL — 无引用

→ 请确认是否删除？
```

## 本地 Checkpoint 规则

**关键阶段必须人工确认**：

| 阶段 | 必须确认 |
|------|----------|
| 代码审查通过 | ✅ 需要人工确认（派蒙或文博） |
| 构建成功 | ✅ 需要验证 |
| 部署到生产 | ❌ 不允许 agent 自行部署 |

## Common Rationalizations

| 借口 | 真相 |
|------|------|
| "能用就行" | 能用但不可读、不安全、架构错误的代码会产生债务 |
| "我写的我知道是对的" | 作者对自己的代码有盲点 |
| "以后再清理" | 以后永远不会来，审查是质量门禁 |
| "AI 生成的代码应该没问题" | AI 代码需要更多审查，不是更少 |
| "测试过了所以没问题" | 测试必要不充分，不捕获架构、安全、可读性问题 |

## Verification

审查完成后：

- [ ] 所有 Critical 问题已解决
- [ ] 所有必要问题已解决或明确延期（附理由）
- [ ] 测试通过
- [ ] 构建成功
- [ ] 验证记录已文档化

## 参考资料

本地项目详细规范见 `references/local-project-rules.md`
