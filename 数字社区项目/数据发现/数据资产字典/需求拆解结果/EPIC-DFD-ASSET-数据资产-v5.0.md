# EPIC-DFD-ASSET - 数据资产 EPIC文档 v5.0

**文档版本**: v5.0
**最后更新**: 2026-04-24
**作者**: Tony Stark
**状态**: 正式版

---

## 📋 元数据头部

| 属性 | 值 | 说明 |
|:---|:---|:---|
| EPIC名称 | 数据资产 | 与菜单名保持一致 |
| EPIC代码 | EPIC-DFD-ASSET | 全局唯一 |
| 产品域 | PD-DFD 数据发现 | 所属产品域 |
| Feature数量 | 4 | 实际数量 |
| FP数量 | 16 | 实际数量 |
| 文档版本 | v5.0 | 固定 |

---

## 🗺️ 结构速览

```
数据资产
├── 资产注册                    ← ⚡ 独立功能
│   ├── 注册表单                ← 基本信息录入
│   ├── 资产分类选择            ← 分类体系
│   └── 标签配置                ← 标签管理
│
├── 资产分类                    ← ⚡ 独立功能
│   ├── 分类目录树              ← 树形结构
│   ├── 分类管理                ← CRUD操作
│   └── 分类统计                ← 资产数量统计
│
├── 资产标签                    ← ⚡ 独立功能
│   ├── 标签创建                ← 新建标签
│   ├── 标签编辑                ← 修改标签
│   └── 标签应用                ← 批量打标
│
└── 资产生命周期                ← ⚡ 独立功能
    ├── 生命周期配置            ← 阶段定义
    ├── 状态变更                ← 上下架
    └── 到期提醒                ← 预警通知
```

---

## ✅ Feature 清单

| # | Feature | 说明 | 开发状态 |
|:---:|:---|:---|:---:|
| 1 | FEAT-DFD-ASSET-REG | 资产注册 | 待开发 |
| 2 | FEAT-DFD-ASSET-CLASS | 资产分类 | 待开发 |
| 3 | FEAT-DFD-ASSET-TAG | 资产标签 | 待开发 |
| 4 | FEAT-DFD-ASSET-LIFE | 资产生命周期 | 待开发 |

---

## 📦 Feature Point（FP）清单

### Feature 1: 资产注册

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-DFD-ASSET-REG-001 | 注册表单 | 基本信息录入（名称/描述/负责人） | asset/register/form.vue |
| FP-DFD-ASSET-REG-002 | 资产分类选择 | 选择所属分类 | asset/register/category.vue |
| FP-DFD-ASSET-REG-003 | 标签配置 | 配置资产标签 | asset/register/tag.vue |
| FP-DFD-ASSET-REG-004 | 注册审批 | 提交注册审批流程 | asset/register/approval.vue |

**Feature 1 小计: 4 FP**

### Feature 2: 资产分类

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-DFD-ASSET-CLASS-001 | 分类目录树 | 树形结构展示分类 | asset/classify/tree.vue |
| FP-DFD-ASSET-CLASS-002 | 分类管理 | 新建/编辑/删除分类 | asset/classify/manage.vue |
| FP-DFD-ASSET-CLASS-003 | 分类统计 | 各分类资产数量统计 | asset/classify/stats.vue |
| FP-DFD-ASSET-CLASS-004 | 分类权限 | 按分类配置访问权限 | asset/classify/permission.vue |

**Feature 2 小计: 4 FP**

### Feature 3: 资产标签

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-DFD-ASSET-TAG-001 | 标签创建 | 创建新标签 | asset/tag/create.vue |
| FP-DFD-ASSET-TAG-002 | 标签编辑 | 修改已有标签 | asset/tag/edit.vue |
| FP-DFD-ASSET-TAG-003 | 标签删除 | 删除标签 | asset/tag/delete.vue |
| FP-DFD-ASSET-TAG-004 | 批量打标 | 批量为资产打标签 | asset/tag/batch.vue |

**Feature 3 小计: 4 FP**

### Feature 4: 资产生命周期

| FP ID | 功能点 | 说明 | 代码路径 |
|:---|:---|:---|:---|
| FP-DFD-ASSET-LIFE-001 | 生命周期配置 | 定义生命周期阶段 | asset/lifecycle/config.vue |
| FP-DFD-ASSET-LIFE-002 | 状态变更 | 资产上下架操作 | asset/lifecycle/status.vue |
| FP-DFD-ASSET-LIFE-003 | 到期提醒 | 资产到期前预警通知 | asset/lifecycle/alert.vue |
| FP-DFD-ASSET-LIFE-004 | 归档管理 | 归档资产的管理 | asset/lifecycle/archive.vue |

**Feature 4 小计: 4 FP**

---

## 📍 菜单映射表

| 一级菜单 | 二级菜单 | 对应Feature | 状态 |
|:---|:---|:---|:---:|
| 数据中台 | 数据资产 | 资产注册 | 待开发 |
| 数据中台 | 数据资产 | 资产分类 | 待开发 |
| 数据中台 | 数据资产 | 资产标签 | 待开发 |
| 数据中台 | 数据资产 | 资产生命周期 | 待开发 |

---

## 📝 版本历史

| 版本号 | 更新日期 | 更新内容 | 作者 |
|:---:|:---:|:---|:---:|
| v5.0 | 2026-04-24 | 初始版本，基于产品需求文档索引 | Tony Stark |

---

🦾 *"我是天才，数据资产 EPIC 文档完成！"*