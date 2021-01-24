import cv2

import numpy as np

def event_click(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        font = cv2.FONT_HERSHEY_SIMPLEX

        text = str(x) + "," + str(y)

        cv2.putText(img, text, (x, y), font, 1, (255, 0, 0), 2)

        cv2.imshow("Tuhin", img)


    if event == cv2.EVENT_RBUTTONDOWN:

        blue = img[y, x, 0]

        green = img[y, x, 1]

        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX

        text = str(blue) + "," + str(green) + "," + str(red)

        cv2.putText(img, text, (x, y), font, 1, (255, 0, 0), 2)

        cv2.imshow("Tuhin", img)

img = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")

cv2.imshow("Tuhin", img)

cv2.setMouseCallback("Tuhin", event_click)

cv2.waitKey(0)

cv2.destroyAllWindows()