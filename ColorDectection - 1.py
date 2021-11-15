import cv2 
import numpy as np
import pyautogui

# px = pyautogui.pixel(1500, 1000)
# print(px)

for x in range(0,100,5) :
    for y in range(0,100,5) :
        px = pyautogui.pixel(x, y)
        print(px)

# img = cv2.imread("color-signals.jpg")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_green = np.array([36, 25, 25])
# upper_green = np.array([70, 255, 255])
# mask1 = cv2.inRange(hsv, lower_green, upper_green)
# contours, hierarchy = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# for data in contours:
#     print("The contours have this data %r"%data)
# cv2.drawContours(img,contours,-1,(255,0,0),3)
# cv2.imshow("Result img", img)
# cv2.imshow("Mask", mask1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()