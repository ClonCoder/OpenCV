import cv2
from cv2 import imread
img = imread('flower.png')
dst = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
t1,dst1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow('a',dst1)

contours, hierarchy = cv2.findContours(dst1,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img,contours,-1,(0,0,255),2)
cv2.imshow('b',img)

cv2.waitKey()
cv2.destroyAllWindows()