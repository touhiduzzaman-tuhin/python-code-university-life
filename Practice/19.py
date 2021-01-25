import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg", 0)

print(img.size)

cv2.waitKey()

cv2.destroyAllWindows()