import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.95

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)

print(loc)

print(res)

cv2.imshow("Main Image", img)

cv2.waitKey()

cv2.destroyAllWindows()