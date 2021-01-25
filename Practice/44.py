import cv2

import numpy as np

img1 = cv2.imread("F:\Final Project\Images\\black_white.jpg")

cv2.resize(img1, (300, 500))

img2 = np.zeros((300, 500, 3), dtype="uint8")

cv2.rectangle(img2, (200, 0), (300, 200), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img2, img1)

cv2.imshow("Black_white", img1)

cv2.imshow("Create_img", img2)

cv2.imshow("Bit_And", bitAnd)

cv2.waitKey(0)

cv2.destroyAllWindows()