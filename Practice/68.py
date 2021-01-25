import cv2

img = cv2.imread("F:\Final Project\Images\\sudoku.jpg", 0)

mean_z = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imshow("Image", img)

cv2.imshow("Mean_Trunc", mean_z)

cv2.waitKey(0)

cv2.destroyAllWindows()