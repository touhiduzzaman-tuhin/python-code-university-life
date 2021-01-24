import cv2

import numpy as np

img2 = cv2.imread("F:\Final Project\Train Images\Afridi\\black_white.jpg")

img1 = np.zeros((300, 500, 3), dtype="uint8")

cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

cv2.imshow("Black_White", img1)

cv2.imshow("Create_img", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()
