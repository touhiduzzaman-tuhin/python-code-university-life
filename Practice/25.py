import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()