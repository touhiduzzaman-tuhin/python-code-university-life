from numpy import *

li = array([1, 2, 3, 4])

print(li)

print(id(li))

print("---")

li1 = li

print(li1)

print(id(li1))

print("---")

li = li + 2

print(li)
print(id(li))

print(li1)
print(id(li1))


print("---")

li1 += 3

print(li)
print(id(li))

print(li1)
print(id(li1))