from numpy import *

li = array([1, 2, 3, 4, 5])

def odd_even(lst):

    e = 0

    o = 0

    for i in li:

        if i % 2 == 0:

            e += 1

        else:

            o += 1
            
    return e, o

a, b = odd_even(li)

print("Even : ", a)
print("Odd : ", b)