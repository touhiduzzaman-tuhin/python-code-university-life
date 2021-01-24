import cv2

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

img = cv2.resize(img, (500, 500))

cv2.imshow("Afridi", img)

cv2.waitKey(0)

cv2.destroyAllWindows()