import cv2
import numpy as np

img = np.ones((300,300,3),np.uint8)*255    #创建画布
for numbers in range(0,100):
    center_x = np.random.randint(0,300)
    center_y = np.random.randint(0,300)
    radius   = np.random.randint(5,50)
    color    = np.random.randint(0,256,size=(3,)).tolist() #随机获取线条颜色，颜色由3个在[0,255]随机数组成的列表表示
    cv2.circle(img,(center_x,center_y),radius,color,-1)

cv2.imshow('a',img)
cv2.waitKey()
cv2.destroyAllWindows()