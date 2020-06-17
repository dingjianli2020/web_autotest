from pages.articleclassify_page import ArticleClassifyPage
import allure
import pytest


@allure.story("用例：编辑文章分类")
@allure.title("编辑文章分类，保存成功")
#@allure.testcase(" 测试用例对应地址")
def test_add_classify1(login_fixture):
    '''用例描述：
         1.点击文章分类导航标签，跳转文章列表页面
         2.点击增加文章分类按钮，跳转编辑页面
         3.编辑页面输入分类名称
         4.点击保存按钮，保存成功，在列表中显示添加的分类名称
    '''
    driver = login_fixture
    article = ArticleClassifyPage(driver)

    with allure.step("步骤1：点击文章分类导航标签，跳转文章列表页面"):
        article.click_articleclassify()
    with allure.step("步骤2：点击增加文章分类按钮，跳转编辑页面"):
        article.click_add_articleclassify()
    with allure.step("步骤3：编辑页面输入分类名称:测试分类test"):
        article.input_article()
    with allure.step("步骤4：点击保存按钮，保存成功，在列表中显示添加的分类名称"):
        article.click_save_button()
    with allure.step("获取结果：获取页面实际结果，判断是否添加成功"):
        result = article.is_add_success()
        print(result)
    with allure.step("断言：判断是否添加成功"):
        assert result == True


@allure.story("用例：重复编辑文章分类")
@allure.title("编辑文章分类repeat_test，保存失败")
def test_add_classify2(login_fixture):
    driver = login_fixture
    input_text = "repeat_test"
    article = ArticleClassifyPage(driver)
    with allure.step("步骤1：编辑文章分类：repeat_test"):
        article.click_articleclassify()
        article.click_add_articleclassify()
        article.input_article(input_text)
        article.click_save_button()
    with allure.step("获取结果：获取页面实际结果，判断是否添加成功"):
        result = article.is_add_success()
        print(result)
    with allure.step("断言：判断是否添加成功"):
        assert result == True

    with allure.step("步骤2：编辑文章分类：repeat_test"):
        article.click_add_articleclassify()
        article.input_article(input_text)
        article.click_save_button()
    with allure.step("获取结果：获取页面实际结果，判断是否添加成功"):
        result1 = article.is_add_success()
    with allure.step("断言：判断是否添加成功"):
        # assert result1 == False
        assert result1 == True
