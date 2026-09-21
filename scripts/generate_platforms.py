#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev Expert Alliance — 多平台成员定义生成器
==========================================
读取 WorkBuddy 原生 agents/*.md（主理人 + 6 名成员），产出其他平台的成员定义：
  - platforms/claude/.claude/agents/<name>.md      (Claude Code 子代理)
  - platforms/trae/.trae/agents/<name>.md          (Trae 自定义代理)
  - platforms/harness/agents/<name>.yaml           (Harness Worker Agent)
  - platforms/openai/specialists.py                (OpenAI Agents SDK 指令字典)

仅做「机械适配」（剥离 WorkBuddy frontmatter 与 SendMessage 段，改平台头/回传说明），
不改变专业内容。编排者（CLAUDE.md / AGENTS.md / alliance.py / team-lead.yaml）由人工编写。
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(ROOT, "agents")
PLATFORMS = os.path.join(ROOT, "platforms")

MEMBERS = [
    "arch-blueprint",
    "backend-engine",
    "frontend-canvas",
    "data-steward",
    "qa-gatekeeper",
    "sec-sentinel",
]


def read_member(name):
    path = os.path.join(AGENTS_DIR, name + ".md")
    text = open(path, encoding="utf-8").read()
    # 剥离 WorkBuddy frontmatter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        body = text[end + 4:]
    else:
        body = text
    # 提取 description
    m = re.search(r'description:\s*"([^"]*)"', text)
    desc = m.group(1) if m else ""
    # 剥离 WorkBuddy 专属的 SendMessage 回传段
    idx = body.find("## SendMessage 回传")
    if idx != -1:
        body = body[:idx].rstrip() + "\n"
    tail = (
        "\n## 回传说明\n"
        "完成分析/修复后，将完整报告作为你的回复输出，由编排者（主 Agent）接收并汇总。"
        "不要自行调用其他子代理/专家，也不要模拟其他角色的专业产出。\n"
    )
    return desc, body + tail


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("written:", os.path.relpath(path, ROOT))


# ---- Claude ----
def gen_claude():
    base = os.path.join(PLATFORMS, "claude", ".claude", "agents")
    for name in MEMBERS:
        desc, body = read_member(name)
        out = f"---\nname: {name}\ndescription: {desc}\ntools: Read, Grep, Glob, Edit, Write, Bash\n---\n\n{body}"
        write(os.path.join(base, name + ".md"), out)


# ---- Trae ----
def gen_trae():
    base = os.path.join(PLATFORMS, "trae", ".trae", "agents")
    for name in MEMBERS:
        desc, body = read_member(name)
        out = f'---\nname: {name}\ndescription: {desc}\ntools: ["read", "edit", "write", "bash"]\n---\n\n{body}'
        write(os.path.join(base, name + ".md"), out)


# ---- Harness ----
def gen_harness():
    base = os.path.join(PLATFORMS, "harness", "agents")
    for name in MEMBERS:
        desc, body = read_member(name)
        # YAML 块标量缩进（prompt 位于 4 空格，内容 6 空格）
        indented = "\n".join(("      " + l) if l.strip() else "      " for l in body.split("\n"))
        out = (
            f"version: 1\n"
            f"name: {name}\n"
            f"description: {desc}\n"
            f"agent:\n"
            f"  uses: harnessAI@1.0.0\n"
            f"  with:\n"
            f"    prompt: |\n{indented}\n"
            f'    connector: account.harnessAnthropic\n'
            f'    max_turns: "50"\n'
            f"  inputs: {{}}\n"
        )
        write(os.path.join(base, name + ".yaml"), out)


# ---- OpenAI ----
def gen_openai():
    lines = []
    lines.append('"""Dev Expert Alliance — OpenAI Agents SDK 专用指令字典（自动生成，勿手改；来源 agents/*.md）"""')
    lines.append("")
    lines.append('SPECIALIST_INSTRUCTIONS = {')
    for name in MEMBERS:
        _, body = read_member(name)
        lines.append(f'    "{name}": \'\'\'{body}\'\'\',')
    lines.append("}")
    lines.append("")
    lines.append('SPECIALIST_DESCRIPTIONS = {')
    for name in MEMBERS:
        desc, _ = read_member(name)
        lines.append(f'    "{name}": {desc!r},')
    lines.append("}")
    lines.append("")
    write(os.path.join(PLATFORMS, "openai", "specialists.py"), "\n".join(lines))


if __name__ == "__main__":
    gen_claude()
    gen_trae()
    gen_harness()
    gen_openai()
    print("DONE")
