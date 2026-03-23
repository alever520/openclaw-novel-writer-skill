#!/bin/bash

# 使用 GitHub Token 推送到仓库
# 需要设置环境变量 GITHUB_TOKEN

if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ 错误：未设置 GITHUB_TOKEN 环境变量"
    echo ""
    echo "请先设置 Token："
    echo "  export GITHUB_TOKEN='your_github_token'"
    echo ""
    echo "获取 Token："
    echo "  https://github.com/settings/tokens"
    echo "  勾选 'repo' 权限"
    exit 1
fi

REPO_URL="https://${GITHUB_TOKEN}@github.com/alever520/openclaw-novel-writer-skill.git"

echo "🚀 推送到 GitHub..."
echo "仓库: https://github.com/alever520/openclaw-novel-writer-skill"
echo ""

# 移除旧的 origin（如果存在）
git remote remove origin 2>/dev/null || true

# 添加新的 origin
git remote add origin "$REPO_URL"

# 推送
if git push -u origin main --force; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "📍 访问仓库："
    echo "   https://github.com/alever520/openclaw-novel-writer-skill"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    exit 1
fi
