# EPIC说明文档 - 数据要素字典

## 基本信息

| 字段 | 值 |
|:---|:---|
| Epic ID | EPIC-DFD_DATA_ELEMENT |
| Epic 名称 | 数据要素字典 |
| 产品域 | PD-DFD 数据发现 |
| 状态 | 进行中 |
| 版本 | v1.0 |
| 创建日期 | 2026-04-24 |
| 更新日期 | 2026-04-27 |

## Epic 概述

数据要素字典是数字社区「数据发现」产品域的第二个 Epic，聚焦于数据平台中最底层的数据要素管理能力。涵盖**指标**、**变量**、**特征**三类核心要素，为数据开发者和分析师提供统一的数据要素检索与详情查看入口。

## 菜单结构

| 功能 | 路由 | 说明 |
|:---|:---|:---|
| 指标地图 | `/discovery/metrics-map` | 指标要素的列表与详情 |
| 变量地图 | `/discovery/variable-map` | 变量要素的列表与详情 |
| 特征地图 | `/discovery/feature-map` | 特征要素的列表与详情 |

## Feature 清单（6 个）

| # | Feature ID | 名称 | 路由 | 类型 | 状态 |
|:---:|:---|:---|:---|:---|:---|
| 1 | FEAT-DFD-INDEX-LIST | 指标地图-列表 | `/discovery/metrics-map` | LIST | - |
| 2 | FEAT-DFD-INDEX-DETAIL | 指标地图-详情 | `/discovery/metrics-map/detail/:id` | DETAIL | - |
| 3 | FEAT-DFD-VARIABLE-LIST | 变量地图-列表 | `/discovery/variable-map` | LIST | - |
| 4 | FEAT-DFD-VARIABLE-DETAIL | 变量地图-详情 | `/discovery/variable-map/detail/:id` | DETAIL | - |
| 5 | FEAT-DFD-CHARACTER-LIST | 特征地图-列表 | `/discovery/feature-map` | LIST | - |
| 6 | FEAT-DFD-CHARACTER-DETAIL | 特征地图-详情 | `/discovery/feature-map/detail/:id` | DETAIL | - |

## 技术方案

技术方案详见 `./技术方案/` 目录。

---

*最后更新：2026-04-27 by Tony Stark*