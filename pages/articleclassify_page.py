from common.base import Base
from pages.login_page import LoginPage
from selenium import webdriver
import time


class ArticleClassifyPage(Base):
    # 文章分类
    loc1 = ("xpath", '//*[@id="left-side"]/ul[1]/li[11]/a')
    # 增加文章分类
    loc2 = ("xpath", '//*[@id="content-block"]/div[1]/div[2]/div/a')
    # 输入框
    loc3 = ("xpath", '//*[@id="id_n"]')
    # 保存按钮
    loc4 = ("xpath", '//*[@id="articleclassify_form"]/div[2]/button')

    # 判断添加成功
    loc5 = ("xpath", '//*[@id="content-block"]/div[2]')

    def click_articleclassify(self):  # 点击文章分类按钮
        self.click(self.loc1)

    def click_add_articleclassify(self):  # 点击增加文章分类按钮
        self.click(self.loc2)

    def input_article(self, text="测试分类test"):  # 输入文章分类名称
        self.send(self.loc3, text)

    def click_save_button(self):
        self.click(self.loc4)

    def is_add_success(self, expected_text="添加成功"):
        text = self.get_text(self.loc5)
        print("获取元素文本内容为：%s" % text)
        return expected_text in text

if __name__ == '__main__':
    # 登录
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()

    article = ArticleClassifyPage(driver)
    article.click_articleclassify()
    article.click_add_articleclassify()
    article.input_article()
    article.click_save_button()

    result = article.is_add_success()
    print(result)

    #time.sleep(5)

    #driver.quit()




