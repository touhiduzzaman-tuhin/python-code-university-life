import cv2

img = cv2.imread("F:\Final Project\Images\\gradient.jpg")

_, trunc = cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)

cv2.imshow("Tuhin", img)

cv2.imshow("Trunc_Image", trunc)

cv2.waitKey(0)

cv2.destroyAllWindows()