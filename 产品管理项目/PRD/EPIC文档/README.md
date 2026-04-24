# EPIC 文档库

> **版本**: v1.0
> **日期**: 2026-04-24
> **维护者**: Tony Stark

---

## 产品域列表

| 产品域 | 目录 | EPIC数 | 说明 |
|:---|:---|:---:|:---|
| 数字社区 | [数字社区](./数字社区/) | 5 | 数字社区产品域 |
| {{product_domain}} | {{directory}} | {{count}} | {{description}} |

---

## 目录结构

```
EPIC文档/
├── README.md              # 本文档
├── 数字社区/               # 产品域目录
│   ├── README.md          # EPIC索引
│   ├── 01-EPIC-xxx.md     # EPIC文档
│   └── 02-EPIC-yyy.md
└── {{product_domain}}/     # 其他产品域目录
    ├── README.md
    └── *.md
```

---

## EPIC 文档命名规范

```
格式：{序号}-EPIC-{EPIC名称}.md

示例：
01-EPIC-统一门户首页.md
02-EPIC-通知管理.md
03-EPIC-文档管理.md
```

---

## 维护说明

- 新增 EPIC：在对应产品域目录下创建文档
- 更新 EPIC：更新对应文档并同步变更日志
- 删除 EPIC：移动到 `../归档/` 目录

---

**文档版本**: v1.0
**最后更新**: 2026-04-24
**维护者**: Tony Stark
