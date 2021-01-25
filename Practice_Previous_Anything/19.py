from numpy import *

li = logspace(1, 10)

print(li)

print("---")

li = logspace(1, 20, 5)

print(li)

print(li[3])
print(li[4])

print(int(li[3]))

print("%.3f" %li[4])