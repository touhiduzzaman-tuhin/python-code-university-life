import cv2

import numpy as np

img = cv2.imread('F:\Final Project\Images\\ronaldo.jpg')

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp, None)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()