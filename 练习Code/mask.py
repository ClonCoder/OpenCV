import cv2
import numpy as np

img1 = np.zeros((150,150,3),np.uint8)
img1[:,:,0] =255   #blue
img2 = np.zeros((150,150,3),np.uint8)
img2[:,:,2] =255   #red

img = cv2.add(img1,img2)
cv2.imshow('1',img)

m = np.zeros((150,150,1),np.uint8)
m[50:100,50:100,:] =255
cv2.imshow('2',m)

img = cv2.add(img1,img2,mask = m)
cv2.imshow('3',img)

cv2.waitKey()
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# img1 = np.zeros((150,150,3),np.uint8)
# img1 [:,:,0] = 255  #蓝色通道赋值255
# img2 = np.zeros((150,150,3),np.uint8)
# img2 [:,:,1] = 255  #绿色通道赋值255
# img3 = np.zeros((150,150,3),np.uint8)
# img3 [:,:,2] = 255  #红色通道赋值255

# cv2.imshow('1',img1)
# cv2.imshow('2',img2)
# cv2.imshow('3',img3)

# img = cv2.add(img1,img2)
# cv2.imshow('1+2',img)  #蓝+绿
# img = cv2.add(img1,img3) 
# cv2.imshow('1+3',img)  #蓝+红
# img = cv2.add(img2,img3)
# cv2.imshow('2+3',img)  #绿+红
# img = cv2.add(img,img3)
# cv2.imshow('1+2+3',img)
# cv2.waitKey()
# cv2.destroyAllWindows()

