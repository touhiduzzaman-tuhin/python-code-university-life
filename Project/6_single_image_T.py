import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

cv2.imshow("Main Image", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.imread("F:\Final Project\Images\\ronaldo_face.jpg", 0)

cv2.imshow("Face", face)

w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_img, face, cv2.TM_CCOEFF_NORMED)

font = cv2.FONT_HERSHEY_SIMPLEX

value = 0.95

loc = np.where(res >= value)

for i in zip(* loc[::-1]):

    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)


cv2.putText(img, "Ronaldo", (i[0] + w, i[1] + h), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

print(loc)

print(res)

cv2.imshow("Result Image", img)

cv2.waitKey()

cv2.destroyAllWindows()