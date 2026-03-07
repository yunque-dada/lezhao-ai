# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

---

## 🎯 技能快速查阅表

### 思考/推理类

| 技能 | 用途 | 何时用 |
|------|------|--------|
| thought-based-reasoning | 思维链推理 | 复杂问题、多步骤 |
| sequential-thinking | 顺序思考 | 系统化分析 |
| self-reflecting-chain | 自我反思 | 复盘、错误分析 |
| multi-agent-brainstorming | 多智能体评审 | 设计决策、方案评审 |
| meta-cognition-parallel | 三层分析 | 多角度决策 |
| prompt-engineering-patterns | Prompt工程 | 写提示词 |

### 搜索/信息类

| 技能 | 用途 | 何时用 |
|------|------|--------|
| baidu-search | 百度搜索 | 中文信息 |
| multi-search-engine | 多引擎搜索 | 综合信息 |
| tavily-search | AI搜索 | 英文/专业信息 |
| summarize | 总结内容 | URL/PDF/视频 |

### 图片/视觉类

| 技能 | 用途 | 何时用 |
|------|------|--------|
| minimax-understand-image | 理解图片 | 看图分析 |
| minimax-web-search | 图片搜索 | 查图相关信息 |

### 飞书类

| 技能 | 用途 | 何时用 |
|------|------|--------|
| feishu-doc | 飞书文档 | 读写文档 |
| feishu-wiki | 知识库 | 维基管理 |
| feishu-drive | 云盘 | 文件管理 |
| feishu-bitable | 多维表格 | 数据管理 |

### GitHub类

| 技能 | 用途 | 何时用 |
|------|------|--------|
| github-cli | GitHub命令行 | 仓库操作 |
| github-actions-generator | 生成工作流 | CI/CD |
| github-issue-resolver | 处理Issue | 问题管理 |
| github-pages-auto-deploy | 自动部署 | 网页部署 |

### 开发/安全类

| 技能 | 用途 | 何时用 |
|------|------|--------|
| superdesign | UI设计 | 页面设计 |
| security-best-practices | 安全实践 | 安全检查 |
| automation-workflows | 自动化 | 工作流 |
| skill-vetter | 技能审核 | 安装前检查 |

### 其他

| 技能 | 用途 | 何时用 |
|------|------|--------|
| self-improving-agent | 自我改进 | 记录错误/学习 |
| byterover | 知识管理 | 存储/查询知识 |
| trello | Trello | 看板管理 |
| slack | Slack | 消息管理 |

---

## ⚡ 快速决策

```
任务 → 检查能用哪个技能 → 用技能 → 记录
```

---

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

<!-- clawx:begin -->
## ClawX Tool Notes

### uv (Python)

- `uv` is bundled with ClawX and on PATH. Do NOT use bare `python` or `pip`.
- Run scripts: `uv run python <script>` | Install packages: `uv pip install <package>`

### Browser

- `browser` tool provides full automation (scraping, form filling, testing) via an isolated managed browser.
- Flow: `action="start"` → `action="snapshot"` (see page + get element refs like `e12`) → `action="act"` (click/type using refs).
- Open new tabs: `action="open"` with `targetUrl`.
- To just open a URL for the user to view, use `shell:openExternal` instead.
<!-- clawx:end -->
