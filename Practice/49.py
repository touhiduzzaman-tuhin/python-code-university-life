import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.rectangle(img, (250, 0), (500, 500), (255, 255, 255), -1)

cv2.imshow("Black", img)

cv2.waitKey(0)

cv2.destroyAllWindows()