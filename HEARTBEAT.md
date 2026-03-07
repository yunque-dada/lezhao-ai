# HEARTBEAT.md

## ⚙️ 技能自动触发器

**每次收到用户消息时，自动判断任务类型并触发相应技能：**

### 任务类型 → 技能映射

| 任务类型 | 判断标准 | 使用技能 |
|----------|----------|----------|
| **简单任务** | 事实、单步操作、查询 | 直接回答，无需技能 |
| **复杂推理** | 多步骤、逻辑分析 | thought-based-reasoning |
| **系统化思考** | 需要调整思路、流程分析 | sequential-thinking |
| **自我复盘** | 分析自身、错误反思 | self-reflecting-chain |
| **设计评审** | 方案、代码、架构决策 | multi-agent-brainstorming |
| **多角度分析** | 需要不同视角、决策选择 | meta-cognition-parallel |
| **写提示词** | Prompt工程 | prompt-engineering-patterns |

---

## 🔧 技能清单检查表

**每次动手前必须检查：能用哪个技能？**

| 场景 | 必须检查的技能 | 优先级 |
|------|----------------|--------|
| **搜索信息** | baidu-search, multi-search-engine, tavily-search | 高 |
| **看图片** | minimax-understand-image + minimax-web-search | 高 |
| **写飞书文档** | feishu-doc | 高 |
| **做设计/UI** | superdesign | 高 |
| **总结内容(URL/PDF)** | summarize | 高 |
| **GitHub操作** | github-cli, github-actions-generator | 高 |
| **自动化任务** | automation-workflows | 中 |
| **安全检查** | security-best-practices | 中 |

---

## ⚡ 快速决策流程

```
收到任务
    ↓
1. 复杂吗？ → 是 → 思维链
    ↓ 否
2. 需要搜索？ → 是 → 用搜索技能
    ↓ 否
3. 看图片？ → 是 → minimax-understand-image
    ↓ 否
4. 写文档？ → 是 → feishu-doc
    ↓ 否
5. 做设计？ → 是 → superdesign
    ↓ 否
6. 直接回答
```

---

## 汇报任务

**不再汇报 GitHub 热门项目**，改为汇报其他内容。

### 待确定汇报内容：
- 等待用户指定汇报主题（如：河源本地资讯、天气、新闻、行业动态等）

### 注意：
- 汇报时间仅在 08:00-23:00
- 需要用户指定具体的汇报内容和数据来源
