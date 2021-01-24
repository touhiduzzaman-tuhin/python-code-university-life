import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.namedWindow("image")

while(1):

    cv2.imshow("image", img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()