import cv2

import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("F:\Final Project\Images\\ball.jpg", cv2.IMREAD_GRAYSCALE)

title = ["Orginal"]

image = [img]

for i in range(1):

    plt.subplot(1, 1, i+1)

    plt.imshow(image[i], "gray")

    plt.title(title[i])

    plt.xticks([])

    plt.yticks([])


plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()

