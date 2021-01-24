import cv2

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

cv2.circle(img, (100, 0), 25, (0, 255, 0))

cv2.circle(img, (0, 100), 25, (0, 0, 255))

cv2.circle(img, (100, 100), 50, (255, 0, 0), 5)

cv2.imshow("Afridi", img)

cv2.waitKey(0)

cv2.destroyAllWindows()