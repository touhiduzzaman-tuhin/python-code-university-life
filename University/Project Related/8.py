import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ban.jpg")

cv2.imshow("Main Img", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

font = cv2.FONT_HERSHEY_SIMPLEX

face = cv2.imread("F:\Final Project\Images\\mushi.jpg", 0)

cv2.imshow("Mushi", face)

w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.95

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)

cv2.putText(img, "Mushi", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

face = cv2.imread("F:\Final Project\Images\\mash.jpg", 0)

cv2.imshow("Mash", face)


w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.95

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)


cv2.putText(img, "Mash", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)


face = cv2.imread("F:\Final Project\Images\\sakib.jpg", 0)

cv2.imshow("Sakib", face)


w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.95

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)

cv2.putText(img, "Sakib", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)


face = cv2.imread("F:\Final Project\Images\\tamim.jpg", 0)

cv2.imshow("Tamim", face)


w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.95

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)

cv2.putText(img, "Tamim", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)


face = cv2.imread("F:\Final Project\Images\\taskin.jpg", 0)

cv2.imshow("Taskin", face)


w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

value = 0.95

loc = np.where(res >= value)

for i in zip(*loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)



cv2.putText(img, "Taskin", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)


cv2.imshow("Detect Image", img)


cv2.waitKey()

cv2.destroyAllWindows()