import numpy as np

li = np.arange(0, 11)

print(li)

n = li[0:6]

n[:] = 88

print(li)

print(n)