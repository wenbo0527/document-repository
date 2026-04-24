# PRD Generation Skill

## 能做什么

基于 requirement-supplement 输出的完整需求说明，自动生成符合 v5.0 规范的 PRD 文档，包含 Feature 清单、FP 清单、菜单映射表、审批流接入点。

## 核心能力

1. **Feature 解析**：从需求说明中提取 Feature 和关联的 FP
2. **FP 拆解**：将 Feature 拆解为具体的功能点
3. **菜单映射**：关联功能点到菜单路径
4. **审批流接入**：标注审批流接入点和审批节点
5. **PRD 输出**：生成符合 v5.0 规范的 PRD 文档

## 激活条件

- **Skill 2 自动触发**：requirement-supplement 完成后自动进入（无需用户再次触发）
- 收到包含 REQ-{YYYYMMDD}-{序号} 的需求ID
- 用户明确要求生成 PRD（"生成 PRD"、"输出需求文档"）

---

## PRD v5.0 文档结构

| # | 章节 | 说明 |
|:---:|:---|:---|
| 1 | **元数据头部** | 产品域、Epic、优先级、状态、负责人 |
| 2 | **结构速览** | Epic-Feature-FP 层级关系 |
| 3 | **Feature 清单** | 所有 Feature 及关联 FP |
| 4 | **功能点(FP)清单** | 所有 FP 的详细描述 |
| 5 | **菜单映射表** | 功能点到菜单路径的映射 |
| 6 | **审批流接入点** | 审批流节点和接入条件 |
| 7 | **版本历史** | PRD 变更记录 |

---

## 步骤定义与边界

| 步骤 | 名称 | 输入 | 输出 | 边界责任 |
| S1 | 接收与解析 | requirement-supplement 输出 | 结构化需求 JSON | 只接收解析，不生成 |
| S2 | Feature 解析 | 需求 JSON | Feature 列表 | 只解析，不拆解 FP |
| S3 | FP 拆解 | Feature 列表 | FP 清单 | 只拆解，不映射菜单 |
| S4 | 菜单映射 | FP 清单 | 菜单映射表 | 只映射，不生成审批流 |
| S5 | 审批流接入 | 菜单映射 | 审批流接入点 | 只标注，不写 PRD |
| S6 | 输出 PRD | 所有步骤结果 | PRD 文档 | 汇总，不做修改 |

---

## 步骤流程图（Mermaid）

```mermaid
flowchart TD
    subgraph Trigger["触发入口"]
        A1["Skill 2 完成后自动触发"]
        A2["用户手动触发（生成PRD）"]
    end

    A1 --> B
    A2 --> B

    B["S1: 接收与解析"]
    B --> C["S2: Feature 解析"]
    C --> D["S3: FP 拆解"]
    D --> E["S4: 菜单映射"]
    E --> F["S5: 审批流接入"]
    F --> G["S6: 输出 PRD 文档"]
    G --> H["✅ Skill 3 完成"]
    H --> I["触发下一步: tony-zhongli-collaboration"]
```

---

## 每步校验机制

| 步骤 | 校验规则 | 校验失败处理 |
| S1 | 能解析出有效的 req_detail JSON | 无效 → 返回错误 |
| S2 | Feature 列表非空 | 为空 → 标注"无 Feature" |
| S3 | 每个 Feature 下有至少 1 个 FP | 无 FP → 自动生成默认 FP |
| S4 | 每个 FP 有对应的菜单路径 | 无路径 → 标注"待定" |
| S5 | 审批流接入点列表存在 | 为空 → 标注"无需审批" |

---

## 中间文档留存

| 步骤 | 中间文档路径 | 文件名格式 |
| S1 接收解析 | /tmp/prd/step1_received_{req_id}.json | 接收的原始 JSON |
| S2 Feature解析 | /tmp/prd/step2_features_{req_id}.json | Feature 列表 |
| S3 FP拆解 | /tmp/prd/step3_fps_{req_id}.json | FP 清单 |
| S4 菜单映射 | /tmp/prd/step4_menu_{req_id}.json | 菜单映射表 |
| S5 审批流 | /tmp/prd/step5_approval_{req_id}.json | 审批流接入点 |
| S6 最终输出 | /tmp/prd/PRD_{req_id}.md + .json | 最终 PRD |

---

## 重试机制

| 场景 | 最大重试次数 | 超过最大次数后 |
| S1 JSON 解析失败 | 1 | 直接返回错误 |
| S2 Feature 为空 | 1 | 输出空 PRD，标注缺失 |
| S3 FP 拆解失败 | 3 | 使用默认 FP 结构 |
| S4 菜单映射失败 | 1 | 标注"待定"继续 |
| S5 审批流失败 | 1 | 标注"无需审批" |

---

## PRD 元数据头部模板

```yaml
---
产品域: {PD-XX} - {产品域名称}
Epic: {Epic 名称}
Epic URI: {Epic:EPIC-XX-XXX}
优先级: {P0/P1/P2/P3}
状态: {draft/review/approved/archived}
负责人: {姓名}
PDM: {PDM姓名}
前端: {前端负责人}
后端: {后端负责人}
测试: {测试负责人}
创建日期: {YYYY-MM-DD}
更新日期: {YYYY-MM-DD}
版本: v1.0
---
```

---

## PRD 结构速览模板

```markdown
## 2. 结构速览

### Epic - Feature - FP 层级

| Epic | Feature | FP 数量 |
|:---|:---|:---:|
| {Epic名称} | {Feature名称} | {N} |
|      | {Feature名称} | {N} |
| **合计** | **{N}** | **{N}** |
```

---

## Feature 清单模板

```markdown
## 3. Feature 清单

| Feature ID | Feature 名称 | 优先级 | 状态 | 关联 FP |
|:---|:---|:---:|:---:|:---:|
| FEAT-{域}-{模块}-{特性} | {Feature名称} | P1 | 待开发 | 5 |
```

---

## FP 清单模板

```markdown
## 4. 功能点(FP)清单

### 4.1 {Feature名称}

| FP ID | 功能点 | 功能说明 | 优先级 | 验收标准 |
|:---|:---|:---|:---:|:---|
| FP-001 | {功能点名称} | {功能描述} | P1 | {验收标准} |
```

---

## 菜单映射表模板

```markdown
## 5. 菜单映射表

| 功能模块 | 一级菜单 | 二级菜单 | 三级菜单 | 路由路径 |
|:---|:---|:---|:---|:---|
| {模块名} | {菜单1} | {菜单2} | {菜单3} | /path/to/page |
```

---

## 审批流接入点模板

```markdown
## 6. 审批流接入点

| 审批节点 | 审批角色 | 接入条件 | 审批方式 |
|:---|:---|:---|:---|
| {节点名称} | {角色} | {条件} | {方式} |
```

---

## 版本历史模板

```markdown
## 7. 版本历史

| 版本 | 日期 | 作者 | 变更内容 |
|:---|:---|:---|:---|
| v1.0 | YYYY-MM-DD | {姓名} | 初始版本 |
```

---

## 错误处理原则

1. 错误在当前步骤内解决：不把错误传到下一步
2. 每步必须校验通过：校验失败 → 重试或标注
3. 中间文档可追溯：任何时候可查看中间文档
4. 重试有上限：超过最大重试次数后，输出错误提示，等待人工介入

---

## 依赖 Skill

| Skill | 关系 | 说明 |
| requirement-supplement | 前置 | 必须先完成需求补充 |
| tony-zhongli-collaboration | 后续 | PRD 生成完成后，进入 Tony-钟离协作 |

---

*Version: 1.0 | For: Tony Stark | Based: PRD v5.0 Template*
