# 产品管理系统 - API 接口规范 v1.0

> **版本**: v1.0
> **日期**: 2026-04-24
> **作者**: Tony Stark
> **状态**: 正式发布

---

## 1. 概述

本文档定义产品管理系统的 API 接口规范，基于 Vue 3 + TypeScript + Element Plus 技术栈。

### 1.1 基础信息

| 项目 | 值 |
|:---|:---|
| 基础URL | `/api/v1` |
| 数据格式 | JSON |
| 字符编码 | UTF-8 |
| 认证方式 | Bearer Token |

---

## 2. 通用响应格式

### 2.1 成功响应

```typescript
interface ApiResponse<T> {
  code: number      // 状态码，0表示成功
  message: string   // 响应消息
  data: T          // 响应数据
  timestamp: number // 时间戳
}
```

**示例**：
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "name": "营销画布"
  },
  "timestamp": 1713926400000
}
```

### 2.2 分页响应

```typescript
interface PageResult<T> {
  content: T[]           // 数据列表
  totalElements: number  // 总记录数
  totalPages: number     // 总页数
  size: number           // 每页大小
  number: number         // 当前页码
  first: boolean         // 是否第一页
  last: boolean          // 是否最后一页
}
```

### 2.3 错误响应

```json
{
  "code": 400,
  "message": "参数错误：缺少必填字段 name",
  "data": null,
  "timestamp": 1713926400000
}
```

### 2.4 HTTP 状态码

| 状态码 | 说明 |
|:---:|:---|
| 200 | 成功 |
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 401 | 未认证 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

## 3. 产品域接口

### 3.1 获取产品域列表

```
GET /api/v1/product-domains
```

**响应示例**：
```json
{
  "code": 0,
  "message": "success",
  "data": [
    {
      "id": 1,
      "uri": "ProductDomain:PD-MKT",
      "label": "数字营销",
      "code": "PD-MKT",
      "description": "数字营销产品域",
      "epicCount": 5,
      "featureCount": 37
    },
    {
      "id": 2,
      "uri": "ProductDomain:PD-RISK",
      "label": "数字风险",
      "code": "PD-RISK",
      "description": "数字风险产品域",
      "epicCount": 2,
      "featureCount": 16
    }
  ]
}
```

### 3.2 获取产品域详情

```
GET /api/v1/product-domains/{code}
```

**路径参数**：
| 参数 | 类型 | 说明 |
|:---|:---|:---|
| code | string | 产品域代码，如 PD-MKT |

---

## 4. Epic 接口

### 4.1 获取 Epic 列表

```
GET /api/v1/epics
```

**查询参数**：
| 参数 | 类型 | 说明 |
|:---|:---|:---|
| productDomain | string | 产品域代码（可选） |
| status | string | 状态（可选） |
| page | number | 页码（默认0） |
| size | number | 每页大小（默认20） |

### 4.2 获取 Epic 详情

```
GET /api/v1/epics/{epicCode}
```

### 4.3 创建 Epic

```
POST /api/v1/epics
```

**请求体**：
```json
{
  "epicCode": "EPIC-MKT-CANVAS",
  "name": "营销画布",
  "description": "营销画布功能模块",
  "productDomain": "PD-MKT",
  "priority": "P1",
  "status": "DRAFT"
}
```

### 4.4 更新 Epic

```
PUT /api/v1/epics/{epicCode}
```

### 4.5 删除 Epic

```
DELETE /api/v1/epics/{epicCode}
```

---

## 5. Feature 接口

### 5.1 获取 Feature 列表

```
GET /api/v1/features
```

**查询参数**：
| 参数 | 类型 | 说明 |
|:---|:---|:---|
| epicCode | string | Epic代码（可选） |
| productDomain | string | 产品域代码（可选） |

### 5.2 获取 Feature 详情

```
GET /api/v1/features/{featureCode}
```

### 5.3 创建 Feature

```
POST /api/v1/features
```

**请求体**：
```json
{
  "featureCode": "FEAT-MKT-CANVAS-001",
  "name": "画布设计器",
  "description": "拖拽式画布设计器",
  "epicCode": "EPIC-MKT-CANVAS",
  "priority": "P1"
}
```

---

## 6. Story 接口

### 6.1 获取 Story 列表

```
GET /api/v1/stories
```

**查询参数**：
| 参数 | 类型 | 说明 |
|:---|:---|:---|
| featureCode | string | Feature代码（可选） |
| status | string | 状态（可选） |

### 6.2 获取 Story 详情

```
GET /api/v1/stories/{storyCode}
```

### 6.3 创建 Story

```
POST /api/v1/stories
```

**请求体**：
```json
{
  "storyCode": "STORY-MKT-CANVAS-001-001",
  "name": "用户拖拽组件到画布",
  "asA": "运营人员",
  "iWant": "拖拽组件到画布",
  "soThat": "设计营销页面",
  "featureCode": "FEAT-MKT-CANVAS-001",
  "acceptanceCriteria": {
    "功能": "可拖拽组件到画布",
    "操作": "鼠标拖拽",
    "数据": "组件数据保存到数据库",
    "交互": "拖拽时有视觉反馈"
  }
}
```

---

## 7. 本体论接口

### 7.1 查询实体

```
GET /api/v1/ontology/entities
```

**查询参数**：
| 参数 | 类型 | 说明 |
|:---|:---|:---|
| type | string | 实体类型（Class/Individual/Property） |
| label | string | 标签关键词 |

### 7.2 查询关系

```
GET /api/v1/ontology/relationships
```

### 7.3 推理验证

```
POST /api/v1/ontology/reasoning
```

**请求体**：
```json
{
  "entityUri": "Epic:EPIC-MKT-CANVAS",
  "reasoningType": "VALIDATION"
}
```

---

## 8. 命名规范

### 8.1 URL 命名

- 使用小写字母
- 单词间用连字符 `-` 分隔
- 资源名称使用复数形式

**示例**：
```
GET /api/v1/product-domains
GET /api/v1/epics/{epicCode}
POST /api/v1/features
```

### 8.2 字段命名

- 使用 camelCase 驼峰命名
- 布尔值使用 is/has/can 前缀

**示例**：
```json
{
  "epicCode": "EPIC-MKT-CANVAS",
  "createdAt": "2026-04-24T10:00:00Z",
  "isActive": true
}
```

---

## 9. 认证与授权

### 9.1 认证方式

```
Authorization: Bearer <token>
```

### 9.2 错误码

| 错误码 | 说明 |
|:---:|:---|
| 40101 | Token 过期 |
| 40102 | Token 无效 |
| 40301 | 无访问权限 |

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark