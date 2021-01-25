from numpy import *

li = array([1, 2, 3, 4])

li1 = li.view()

print(li)
print(li1)

print(id(li))
print(id(li1))