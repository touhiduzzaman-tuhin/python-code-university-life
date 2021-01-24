import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

resize = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))

cv2.imshow("Orginal", img)

cv2.imshow("Resized", resize)

cv2.waitKey(0)

cv2.destroyAllWindows()