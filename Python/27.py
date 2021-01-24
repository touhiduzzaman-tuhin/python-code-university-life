import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

circle = cv2.circle(img, (250, 300), 100, (255, 0, 0), 2)

cv2.imshow("Circle", circle)

cv2.waitKey(0)

cv2.destroyAllWindows()