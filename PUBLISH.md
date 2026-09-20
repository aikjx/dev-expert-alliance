# 发布指南 / Publish Guide

本仓库已是一个干净的 Git 仓库（首次提交，20 个文件，含 MIT 许可证与 `.gitignore`）。
要将其发布为 GitHub 公开仓库，只需完成下面三步。

## 1. 在 GitHub 上创建空仓库

1. 打开 <https://github.com/new>
2. Repository name 填写：`dev-expert-alliance`
3. 设为 **Public**
4. **不要**勾选 "Add a README file" / "Add .gitignore" / "Choose a license"（本仓库已自带这些文件）
5. 点击 **Create repository**

创建后会得到一个地址，形如：
`https://github.com/<你的用户名>/dev-expert-alliance.git`

## 2. 关联远程仓库并推送

在本仓库根目录（`dev-expert-alliance/`）执行：

```bash
git remote add origin https://github.com/<你的用户名>/dev-expert-alliance.git
git branch -M main
git push -u origin main
```

若使用 SSH 密钥，可将地址替换为：
`git@github.com:<你的用户名>/dev-expert-alliance.git`

## 3. 验证

推送完成后，打开仓库页面，确认以下结构已上线：

```
.codebuddy-plugin/plugin.json
README.md
LICENSE
settings.json
agents/        # 7 个专家定义（含 team-lead）
avatars/       # 8 张头像
```

## 备注

- 本机未安装 `gh` CLI，故未自动创建远程仓库；你也可以安装 `gh` 后改用
  `gh repo create dev-expert-alliance --public --source=. --remote=origin --push`。
- 已注册的本地专家包位于
  `~/.workbuddy/plugins/marketplaces/my-experts/plugins/dev-expert-alliance/`，
  本仓库是其开源发布副本。
