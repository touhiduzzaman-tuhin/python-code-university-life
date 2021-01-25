from numpy import *

li = matrix('1, 2, 3; 4, 5, 6')

li1 = matrix('1, 2, 3; 8, 9, 3')

print(li)
print(li1)

res = li - li1

print(res)