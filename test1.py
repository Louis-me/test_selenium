# -*- coding: utf-8 -*-
import unittest
from time import ctime
from selenium import webdriver
from threading import Thread
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
本地运行用例,多线程执行

"""
class MyTestCase(unittest.TestCase):

    def setUp(self):
        chromedriver = PATH("exe/chromedriver.exe")
        print(chromedriver)
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.maximize_window()

    def test_something(self):
        self.driver.get("https://www.baidu.com")
        print(self.driver.title)

        self.assertEqual(self.driver.name, "chrome")

    def test_search_button(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("zalenium")
        self.driver.find_element_by_id("su").click()
        print(self.driver.title)
        self.assertTrue(self.driver.find_element_by_id("su").is_displayed())

    def tearDown(self):
        self.driver.quit()


def run():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    threads = []
    for i in range(2):
        t = Thread(target=run, args=())
        threads.append(t)
    for t in range(2):
        threads[t].start()

    for t in range(2):
        threads[t].join()

    print('end:%s' % ctime())
