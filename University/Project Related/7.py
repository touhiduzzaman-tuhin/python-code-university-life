import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ban.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\mash.jpg", 0)

face1 = cv2.imread("F:\Final Project\Images\\mushi.jpg", 0)

face2 = cv2.imread("F:\Final Project\Images\\sakib.jpg", 0)

face3 = cv2.imread("F:\Final Project\Images\\tamim.jpg", 0)

face4 = cv2.imread("F:\Final Project\Images\\mushi.jpg", 0)

w, h = face.shape[::-1]

a, b = face1.shape[::-1]

c, d = face2.shape[::-1]

m, n = face3.shape[::-1]

x, y = face4.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

res1 = cv2.matchTemplate(gray_img, face1, cv2.TM_SQDIFF_NORMED)

res2 = cv2.matchTemplate(gray_img, face2, cv2.TM_CCOEFF_NORMED)

res3 = cv2.matchTemplate(gray_img, face3, cv2.TM_CCOEFF_NORMED)

res4 = cv2.matchTemplate(gray_img, face4, cv2.TM_CCOEFF_NORMED)

print("\n")

value = 0.95

value1 = 0.95

value2 = 0.95

value3 = 0.95

value4 = 0.95


loc = np.where(res >= value)

loc1 = np.where(res >= value1)

loc2 = np.where(res >= value2)

loc3 = np.where(res >= value3)

loc4 = np.where(res >= value4)


font = cv2.FONT_HERSHEY_SIMPLEX

print(loc)


for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)

    cv2.putText(img, "Mash", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)


for i in zip(*loc1[::-1]):

    cv2.rectangle(img, i, (i[0] + a, i[1] + b), (0, 0, 255), 2)

    cv2.putText(img, "Mushi", (i[0] + a, i[1] + b), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

for i in zip(*loc2[::-1]):

    cv2.rectangle(img, i, (i[0] + c, i[1] + d), (0, 0, 255), 2)


for i in zip(*loc3[::-1]):

    cv2.rectangle(img, i, (i[0] + m, i[1] + n), (0, 0, 255), 2)

for i in zip(*loc4[::-1]):

    cv2.rectangle(img, i, (i[0] + x, i[1] + y), (0, 0, 255), 2)



cv2.imshow("Main Image", img)

cv2.waitKey()

cv2.destroyAllWindows()