#!/bin/bash

# Novel Writer Skill - GitHub 部署脚本
# 使用方法：
# 1. 在 GitHub 上创建仓库 openclaw-novel-writer
# 2. 运行此脚本：bash deploy-to-github.sh

echo "🚀 Novel Writer Skill - GitHub 部署"
echo "=================================="
echo ""

# 检查是否在正确的目录
if [ ! -f "SKILL.md" ]; then
    echo "❌ 错误：请在 novel-writer 目录下运行此脚本"
    exit 1
fi

# 检查 Git 配置
echo "📝 检查 Git 配置..."
GIT_USER=$(git config user.name)
GIT_EMAIL=$(git config user.email)

if [ -z "$GIT_USER" ] || [ -z "$GIT_EMAIL" ]; then
    echo "⚠️  Git 用户信息未配置"
    echo "请运行以下命令配置："
    echo "  git config --global user.name \"Your Name\""
    echo "  git config --global user.email \"your@email.com\""
    exit 1
fi

echo "✅ Git 用户: $GIT_USER <$GIT_EMAIL>"
echo ""

# 提示用户创建远程仓库
echo "📦 准备推送到 GitHub..."
echo ""
echo "请确保已在 GitHub 上创建仓库："
echo "  仓库名: openclaw-novel-writer"
echo "  可见性: Public"
echo "  不要初始化 README、.gitignore 或 License"
echo ""
read -p "已创建仓库？(y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ 请先创建 GitHub 仓库"
    exit 1
fi

# 获取 GitHub 用户名
read -p "请输入你的 GitHub 用户名: " GITHUB_USER

if [ -z "$GITHUB_USER" ]; then
    echo "❌ 用户名不能为空"
    exit 1
fi

# 添加远程仓库
echo ""
echo "🔗 添加远程仓库..."
REPO_URL="https://github.com/$GITHUB_USER/openclaw-novel-writer.git"

# 检查是否已有 origin
if git remote get-url origin &> /dev/null; then
    echo "⚠️  检测到已存在的 origin，将其移除..."
    git remote remove origin
fi

git remote add origin "$REPO_URL"
echo "✅ 远程仓库已添加: $REPO_URL"
echo ""

# 推送到 GitHub
echo "📤 推送到 GitHub..."
if git push -u origin main; then
    echo ""
    echo "🎉 部署成功！"
    echo ""
    echo "📍 仓库地址："
    echo "   https://github.com/$GITHUB_USER/openclaw-novel-writer"
    echo ""
    echo "📖 下一步："
    echo "   1. 访问仓库查看内容"
    echo "   2. 编辑 README.md 添加仓库链接"
    echo "   3. 创建 Release 发布版本"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因："
    echo "  1. GitHub 仓库不存在"
    echo "  2. 没有推送权限"
    echo "  3. 需要配置 Personal Access Token"
    echo ""
    echo "解决方法："
    echo "  1. 确认仓库已创建"
    echo "  2. 使用 HTTPS + Token 或 SSH 方式"
    echo "  3. 参考: https://docs.github.com/cn/authentication"
    echo ""
    exit 1
fi
