# Bubble Sort

li = []

n = int(input("Enter How many Number : "))

print("Enter the elements : ")

for i in range(n):
    e = int(input())

    li.append(e)

print(li)

print("---")



def bubble_sort(li, n):

    for i in range(n):

        for j in range(n-i-1):

            if li[j] > li[j+1]:

                temp = li[j]

                li[j] = li[j+1]

                li[j+1] = temp

        print(li)

        print("---")



bubble_sort(li, n)

print(li)
