import cv2

from matplotlib import pyplot as plt

img = cv2.imread("F:\Final Project\Images\\afridi.jpg")

cv2.imshow("Tuhin", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)

plt.show()


cv2.waitKey(0)

cv2.destroyAllWindows()