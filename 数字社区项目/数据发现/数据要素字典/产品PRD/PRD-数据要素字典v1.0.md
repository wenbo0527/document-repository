---
neo4j:
  epic: "Epic:EPIC-DFD_xxx"
feishu:
  wiki: "V8KEfpg1vlkCZld"
doc:
  title: "PRD-数据要素字典v1.0"
  version: "v3.3"
  type: "PRD"
  productDomain: "PD-DFD"
  author: "Tony Stark"
  createdAt: "2026-04-28"
  updatedAt: "2026-04-29"
---

# PRD-数据要素字典 v1.0

产品需求文档 (PRD)
数据要素字典 (EPIC-DFD-ELEMENT) - 完整版

**文档版本**: v1.0
**创建日期**: 2026-04-24
**作者**: Tony Stark
**状态**: 正式版

---

## 一、产品概述

### 1.1 产品定位
数据要素字典是数据发现产品域的核心组成部分，提供统一的数据要素（字段/指标）定义、管理和检索能力，确保数据口径一致。

### 1.2 核心价值

| 价值 | 说明 |
|:---|:---|
| 口径统一 | 统一管理数据要素定义，确保口径一致 |
| 快速检索 | 多维度检索数据要素，提升查找效率 |
| 血缘追溯 | 追溯要素上下游血缘关系 |

---

## 二、产品架构

| Feature | 说明 | 优先级 | FP |
|:---|:---|:---:|:---:|
| FEAT-DFD-ELEMENT-TYPE | 要素类型管理 | P0 | 2 |
| FEAT-DFD-ELEMENT-DEF | 要素定义管理 | P0 | 3 |
| FEAT-DFD-ELEMENT-SEARCH | 要素检索 | P0 | 3 |
| FEAT-DFD-ELEMENT-STANDARD | 要素标准 | P1 | 2 |

---

## 三、功能详细说明

### 3.1 要素类型管理

| FP ID | 功能点 | 验收标准 |
|:---|:---|:---|
| FP-DFD-ELEMENT-TYPE-001 | 要素类型配置 | ✅ 功能：配置要素类型<br>✅ 操作：配置保存正常 |
| FP-DFD-ELEMENT-TYPE-002 | 要素类型查询 | ✅ 功能：查询类型列表<br>✅ 操作：列表展示正常 |

### 3.2 要素定义管理

| FP ID | 功能点 | 验收标准 |
|:---|:---|:---|
| FP-DFD-ELEMENT-DEF-001 | 要素创建 | ✅ 功能：创建要素<br>✅ 操作：创建流程正常 |
| FP-DFD-ELEMENT-DEF-002 | 要素编辑 | ✅ 功能：编辑要素<br>✅ 操作：编辑保存正常 |
| FP-DFD-ELEMENT-DEF-003 | 要素审核 | ✅ 功能：审核要素<br>✅ 操作：审核流程正常 |

### 3.3 要素检索

| FP ID | 功能点 | 验收标准 |
|:---|:---|:---|
| FP-DFD-ELEMENT-SEARCH-001 | 要素搜索 | ✅ 功能：搜索要素<br>✅ 操作：搜索响应正常 |
| FP-DFD-ELEMENT-SEARCH-002 | 要素详情 | ✅ 功能：查看详情<br>✅ 操作：详情展示正常 |
| FP-DFD-ELEMENT-SEARCH-003 | 要素血缘 | ✅ 功能：查看血缘<br>✅ 操作：血缘展示正常 |

### 3.4 要素标准

| FP ID | 功能点 | 验收标准 |
|:---|:---|:---|
| FP-DFD-ELEMENT-STD-001 | 标准要素库 | ✅ 功能：标准库管理<br>✅ 操作：标准库维护正常 |
| FP-DFD-ELEMENT-STD-002 | 要素映射 | ✅ 功能：映射管理<br>✅ 操作：映射配置正常 |

---

## 四、工作量汇总

| 优先级 | Feature | FP | 占比 |
|:---:|:---|:---:|:---:|
| P0 | 3个 | 8 | 80% |
| P1 | 1个 | 2 | 20% |

**总计: 10 FP**

---

🦾 *EPIC-DFD-ELEMENT 数据要素字典 PRD 完成！*