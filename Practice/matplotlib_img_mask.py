import cv2

import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("F:\Final Project\Images\\ball.jpg", cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

title = ["Orginal", "Mask"]

image = [img, mask]

for i in range(2):

    plt.subplot(1, 2, i+1)

    plt.imshow(image[i], "gray")

    plt.title(title[i])

    plt.xticks([])

    plt.yticks([])


plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()

