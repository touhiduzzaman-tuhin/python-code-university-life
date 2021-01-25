from array import *

li = array('i', [])

n = int(input("Enter The Array Length : "))

print("Enter Array Elements :")

for i in range(n):

    e = int(input())

    li.append(e)


print(li)