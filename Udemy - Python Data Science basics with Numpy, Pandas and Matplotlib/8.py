import numpy as np

li = np.array([1, 2, 3, 4])

print(li)

print(type(li))

li = np.arange(10)

print(li)

print(type(li))

print(li.reshape(5, 2))

print(li.shape)

print(li.ndim)

print(li.dtype)

print(li.sum())

print(li.max())

print(li.min())

print(li.mean())

print(li.var())

print(li.std())

print(li)

li1 = [1, 2, 3, 4]

print(li1)

print(type(li1))

li1 = np.array(li)

print(li1)

print(type(li1))

li = np.zeros(100)

print(li)

li = li.reshape(10, 10)

print(li)

li = np.ones(100)

print(li)

li = li.reshape(10, 10)

print(li)

li = np.eye(6)

print(li)

li = li.reshape(6, 2, 3)

print(li)

li = np.empty((2, 3))

print(li)

print("---")

li = np.full((2, 3), 1)

print(li)