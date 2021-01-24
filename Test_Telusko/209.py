from array import *

li = array('i', [])

n = int(input("Enter The Array Length : "))

print("Enter The Elements : ")

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

a = int(input("Enter A Element For Search :"))

print(a, "Found At : ", li.index(a+1))
