import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

def click_event(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        points.append((x, y))

        if len(points) >= 2:
            cv2.line(img, (points[-1]), (points[-2]), (0, 255, 0), 5)

            cv2.imshow("Tuhin", img)

cv2.imshow("Tuhin", img)

points = []

cv2.setMouseCallback("Tuhin", click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()