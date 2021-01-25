# Bubble Sort

from array import *

li = array('i', [])


n = int(input("Enter How Many Number :"))

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

def bubble_sort(li, n):

    for i in range(n):

        for j in range(n - i - 1):

            if li[j] > li[j + 1]:

                li[j], li[j + 1] = li[j + 1], li[j]

    print(li)


bubble_sort(li, n)

print(li)