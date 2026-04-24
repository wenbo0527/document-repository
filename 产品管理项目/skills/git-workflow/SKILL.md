---
name: git-workflow
description: Git 工作流规范。适用于任何代码变更：提交、分支、解决冲突、多任务并行处理。本地项目包括：数据社区(data_community, ~/Documents/project/)、产品管理系统(product/, ~/Documents/project/)、Agent Dashboard(~/)。所有代码变更必须遵循本规范。
---

# Git Workflow and Versioning (本地定制版)

## Overview

Git 是你的安全网。把提交当作存档点，分支当作沙盒，历史当作文档。AI agent 高速生成代码时，规范的版本控制是保持变更可管理、可审查、可回滚的机制。

## 本地项目分支规范

### 项目与分支路径

| 项目 | Git 仓库路径 | 默认分支 |
|------|-------------|---------|
| 数据社区 | `~/Documents/project/data_community/.git/` | main |
| 产品管理系统 | `~/Documents/project/product/.git/` | main |
| Agent Dashboard | `~/Documents/05_AgentOutput/agent_work/Zhongli/.git/` | main |

### 本地分支命名

```
<项目>/<类型>/<简短描述>

示例：
data_community/feature/new-dashboard
data_community/fix/sidebar-menu
product/refactor/api-layer
zhongli/chore/update-deps
```

## 核心原则

### 1. Trunk-Based Development

保持 `main` 始终可部署。工作在 1-3 天内合并的短生命周期分支中进行。

```
main ──●──●──●──●──●──●──●──●──●──  (始终可部署)
        ╲      ╱  ╲    ╱
         ●──●─╱    ●──╱    ← 短生命周期分支 (1-3 天)
```

### 2. 原子提交

每次提交做一件逻辑事：

```
✅ 良好：每提交自包含
git log --oneline
a1b2c3d 添加任务创建端点与验证
d4e5f6g 添加任务创建表单组件
h7i8j9k 连接表单到 API 并添加加载状态

❌ 糟糕：什么都混在一起
git log --oneline
x1y2z3a 添加任务功能、修复侧边栏、更新依赖、重构工具
```

### 3. 描述性提交信息

```
✅ 良好：解释 why，不只是 what
feat: 添加注册端点邮箱验证

阻止无效邮箱格式到达数据库。
使用 Zod schema 在路由处理器层验证，
与 auth.ts 中现有验证模式一致。

❌ 糟糕：描述显而易见的
update auth.ts
```

**格式**:
```
<type>: <简短描述>

<可选正文，解释为什么>
```

**Type**:
- `feat` — 新功能
- `fix` — Bug 修复
- `refactor` — 代码重构（无功能变化）
- `test` — 添加或更新测试
- `docs` — 仅文档
- `chore` — 工具、依赖、配置

### 4. 变更大小

```
~100 行   → ✅ 良好，易审查
~300 行   → ⚠️ 可接受，单个逻辑变化
~500+ 行  → ❌ 太大，拆分
```

### 5. 关注点分离

格式修改与行为修改分开。重构与功能分开。

```
✅ 良好：分离关注点
git commit -m "refactor: 提取验证逻辑到共享工具"
git commit -m "feat: 添加注册手机号验证"

❌ 糟糕：混合
git commit -m "重构验证并添加手机号字段"
```

## 本地项目 Worktree 使用

对于并行 AI agent 工作，使用 git worktree：

```bash
# 数据社区：创建功能分支 worktree
cd ~/Documents/project/data_community
git worktree add ../data-community-feature-a feature/new-dashboard

# 产品管理系统：创建修复分支 worktree
cd ~/Documents/project/product
git worktree add ../product-fix-api product/fix/api-endpoint

# 查看所有 worktree
git worktree list
```

**好处**：
- 多个 agent 可同时在不同功能上工作
- 无需分支切换
- 实验失败直接删除 worktree，无损失

## 变更总结模式

提交后提供结构化总结：

```
变更内容：
- src/routes/tasks.ts: POST 端点添加验证中间件
- src/lib/validation.ts: 使用 Zod 添加 TaskCreateSchema

未触及（有意为之）：
- src/routes/auth.ts: 有类似验证缺口但超出范围
- src/middleware/error.ts: 错误格式可改进（单独任务）

潜在问题：
- Zod schema 严格 — 拒绝额外字段。确认这是期望的。
- 添加 zod 为依赖（72KB gzip）— 已在 package.json 中
```

## 本地 Checkpoint 规则

**必须人工确认**：
- 合并到 main 前需要至少一个 reviewer 确认
- 部署到生产需要文博手动执行
- 危险操作（force push、删除分支）需要确认

## Pre-Commit 检查清单

```bash
# 1. 查看将要提交的内容
git diff --staged

# 2. 确保无 secrets
git diff --staged | grep -i "password\|secret\|api_key\|token"

# 3. 运行测试
npm test

# 4. 运行 lint
npm run lint

# 5. 运行类型检查
npx tsc --noEmit
```

## 本地 .gitignore 规范

每个项目必须有 `.gitignore` 覆盖：

```
node_modules/
dist/
.env
.env.local
*.pem
```

## 常见 Rationalizations

| 借口 | 真相 |
|------|------|
| "功能完成后再提交" | 一次巨大提交无法审查、调试、回滚 |
| "message 不重要" | message 是文档，未来需要理解变更原因 |
| "以后再 squash" | squash 破坏开发叙事 |
| "分支增加开销" | 短生命周期分支免费，防止冲突 |
| "以后再拆分变更" | 大变更更难审查、风险更高、更难回滚 |

## Red Flags

- 积累大量未提交变更
- "fix"、"update"、"misc" 类提交信息
- 格式修改与行为修改混合
- 项目无 `.gitignore`
- 提交 `node_modules/`、`.env` 或构建产物
- 长时间脱离 main 的分支
- 对共享分支 force push

## Verification

每次提交验证：

- [ ] 提交做了一件逻辑事
- [ ] message 解释 why，符合 type 规范
- [ ] 提交前测试通过
- [ ] diff 中无 secrets
- [ ] 格式修改与行为修改未混合
- [ ] `.gitignore` 覆盖标准排除项

## 参考资料

本地项目详细规范见 `references/local-project-rules.md`
