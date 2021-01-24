import numpy as np

li = np.arange(100)

print(li)

li = li.reshape(10, 10)

print(li)

li = li.reshape(5, 4, 5)

print(li)

print(li[2])

print(li[2][3])

print(li[3][1][2])


li = np.arange(100)

li = li.reshape(10, 10)

print(li)

print("---")

li1 = np.arange(100, 200)

li1 = li1.reshape(10, 10)

print(li1)

print("---")

print(np.add(li, li1))

print("----")

print(np.subtract(li, li1))

print("---")

print(np.multiply(li, li1))

print("---")

print(np.divide(li, li1))

print("---")

print(np.maximum(li, li1))

print("---")

print(np.minimum(li, li1))

print("---")

li = np.arange(10)

print(li)

li = li.reshape(5, 2)

print(li)

print(np.transpose(li))

print(li.transpose())

li = np.arange(10).reshape(5, 2)

print(li)

print(li.sum())

print(li.max())
print(li.min())
print(li.mean())
print(li.std())
print(li.var())

li1 = np.where(li < 5, 4, li)

print(li1)