# Linear Search

from numpy import *

li = array([1, 2, 3, 5, 2, 8, 9, 4, 6])

n = 9

for i in range(len(li)):

    if li[i] == n:

        print("Found At :", i+1)

        break

else:

    print("Not Found")