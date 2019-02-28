# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:29 
# @Author: mild
# @File  : base_page.py
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Action(object):

    def __init__(self, se_driver):
        self.driver = se_driver

    def find_android_id(self, loc):
        try:
            return self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("' + loc + '")')
        except Exception as e:
            print("cannot find id", e, loc)

    def find_android_ids(self, loc):
        try:
            return self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().resourceId("' + loc + '")')
        except Exception as e:
            print("cannot find id subscript", e, loc)

    def find_android_className(self, loc):
        try:
            return self.driver.find_element_by_android_uiautomator(
                'new UiSelector().className("' + loc + '")')
        except Exception as e:
            print("cannot find ClassName", e, loc)

    def find_android_classNames(self, loc):
        try:
            return self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().className("' + loc + '")')
        except Exception as e:
            print("cannot find classNames", e, loc)

    def find_android_text(self, loc):
        try:
            return self.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("' + loc + '")')
        except Exception as e:
            print("cannot find text", e, loc)

    def find_android_class_index(self, locclass, locindex):
        try:
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().className("' + locclass + '").childSelector(new UiSelector().index("'
                + locindex + '"))')
        except Exception as e:
            print("cannot find class index", e, locclass, locindex)

    def find_android_fu_xpath(self, loc0, loc1):
        try:
            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().className("' + loc0 + '").childSelector(new UiSelector().className('
                                                        '"' + loc1 + '"))').click()
        except Exception as e:
            print("cannot find id", e, loc1)

    def touch_tap(self, x, y, x1, y1):  # 点击坐标  ,x1,x2,y1,y2,duration
        self.driver.tap([(x, y), (x1, y1)], 100)

    def TouchAction(self, identi, times, ids, ii):
        if identi == "id":
            action1 = TouchAction(self.driver)
            el = self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("' + ids + '")')
            action1.long_press(el, None, None, times).wait(2000).perform()
        elif identi == "ids":
            action1 = TouchAction(self.driver)
            el = self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().resourceId("' + ids + '")')[ii]
            action1.long_press(el, None, None, times).wait(100).perform()

        elif identi == "idclass":
            action1 = TouchAction(self.driver)
            el = self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().className("' + ids + '")')[2]
            action1.long_press(el, None, None, times).wait(2000).perform()

    def isElement(self, identifyBy, loc):
        """
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        """
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("' + loc + '")')
            elif identifyBy == "ids":
                # self.driver.implicitly_wait(60)
                self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("' + loc + '")')
            elif identifyBy == "class":
                self.driver.find_element_by_android_uiautomator('new UiSelector().className("' + loc + '")')
            elif identifyBy == "link text":
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + loc + '")')
            flag = True
        except Exception:
            flag = False
        finally:
            return flag

    def im_wait(self):
        self.driver.implicitly_wait(8)

    def back_menu(self):
        self.driver.back()

    def judge_toast(self, message):
        try:
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
            return element
        except Exception:
            return "失败"

    def is_toast_exist(self, text, timeout=5, poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(self, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception:
            return False

    def swipes(self, x, y, x1, y1):
        print(self.driver.get_window_size())
        self.driver.swipe(x, y, x1, y1, 300)  # 滑屏
