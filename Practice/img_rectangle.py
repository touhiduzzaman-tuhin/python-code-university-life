import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(img, (50, 50), (300, 300), (0, 20, 200), 10)

cv2.imshow("Rectangle", img)

cv2.waitKey(0)

cv2.destroyAllWindows()