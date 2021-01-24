import cv2

img = cv2.imread("F:\Final Project\Images\\gradient.jpg")

_, to_zero = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)

cv2.imshow("Tuhin", img)

cv2.imshow("TO_Zero", to_zero)

cv2.waitKey(0)

cv2.destroyAllWindows()