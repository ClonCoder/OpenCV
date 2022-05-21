import numpy as np
import cv2

def encode(img,img_key):
    result = img = cv2.bitwise_xor(img,img_key)
    return result

flower = cv2.imread('flowers.png')
rows,cols,channel = flower.shape
img_key = np.random.randint(0,256,(rows,cols,3),np.uint8)
cv2.imshow('1',flower)
cv2.imshow('2',img_key)

result = encode(flower,img_key)
cv2.imshow('3',result)
result = encode(result,img_key)
cv2.imshow('4',result)
cv2.waitKey()
cv2.destroyAllWindows()