# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:23
# @Author: mild
# @File  : test_creat.py
from appium import webdriver
import unittest
from com.tianrun.zhmh.pages.creat_page import CreatPage
import time


class Test(unittest.TestCase):
    """智慧门户初始化apk信息"""

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'automationName': 'appium',
            'deviceName': '8BN0217B14002095',
            'appPackage': 'com.yuntongxun.rongxin.lite',
            'appActivity': 'com.yuntongxun.pluginexample.ui.LauncherUI',
            'noReset': True,
            # 'app': 'C:/Users/18801/Desktop/DOME/PYTHON/TianRun/com/tianrun/zhmh/apk/Android_TianRun_V1.1.0.apk',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
        }
        # 打开 应用
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 最大等待时间
        self.driver.implicitly_wait(20)

    def q_test_install(self):
        """安装app进入登陆"""
        sp = CreatPage(self.driver)
        sp.add_button_link()

    def q_test_message(self):
        """消息用例"""
        sp = CreatPage(self.driver)
        sp.button_message()
        a = sp.button_message_two()
        self.assertEqual(a, "ojbk", msg="条件失败  no ojbk")

    def q_test_message_two(self):
        """消息界面 用例"""
        sp1 = CreatPage(self.driver)
        sp1.message_Interface_find()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()