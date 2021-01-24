import numpy as np

import cv2

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.line(img, (100, 100), (300, 300), (0, 255, 0), 20)

cv2.imshow("Line", img)

cv2.waitKey(0)

cv2.destroyAllWindows()