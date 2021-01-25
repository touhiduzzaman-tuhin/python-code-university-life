from numpy import *

li = array([1, 2, 3])

li1 = li.view()

print(li)
print(li1)

print(id(li))
print(id(li1))

print("---")

li += 1

print(li)
print(li1)

print(id(li))
print(id(li1))