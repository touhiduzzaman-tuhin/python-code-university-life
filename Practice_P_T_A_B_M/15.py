# Selection sort

from array import *

li = array('i', [])

n = int(input("Enter How Many Number :"))

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

def selection_sort(lst, n):

    for i in range(n):

        min = i

        for j in range(i+1, n):

            if li[j] < li[min]:

                min = j


        if min != i:

            temp = li[i]

            li[i] = li[min]

            li[min] = temp

        print(li)

selection_sort(li, n)

print(li)