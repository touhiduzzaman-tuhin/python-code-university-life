import cv2

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Afridi", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()