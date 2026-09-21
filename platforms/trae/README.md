# 开发专家联盟 · Trae 适配

在 **Trae**（字节跳动 AI IDE）中使用开发专家联盟。Trae 原生读取 `AGENTS.md`，并支持 `.trae/rules/` 与 `.trae/agents/`。

## 文件
- `AGENTS.md` — 跨 AI 通用项目指引（与 Cursor / Windsurf / Claude Code 兼容）
- `.trae/rules/dev-expert-alliance.md` — 强制协作规范（alwaysApply，每次对话自动加载）
- `.trae/agents/*.md` — 六位专家代理（frontmatter `name`/`description`/`tools`）

## 安装
把本目录内容合并进你的项目根目录：

```bash
# 复制 AGENTS.md
cp AGENTS.md <你的项目>/AGENTS.md

# 复制 .trae 目录（rules + agents）
cp -r .trae <你的项目>/.trae
```

## 使用
1. 在 Trae 中打开项目。
2. **启用 AGENTS.md**：`Settings → Import Settings`，开启「Include AGENTS.md in the context」（若用 `.trae/rules` 则无需此步，规则默认生效）。
3. 提出任务，例如「从架构、后端、前端、数据、测试、安全六个维度审计本仓库并输出问题台账」。
4. 调用单个专家：`/agent backend-engine 帮我检查这个接口的事务为什么没回滚`。

## 说明
- `AGENTS.md` 是跨工具通用格式，可同时被 Cursor / Windsurf / Claude Code 读取，便于团队统一。
- `.trae/agents/` 的代理格式以 Trae 文档为准；若你的 Trae 版本尚未正式支持自定义 agent 文件，可仅用 `AGENTS.md` + `.trae/rules/` 获得同等编排效果。
