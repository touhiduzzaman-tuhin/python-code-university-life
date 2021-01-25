import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

cv2.circle(img, (100, 0), 25, (0, 255, 0))

cv2.circle(img, (0, 100), 25, (0, 0, 255))

cv2.circle(img, (100, 100), 50, (255, 0, 0), 5)

cv2.imshow("Ronaldo", img)

cv2.waitKey(0)

cv2.destroyAllWindows()