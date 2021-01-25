import cv2


image = cv2.imread('F:\Final Project\Images\\ronaldo.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


sift  = cv2.xfeatures2d.SIFT_create()


keypoints,descriptors = sift.detectAndCompute(gray,None)


with_keypoints = cv2.drawKeypoints(gray,keypoints, None)


cv2.imshow("Image", with_keypoints)

cv2.waitKey(0)

cv2.destroyAllWindows()