from numpy import *

li = array([1, 2, 3, 4])

print(li)

print("---")

li1 = li

print(li1)

li1[1] = 3

print(li)

print(li1)

print("--")

li[2] = 4

print(li)

print(li1)