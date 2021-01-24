import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.line(img, (100, 100), (300, 300), (255, 0, 0), 10)

cv2.imshow("Line", img)

cv2.waitKey(0)

cv2.destroyAllWindows()