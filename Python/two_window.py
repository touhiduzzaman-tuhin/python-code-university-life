import cv2

import numpy as np

def track(x):
    pass

cv2.namedWindow("Track")

while(1):

    img = cv2.imread("F:\Final Project\Images\\ball.jpg")

    cv2.imshow("image", img)

    k = cv2.waitKey(1)

    if k == 27:
        break

cv2.destroyAllWindows()