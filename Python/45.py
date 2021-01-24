import cv2

import numpy as np

img1 = cv2.imread("F:\Final Project\Images\\black_white.jpg")

cv2.resize(img1, (300, 500))

img2 = cv2.bitwise_not(img1)

cv2.imshow("Orginal", img1)

cv2.imshow("Bit_Not", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()