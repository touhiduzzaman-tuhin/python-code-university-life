import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\sudoku.jpg", 0)



th_m = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Image", img)

cv2.imshow("Adaptive", th_m)

cv2.waitKey(0)

cv2.destroyAllWindows()