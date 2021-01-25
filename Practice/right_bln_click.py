import cv2

import numpy as np

#img = np.zeros((500, 500, 3), dtype="uint8")

img = cv2.imread('F:\Final Project\Images\\ronaldo.jpg')


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:

        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX

        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)

        cv2.putText(img, strBGR, (x, y), font, 1, (0, 255, 0), 2)

        cv2.imshow("Tuhin", img)

cv2.imshow("Tuhin", img)

cv2.setMouseCallback("Tuhin", click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()