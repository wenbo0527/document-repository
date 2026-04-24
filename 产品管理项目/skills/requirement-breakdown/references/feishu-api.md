# 飞书 API 规范

## 认证

```python
APP_ID = 'cli_a9283cfac6b9dbb6'
APP_SECRET = 'r5ekmgR3NY9ZRwtbzv8KbebyVmzx8DD6'

def get_token():
    r = requests.post(
        'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
        json={'app_id': APP_ID, 'app_secret': APP_SECRET},
        timeout=10
    )
    return r.json()['tenant_access_token']
```

**⚠️ token 有时效，每次请求前重新获取**

## 多维表格操作

### 常用端点

| 操作 | 方法 | 端点 |
|:---|:---|:---|
| 查询记录 | GET | `/bitable/v1/apps/{app_token}/tables/{table_id}/records` |
| 批量创建 | POST | `/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create` |
| 批量删除 | POST | `/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_delete` |
| 创建表 | POST | `/bitable/v1/apps/{app_token}/tables` |
| 删除表 | DELETE | `/bitable/v1/apps/{app_token}/tables/{table_id}` |
| 查字段 | GET | `/bitable/v1/apps/{app_token}/tables/{table_id}/fields` |

### 统一多维表格
```
APP_TOKEN = 'ANhxbU3MDabWsysyeI8c4t0mnfe'
Epic拆解总表 TABLE_ID = 'tblTckLegZWIOgTF'
```

### 字段类型

| type | 类型 |
|:---:|:---|
| 1 | 单行文本 |
| 2 | 数字 |
| 3 | 单选 |
| 4 | 多选 |
| 5 | 日期 |
| 7 | 复选框 |
| 11 | 多行文本 |
| 13 | 关联记录 |

### 批量限制
- 每批创建 ≤ 500 条（实际建议 20 条）
- 每批删除 ≤ 500 条（实际建议 20 条）
- 每批间隔 ≥ 0.3s 避免限流

## ⚠️ 常见错误

### 字段名 vs 字段 ID

```python
# ❌ 错误：使用字段 ID（batch_create 不支持）
{"fields": {"fldDVyjJQc": "1"}}  # 不生效

# ✅ 正确：使用中文字段名
{"fields": {"序号": "1", "Epic ID": "EPIC-XXX"}}
```

### 建表时字段名示例

```python
{"table": {"name": "Epic拆解总表", "fields": [
    {"field_name": "序号", "type": 1},
    {"field_name": "Epic ID", "type": 1},
    {"field_name": "Epic名称", "type": 1},
    {"field_name": "产品域", "type": 1},
    {"field_name": "Feature ID", "type": 1},
    {"field_name": "Feature名称", "type": 1},
    {"field_name": "Story ID", "type": 1},
    {"field_name": "Story名称", "type": 1},
    {"field_name": "验收标准", "type": 11},  # 多行文本
    {"field_name": "优先级", "type": 3, "property": {"options": [
        {"name": "P0", "color": 4}, {"name": "P1", "color": 2},
        {"name": "P2", "color": 1}, {"name": "P3", "color": 0},
    ]}},
    {"field_name": "状态", "type": 3, "property": {"options": [
        {"name": "已完成", "color": 4}, {"name": "待开发", "color": 1},
        {"name": "待确认", "color": 0},
    ]}},
    {"field_name": "原始来源", "type": 1},
]}}
```

## 分页查询

```python
all_records = []
page_token = None
while True:
    params = {'page_size': 500}
    if page_token:
        params['page_token'] = page_token
    resp = requests.get(
        f'https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records',
        headers={'Authorization': f'Bearer {token}'},
        params=params, timeout=30
    )
    data = resp.json().get('data', {})
    all_records.extend(data.get('items', []))
    if not data.get('has_more'):
        break
    page_token = data.get('page_token')
    time.sleep(0.2)
```
