# Wiki Maintenance Skill

> Wiki知识库维护标准化流程
> 版本: v1.1
> 创建: 2026-04-14
> 维护者: 尼克·弗瑞
> 
> **重要**: 本Skill整合了Wiki中已有的流程文档：
> - `wiki/process/ingest.md` - Ingest流程
> - `wiki/process/lint.md` - Lint检查流程
> - `wiki/process/content-quality-control.md` - 内容质量控制

---

## 触发条件

当以下情况时使用此Skill：
1. 需要引入新内容到Wiki → 执行 **Ingest流程**
2. 需要进行Wiki健康检查 → 执行 **Lint流程**
3. 需要更新index.md或log.md → 执行 **更新规范**
4. 发现Wiki中有问题需要修复 → 执行 **问题修复**
5. 用户要求"检查Wiki" → 执行 **Lint流程**

---

## Wiki流程文件位置

| 文件 | 路径 | 说明 |
|------|------|------|
| Ingest流程 | `/Users/wenbo/Documents/project/Wiki/wiki/process/ingest.md` | 信息消化标准流程 |
| Lint流程 | `/Users/wenbo/Documents/project/Wiki/wiki/process/lint.md` | 健康检查每周流程 |
| 内容质量控制 | `/Users/wenbo/Documents/project/Wiki/wiki/process/content-quality-control.md` | 内容质量标准 |

---

## 一、Ingest 流程（信息消化）

> 完整流程见 `wiki/process/ingest.md`

### 1.1 流程图

```
新信息到达
    ↓
Step 1: 判断类型 → 洞察/实体/主题/项目
    ↓
Step 2: 评估价值 → ⭐1-5星
    ↓
Step 3: 写入文档 → 按模板创建
    ↓
Step 4: 关联链接 → 双向链接
    ↓
Step 5: 记录更新 → 更新log.md
```

### 1.2 价值评级

| 评级 | 说明 | 处理方式 |
|------|------|---------|
| ⭐⭐⭐⭐⭐ | 卓越见解，开创新领域 | 立即写入insights/，通知派蒙 |
| ⭐⭐⭐⭐ | 高价值，扩展现有体系 | 写入insights/，补充相关Topic |
| ⭐⭐⭐ | 有价值，补充现有专题 | 更新相关Topic的内容 |
| ⭐⭐ | 待观察，补充有限 | 暂存sources/待定，定期回顾 |
| ⭐ | 无价值，不引入 | 归档到sources/rejected/ |

### 1.3 Topic归属判断

| Topic目录 | 覆盖范围 |
|------------|----------|
| `fintech/compliance` | 合规、监管、AML/KYC |
| `fintech/data-platform` | 数据中台、数仓、ETL、数据治理 |
| `fintech/infrastructure` | 云原生、K8s、DevOps、分布式 |
| `fintech/intelligent-systems` | 智能客服、智能信贷、支付 |
| `fintech/llm-finance` | LLM，大模型、RAG |
| `fintech/marketing-suite` | 营销、用户增长、A/B测试 |
| `fintech/open-banking` | 开放银行、API Bank |
| `fintech/risk-management` | 风控、反欺诈、信用评估 |
| `ai-native` | AI Native开发方法论 |
| `ai-programming` | AI编程实践（Vibe Coding、Superpowers等）|
| `analysis-frameworks` | 分析框架、方法论 |
| `product-management` | 产品管理（托尼负责）|

---

## 二、Lint 流程（健康检查）

> 完整流程见 `wiki/process/lint.md`

### 2.1 流程图

```
派蒙触发 Lint 检查
    ↓
Step 1: 孤立页面检查 → 无引用的页面
    ↓
Step 2: 过时内容检查 → 超过3个月未更新
    ↓
Step 3: 矛盾信息检查 → 同一实体描述矛盾
    ↓
Step 4: 链接完整性检查 → 双向链接/外部链接
    ↓
Step 5: 生成检查报告 → 更新log.md
```

### 2.2 检查清单

| 检查项 | 标准 | 处理 |
|--------|------|------|
| 孤立页面 | 无双向链接引用 | 添加链接或删除 |
| 过时内容 | Insights >3个月，Topics >6个月 | 标记【待更新】 |
| 矛盾信息 | 同一实体描述不一致 | 立即标记，协调解决 |
| 链接问题 | 双向链接失效 | 修复或删除 |

### 2.3 执行频率

| 检查类型 | 频率 | 执行人 |
|---------|------|--------|
| 快速检查 | 每日 | 自动 |
| 完整Lint | 每周日 | 派蒙触发，尼克执行 |
| 深度检查 | 每月末 | 派蒙协调，尼克执行 |

---

## 三、更新规范

### 3.1 文件命名

| 类型 | 格式 | 示例 |
|------|------|------|
| 洞察页 | `insight-YYYYMMDD-{slug}.md` | `insight-20260414-vibe-coding.md` |
| 主题页 | `kebab-case.md` | `llm-agent.md` |
| 实体页 | `{type}/{slug}.md` | `companies/openai.md` |
| Epic页 | `EPIC-{code}-{name}.md` | `EPIC-MKT_CAMPAIGN-营销活动.md` |

### 3.2 元信息模板

```markdown
> 来源: {信息来源}
> 整理时间: YYYY-MM-DD
> 维护者: {Agent名称}
> 评级: ⭐⭐⭐⭐⭐
```

### 3.3 内部链接规范

```markdown
# 正确格式
[[topics/ai-programming/README]] 或 [[ai-programming/README]]

# 错误格式
[AI编程](../topics/ai-programming/README.md)  ❌
```

### 3.4 更新规则

| 操作 | 必须更新 |
|------|----------|
| 新建Topic | index.md, log.md |
| 新建Insight | log.md |
| 移动文件 | index.md, log.md |
| 大幅修改 | log.md |

---

## 四、日志规范

### 4.1 log.md格式

```markdown
### YYYY-MM-DD

#### Ingest | {操作类型}

**新增/更新/删除 {类型}**

| 操作 | 页面 | 说明 |
|------|------|------|
| 新建 | [[page]] | 简要说明 |
| 更新 | [[page]] | 更新内容 |
| 删除 | page | 删除原因 |

#### Lint | Wiki健康检查

- 执行人: {派蒙/尼克}
- 检查页面数: {n}
- 发现问题数: {n}
- 已修复数: {n}
```

### 4.2 操作类型

| 类型 | 说明 |
|------|------|
| Ingest | 引入新资料 |
| Query | 回答问题产生 |
| Lint | 健康检查修复 |
| Refactor | 重构整理 |

---

## 五、快速检查命令

```bash
# Wiki根目录
WIKI_ROOT="/Users/wenbo/Documents/project/Wiki/wiki"

# 文件数
find "$WIKI_ROOT" -name "*.md" -type f | wc -l

# 检查重复
basename -a "$WIKI_ROOT"/**/*.md 2>/dev/null | sort | uniq -c | sort -rn | head -5

# 检查孤立（无内部链接）
for f in $(find "$WIKI_ROOT" -name "*.md" -type f); do
  links=$(grep -c "\[\[" "$f" 2>/dev/null || echo 0)
  if [ "$links" -eq 0 ] && [ "$(basename "$f")" != "README.md" ]; then
    echo "孤立: $(basename "$f")"
  fi
done

# 检查过时（超过3个月未更新）
find "$WIKI_ROOT/insights" -name "*.md" -mtime +90 -exec basename {} \;
```

---

## 六、内容质量标准

> 完整标准见 `wiki/process/content-quality-control.md`

### 6.1 事实核对
- [ ] 数据有来源引用
- [ ] 时间/数字准确
- [ ] 无明显错误

### 6.2 合规要求
- [ ] 无侵权内容
- [ ] 敏感信息脱敏
- [ ] 商业机密保护

### 6.3 风格表达
- [ ] 结构清晰
- [ ] 语言准确
- [ ] 格式统一

---

## 七、相关文件路径

| 文件 | 绝对路径 |
|------|----------|
| Wiki根目录 | `/Users/wenbo/Documents/project/Wiki/wiki/` |
| index.md | `/Users/wenbo/Documents/project/Wiki/wiki/index.md` |
| log.md | `/Users/wenbo/Documents/project/Wiki/wiki/log.md` |
| AGENT_COLLAB_GUIDE.md | `/Users/wenbo/Documents/project/Wiki/wiki/AGENT_COLLAB_GUIDE.md` |
| ingest.md | `/Users/wenbo/Documents/project/Wiki/wiki/process/ingest.md` |
| lint.md | `/Users/wenbo/Documents/project/Wiki/wiki/process/lint.md` |
| content-quality-control.md | `/Users/wenbo/Documents/project/Wiki/wiki/process/content-quality-control.md` |

---

## 八、问题修复

### 8.1 常见问题

| 问题 | 解决方案 |
|------|----------|
| 孤立页面 | 添加到相关专题的README，或删除 |
| 重复专题 | 合并到一处，更新index.md |
| 过时内容 | 更新日期或移至archive |
| 链接失效 | 修复或删除死链 |

### 8.2 修复流程

```
发现问题
    ↓
评估影响范围
    ↓
制定修复方案
    ↓
执行修复
    ↓
更新 index.md / log.md
    ↓
验证修复
```

---

*最后更新: 2026-04-14*
*版本: v1.1*
