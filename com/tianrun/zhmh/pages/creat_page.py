# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:28 
# @Author: mild
# @File  : creat_page.py

from com.tianrun.zhmh.pages import base_page
from com.tianrun.zhmh.pages.method import Methods
from com.tianrun.zhmh.pages import id_page
import time


class CreatPage(base_page.Action, id_page.Elements):

    """用例1--登陆"""
    def add_button_link(self):
        self.find_android_id(self.add_button_loc).click()  # 点击立即进入 进入app
        time.sleep(2)
        for quanx in range(0, 5):  # 获取手机权限
            self.find_android_id(self.jurisdiction_loc).click()

    def name_password(self):  # 输入用户名 密码
        pass

    def py_image(self):  # 验证码 识别
        pass

    """用例2   消息"""
    def button_message(self):
        meth = Methods(self)
        self.find_android_className(self.iphone_button).click()  # 点击电话按钮
        self.im_wait()
        for iphone1 in range(0, 11):   # 输入电话号
            self.find_android_id(self.iphone[iphone1]).click()
        self.find_android_id(self.iphone_bohao).click()  # 点击拨号
        self.im_wait()
        meth.th_fy()  # 判断元素 是否存在
        self.back_menu()
        self.find_android_id(self.iphone_add).click()  # 点击 + 号
        self.find_android_id(self.iphone_esc).click()  # 点击取消
        for dell in range(0, 8):
            self.find_android_id(self.del_button).click()

    """拨号  > 按钮 操作"""
    def button_message_two(self):
        meth = Methods(self)
        self.find_android_ids(self.button_youfu)[0].click()  # 点击list第一个通话记录 的用户
        self.find_android_id(self.text_thjl).click()  # 通话记录
        self.back_menu()
        guanzhu = self.find_android_id(self.button_specialFocusTv)  # 详情页 关注用户
        guanzhu.click()
        display = guanzhu.text
        if display == "已关注":
            print("ojbk")
        else:
            print("失败")
        self.im_wait()
        guanzhu.click()
        self.im_wait()
        self.find_android_id(self.button_phoneCapability).click()  # 点击通话按钮
        meth.th_fy()  # 判断元素 是否存在
        self.back_menu()
        sjh = self.find_android_id(self.iphone_shoujihao)  # 获取详情中 中发件人 电话号
        sjhsms = sjh.text
        self.find_android_id(self.button_smsCapability).click()  # 点击短信
        sjh1 = self.find_android_id(self.iphone_duanxingshoujihao)  # 获取短信中发件人 电话号
        sjhsms1 = sjh1.text
        self.back_menu()
        print("***" + sjhsms1 + "***")
        self.find_android_id(self.button_chatCapability).click()  # 发消息
        m = self.find_android_id(self.chatting_content_et)
        m.click()
        m.clear()
        m.send_keys("  ~!@#$%^&*()_+123456`678900-=qwertyuiop[]\{}|asdfghjkl;':zxcvbmm,<><>,./?")
        self.find_android_id(self.chatting_send_btn).click()
        self.im_wait()
        self.find_android_fu_xpath(self.page0_class, self.page1_class)  # 好友操作
        self.find_android_id(self.member_head).click()
        iselenment = self.isElement("id", self.operateFriendBtn)  # 判断页面是否存在
        if iselenment:
            print("跳转成功 页面存在")
        else:
            print("跳转失败 页面不存在")
        self.back_menu()
        self.find_android_id(self.adds).click()  # 点击 + 号创建 讨论组
        for cbs in range(0, 2):  # 选择好友
            cc = self.find_android_ids(self.ytx_select_cbs)[cbs]
            dis = cc.is_displayed()
            if dis:
                cc.click()
            else:
                print("不可选")
        option_style_button = self.find_android_id(self.action_option_style_button)
        option_style_button.click()
        self.im_wait()
        self.judge_toast("群组创建成功")
        self.back_menu()
        self.find_android_fu_xpath(self.page0_class, self.page1_class)
        self.find_android_id(self.clear_msg).click()
        self.find_android_id(self.ytx_positive_btn).click()
        self.judge_toast("清除成功")
        self.back_menu()
        self.back_menu()
        dis = self.find_android_id(self.operateFriendBtn)  # 添加好友
        print(dis.text)
        if dis.text == "添加好友":
            dis.click()
            sear = self.find_android_id(self.search_et)
            sear.click()
            sear.clear()
            sear.send_keys("你好!你好!你好!")
            self.im_wait()
            option_style_button.click()
            self.judge_toast("发送邀请成功")
        else:
            self.find_android_id(self.operateFriendBtn).click()  # 删除好友
            self.find_android_id(self.ytx_positive_btn).click()
            self.judge_toast("删除成功")
            if dis.text == "添加好友":
                print("好友删除成功")
        rrr = None
        for rr in range(0, 11):
            if sjhsms[rr] in sjhsms1:
                rrr = True
            else:
                rrr = False
                break
            pass
        if rrr and display == "已关注":  # 判断两个号码 是否一致
            re = "ojbk"
            print("ojbk 两个号码一样")
            return re
        else:
            print("omg 不一样")
            re = "no pass"
            return re

    """ 消息界面 显示 """
    def message_Interface_find(self):
        fs = Methods(self)
        try:
            self.find_android_id(self.nw_detail).is_displayed()
            print("无网络 不做操作")
        except Exception:
            items = self.isElement("id", self.conversation_items)  # 登陆进来判断是否有消息
            if items:
                list_yh = self.find_android_ids(self.nickname_tv)[0].text  # 点击第一条信息
                if list_yh == "文件传输助手":
                    l_yh = self.find_android_ids(self.conversation_items)[1]
                else:
                    l_yh = self.find_android_ids(self.conversation_items)[0]
                l_yh.click()
                shuru = self.find_android_id(self.chatting_content_et)
                shuru.clear()
                fs.fs_yy()  # 发送语音  松开发送
                self.find_android_id(self.chatting_attach_btn).click()  # 发送图片
                self.im_wait()
                imag = self.find_android_ids(self.app_grid_item_icon)[0]
                imag.click()
                imags = self.find_android_ids(self.rcv_choices)[0]
                imags.click()
                imags = self.find_android_ids(self.rcv_choices)[2]
                imags.click()
                self.find_android_id(self.action_option_style_button).click()
                iv = self.find_android_id(self.chatting_smiley_btn)  # 点击表情 第一个 和 第二个
                iv.click()
                iv.click()
                time.sleep(0.5)
                self.touch_tap(47, 1279, 137, 1372)
                self.touch_tap(196, 1279, 286, 1372)
                """输入字符发送发送"""
                shuru.click()
                shuru.send_keys("1234567890 测试一 test ~`!@#$%^&*()_+ ")
                time.sleep(0.5)
                send_btn = self.find_android_id(self.chatting_send_btn)
                send_btn.click()

                """消息长按操作"""
                im = self.isElement("id", self.chatting_content_itv)
                if im:
                    self.TouchAction("ids", None, self.chatting_content_itv, -1)
                    self.im_wait()
                    for tit in range(0, 6):
                        tt = self.find_android_classNames(self.titleclass)[tit].text
                        if tt == "重发":
                            print("消息 未 发送 成功")
                        else:
                            print(tt)
                        if tit == 3 and tt != "撤回":
                            break
                    self.find_android_classNames(self.titleclass)[0].click()
                    self.judge_toast("已复制到剪切板")
                    """转发操作"""
                    self.TouchAction("ids", None, self.chatting_content_itv, -1)
                    self.find_android_classNames(self.titleclass)[1].click()
                    self.find_android_ids(self.ytx_select_cbs)[0].click()
                    self.find_android_ids(self.ytx_select_cbs)[1].click()
                    self.find_android_id(self.action_option_style_button).click()
                    fs = self.find_android_id(self.ytx_positive_btn)
                    fs.click()
                    """收藏"""
                    self.TouchAction("ids", None, self.chatting_content_itv, -1)
                    self.find_android_classNames(self.titleclass)[2].click()
                    ssss = self.is_toast_exist("收藏成功")
                    print(ssss)
                    """删除"""
                    self.TouchAction("ids", None, self.chatting_content_itv, -1)
                    self.find_android_classNames(self.titleclass)[4].click()
                    fs.click()
                    """撤回"""
                    self.TouchAction("ids", None, self.chatting_content_itv, -1)
                    self.find_android_classNames(self.titleclass)[3].click()
                    chehui = self.find_android_ids(self.chatting_content_itv)[-1].text
                    print(chehui)
                    if chehui == "你撤回了一条消息":
                        print("撤回成功")
                    else:
                        print("撤回失败")

                    """更多"""
                    shuru.clear()
                    shuru.click()
                    shuru.send_keys("001125")
                    time.sleep(0.5)
                    try:
                        self.touch_tap(924, 963, 1056, 1059)
                        self.TouchAction("ids", None, self.chatting_content_itv, -1)
                        self.find_android_classNames(self.titleclass)[5].click()
                        time.sleep(0.5)
                        self.touch_tap(0, 1776, 1080, 1920)
                        self.find_android_ids(self.ytx_select_cbs)[0].click()
                        self.find_android_ids(self.ytx_select_cbs)[1].click()
                        self.find_android_id(self.action_option_style_button).click()
                        fs.click()
                    except Exception:
                        print("失效")
                else:
                    print("无消息 找不到id")
                self.im_wait()
                """选取图片超过9张吐司提示"""
                attach = self.find_android_id(self.chatting_attach_btn)
                attach.click()
                attach.click()
                imag = self.find_android_ids(self.app_grid_item_icon)[0]
                imag.click()
                for im in range(0, 10):
                    self.find_android_ids(self.rcv_choices)[im].click()
                    if im == 9:
                        self.judge_toast("最多选择9张图片")
                        self.find_android_id(self.action_option_style_button).click()
                """相机交互"""
                attach.click()
                attach.click()
                self.find_android_ids(self.app_grid_item_icon)[1].click()
                self.touch_tap(372, 1534, 708, 1870)
                time.sleep(1.5)
                self.touch_tap(690, 1582, 930, 1822)
                self.find_android_ids(self.app_grid_item_icon)[1].click()
                self.back_menu()
                self.find_android_ids(self.app_grid_item_icon)[1].click()
                self.find_android_classNames(self.imageview)[0].click()
                time.sleep(0.5)
                self.TouchAction("idclass", 5000, self.photograph, None)
                time.sleep(1.5)
                self.touch_tap(690, 1582, 930, 1822)
                """个人名片"""
                self.find_android_id(self.chatting_attach_btn).click()
                self.find_android_id(self.chatting_attach_btn).click()
                self.find_android_ids(self.app_grid_item_icon)[7].click()
                cesy = self.find_android_ids(self.ytx_employee_root)
                cesy[1].click()
                dialog = self.find_android_id(self.confirm_dialog_btn1)
                dialog.click()
                self.find_android_ids(self.app_grid_item_icon)[7].click()
                shousuo = self.find_android_id(self.multi_select_contact_edittext)
                shousuo.click()
                shousuo.clear()
                shousuo.send_keys("安卓测试一")
                cesy[0].click()
                dialog.click()
                self.find_android_ids(self.app_grid_item_icon)[7].click()
                self.find_android_ids(self.ytx_label_name)[0].click()

                ces = self.find_android_id(self.multi_select_contact_edittext)
                ces.click()
                ces.clear()
                ces.send_keys("测试一")
                cesy = self.find_android_ids(self.ytx_employee_root)
                tces = cesy[0].text
                if tces == "测试一":
                    cesy[0].click()
                else:
                    cesy[1].click()
                dialog.click()
                """阅后即焚"""
                self.find_android_ids(self.app_grid_item_icon)[6].click()
                shuru.click()  # 输入字符发送
                shuru.send_keys("001125 test一 test ~`!@#$%^&*()_+ ")
                time.sleep(0.5)
                send_btn = self.find_android_id(self.chatting_send_btn)
                time.sleep(0.5)
                send_btn.click()
                fs.fs_yy()  # 语音
                yhjf = self.find_android_id(self.chatting_attach_burn_btn)
                yhjf.is_displayed()
                if yhjf.is_displayed():
                    print("阅后即焚存在")
                    yhjf.click()  # 点击取消

                self.find_android_id(self.chatting_attach_btn).click()  # 点击+号 翻页
                x = self.driver.get_window_size()['width']  # 获取屏幕宽
                y = self.driver.get_window_size()['height']  # 获取屏幕高
                print(x, y)
                self.swipes(1000, 3 / 4 * y, 100, 3 / 4 * y)
                self.find_android_ids(self.app_grid_item_icon)[2].click()
                jump = self.find_android_id(self.ytx_action_title).text
                print(jump)
            else:
                print("界 面 没 消 息")
