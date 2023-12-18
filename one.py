from time import sleep

import screen_brightness_control as sbc
import win32gui

# 获取笔记本显示器名称
monitors = sbc.list_monitors("wmi")
currentLight = sbc.get_brightness(display=monitors[0])[0]
# 目标：永劫无间
gameName = "Naraka"
var = 1
while var == 1:
    hwnd = win32gui.GetForegroundWindow()
    # 检测运行了游戏
    if win32gui.GetWindowText(hwnd) == gameName:
        print("目标出现，亮度调至100")
        sbc.fade_brightness(100, display=monitors[0])
    else:
        if win32gui.GetWindowText(hwnd) != gameName and sbc.get_brightness(display=monitors[0])[0]!=currentLight:
            print("目标关闭，亮度调至" + str(currentLight))
            sbc.fade_brightness(currentLight, display=monitors[0])
    sleep(0.2)
