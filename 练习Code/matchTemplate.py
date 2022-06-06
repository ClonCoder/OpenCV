import cv2
img = cv2.imread('1.jpg')
templ1 = cv2.imread('template3.png')
templ2 = cv2.imread('2.png')

height1, widgh1,c1 = templ1.shape
result1 = cv2.matchTemplate(img,templ1,cv2.TM_SQDIFF_NORMED)
minValue,maxValue,minLoc1,maxLoc = cv2.minMaxLoc(result1)

height2, widgh2,c2 = templ2.shape
result2 = cv2.matchTemplate(img,templ2,cv2.TM_SQDIFF_NORMED)
minValue,maxValue,minLoc2,maxLoc = cv2.minMaxLoc(result2)


resultpoint1 = minLoc1
resultpoint2 = (resultpoint1[0]+widgh1,resultpoint1[1]+height1)

resultpoint3 = minLoc2
resultpoint4 = (resultpoint3[0]+widgh2,resultpoint3[1]+height2)


cv2.rectangle(img,resultpoint1,resultpoint2,(0,0,255),2)
cv2.rectangle(img,resultpoint3,resultpoint4,(0,0,255),2)

cv2.imshow('a',img)
cv2.waitKey()
cv2.destroyAllWindows()