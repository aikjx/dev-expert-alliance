# 开发专家联盟 · Claude 适配

在 **Claude Code** 中使用开发专家联盟：主 Agent 作为交付总监（齐活林），通过子代理机制调度六位专家。

## 文件
- `CLAUDE.md` — 项目指引（编排说明、路由表、5 条 Workflow、铁律、严重级口径、报告模板）
- `.claude/agents/*.md` — 六位专家子代理（带 frontmatter `name`/`description`/`tools`）

## 安装
把本目录内容合并进你的项目根目录：

```bash
# 1. 复制项目指引
cp CLAUDE.md <你的项目>/CLAUDE.md

# 2. 复制专家子代理
mkdir -p <你的项目>/.claude/agents
cp .claude/agents/*.md <你的项目>/.claude/agents/
```

## 使用
1. 在项目中打开 **Claude Code**，它会自动加载 `CLAUDE.md`。
2. 直接提出综合性任务，例如「对当前仓库做一次全维分析、修复、验证与优化」。
3. Claude 会按 Workflow A 用 **Task 工具** 自动并行调度 `arch-blueprint`、`backend-engine`、`frontend-canvas`、`data-steward`、`sec-sentinel` 等子代理，最后由「齐活林」汇编报告。

## 说明
- 子代理 `tools` 默认：`Read, Grep, Glob, Edit, Write, Bash`（Phase 1 只读盘点时仅读取，不编辑）。
- 也可用 `/agent <name>` 显式调用单个专家做单域深挖（Workflow B）。
