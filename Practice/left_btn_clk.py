import cv2

import numpy as np

def click_event(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' , ',  y)

        font = cv2.FONT_HERSHEY_SIMPLEX

        strXY = str(x) + ' , ' + str(y)

        cv2.putText(img, strXY, (x, y), font, 1,  (0, 255, 0), 2)

        cv2.imshow("Tuhin", img)

img = cv2.imread('F:\Final Project\Images\\ronaldo.jpg')

#img = np.zeros((500, 500, 3), dtype="uint8")


cv2.imshow("Tuhin", img)

cv2.setMouseCallback("Tuhin", click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()