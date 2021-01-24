import cv2

import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("F:\Final Project\Images\\ball1.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((2, 2), np.uint8)

ditale = cv2.dilate(img, kernel, iterations=2)

erison = cv2.erode(img, kernel, iterations=1)

open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

title = ["Orginal", "Dilate", "Erison", "OPen"]

image = [img, ditale, erison, open]

for i in range(4):

    plt.subplot(2, 2, i+1)

    plt.imshow(image[i], "gray")

    plt.title(title[i])

    plt.xticks([])

    plt.yticks([])


plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()

