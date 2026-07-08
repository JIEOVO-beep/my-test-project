# GitHub 从零开始使用指南

## 一、注册 GitHub 账号

1. 打开 https://github.com
2. 点击 "Sign up"，输入邮箱、密码、用户名
3. 完成邮箱验证

## 二、配置本地 Git

打开终端，执行以下命令（替换成你的信息）：

```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的注册邮箱"
```

## 三、创建 SSH Key（免密码推送）

```bash
# 生成密钥（一路回车即可）
ssh-keygen -t ed25519 -C "你的邮箱"

# 查看公钥
cat ~/.ssh/id_ed25519.pub
```

复制输出的内容，然后：
1. 登录 GitHub → 右上角头像 → Settings
2. 左边栏 → SSH and GPG keys
3. 点 "New SSH key"，粘贴公钥，保存

测试连接：
```bash
ssh -T git@github.com
# 看到 "Hi xxx! You've successfully authenticated" 就成功了
```

## 四、创建仓库并推送代码

### 方式 A：在 GitHub 上创建新仓库

1. 登录 GitHub，点右上角 "+" → "New repository"
2. 输入仓库名（比如 `my-test-project`）
3. 勾选 "Add a README file"
4. 点击 "Create repository"

### 方式 B：从本地推送已有项目

```bash
# 1. 进入项目目录
cd /Users/jieovo/Documents/Codex/2026-07-08/ni/outputs/test-project

# 2. 初始化 git
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "first commit: initial test project structure"

# 5. 在 GitHub 上创建空仓库（不要勾选 README）
#    然后复制仓库地址，例如：git@github.com:你的用户名/my-test-project.git

# 6. 关联远程仓库并推送
git remote add origin git@github.com:你的用户名/my-test-project.git
git branch -M main
git push -u origin main
```

## 五、日常 Git 命令

```bash
# 查看当前状态
git status

# 查看修改内容
git diff

# 添加文件到暂存区
git add 文件名        # 添加特定文件
git add .             # 添加所有改动

# 提交
git commit -m "写了什么改动"

# 推送到 GitHub
git push

# 拉取最新代码
git pull

# 查看提交历史
git log --oneline
```
