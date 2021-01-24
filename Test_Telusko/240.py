from numpy import *

li = array([1, 2, 3])

li1 = li.copy()

print(li)
print(li1)

print(id(li))
print(id(li1))

li += 2

print(li)
print(li1)

print(id(li))
print(id(li1))