import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.9

loc = np.where(res >= value)

print(loc)

print(res)

cv2.waitKey()

cv2.destroyAllWindows()