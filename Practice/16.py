import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", 1)

print(img.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()