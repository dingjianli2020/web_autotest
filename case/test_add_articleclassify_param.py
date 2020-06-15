from pages.articleclassify_page import ArticleClassifyPage
import allure
import pytest
import os
from common.read_yaml import readyml

# 测试数据
'''
test_datas = [
    ["测试中文", True],
    ["English", True],
    ["112233", True]
]
'''

# yaml文件读取测试数据
cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(cur_path, 'data_test2.yml')
print(yaml_path)
b = readyml(yaml_path)
print(b['test_add_articleclassify_param2'])

test_data = b['test_add_articleclassify_param2']


@pytest.fixture(scope="function")
def delete_data():
    print("连接数据库，清理数据")


@allure.story("用例：编辑文章分类")
# @allure.title("编辑文章分类，保存成功")
# @allure.testcase(" 测试用例对应地址")
@pytest.mark.parametrize("input_text, expected",
                         test_data,
                         # ids用例标题
                         ids=["文章分类输入中文，保存成功",
                              "文章分类输入英文，保存成功",
                              "用文章分类输入英文，保存成功"]
                         )
def test_add_classify1(login_fixture, delete_data, input_text, expected):
    '''用例描述：
         1.点击文章分类导航标签，跳转文章列表页面
         2.点击增加文章分类按钮，跳转编辑页面
         3.编辑页面输入分类名称
         4.点击保存按钮，保存成功，在列表中显示添加的分类名称
    '''
    driver = login_fixture
    # input_text = "中文"
    article = ArticleClassifyPage(driver)

    with allure.step("步骤1：点击文章分类导航标签，跳转文章列表页面"):
        article.click_articleclassify()
    with allure.step("步骤2：点击增加文章分类按钮，跳转编辑页面"):
        article.click_add_articleclassify()
    with allure.step("步骤3：编辑页面输入分类名称:测试分类test"):
        article.input_article(input_text)
    with allure.step("步骤4：点击保存按钮，保存成功，在列表中显示添加的分类名称"):
        article.click_save_button()
    with allure.step("获取结果：获取页面实际结果，判断是否添加成功"):
        result = article.is_add_success()
        print(result)
    with allure.step("断言：判断是否添加成功"):
        assert result == expected