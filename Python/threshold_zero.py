import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\gradient.jpg")

_, th_b_z = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)

while(1):

    cv2.imshow("Image", img)

    cv2.imshow("Trunc", th_b_z)

    k = cv2.waitKey(1)

    if k == 27:
        break

cv2.destroyAllWindows()
