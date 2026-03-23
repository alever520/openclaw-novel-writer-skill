# 推送到 GitHub 的详细步骤

由于 OpenClaw 环境的限制，需要手动完成推送。以下是详细步骤：

---

## 方式1: 使用 GitHub Web UI（最简单）

### 步骤1: 下载项目文件
```bash
cd /root/.openclaw/workspace/novel-writer
tar -czf novel-writer-v1.0.0.tar.gz \
  SKILL.md README.md QUICKSTART.md DEPLOY.md LICENSE .gitignore \
  deploy-to-github.sh push-with-token.sh \
  templates/ references/
```

### 步骤2: 在 GitHub 上传
1. 访问 https://github.com/alever520/openclaw-novel-writer-skill
2. 如果仓库是空的，直接上传文件
3. 如果仓库已有内容，可以用 Web 编辑器逐个添加/更新文件

---

## 方式2: 使用 GitHub CLI（推荐）

如果环境中有 `gh` 命令：

```bash
cd /root/.openclaw/workspace/novel-writer

# 登录 GitHub
gh auth login

# 推送仓库
gh repo sync alever520/openclaw-novel-writer-skill --source .
```

---

## 方式3: 使用 Personal Access Token

### 步骤1: 生成 Token
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 点击 "Generate token"
5. 复制生成的 Token（只显示一次！）

### 步骤2: 设置环境变量并推送
```bash
cd /root/.openclaw/workspace/novel-writer

# 设置 Token（替换为你的实际 Token）
export GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 运行推送脚本
bash push-with-token.sh
```

或者直接使用 Token URL：
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/alever520/openclaw-novel-writer-skill.git
git push -u origin main --force
```

---

## 方式4: 配置 SSH Key

### 步骤1: 生成 SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# 一路回车使用默认设置
```

### 步骤2: 添加到 GitHub
```bash
# 显示公钥
cat ~/.ssh/id_ed25519.pub

# 复制输出的内容
```

访问 https://github.com/settings/keys
- 点击 "New SSH key"
- 粘贴公钥内容
- 保存

### 步骤3: 推送
```bash
cd /root/.openclaw/workspace/novel-writer
git remote set-url origin git@github.com:alever520/openclaw-novel-writer-skill.git
git push -u origin main
```

---

## 方式5: 使用 Git Credential Manager

### 配置缓存
```bash
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
```

### 推送（会提示输入用户名和密码/Token）
```bash
cd /root/.openclaw/workspace/novel-writer
git remote set-url origin https://github.com/alever520/openclaw-novel-writer-skill.git
git push -u origin main

# 用户名: alever520
# 密码: 粘贴你的 Personal Access Token
```

---

## 验证推送成功

推送成功后，访问以下URL确认：

- **仓库首页**: https://github.com/alever520/openclaw-novel-writer-skill
- **提交历史**: https://github.com/alever520/openclaw-novel-writer-skill/commits/main
- **文件列表**: https://github.com/alever520/openclaw-novel-writer-skill/tree/main

应该能看到：
- ✅ SKILL.md - 核心文档
- ✅ README.md - 用户指南
- ✅ QUICKSTART.md - 快速开始
- ✅ templates/ - 模板目录
- ✅ 4次提交记录

---

## 常见问题

### Q1: Permission denied (publickey)
**原因**: 没有配置 SSH Key
**解决**: 使用方式3（Token）或方式4（配置SSH Key）

### Q2: could not read Username
**原因**: HTTPS 方式需要认证
**解决**: 使用 Token 或配置 credential helper

### Q3: fatal: Authentication failed
**原因**: Token 过期或权限不足
**解决**: 重新生成 Token，确保勾选 `repo` 权限

---

## 推荐流程

1. **最快**: 方式1（Web UI）- 适合小项目
2. **最安全**: 方式4（SSH Key）- 一次配置，长期使用
3. **最灵活**: 方式3（Token）- 临时推送

---

## 下一步

推送成功后：
1. [ ] 查看仓库是否正常显示
2. [ ] 创建第一个 Release (v1.0.0)
3. [ ] 编辑 README.md 添加 Badge
4. [ ] 添加 Topics 标签

---

**当前状态**: 
- ✅ 本地已完成所有提交
- ⏳ 等待推送到远程仓库

**本地路径**: `/root/.openclaw/workspace/novel-writer`
**目标仓库**: https://github.com/alever520/openclaw-novel-writer-skill
