import pygame
import math
import pyautogui
import time
from pynput import keyboard
from pygame.math import Vector2

screenWidth, screenHeight = pyautogui.size()

#pyautogui.moveTo(screenWidth/2, screenHeight/2)


def on_press(key):
    try:
        if key.char == 'f':  # 检测到按下了 'k' 键
            mouse_x, mouse_y = pyautogui.position()
            pyautogui.moveTo(mouse_x + 220, mouse_y + 220)
            print("你按下了 'f' 键，执行某项操作！")
    except AttributeError:
        pass

# 启动键盘监听器
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()