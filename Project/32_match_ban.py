import cv2

img1 = cv2.imread("F:\Final Project\Images\\ban.jpg", cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1, (500, 500))

img2 = cv2.imread("F:\Final Project\Images\\mash.jpg", cv2.IMREAD_GRAYSCALE)

img2 = cv2.resize(img2, (500, 500))

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)

kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)

match = bf.match(des1, des2)

match = sorted(match, key=lambda x: x.distance)

match_result = cv2.drawMatches(img1, kp1, img2, kp2, match[:50], None, flags=2)

cv2.imshow("Image", match_result)

cv2.waitKey(0)

cv2.destroyAllWindows()