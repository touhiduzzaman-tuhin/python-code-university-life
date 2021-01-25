import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

res = cv2.matchTemplate(gray_img, face, cv2.TM_SQDIFF)

value = 0.95

loc = np.where(res >= value)

print(res)

print(loc)

cv2.waitKey(0)

cv2.destroyAllWindows()