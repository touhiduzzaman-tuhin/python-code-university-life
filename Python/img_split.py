import cv2

import numpy as np


img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

b, g, r = cv2.split(img)

img = cv2.merge((b, g, r))

cv2.imshow("Tuhin", img)

cv2.waitKey(0)

cv2.destroyAllWindows()