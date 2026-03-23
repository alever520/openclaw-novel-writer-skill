# Novel Writer Skill - 快速开始指南

欢迎使用 Novel Writer Skill！这个指南将帮助你快速上手。

---

## 🚀 5分钟快速开始

### 步骤1: 初始化新项目

在 OpenClaw 中说：
```
初始化小说项目：我的第一部小说
```

Skill 会自动创建标准目录结构。

### 步骤2: 完善大纲

编辑 `references/outline-template.md`，填写：
- 核心设定（主角、世界观、理念）
- 故事主线（分卷、分章）
- 人物设定（主角、配角、反派）

### 步骤3: 开始创作

在 OpenClaw 中说：
```
写第一章
```

Skill 会：
- 根据大纲创作章节
- 自动保存到 `chapters/`
- 提交到 Git

### 步骤4: 持续创作

每次说 `写第X章` 或 `继续写`，Skill 会自动处理后续章节。

---

## 📚 使用模板快速开始

### 方式1: 使用基础模板

```bash
# 复制基础模板
cp -r templates/project-template my-novel/
cd my-novel/

# 编辑基础信息
# 1. 修改 README.md
# 2. 填写 references/outline-template.md
# 3. 根据需要调整 references/writing-guide.md

# 初始化 Git
git init
git add .
git commit -m "初始化项目"

# 关联远程仓库
git remote add origin https://github.com/yourusername/my-novel.git
git push -u origin main
```

### 方式2: 参考完整示例

```bash
# 复制示例项目
cp -r templates/example-novel/truth-floating-city my-novel/
cd my-novel/

# 查看示例内容
# - chapters/ 有3个完整示例章节
# - references/outline.md 有详细大纲
# - references/writing-guide.md 有完善指南

# 用自己的内容替换
# 删除示例章节，保留大纲结构
# 修改为自己的设定
```

---

## 🎯 核心工作流

### 创作章节
```
你: 写第一章
AI: 
  1. 读取大纲第一章任务
  2. 读取 writing-guide.md、characters.md、reader-feedback.md
  3. 创作3000-5000字章节
  4. 【正文自检循环】
     - 第一轮: 对照 writing-guide.md 逐条核查
     - 第二轮: 对照 characters.md 逐角色核查
     - 第三轮: 对照 reader-feedback.md 核查待处理问题
     - 发现问题立即修正正文，全部通过才提交
  5. 提交到 Git
  6. 汇报完成情况（含自检循环结果）
```

### 处理反馈
```
你: [粘贴读者反馈]
AI:
  1. 记录到 reader-feedback.md
  2. 分析影响范围
  3. 提供处理建议
  4. 询问是否修改
```

### 更新最佳实践
```
你: 更新最佳实践
AI:
  1. 扫描 docs/ 新增内容
  2. 提取关键要点
  3. 更新 writing-guide.md
  4. 应用到后续创作
```

---

## 📂 项目结构说明

```
your-novel/
├── chapters/              # 章节文件
│   ├── 第001章-标题.md
│   ├── 第002章-标题.md
│   └── ...
├── references/            # 参考文档
│   ├── outline.md         # 大纲（必填）
│   ├── writing-guide.md   # 创作指南（可选）
│   └── reader-feedback.md # 读者反馈（自动）
├── docs/                  # 参考资料
│   ├── 网文写作指南.md
│   └── ...
└── README.md              # 项目首页
```

---

## 💡 常见场景

### 场景1: 我有详细大纲，想快速创作
```
1. 初始化项目
2. 填写 references/outline.md
3. 说 "写第一章"
4. 持续创作 "写第二章"、"写第三章"...
```

### 场景2: 我想边写边完善大纲
```
1. 初始化项目，先写简单大纲
2. 创作前几章
3. 根据创作感觉，补充后续大纲
4. 继续创作
```

### 场景3: 我有参考资料想整合
```
1. 将参考资料放入 docs/
2. 说 "更新最佳实践"
3. Skill 自动提取要点到 writing-guide.md
4. 后续创作自动应用这些原则
```

### 场景4: 读者有反馈需要处理
```
1. 粘贴读者反馈给 AI
2. AI 记录到 reader-feedback.md
3. AI 分析并提供建议
4. 选择：立即修改 / 后续注意 / 忽略
```

---

## ⚙️ 高级功能

### 版本回滚
如果修改不满意，可以回滚：
```
你: 查看版本历史
AI: [显示最近5次提交]

你: 回滚到第3次提交
AI: [创建备份分支，回滚，请求确认]
```

### 批量更新章节
如果反馈影响多个章节：
```
你: 有读者说第3-5章的节奏太慢
AI: 
  - 记录反馈
  - 分析影响：第3、4、5章
  - 建议：修改这3章
  
你: 立即修改
AI: [逐章修改，提交]
```

---

## 📊 项目管理

### 查看进度
README.md 自动记录：
- 当前进度：X章 / 总章数
- 已完成字数
- 最后更新时间
- 最近5次提交

### 统计信息
```bash
# 总字数
find chapters/ -name "*.md" -exec wc -w {} + | tail -1

# 章节数
ls chapters/*.md | wc -l

# 提交次数
git log --oneline | wc -l
```

---

## 🛠️ 故障排查

### 问题1: Git 提交失败
```bash
# 检查 Git 配置
git config user.name
git config user.email

# 如果未配置，设置：
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 问题2: 章节没有保存
检查：
1. 是否说了"写第X章"（不是"帮我写"）
2. 是否在 chapters/ 目录
3. 是否有写入权限

### 问题3: 大纲无法识别
检查：
1. 文件名是否为 `references/outline.md`
2. 格式是否正确（Markdown）
3. 是否有必填字段

---

## 📖 推荐阅读

1. [完整文档](SKILL.md) - 详细功能说明
2. [示例项目](templates/example-novel/) - 完整示例
3. [基础模板](templates/project-template/) - 快速开始

---

## 🤝 获取帮助

- GitHub Issues: 报告问题或建议
- 示例项目: 查看实际使用案例
- OpenClaw 社区: 交流讨论

---

## ✅ 检查清单

创作前确认：
- [ ] 已初始化项目
- [ ] 已填写大纲
- [ ] 已配置 Git
- [ ] 已关联 GitHub 仓库（可选）

每章创作后确认：
- [ ] 符合大纲规划
- [ ] 通过自检清单
- [ ] 已提交到 Git
- [ ] 更新了 README.md 进度

---

祝创作愉快！🎉
