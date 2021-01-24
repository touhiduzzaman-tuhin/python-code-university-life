from numpy import *

li = array([1, 2, 3, 4])

print(li)

print("--")

li1 = li.view()

print(li1)

print("---")

li[2] = 7

print(li)
print(li1)

print("---")

li1[1] = 9

print(li)
print(li1)