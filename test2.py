# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import os
# https://github.com/TesterlifeRaymond/BeautifulReport
from BeautifulReport import BeautifulReport

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
本地使用用例，测试报告用BeautifulReport
"""


class MyTestCase(unittest.TestCase):
    img_path = 'img'

    def setUp(self):
        chromedriver = PATH("exe/chromedriver.exe")
        print(chromedriver)
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.maximize_window()  # 将浏览器最大化

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @BeautifulReport.add_test_img('test_something')
    def test_something(self):
        """
        打开百度
        """
        self.driver.get("https://www.baidu.com")
        print(self.driver.title)
        self.driver.find_element_by_id("kw1")
        # self.assertEqual(self.driver.name, "chrome")

    def test_search_button(self):
        """
        搜索内容
        """
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("zalenium")
        self.driver.find_element_by_id("su").click()
        print(self.driver.title)
        self.assertTrue(self.driver.find_element_by_id("su1").is_displayed())

    def tearDown(self):
        self.driver.quit()


def run():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite = unittest.TestSuite([suite1])
    # runner = HTMLTestRunner(output='example_suite')
    result = BeautifulReport(suite)
    # runner.run(suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')


if __name__ == '__main__':
    run()
