import cv2

import numpy as np



def track(x):

    print(x)


img = np.zeros((500, 500, 3), dtype="uint8")

cv2.namedWindow("Tuhin")

cv2.createTrackbar("B", "Tuhin", 0, 255, track)

cv2.createTrackbar("G", "Tuhin", 0, 255, track)

cv2.createTrackbar("R", "Tuhin", 0, 255, track)

while(1):

    cv2.imshow("Tuhin", img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    b = cv2.getTrackbarPos("B", "Tuhin")

    g = cv2.getTrackbarPos("G", "Tuhin")

    r = cv2.getTrackbarPos("R", "Tuhin")

    img[:] = [b, g, r]

cv2.destroyAllWindows()