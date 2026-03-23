# 项目模板说明

本目录包含用于快速启动新小说项目的模板文件。

---

## 模板列表

### 1. project-template
基础项目模板，包含：
- 标准目录结构
- README.md 模板
- 大纲模板 (outline-template.md)
- 创作指南模板 (writing-guide.md)
- 读者反馈模板 (reader-feedback.md)

### 2. example-novel
完整示例项目（基于《真理法则：浮空城编年史》）：
- 完整的项目结构
- 3个示例章节
- 详细的大纲
- 完善的创作指南
- 读者反馈示例

---

## 使用方法

### 方法1: 使用 Novel Writer Skill 自动初始化
```
初始化小说项目：[你的小说名称]
```

Skill 会自动创建标准结构。

### 方法2: 手动复制模板
```bash
# 复制基础模板
cp -r templates/project-template your-novel-name/

# 或复制示例项目（包含参考内容）
cp -r templates/example-novel your-novel-name/

# 进入项目目录
cd your-novel-name/

# 初始化 Git
git init
git add .
git commit -m "初始化项目"

# 关联远程仓库
git remote add origin https://github.com/yourusername/your-novel-name.git
git push -u origin main
```

---

## 模板定制

### 修改基础信息
编辑以下文件以适配你的项目：
- `README.md` - 项目名称、简介、作者信息
- `references/outline-template.md` - 大纲内容
- `references/writing-guide.md` - 创作风格和原则

### 添加参考资料
将创作参考资料放入 `docs/` 文件夹，然后运行：
```
更新最佳实践
```

Skill 会自动提取关键要点并更新创作指南。

---

## 注意事项

- 模板中的 `[占位符]` 需要替换为实际内容
- 大纲是创作的基础，建议先完善大纲再开始创作
- 定期更新 README.md 的进度信息
- 每章完成后立即提交到 Git

---

## 获取帮助

- 详细文档：[../SKILL.md](../SKILL.md)
- 使用指南：[../README.md](../README.md)
- Issue 反馈：提交到 GitHub Issues
