import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.ellipse(img, (200, 200), (100, 50),0, 0, 1800, 255, -1)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()