import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

res = cv2.matchTemplate(gray_img, face, cv2.TM_SQDIFF_NORMED)

w, h = face.shape[::-1]

value = 0.77

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (255, 0, 255), 2)


print(res)

print(loc)

cv2.imshow("main Img", img)

cv2.waitKey(0)

cv2.destroyAllWindows()