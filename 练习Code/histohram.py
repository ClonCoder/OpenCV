import cv2
import numpy as np
from matplotlib import pyplot as plt


img =cv2.imread('boy.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
plt.xlim([0,256])
plt.show()