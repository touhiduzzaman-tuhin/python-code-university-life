import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

img_2 = cv2.imread("F:\Final Project\Train Images\Afridi\\7.jpg")

img = cv2.resize(img, (500, 500))

img_2 = cv2.resize(img_2, (500, 500))

new = cv2.add(img, img_2)

cv2.imshow("Tuhin", new)

cv2.waitKey(0)

cv2.destroyAllWindows()
