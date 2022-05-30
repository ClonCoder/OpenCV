import cv2
from cv2 import imread
from matplotlib.pyplot import gray
img = imread('shape2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
t, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])

cv2.polylines(img,[hull],True,(0,0,255),2)

cv2.imshow('a',img)
cv2.waitKey()
cv2.destroyAllWindows()