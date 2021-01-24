import cv2

img1 = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread("F:\Final Project\Images\\ronaldo_1.jpg", cv2.IMREAD_GRAYSCALE)

surf = cv2.xfeatures2d.SURF_create()

kp1, des1 = surf.detectAndCompute(img1, None)

kp2, des2 = surf.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)

match = bf.match(des1, des2)

match = sorted(match, key=lambda x: x.distance)

match_result = cv2.drawMatches(img1, kp1, img2, kp2, match[:10], None, flags=2)

cv2.imshow("Image", match_result)

cv2.waitKey(0)

cv2.destroyAllWindows()