import cv2

import numpy as np

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

def click_event(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:

        blue = img[x, y, 0]

        green = img[x, y, 1]

        red = img[x, y, 2]

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        new_img = np.zeros((500, 500, 3), dtype="uint8")

        new_img[:] = [blue, green, red]

        cv2.imshow("New", new_img)

cv2.imshow("Tuhin", img)


cv2.setMouseCallback("Tuhin", click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()