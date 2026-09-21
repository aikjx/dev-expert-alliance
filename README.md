# Dev Expert Alliance（开发专家联盟）

> 开源的 WorkBuddy **Team 型专家团**。面向软件研发全流程的多角色协作 AI 团队，覆盖架构、后端、前端、数据、测试、安全六个专业域，由交付总监按标准 SOP 编排，完成「全维分析 → 修复 → 独立验证 → 优化」的闭环交付。
>
> License: [MIT](./LICENSE)

## 类型

Team 型（多角色协作团队）

## 成员

| Agent ID | 名字 | 职业 | 专业域 |
|----------|------|------|--------|
| dev-expert-alliance-team-lead | 齐活林 | 交付总监 | 编排调度 · 汇编交付 |
| arch-blueprint | 高见远 | 架构师 | 分层 · 依赖 · 扩展性 · 技术债 |
| backend-engine | 寇豆码 | 后端工程师 | 接口契约 · 事务 · 并发 · 日志 |
| frontend-canvas | 甄界面 | 前端工程师 | 组件 · 状态 · 请求层 · 加载态 |
| data-steward | 陈数仓 | 数据架构师 | 表结构 · 索引 · SQL · 脏数据 |
| qa-gatekeeper | 严过关 | 质量门禁官 | 用例 · 门禁 · 回归 · 证据 |
| sec-sentinel | 安如山 | 安全审计官 | 鉴权 · 越权 · 注入 · 密钥 |

## 功能

- **全维分析修复验证优化（Workflow A）**：五域并行只读盘点出问题台账 → 测试域设计门禁 → 分域修复 → 独立验证 → 汇编报告。
- **单域深挖（Workflow B）**：只关心一个专业域时直接调度对应成员。
- **缺陷定位与修复（Workflow C）**：由现象（截图/日志/堆栈）出发交叉定位根因并修复复验。
- 所有结论强制附带可核验证据（`文件:行` / 命令 / 退出码 / SQL / 实测计数），修复者与验证者分离。

## 使用示例

- 对当前仓库做一次全维分析、修复、验证与优化
- 从架构、后端、前端、数据、测试、安全六个维度审计本仓库并输出问题台账
- 定位并修复本仓库的高危缺陷，并给出可复现的验证证据

## 多平台支持

同一套「开发专家联盟」已适配多个 AI 研发平台，专业内容与 SOP 完全一致，仅运行时形态不同：

| 平台 | 形态 | 专家运行时 | 入口文件 | 说明 |
|------|------|-----------|----------|------|
| WorkBuddy | Team 型专家团 | 原生 Agent | `.codebuddy-plugin/plugin.json` | 当前仓库即 WorkBuddy 原生包（见下方「安装」） |
| Claude | 子代理 + 项目指引 | Claude Code subagent | `platforms/claude/CLAUDE.md` + `.claude/agents/` | [详情](platforms/claude/README.md) |
| OpenAI | Agents SDK / Custom GPT | OpenAI Agents | `platforms/openai/alliance.py` / `GPT_INSTRUCTIONS.md` | [详情](platforms/openai/README.md) |
| Trae | AGENTS.md + Rules + Agents | Trae agent | `platforms/trae/AGENTS.md` + `.trae/` | [详情](platforms/trae/README.md) |
| Harness | Worker Agent (YAML) | Harness AI Agent | `platforms/harness/agents/*.yaml` | [详情](platforms/harness/README.md) |

> 跨平台成员定义由 `scripts/generate_platforms.py` 从 `agents/*.md` 自动生成，保证五套平台内容一致、可一键再生。

## 安装（WorkBuddy）

**方式一：从源码安装**

```bash
# 1. 克隆到专家目录
git clone <本仓库地址> "$HOME/.workbuddy/plugins/marketplaces/my-experts/plugins/dev-expert-alliance"

# 2. 注册使之中心可见（需 WorkBuddy expert-manager 技能里的 scripts/register_expert.py）
python3 scripts/register_expert.py "$HOME/.workbuddy/plugins/marketplaces/my-experts/plugins/dev-expert-alliance"
```

**方式二：手动放置**

将本仓库内容放到以下目录，再运行上面的注册命令：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/dev-expert-alliance/
```

注册后，在 WorkBuddy 左侧「专家中心 → 我的专家」中即可看到「开发专家联盟」并开聊。

## 目录结构

```
dev-expert-alliance/
├── .codebuddy-plugin/plugin.json   # WorkBuddy 专家包元信息（展示字段、成员、SOP 引用）
├── agents/                         # 主理人 + 6 名团员的角色定义（WorkBuddy 原生，跨平台内容源）
├── avatars/                        # 团队与成员头像
├── settings.json                   # Team 入口声明（指向主理人 Agent）
├── platforms/                      # 跨平台适配
│   ├── claude/                     #   CLAUDE.md + .claude/agents/
│   ├── openai/                     #   alliance.py (Agents SDK) + GPT_INSTRUCTIONS.md + specialists.py
│   ├── trae/                       #   AGENTS.md + .trae/rules/ + .trae/agents/
│   └── harness/                    #   agents/*.yaml (Worker Agent)
├── scripts/                        # generate_platforms.py（成员定义生成器）
├── README.md
├── LICENSE
└── .gitignore
```

## 头像

头像位于 `avatars/`（`team.png` 为团队头像，其余为成员头像）。如需替换：PNG/JPG、512×512 px、单张 ≤500KB，保持现有文件名即可。

## License

[MIT](./LICENSE) © 2026 Dev Expert Alliance Contributors
