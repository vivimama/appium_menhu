# -*- coding: utf-8 -*-
# @Time  : 2018/7/30 16:55 
# @Author: mild
# @File  : method.py


class Methods:
    def __init__(self, self_s):
        self.self_s = self_s

    """循环判断"""
    def th_fy(self):
        try:
            for call_one in range(0, 5):
                self.self_s.find_android_id(self.self_s.iphone_callthree[call_one]).is_displayed()
        except Exception:
            print("未找到元素")
        else:
            print("元素存在")
            self.self_s.find_android_id(self.self_s.iphone_callthree[1]).click()  # 点击拨号 显示不可用
        """获取吐司内容"""
        self.self_s.judge_toast(u"暂不可用")
    """语音发送"""
    def fs_yy(self):
        self.self_s.find_android_id(self.self_s.chatting_mode_btn).click()  # 发送语音  松开发送
        self.self_s.TouchAction("id", 5000, self.self_s.audioRecord, None)  # 长按5秒
