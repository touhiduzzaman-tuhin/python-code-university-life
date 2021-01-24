# Linear Search

from array import *

li = array('i', [])

n = int(input("Enter How many numbers :"))

print("Enter The elements :")

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

a = int(input("Enter Your search element :"))

for i in range(n):

    if li[i] == a:

        print("Found At :", i+1)

        break

else:

    print("Not Found")