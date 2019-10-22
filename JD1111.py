# coding=utf-8

import os
import time


# 2019双11
# 适配小米9

# 全民养红包每日任务页面
# 1.逛逛好店 0/25
# 2.精彩会场 0/3
# 3.精选好物 0/25
# 4.更多好玩互动 0/4
# 5.邀请好友助力 0/30
# 6.看京东推荐官直播/视频 0/4
def startTask():
    for i in range(26, 62):
        print('第 {} 次'.format(i))
        time.sleep(2)

        if 1 <= i <= 25:  # 活动1：逛逛好店
            os.system('adb shell input tap 930 950')
            print('第 {} 次逛逛好店'.format(i))
        elif 1 <= i - 25 <= 3:  # 活动2：精彩会场
            os.system('adb shell input tap 930 1170')
            print('第 {} 次精彩会场'.format(i - 25))
        elif 1 <= i - 28 <= 25:  # 活动3：精选好物
            os.system('adb shell input tap 930 1400')
            print('第 {} 次精选好物'.format(i - 28))
        elif 1 <= i - 53 <= 4:  # 活动4：更多好玩互动
            os.system('adb shell input tap 930 1610')
            print('第 {} 次更多好玩互动'.format(i - 53))
        elif 1 <= i - 57 <= 4:  # 活动6：看京东推荐官直播/视频
            os.system('adb shell input tap 930 2050')
            print('第 {} 次看京东推荐官直播/视频'.format(i - 57))

        time.sleep(2)
        # 活动比较简单，直接返回上一个页面就行
        os.system('adb shell input keyevent KEYCODE_BACK')
        time.sleep(2)
        # 点击朕知道了
        os.system('adb shell input tap 550 1600')

    print('完成任务')


startTask()
