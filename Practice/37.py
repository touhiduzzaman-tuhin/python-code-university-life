import cv2

import numpy as np

event = [i for i in dir(cv2) if "EVENT" in i]

print(event)