import cv2

import numpy as np

a = np.random.random((512,512,3)).astype(np.float32)
b = np.ones((512,512,1), dtype=np.int32)
c = a / b
x = c.astype(np.float32)

print(x)