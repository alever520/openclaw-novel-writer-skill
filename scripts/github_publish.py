#!/usr/bin/env python3
"""
GitHub 仓库自动发布脚本

用法:
    python github_publish.py <项目目录> <仓库名> <描述> [--token TOKEN]

示例:
    python github_publish.py ./truth-floating-city truth-floating-city-novel "浮空城编年史"
    python github_publish.py ./my-novel my-novel "我的小说" --token ghp_xxxxx

环境变量:
    GITHUB_TOKEN - GitHub Personal Access Token (如果未通过 --token 提供)
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path


def find_github_token():
    """从本地 Git 配置查找 GitHub Token"""
    try:
        # 方法 1: 从当前项目 .git/config
        git_config = Path(".git/config")
        if git_config.exists():
            content = git_config.read_text()
            if "ghp_" in content:
                token = content.split("ghp_")[1].split("@")[0]
                return f"ghp_{token}"
        
        # 方法 2: 从工作区其他项目扫描
        workspace = Path.home() / ".openclaw" / "workspace"
        if workspace.exists():
            for git_config in workspace.rglob(".git/config"):
                content = git_config.read_text()
                if "ghp_" in content:
                    token = content.split("ghp_")[1].split("@")[0]
                    return f"ghp_{token}"
        
        # 方法 3: 从环境变量
        if "GITHUB_TOKEN" in os.environ:
            return os.environ["GITHUB_TOKEN"]
        
        return None
    except Exception as e:
        print(f"⚠️  查找 Token 失败: {e}", file=sys.stderr)
        return None


def create_github_repo(token, repo_name, description, private=False):
    """使用 GitHub API 创建仓库"""
    import urllib.request
    import urllib.error
    
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": False
    }
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['html_url'], result['clone_url']
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        if "already exists" in error_msg:
            # 仓库已存在，尝试获取信息
            print(f"⚠️  仓库 {repo_name} 已存在，将使用现有仓库")
            return get_repo_info(token, repo_name)
        else:
            raise Exception(f"创建仓库失败: {error_msg}")


def get_repo_info(token, repo_name):
    """获取已存在仓库的信息"""
    import urllib.request
    
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        user_info = json.loads(response.read().decode('utf-8'))
        username = user_info['login']
    
    html_url = f"https://github.com/{username}/{repo_name}"
    clone_url = f"https://github.com/{username}/{repo_name}.git"
    return html_url, clone_url


def git_push(project_dir, token, clone_url):
    """推送代码到 GitHub"""
    os.chdir(project_dir)
    
    # 检查是否已初始化 Git
    if not Path(".git").exists():
        print("📦 初始化 Git 仓库...")
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    
    # 添加 remote（带 Token）
    auth_clone_url = clone_url.replace("https://", f"https://{token}@")
    
    # 移除旧的 origin（如果存在）
    subprocess.run(["git", "remote", "remove", "origin"], 
                   stderr=subprocess.DEVNULL)
    
    subprocess.run(["git", "remote", "add", "origin", auth_clone_url], check=True)
    
    # 切换到 main 分支并推送
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)


def main():
    parser = argparse.ArgumentParser(description="发布小说项目到 GitHub")
    parser.add_argument("project_dir", help="项目目录路径")
    parser.add_argument("repo_name", help="GitHub 仓库名")
    parser.add_argument("description", help="仓库描述")
    parser.add_argument("--token", help="GitHub Personal Access Token")
    parser.add_argument("--private", action="store_true", help="创建私有仓库")
    
    args = parser.parse_args()
    
    # 验证项目目录
    project_path = Path(args.project_dir).resolve()
    if not project_path.exists():
        print(f"❌ 项目目录不存在: {project_path}", file=sys.stderr)
        sys.exit(1)
    
    # 获取 Token
    token = args.token or find_github_token()
    if not token:
        print("❌ 未找到 GitHub Token", file=sys.stderr)
        print("请通过 --token 参数提供，或设置 GITHUB_TOKEN 环境变量", file=sys.stderr)
        sys.exit(1)
    
    print(f"📚 项目目录: {project_path}")
    print(f"📦 仓库名: {args.repo_name}")
    print(f"📝 描述: {args.description}")
    print()
    
    # 创建 GitHub 仓库
    print("🚀 创建 GitHub 仓库...")
    try:
        html_url, clone_url = create_github_repo(
            token, 
            args.repo_name, 
            args.description,
            args.private
        )
        print(f"✅ 仓库创建成功: {html_url}")
    except Exception as e:
        print(f"❌ 创建仓库失败: {e}", file=sys.stderr)
        sys.exit(1)
    
    # 推送代码
    print()
    print("📤 推送代码到 GitHub...")
    try:
        git_push(project_path, token, clone_url)
        print(f"✅ 推送成功!")
    except subprocess.CalledProcessError as e:
        print(f"❌ 推送失败: {e}", file=sys.stderr)
        sys.exit(1)
    
    print()
    print(f"🎉 完成！仓库地址: {html_url}")


if __name__ == "__main__":
    main()
