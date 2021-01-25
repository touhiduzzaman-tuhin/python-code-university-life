import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.arrowedLine(img, (200, 200), (400, 400), (0, 255, 0), 10)

cv2.imshow("tuhin", img)

cv2.waitKey(0)

cv2.destroyAllWindows()