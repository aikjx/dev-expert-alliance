# 开发专家联盟 (Dev Expert Alliance) v1.2.0

一个跨开发领域的 **WorkBuddy Team 型专家联盟**，由 1 个编排中枢（Team Lead）+ 7 个领域专家组成，覆盖信息化项目开发的全生命周期：**产品与设计 → 架构 → 后端 → 前端 → 数据 → 测试 → 安全**。

## ✨ 核心特性

- **七位一体专家团队**：架构蓝图师、后端引擎师、前端画布师、数据管家、质量守门人、安全哨兵、产品设计师（设身处）。
- **六大协同工作流**：
  - **A. 全维分析-修复-验证-优化**：端到端接管整个代码库 / 项目。
  - **B. 单域深攻**：聚焦某一个专家领域做深做透。
  - **C. 缺陷定位**：快速定位并修复线上 / 测试问题。
  - **D. 架构设计与脚手架（0→1）**：从需求到可运行的工程骨架。
  - **E. 性能专项优化**：定位瓶颈，给出可量化收益的方案。
  - **F. 产品与需求研判 · 战略布局**：先想清楚「该不该做」，七步研判需求价值 / 开源现状 / 竞品差异 / 创新 / 用户洞察 / 最佳操盘 / 布局。
- **统一交付纪律**：每次任务产出结构化「最终交付报告」（问题台账 / 修复记录 / 验证结论 GATE / 残留风险 / 优化建议 / 回滚方案）。
- **跨平台可移植**：同一套专家定义，原生适配 **WorkBuddy / Claude / OpenAI / Trae / Harness** 五大平台。

## 🌐 多平台支持矩阵

| 平台 | 形态 | 专家运行时 | 入口文件 |
|------|------|-----------|---------|
| WorkBuddy | 专家包（Team） | 原生多智能体 | `agents/` + `.codebuddy-plugin/plugin.json` |
| Claude | `CLAUDE.md` + `.claude/agents/*.md` | 子代理 | `platforms/claude/CLAUDE.md` |
| OpenAI | Agents SDK | `Agent` + `handoff` | `platforms/openai/alliance.py` |
| Trae | `AGENTS.md` + `.trae/agents/*.md` | 原生代理 | `platforms/trae/AGENTS.md` |
| Harness | Worker Agent YAML | 编排 `swarm` | `platforms/harness/agents/team-lead.yaml` |

每个平台目录内含 `README.md`，给出安装与调用方式。成员专家文件由 `scripts/generate_platforms.py` 从 `agents/*.md` 机械生成，保证五端一致、可复现。

## 🚀 快速开始（WorkBuddy）

```bash
# 方式一：作为专家包安装（marketplace）
# 在 WorkBuddy 专家中心导入本仓库，启用「开发专家联盟」

# 方式二：直接放入项目
cp -r agents .codebuddy-plugin <你的项目>/.workbuddy/
```

其余平台见各 `platforms/<平台>/README.md`。

## 📦 版本变更（v1.1.0 → v1.2.0）

- 新增第 7 位专家 **产品设计师·设身处（product-design）**：负责需求价值判断、开源现状尽调、竞品差异化、创新路径、用户洞察、最佳操盘与战略布局。
- 新增 **Workflow F 产品与需求研判 · 战略布局**（七步研判法），并让 product-design 在 Workflow D 中前置参与需求与定位。
- 专家包版本 `plugin.json` 升至 `1.2.0`；四套平台（Claude / OpenAI / Trae / Harness）成员定义由 `scripts/generate_platforms.py` 同步新增该专家。

### 历史（v1.0.0 → v1.1.0）

- 新增 **Workflow D 架构设计与脚手架**、**Workflow E 性能专项优化**。
- 新增「最终交付报告模板」，统一交付物结构。
- 新增 **Claude / OpenAI / Trae / Harness** 四套原生定义（共 23 个成员专家文件 + 4 个编排入口）。
- 新增 `scripts/generate_platforms.py` 一键生成四端成员文件。
- 专家包版本 `plugin.json` 升至 `1.1.0`。

## 🔗 相关

- 仓库：https://github.com/aikjx/dev-expert-alliance
- 问题反馈：https://github.com/aikjx/dev-expert-alliance/issues
