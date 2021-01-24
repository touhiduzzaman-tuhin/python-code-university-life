import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ball.jpg")

cv2.namedWindow("Tuhin")

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()