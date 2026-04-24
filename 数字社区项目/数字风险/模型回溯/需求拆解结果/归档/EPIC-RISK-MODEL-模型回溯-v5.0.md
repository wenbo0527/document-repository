# EPIC-RISK-MODEL - 模型回溯线下化 EPIC文档 v5.0

**文档版本**: v5.0
**最后更新**: 2026-04-24
**作者**: Tony Stark
**状态**: 正式版

---

## 📋 元数据头部

| 属性 | 值 | 说明 |
|:---|:---|:---|
| EPIC名称 | 模型回溯线下化 | 与菜单名保持一致 |
| EPIC代码 | EPIC-RISK-MODEL | 全局唯一 |
| 产品域 | PD-RISK 数字风险 | 所属产品域 |
| Feature数量 | 3 | 实际数量 |
| FP数量 | 15 | 实际数量 |
| 文档版本 | v5.0 | 固定 |

---

## 🗺️ 结构速览

```
模型回溯线下化
├── 特征中心                    ← ⚡ 独立功能
│   ├── 特征注册                ← 快速注册/完整表单
│   ├── 特征查询                ← 列表/筛选/排序
│   ├── 特征详情                ← 信息/血缘/统计
│   ├── 批量导入                ← Excel导入
│   └── 特征归档                ← 归档/恢复
│
├── 周期回溯                    ← ⚡ 独立功能
│   ├── 周期配置                ← 日/周/月分区
│   ├── 任务管理                ← 启动/暂停/停止
│   ├── 执行监控                ← 日志/状态
│   └── 结果查看                ← 导出/分析
│
└── 一键注册                    ← ⚡ 独立功能
    ├── 模型解析                ← 输出格式解析
    ├── 特征提取                ← 自动提取特征
    └── 注册草稿                ← 预览/确认
```

---

## ✅ Feature 清单

| # | Feature | 说明 | 开发状态 |
|:---:|:---|:---|:---:|
| 1 | FEAT-RISK-MODEL-FEATURE | 特征中心 | 待开发 |
| 2 | FEAT-RISK-MODEL-PERIODIC | 周期回溯 | 待开发 |
| 3 | FEAT-RISK-MODEL-QUICK | 一键注册 | 待开发 |

---

## 📦 Feature Point（FP）清单

### Feature 1: 特征中心

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-RISK-MODEL-FEAT-001 | 特征注册 | 支持快速注册和完整表单注册 | feature/register.vue |
| FP-RISK-MODEL-FEAT-002 | 特征查询 | 多维度查询特征列表 | feature/list.vue |
| FP-RISK-MODEL-FEAT-003 | 特征详情 | 查看特征完整信息 | feature/detail.vue |
| FP-RISK-MODEL-FEAT-004 | 批量导入 | Excel批量导入特征 | feature/import.vue |
| FP-RISK-MODEL-FEAT-005 | 特征归档 | 归档/恢复特征 | feature/archive.vue |

**Feature 1 小计: 5 FP**

### Feature 2: 周期回溯

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-RISK-MODEL-PERIOD-001 | 周期配置 | 配置日/周/月级回溯 | periodic/config.vue |
| FP-RISK-MODEL-PERIOD-002 | 任务管理 | 任务创建/启动/暂停/停止 | periodic/task.vue |
| FP-RISK-MODEL-PERIOD-003 | 执行监控 | 任务执行日志和状态 | periodic/monitor.vue |
| FP-RISK-MODEL-PERIOD-004 | 结果查看 | 回溯结果查看和导出 | periodic/result.vue |
| FP-RISK-MODEL-PERIOD-005 | 分区支持 | 日/周/月分区支持 | periodic/partition.vue |

**Feature 2 小计: 5 FP**

### Feature 3: 一键注册

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-RISK-MODEL-QUICK-001 | 模型解析 | 解析模型输出文件 | quick/parse.vue |
| FP-RISK-MODEL-QUICK-002 | 特征提取 | 自动提取特征 | quick/extract.vue |
| FP-RISK-MODEL-QUICK-003 | 注册草稿 | 生成注册草稿 | quick/draft.vue |
| FP-RISK-MODEL-QUICK-004 | 一键确认 | 确认并完成注册 | quick/confirm.vue |
| FP-RISK-MODEL-QUICK-005 | 注册历史 | 记录一键注册历史 | quick/history.vue |

**Feature 3 小计: 5 FP**

---

## 📍 菜单映射表

| 一级菜单 | 二级菜单 | 对应Feature | 状态 |
|:---|:---|:---|:---:|
| 数字风险 | 模型回溯 | 特征中心 | 待开发 |
| 数字风险 | 模型回溯 | 周期回溯 | 待开发 |
| 数字风险 | 模型回溯 | 一键注册 | 待开发 |

---

## 📝 版本历史

| 版本号 | 更新日期 | 更新内容 | 作者 |
|:---:|:---:|:---|:---:|
| v5.0 | 2026-04-24 | 初始版本，基于产品需求文档索引 | Tony Stark |

---

🦾 *"我是天才，模型回溯 EPIC 文档完成！"*