import cv2

import numpy as np

def track(x):

    print(x)

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.namedWindow("Tuhin")

cv2.createTrackbar("B", "Tuhin", 0, 255, track)

cv2.createTrackbar("G", "Tuhin", 0, 255, track)

cv2.createTrackbar("R", "Tuhin", 0, 255, track)

cv2.imshow("Tuhin", img)

cv2.waitKey(0)

cv2.destroyAllWindows()