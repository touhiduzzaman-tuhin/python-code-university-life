from numpy import *

li = array([1, 2, 3, 4])

print(li)

print("---")

li1 = li.copy()

print(li1)

print("---")

li[2] = 9

print(li)

print(li1)

print("---")

li1[3] = 8

print(li)
print(li1)