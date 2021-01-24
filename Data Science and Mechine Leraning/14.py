import numpy as np

li = np.random.randint(0, 100, 9)

print(li)

print("---")

li = li.reshape(3, 3)

print(li)

print("---")

print(li.min())

print(li.argmin())

print(li.max())

print(li.argmax())

print(li.mean())

print(li.shape)

print(li.ndim)

print(li.size)

print(li.diagonal())

print(li.sum())

print(li.var())

print(li.sum())

print(li.dtype)
