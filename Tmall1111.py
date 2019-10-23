# coding=utf-8

import os
import time


# 2019.10.21-2019.11.11
# 适配小米9，有 bug，领喵币中心页面的部分栏目会消失，并且有些店铺名字过长

# 领喵币中心页面
# 1.分享给好友 0/5
# 2.逛店铺 0/20
# 3-6. 其它活动 0/1
def startTask():
    for i in range(1, 20):
        print('第 {} 次'.format(i))
        time.sleep(5)

        if 1 <= i <= 20:  # 活动1：逛店铺
            os.system('adb shell input tap 900 1270')
        else:  # 活动2：其它活动
            y = 1270 + (i - 20) * 185
            os.system('adb shell input tap 900 ' + str(y))

        # 活动要求：需要往下滑动
        for j in range(1, 15):
            time.sleep(1)  # 每隔 1s 滑动一次
            os.system('adb shell input swipe 900 800 900 500')  # 滑动页面

        os.system('adb shell input keyevent KEYCODE_BACK')  # 返回上一个页面
    print('完成任务')


startTask()
