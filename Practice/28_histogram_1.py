import cv2

img1 = cv2.imread("F:\Final Project\Images\\ban.jpg")

img2 = cv2.imread("F:\Final Project\Images\\mash.jpg")

cv2.imshow("Image1", img1)

cv2.imshow("Image", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()