import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(img, (200, 0), (300, 200), (255, 255, 255), -1)

cv2.imshow("Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()