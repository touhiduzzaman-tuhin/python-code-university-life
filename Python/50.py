import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img1)

cv2.waitKey(0)

cv2.destroyAllWindows()