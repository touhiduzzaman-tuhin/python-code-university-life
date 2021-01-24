import cv2

import numpy as np

def track(x):
    pass

cv2.namedWindow("Track")

cv2.createTrackbar("LH", "Track", 0, 255, track)

cv2.createTrackbar("LS", "Track", 0, 255, track)

cv2.createTrackbar("LV", "Track", 0, 255, track)

cv2.createTrackbar("UH", "Track", 255, 255, track)

cv2.createTrackbar("US", "Track", 255, 255, track)

cv2.createTrackbar("UV", "Track", 255, 255, type)



while(1):

    img = cv2.imread("F:\Final Project\Images\\ball.jpg")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Track")

    l_s = cv2.getTrackbarPos("LS", "Track")

    l_v = cv2.getTrackbarPos("LV", "Track")

    u_h = cv2.getTrackbarPos("UH", "Track")

    u_s = cv2.getTrackbarPos("US", "Track")

    u_v = cv2.getTrackbarPos("UV", "Track")

    l_b = np.array([l_h, l_s, l_v])

    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("image", img)

    cv2.imshow("Mask", mask)

    cv2.imshow("Result", result)

    k = cv2.waitKey(1)

    if k == 27:
        break

cv2.destroyAllWindows()