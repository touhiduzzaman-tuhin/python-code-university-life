from numpy import *

li = array([1, 2, 4, 5])

print(li)

print("--")

li1 = array([3, 5, 7, 1])

print(li1)

print("---")

print(li, li1)

print("---")

li2 = li, li1

print(li2)

print("---")

print(concatenate([li, li1]))