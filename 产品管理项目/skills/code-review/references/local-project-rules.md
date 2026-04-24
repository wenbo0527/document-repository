# 本地项目审查规则

## 项目概览

### 数据社区 (data_community)

**路径**: `~/Documents/project/data_community/`

**技术栈**: Vue 3 + Vite + TypeScript + Arco Design

**架构约束**:
- UI 组件库：统一使用 Arco Design
- 核心约束：
  - **禁止修改** `accompany.ts` 中的定义
  - 计算公式统一使用 `calculation.ts` 中的现有方法
  - 路由更新需同步修改侧边栏菜单配置

**代码规范**:
- 使用 `<script setup>` 语法
- 遵循 TypeScript 类型定义规范
- 关键步骤需添加日志输出便于调试

**已知问题**:
- `IconHistogram` 不存在于 Arco Design v2.57.0 → 使用 `IconBarChart` 替代
- WebSocket 连接失败（远程服务器无 WebSocket 端点）
- SPA 路由需使用 `-s` 参数 fallback 到 index.html

### 产品管理系统 (product)

**路径**: `~/Documents/project/product/`

**技术栈**: Spring Boot + Vue 3 + Neo4j

**架构**:
- 前端：`product-frontend` (端口 4000)
- 后端：`product-backend` (端口 8080)
- 数据库：Neo4j (端口 7687/7474)
- PM2 管理

**已知问题**:
- controller 目录为空，所有 REST API 返回 404
- 后端框架正常但业务 API 完全缺失

**安全约束**:
- 数据库不暴露公网，仅通过 Tailscale 内网访问
- API 路径 `/api/` 代理到 product-backend:8080

### Agent Dashboard

**路径**: `~/Documents/05_AgentOutput/agent_work/Zhongli/`

**技术栈**: React + TypeScript + Express

**架构**: Agent 任务管理看板

---

## 变更大小规范

| 大小 | 行数 | 说明 |
|------|------|------|
| ✅ 合适 | ~100 行 | 一次审查完 |
| ⚠️ 可接受 | ~300 行 | 单个逻辑变化 |
| ❌ 太大 | ~500+ 行 | 必须拆分 |

## 分支命名规范

```
feature/<描述>       → feature/task-creation
fix/<描述>           → fix/duplicate-tasks
chore/<描述>         → chore/update-deps
refactor/<描述>      → refactor/auth-module
```

## Commit Message 规范

```
<type>: <简短描述>

<可选的详细正文，解释为什么>
```

**Type**:
- `feat` — 新功能
- `fix` — Bug 修复
- `refactor` — 重构（无功能变化）
- `test` — 测试
- `docs` — 文档
- `chore` — 工具、依赖、配置

## Checkpoint 规则

| 阶段 | 人工确认 | 说明 |
|------|:--------:|------|
| 需求定义 | ✅ | 派蒙确认 |
| 任务拆分 | ✅ | 派蒙确认 |
| 代码审查 | ✅ | 钟离或文博确认 |
| 构建成功 | 自动 | CI/CD 验证 |
| 部署到生产 | ❌ | 必须文博手动执行 |

---

*最后更新：2026-04-20*
