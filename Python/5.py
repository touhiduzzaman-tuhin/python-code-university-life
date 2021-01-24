import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

cv2.imshow("Short", face)

cv2.imshow("Ronaldo", img)

cv2.imshow("Face", gray_img)

cv2.waitKey()

cv2.destroyAllWindows()