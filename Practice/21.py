import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

resize = cv2.resize(img, (500, 500))

cv2.imshow("Orgian", img)

cv2.imshow("Ronaldo", resize)

cv2.waitKey(0)

cv2.destroyAllWindows()