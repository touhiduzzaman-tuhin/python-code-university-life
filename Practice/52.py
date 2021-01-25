import cv2

img = cv2.imread("F:\Final Project\\Images\Afridi.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("F:\Final Project\\Images\Afridi.jpg", gray)

#save image as gray image