import cv2

import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

text = cv2.FONT_HERSHEY_SIMPLEX

x = str(input("Enter Your Name : "))

cv2.putText(img, x, (50, 200), text, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("Text", img)

cv2.waitKey(0)

cv2.destroyAllWindows()