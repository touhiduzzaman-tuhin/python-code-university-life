import cv2

img1 = cv2.imread("F:\Final Project\Images\\ban.jpg")

hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

img2 = cv2.imread("F:\Final Project\Images\\mash.jpg")

hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

cv2.imshow("Image1", hsv1)

cv2.imshow("Image", hsv2)

cv2.waitKey(0)

cv2.destroyAllWindows()