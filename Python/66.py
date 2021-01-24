import cv2

img = cv2.imread("F:\Final Project\Images\\sudoku.jpg", 0)

th_m = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imshow("Tuhin", img)

cv2.imshow("Mean", th_m)

cv2.waitKey(0)

cv2.destroyAllWindows()