from array import *

li = []

n = int(input("Enter How many Students : "))

print("Enter Name :")

for i in range(n):

    e = str(input())

    li.append(e)

print(li)

def odd_even(lst):
    u = 0

    l = 0

    for i in li:

        ln = 0

        ln = len(i)

        if ln < 5:

            l += 1


        else:

            u += 1

    return u, l


a, b = odd_even(li)

print("Upper : ", a)
print("Lower : ", b)