import cv2
import numpy as np

img = cv2.imread('car.jpg')
rows = len(img)
cols = len(img[0])
p1   = np.zeros((4,2),np.float32)
p1[0] = [0,0]
p1[1] = [cols-1,0]
p1[2] = [0,rows-1]
p1[3] =[cols-1,rows-1]
p2   = np.zeros((4,2),np.float32)
p2[0] = [90,0]
p2[1] = [cols-90,0]
p2[2] = [0,rows-1]
p2[3] = [cols-1,rows-1]
M =cv2.getPerspectiveTransform(p1,p2)
dst =cv2.warpPerspective(img,M,(cols,rows))
cv2.imshow('a',img)
cv2.imshow('b',dst)
cv2.waitKey()
cv2.destroyAllWindows()