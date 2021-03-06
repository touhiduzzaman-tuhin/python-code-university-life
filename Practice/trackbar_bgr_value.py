import cv2

import numpy as np

def track(x):

    print(x)

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.namedWindow("image")

cv2.createTrackbar("B", "image", 0, 255, track)

cv2.createTrackbar("G", "image", 0, 255, track)

cv2.createTrackbar("R", "image", 0, 255, track)

while(1):

    cv2.imshow("image", img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()