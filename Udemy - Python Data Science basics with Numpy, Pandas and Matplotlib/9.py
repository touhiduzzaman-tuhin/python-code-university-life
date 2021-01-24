import numpy as np

li = np.random.random((2, 3))

print(li)

li1 = np.random.random((2, 3))

print(li1)

li2 = li +  li1

print(li2)

print("---")

li2 = li -  li1

print(li2)

print("---")

li2 = li *  li1

print(li2)

print("---")

li2 = li /  li1

print(li2)

print("---")

li = np.arange(10)

print(li)

print(li[0])
print(li[0:])
print(li[2:5])
print(li[2:])
print(li[:4])

print(li[-1])

print(li[::-1])

print(li)

li1 = li.copy()


print(li1)

li1 = li1 ** 2

print(li1)

li[:3] = 1

print(li)

li[7:] = 2

print(li)

print(li.__len__())

print(len(li))

print(type(li))

li[4] = 9

print(li)
