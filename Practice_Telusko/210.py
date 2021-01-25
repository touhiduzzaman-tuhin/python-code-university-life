from array import *

li = array('i', [])

n = int(input("Enter The Array Length : "))

print("Enter The Elements : ")

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

a = int(input("Enter A Element For Search :"))

for i in li:

    if i == a:

        print("Found At : ", i)