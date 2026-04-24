# Demo 代码路径规范

## 核心关系

```
需求文档（PRD）→ 定义功能（做什么）
       ↓
前端 Demo（/src）→ 验证交互实现（怎么操作、界面怎么响应）
       ↓
Neo4j Story.codePath → 记录 Demo 路径，供追溯
```

**Demo 完成 ≠ 功能已上线。Demo 只是交互参考，真正的生产代码是另一套。**

## 代码库路径

```
/Users/wenbo/Documents/project/data_community/src/
```

## 各产品域的 Demo 代码路径

### PD-DEX（数据探索）
```
pages/discovery/
├── customer360/              # 客户360
│   ├── detail.vue
│   └── components/
│       ├── MainTabs.vue
│       ├── InfoModuleTabs.vue
│       ├── CustomerProfile.vue
│       ├── CustomerOverview.vue
│       ├── BusinessCoreDetails.vue
│       ├── HistorySliceQuery.vue
│       ├── TouchRecords.vue
│       ├── BenefitRecords.vue
│       ├── CollectionRecords.vue
│       └── CreditReports.vue
├── metric/                   # 指标体系
│   ├── index.vue
│   └── components/
└── analysis/                # 统一分析
```

### PD-DFD（数据资产）
```
pages/data-asset/             # 数据资产
├── asset-list.vue
├── asset-detail.vue
└── components/
pages/data-element/           # 数据要素
├── element-dict.vue
└── components/
pages/data-resource/          # 数据资源
├── resource-list.vue
└── components/
```

### PD-MKT（营销）
```
pages/marketing/
├── canvas/                   # 营销画布
├── reach/                    # 触达系统
├── benefit/                  # 权益中心
├── crowd/                    # 客群中心
└── manual-sales/            # 人工电销
```

### PD-DMT（数据管理）
```
pages/data-std/               # 数据标准
├── std-list.vue
└── components/
pages/metadata/              # 元数据字典
├── meta-list.vue
└── components/
pages/biz-concept/           # 业务概念
├── concept-list.vue
└── components/
pages/data-service/          # 数据服务
├── service-list.vue
└── components/
```

## 查找 Demo 代码的方法

```bash
# 1. 按关键词找文件
find /Users/wenbo/Documents/project/data_community/src \
  -type f \( -name "*.vue" -o -name "*.ts" -o -name "*.tsx" \) \
  | xargs grep -l "customer360" 2>/dev/null | grep -v node_modules

# 2. 按目录结构找
ls /Users/wenbo/Documents/project/data_community/src/pages/discovery/customer360/components/

# 3. 读取文件确认实现
cat /Users/wenbo/Documents/project/data_community/src/pages/discovery/customer360/detail.vue
```

## codePath 格式规范

```
{模块}/{子模块}/{组件文件}.vue
```

示例：
```
discovery/customer360/components/SearchModule.vue
data-asset/asset-list.vue
marketing/canvas/designer.vue
```

**注意：存储时使用相对路径（不带 /Users/wenbo/... 前缀）**

## Demo 状态判断

| Demo 代码情况 | demoStatus | 说明 |
|:---|:---|:---|
| 有完整 Demo 组件 | 已完成 | 只是参考，不等于上线 |
| Demo 部分实现 | 部分完成 | 需要补充 |
| 无 Demo | 待开发 | 从未有过实现 |
| Demo 存在但已废弃 | 已废弃 | 需求变更 |

## Story.codePath 的实际用途

1. **追溯**：知道这个功能最初参考了哪段 Demo
2. **对比**：Prod 代码如果和 Demo 不一致，能发现差异
3. **交接**：新同学能快速找到参考实现

## Story 备注字段完整格式

```
{功能描述} | Demo路径: {codePath} | Demo状态: {demoStatus}
```

示例：
```
客户搜索 | Demo路径: discovery/customer360/components/SearchModule.vue | Demo状态: 已完成
指标看板 | Demo路径: discovery/metric/index.vue | Demo状态: 已完成
```
