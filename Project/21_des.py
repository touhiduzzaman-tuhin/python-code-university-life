import cv2

img1 = cv2.imread("F:\Final Project\Images\\ronaldo_1.jpg", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()

kp, des = orb.detectAndCompute(img1, None)

for i in des:

    print(i)

cv2.waitKey(0)

cv2.destroyAllWindows()