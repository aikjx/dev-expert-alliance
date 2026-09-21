# 开发专家联盟 · OpenAI 适配

在 **OpenAI** 生态中使用开发专家联盟，提供两种形态：

1. **OpenAI Agents SDK**（`alliance.py`）——真正的多 Agent 编排，主理人通过 `handoff` 转交六位专家子 Agent。
2. **Custom GPT**（`GPT_INSTRUCTIONS.md`）——单 Agent 模拟，用严格输出协议呈现六角色协作。

## 一、OpenAI Agents SDK

### 安装依赖
```bash
pip install openai-agents        # PyPI 包名 openai-agents，import 名 agents
export OPENAI_API_KEY=sk-...     # 或写在环境变量
```

### 运行
```bash
# 仅校验加载
python alliance.py

# 驱动一次任务
python alliance.py "对当前仓库做一次全维分析、修复、验证与优化"
```

- `specialists.py` 由仓库根 `scripts/generate_platforms.py` 自动生成（来源 `../../agents/*.md`），勿手改。
- 专家子 Agent 默认不带工具；如需让其读写代码/跑命令，可在 `build()` 中为每个 `Agent` 添加 `tools=[...]`（如 `function_tool` 封装的文件读写、shell 执行）。
- 主理人 `dev-expert-alliance-team-lead` 通过 `handoff` 自动把任务转交对应专家。

## 二、Custom GPT（无需写代码）

1. 打开 <https://chat.openai.com/gpts> → Create a GPT。
2. 把 **`GPT_INSTRUCTIONS.md`** 全文粘贴到 Instructions。
3. 保存并发布（可选私用）。
4. 直接对话，例如「定位并修复本仓库的高危缺陷，并给出可复现的验证证据」。

## 说明
- OpenAI Agents SDK 当前要求 Python 3.8+，且需要可访问 OpenAI API 的网络环境。
- Custom GPT 形态受单 Agent 限制，「多角色」通过输出协议区块（🔷🔶🟦🟩🟧🔴🟣）呈现，而非真正并行子 Agent。
