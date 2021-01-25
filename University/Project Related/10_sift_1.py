import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(img, None)

img = cv2.drawKeypoints(img, kp, None)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()