import cv2

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create(nfeatures=200)

kp, descriptors = sift.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, kp, None)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()