import cv2

import numpy as np

img1 = np.zeros((500, 500, 3), dtype="uint8")

img2 = cv2.bitwise_not(img1)

cv2.imshow("Orginal", img1)

cv2.imshow("Bit_Not", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()