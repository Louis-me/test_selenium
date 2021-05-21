# coding=utf-8
import unittest
from BeautifulReport import BeautifulReport
import os

# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "case")
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)
# 获取测试报告目录
reportpath = os.path.join(curpath, "report")
if not os.path.exists(reportpath): os.mkdir(reportpath)


def add_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover

def run():
    cases = add_case()
    result = BeautifulReport(cases)
    result.report(filename='report.html', description='测试deafult报告', log_path='report')

if __name__ == '__main__':
    run()