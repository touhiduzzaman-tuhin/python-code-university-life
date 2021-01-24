import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cir = cv2.circle(img, (200, 250), 100, (0, 255, 0), 2)

cv2.imshow("Circel", cir)

cv2.waitKey(0)

cv2.destroyAllWindows()