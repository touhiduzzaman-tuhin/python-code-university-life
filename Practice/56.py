import cv2

import numpy as np

def event_click(event, x, y, flags, param):

    if event == cv2.EVENT_RBUTTONDOWN:


        blue = img[x, y, 0]

        green = img[x, y, 1]

        red = img[x, y, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX

        text = str(blue) + "," + str(green) + "," + str(red)

        cv2.putText(img, text, (x, y), font, 1, (255, 0, 0), 2)

        cv2.imshow("Tuhin", img)


img = np.zeros((500, 500, 3), dtype="uint8")

cv2.imshow("Tuhin", img)

cv2.setMouseCallback("Tuhin", event_click)

cv2.waitKey(0)

cv2.destroyAllWindows()