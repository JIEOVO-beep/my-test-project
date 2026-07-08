# 软件测试练习项目

本仓库包含针对开源电商平台 JPetStore 的完整测试实践，包括：
- 测试计划与用例设计
- Bug 报告示例
- API 接口自动化测试脚本
- GitHub 使用指南

## 项目结构

```
test-project/
├── README.md                  # 本文件
├── github-guide.md            # GitHub 使用教程
├── test-plan/
│   └── test-plan.md           # 测试计划模板
├── test-cases/
│   └── login-test-cases.csv   # 登录模块测试用例
└── api-tests/
    ├── requirements.txt       # Python 依赖
    ├── test_bookstore_api.py  # 接口测试脚本
    └── pytest.ini             # pytest 配置
```

## 练习目标

1. 理解功能测试的完整流程：需求分析 → 用例设计 → 执行 → Bug 跟踪
2. 掌握接口自动化测试：Python + Requests + Pytest
3. 学会使用 Git/GitHub 管理代码

## 推荐练习项目

### 1. JPetStore (电商，最适合入门)
- 在线 demo：https://petstore.octoperf.com/
- 特点：经典电商场景，注册/登录/浏览/搜索/购物车/下单
- 适合：功能测试 + Selenium 自动化

### 2. WordPress (博客系统)
- 下载：https://wordpress.org/download/
- 特点：功能丰富，文章/评论/用户/设置模块
- 适合：功能测试 + 接口测试

### 3. Swagger Petstore (纯 API)
- 在线地址：https://petstore.swagger.io/
- 特点：RESTful API 标准，适合做接口自动化
