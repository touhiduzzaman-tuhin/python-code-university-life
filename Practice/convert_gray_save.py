import cv2

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("F:\Final Project\Train Images\Afridi\\1_gray.jpg", image_gray)

