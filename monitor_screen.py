import mouseinfo
import pyautogui

from ultralytics import YOLOv10
from PIL import ImageGrab,Image
import keyboard
import pyautogui as pt
import pygame
import pygetwindow
import numpy as np
import cv2 as cv
import torch
import math
import mss
import time
import pydirectinput

# 计算鼠标需要相对移动的距离

# 示例

# 屏幕分辨率假设为 1920x1080

# 相对移动鼠标


'''class PI_control:
    def __init__(self,Kp,Ki)->None:
        self.Kp = Kp
        self.Ki = Ki
        self.integral = 0
        self.previous_error = 0

    def __call__(self, error):
        delta_error = error - self.previous_error
        self.previous_error = error
        self.integral += delta_error
        delta_u = (self.Kp * delta_error) + (self.Ki * self.integral)
        return delta_u

x_pi = PI_control(0.35,0.5)
y_pi = PI_control(0.17,0.26)
'''


st=False
model = YOLOv10("yolov10b.pt")
windows_title = "Counter"
#windows_title = "google"
window = pygetwindow.getWindowsWithTitle(windows_title)[0]
device = torch.device("cuda:0")
model.to(device)
while True:
    if window:
        x,y,w,h=window.left,window.top,window.width,window.height
        screenshot=ImageGrab.grab(bbox=[x,y,x+w,y+h])
        image_src=cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)
        size_x,size_y=image_src.shape[1],image_src.shape[0]
        #image_src=cv.resize(image_src,(640,640))
        result=model.predict(source=image_src,imgsz=640,conf=0.8,show=False)
        boxes=result[0].boxes.xywhn
        best_xy=None
        mouse_x,mouse_y=pt.position()
        print(pt.position())
        for box in boxes:
            x,y=box[0],box[1]
            y=box[1]-box[3]/4
            dist=((x*size_x+window.left-mouse_x)**2+(y*size_y+window.top-mouse_y)**2)**0.5
            cv.rectangle(image_src,(int((box[0]-box[2]/2)*size_x),int((box[1]-box[3]/2)*size_y)),(int((box[0]+box[2]/2)*size_x),int((box[1]+box[3]/2)*size_y)),color=(255,255,0),thickness=5)
            if not best_xy:
                best_xy=((x,y),dist)
            else:
                _,old_dist=best_xy
                if dist<old_dist:
                    best_xy=((x,y),dist)
        mouse_x, mouse_y = pt.position()
        print(pt.position())
        '''if best_xy and not keyboard.is_pressed('f'):
            target_x = int(best_xy[0][0] * size_x + window.left)
            target_y = int(best_xy[0][1] * size_y + window.top)
            print(target_x, target_y)
            # 计算相对移动距离
            move_x = target_x - mouse_x
            move_y = target_y - mouse_y'''

            # 使用 pydirectinput 移动鼠标
        '''if keyboard.is_pressed('f'):
            st=not st'''
        if  keyboard.is_pressed('f') and best_xy:
            target_x = int(best_xy[0][0] * size_x + window.left)
            target_y = int(best_xy[0][1] * size_y + window.top)
            print(target_x, target_y)
            # 计算相对移动距离
            move_x = target_x - mouse_x
            move_y = target_y - mouse_y

            # 使用 pydirectinput 移动鼠标
            print(move_x, move_y)
            sensitivity_factor = 0.38  # 根据游戏的鼠标灵敏度调整这个值
            move_x = int(move_x * sensitivity_factor)
            move_y = int(move_y * sensitivity_factor)

            pydirectinput.moveRel(xOffset=move_x, yOffset=move_y,relative=True)
            pyautogui.click()
            #pt.moveTo(best_xy[0][0] * size_x+window.left, best_xy[0][1] * size_y+window.top)
            #pt.move(move_x, move_y)
        else:
            pass
            '''with keyboard.Listener(on_press=on_press) as listener:
                listener.join()'''

            #print(box[0],box[1],box[2],box[3])
        cv.imshow('lwj',image_src)
        cv.waitKey(1)

# 启动键盘监听器