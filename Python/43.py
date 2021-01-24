import cv2

import numpy as np

img1 = cv2.imread("F:\Final Project\Images\\black_white.jpg")

cv2.resize(img1, (300, 300))

cv2.imshow("Image", img1)

cv2.waitKey(0)

cv2.destroyAllWindows()