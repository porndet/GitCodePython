from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(660,350,600,400))
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))
            if b == 195:
                pyautogui.click(x+width,h+height)
                time.sleep(0.1)
                break