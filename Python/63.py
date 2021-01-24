import cv2

img = cv2.imread("F:\Final Project\Images\\gradient.jpg")

_, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Tuhin", img)

cv2.imshow("Binary", binary)

cv2.waitKey(0)

cv2.destroyAllWindows()