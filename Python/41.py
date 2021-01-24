import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\black_white.jpg")

cv2.imshow("Black_White", img)

cv2.waitKey(0)

cv2.destroyAllWindows()