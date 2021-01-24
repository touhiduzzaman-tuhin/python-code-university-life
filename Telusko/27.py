from array import *

arr = array('i', [])

x = int(input("Enter Your A Array Length : "))

for i in range(x):

    n = int(input("Enter The Next value : "))

    arr.append(n)

print(arr)

print("----")

arr = array('i', [])

x = int(input("Enter Your A Array Length : "))

print("Enter The Value : ")

for i in range(x):

    n = int(input())

    arr.append(n)

print(arr)

print("----")

a = int(input("Enter The Value : "))

print("Index Number : ", arr.index(a))

print("---")

k = 0

for i in arr:

    if i == a:

        print("Index Number : ", k)


    k += 1