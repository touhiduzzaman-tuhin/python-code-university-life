import cv2

import numpy as np

img1 = cv2.imread("F:\Final Project\Images\\black_white.jpg")

img2 = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

img = cv2.resize(img1, (300, 500))

img1 = cv2.resize(img2, (300, 500))

new = cv2.addWeighted(img, .6, img1, .4, 0)

cv2.imshow("Image", new)

cv2.waitKey(0)

cv2.destroyAllWindows()