# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

"""
远程调用服务器
"""


class MyTestCase(unittest.TestCase):

    def setUp(self):
        chrome_capabilities = {
            "browserName": "chrome",
            "version": "90.0.4430.85",
            "platform": "ANY",
            "javascriptEnabled": True,
            "marionette": True
        }

        self.driver = webdriver.Remote("http://192.210.206.201:4444/wd/hub",
                                       desired_capabilities=chrome_capabilities)

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
    run()
