import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Afridi", img)

cv2.imshow("Gray", gray_img)

cv2.waitKey()

cv2.destroyAllWindows()