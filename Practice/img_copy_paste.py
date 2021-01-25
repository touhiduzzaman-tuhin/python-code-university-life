import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Train Images\Afridi\\9.jpg")

nose = img[464:582, 549:580]

img[51:546, 132:568] = nose

cv2.imshow("Tuhin", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

