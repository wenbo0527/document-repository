# SOP-S6: Epic交付开发

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 草稿

---

## 1. 概述

### 1.1 目标

将 Epic 交付给开发团队，跟踪开发进度，完成验收

### 1.2 触发时机

- PRD 审核通过
- 需要启动开发

### 1.3 输入

- PRD v5.0 文档
- Spec 文档
- 任务列表

### 1.4 输出

- 开发完成确认
- Epic 状态更新为 COMPLETED

---

## 2. 处理流程

### 步骤 1: Epic 交付（IF-001）

**操作**：
1. Tony 准备 EPIC 交付包
2. 交付内容包括：
   - EPIC 文档
   - PRD 文档
   - Spec 文档
   - 任务列表
3. 更新 Epic 状态为 `PENDING`

**接口定义**：

| 项目 | 值 |
|:---|:---|
| 接口 | IF-001: EPIC 交付 |
| 方向 | Tony Stark → 钟离 |
| 内容 | EPIC 文档、技术要求、Spec |
| 状态 | PENDING |
| 触发 | PM 审核通过后 |

---

### 步骤 2: 技术评估

**操作**：
1. 钟离接收 EPIC
2. 技术可行性评估
3. 工时评估
4. 返回可行性报告

**接口定义**：

| 项目 | 值 |
|:---|:---|
| 接口 | IF-002: 技术可行性 |
| 方向 | 钟离 → Tony Stark |
| 内容 | 可行性报告、工时评估 |
| 状态 | APPROVED / NEED_REVISION / REJECTED |

---

### 步骤 3: 评审与确认

**决策**：

| 状态 | 操作 |
|:---|:---|
| APPROVED | 进入开发阶段 |
| NEED_REVISION | 修订后重新提交 |
| REJECTED | 终止或重新规划 |

**操作**：
1. Tony 审核可行性报告
2. 确认或要求修订
3. 通知钟离开始开发

---

### 步骤 4: 开发阶段

**操作**：
1. 钟离启动开发
2. 更新 Epic 状态为 `IN_PROGRESS`
3. Feature/Story 状态更新
4. Git 分支创建

**Git 工作流**：
```bash
# 创建开发分支
git checkout -b feature/EPIC-XX-XXX

# 提交代码
git add .
git commit -m "feat: EPIC-XX-XXX {description}"

# 创建 MR
git push -u origin feature/EPIC-XX-XXX
```

---

### 步骤 5: Story 验收（IF-003）

**操作**：
1. 钟离完成 Story 开发
2. Tony 执行 4 项验收：
   - 功能验收
   - 操作验收
   - 数据验收
   - 交互验收

**接口定义**：

| 项目 | 值 |
|:---|:---|
| 接口 | IF-003: Story 验收 |
| 方向 | Tony Stark → 钟离 |
| 内容 | Story 验收标准 |
| 状态 | ACCEPT / PARTIAL / REJECT |

**Story 验收标准（4项）**：

| 验收类型 | 检查内容 |
|:---|:---|
| 功能验收 | 功能是否完整、实现正确 |
| 操作验收 | 操作流程是否符合预期 |
| 数据验收 | 数据是否准确、计算正确 |
| 交互验收 | 界面交互是否友好 |

---

### 步骤 6: Epic 完成（IF-004）

**操作**：
1. 所有 Story 验收通过
2. 更新 Epic 状态为 `COMPLETED`
3. 钟离确认完成

**接口定义**：

| 项目 | 值 |
|:---|:---|
| 接口 | IF-004: 开发完成 |
| 方向 | 钟离 → Tony Stark |
| 内容 | 完成确认、问题列表 |
| 状态 | COMPLETED |

---

## 3. 接口汇总

| 接口 | 方向 | 内容 | 状态 |
|:---|:---|:---|:---|
| IF-001 | Tony → 钟离 | EPIC 文档、技术要求 | PENDING |
| IF-002 | 钟离 → Tony | 可行性报告、工时 | APPROVED/NEED_REVISION |
| IF-003 | Tony → 钟离 | Story 验收 | ACCEPT/PARTIAL/REJECT |
| IF-004 | 钟离 → Tony | 完成确认 | COMPLETED |

---

## 4. Epic 状态流转

```
DRAFT → PENDING → IN_PROGRESS → COMPLETED
         ↓
    NEED_REVISION
         ↓
    PENDING（重新提交）
```

---

## 5. 验收检查清单

**交付前**：
- [ ] EPIC 文档完整
- [ ] PRD 文档完整
- [ ] Spec 文档完整
- [ ] 任务列表完整

**开发中**：
- [ ] 技术可行性已评估
- [ ] 开发进度正常
- [ ] 代码符合规范

**验收时**：
- [ ] 功能验收通过
- [ ] 操作验收通过
- [ ] 数据验收通过
- [ ] 交互验收通过
- [ ] 代码已合并

**完成后**：
- [ ] Epic 状态为 COMPLETED
- [ ] 所有文档已更新
- [ ] 飞书状态已同步

---

## 6. 关联 Skill

| Skill | 用途 | 调用时机 |
|:---|:---|:---|
| `tony-zhongli-collaboration` | Tony-钟离协作 | 全流程 |
| `git-workflow` | Git 工作流 | 步骤4 开发阶段 |
| `code-review` | 代码审查 | 步骤4 代码审查 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
