import cv2

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()