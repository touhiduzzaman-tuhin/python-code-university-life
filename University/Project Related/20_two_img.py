import cv2

img1 = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread("F:\Final Project\Images\\ronaldo_1.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image1", img1)

cv2.imshow("Image2", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()