# 项目说明
web自动化

# 环境准备
- windows
- python3.6
- pytest4.5.1
- allure

# 依赖安装包

使用pip安装依赖包
> pip install -r requirements.txt

# 运行用例

运行用例，生成报告在./report
> pytest --alluredir ./report

# 生成allure

启动allure服务查看报告
> allure serve ./report