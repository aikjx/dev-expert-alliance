# 开发专家联盟 · Harness 适配

在 **Harness AI** 中使用开发专家联盟：每个专家与交付总监都是 **Worker Agent**（YAML 定义），由 Harness 在 CI/CD 流水线或 Swarm 中调度。

## 文件
- `agents/team-lead.yaml` — 交付总监（**Swarm** 编排 Agent，`swarm: "true"`），自动协调六位专家
- `agents/<member>.yaml` — 六位专家 Worker Agent（架构/后端/前端/数据/测试/安全）

## 安装
1. 打开 Harness 控制台 → **Harness AI → Worker Agents → Catalog**。
2. 对每个 YAML 文件：切到 **YAML** 标签页，粘贴文件内容，保存。
   - 或将其作为流水线 step 引入（参考 Harness 官方 `agent: step: run: ...` 形态）。
3. **替换 connector**：把 `connector: account.harnessAnthropic` 改成你账号里实际的 Model Connector（Anthropic 或 OpenAI 均可；OpenAI 兼容后端可设 `backend: openai`）。

## 使用
- **整体编排**：运行 `team-lead`（Swarm），它会在收到综合性任务时自动把子任务分派给六位专家 Worker Agent，最后汇总报告。
- **单专家**：直接运行某个 `agents/<member>.yaml`（如 PR 评审只挂 `sec-sentinel` 或 `qa-gatekeeper`）。
- **流水线集成**：把任意 Worker Agent 作为 pipeline step 挂载到 Plan/Code/Test/Deploy 任一环节。

## 说明
- YAML 字段以 Harness 官方参考为准（`agent.uses: harnessAI@1.0.0` + `with.prompt/connector/max_turns/swarm`）。
- `inputs` 当前为空；如需动态注入 `projectName`/`repoName` 等，按 Harness 变量表达式扩展。
- Harness 默认域 `harness.io` 已允许；如需访问外部域名，配置 `allowed_domains`。
