import cv2
from cv2 import imread
import numpy as np

img = imread('spider.png')
img2 = imread('spider2.png')
k = np.ones((5,5),np.uint8)
# dst1 = cv2.dilate(img,k)
# dst2 = cv2.erode(dst1,k)
cv2.imshow('0',img)

dst3 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k) #梯度运算
dst4 = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,k)  #顶帽运算
dst5 = cv2.morphologyEx(img2,cv2.MORPH_BLACKHAT,k)  #黑帽运算
cv2.imshow('3',dst3)
cv2.imshow('4',dst4)
cv2.imshow('5',dst5)
# cv2.imshow('2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()