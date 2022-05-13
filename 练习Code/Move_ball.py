import numpy as np
import cv2
import time

width,height = 300,300   #画布宽、高
r = 20   #球半径
x = r+20   #球横坐标起点位置
y = r+100  #球纵坐标起点位置
x_v = y_v = 4  #每一帧运动速度

while cv2.waitKey(1) == -1:
    if x > width-r or x < r :#如果圆横坐标超出边界
        x_v *= -1  #横坐标速度取反
    if y > height-r or y <r :
        y_v *= -1
    x += x_v  #圆心按横坐标速度移动
    y += y_v
    img = np.ones((width,height,3),np.uint8)*255 #创建画布
    cv2.circle(img,(x,y),r,(0,0,255),-1)   #画圆
    cv2.imshow('a',img)
    time.sleep(1/60)  #每秒60帧
cv2.destroyAllWindows()