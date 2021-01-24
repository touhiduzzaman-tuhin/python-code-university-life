import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg", 0)

cv2.imshow("Afridi", img)

cv2.waitKey(0)

cv2.destroyAllWindows()