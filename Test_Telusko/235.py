from numpy import *

li = array([1, 2,3 ,4, 5])

li1 = li

print(li)

print(li1)

print(id(li))
print(id(li1))

li = li +3

print(li)
print(li1)

print(id(li))
print(id(li1))

print("--")


li1 += 2

print(li)
print(li1)

print(id(li))
print(id(li1))