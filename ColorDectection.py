import cv2 
import numpy as np

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

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()