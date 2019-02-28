# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:19 
# @Author: mild
# @File  : main.py

import unittest
import HTMLTestRunner
import time

testcase_path = ".\\test"  # 相对路径
report_path = ".\\report\\"  # 存放html地址


def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit


suite = creat_suite()
#  定义生成测试报告的名称
filename = r"" + str(time.strftime('%Y%m%d%H%M%S')) + ".html"
fp = open(report_path + filename, 'wb')
# 定义测试报告的路径，标题，描述等内容
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试报告')
runner.run(suite)
fp.close()
