import cv2

img = cv2.imread("F:\Final Project\Images\\gradient.jpg")

_, to_zero_inv = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Tuhin", img)

cv2.imshow("Inverse_Zero", to_zero_inv)

cv2.waitKey(0)

cv2.destroyAllWindows()