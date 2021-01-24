import numpy as np

li = np.arange(0, 10)

print(li)

print("---")

li1 = li.copy()

print(li1)

print("---")

li[:4] = 10

print(li)

print(li1)