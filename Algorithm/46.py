# Insertion Sort

li = []

n = int(input("Enter How many Number : "))

print("Enter the elements : ")

for i in range(n):
    e = int(input())

    li.append(e)

print(li)

print("---")



def insertion_sort(li, n):

    for i in range(1, n):

        item = li[i]

        j = i - 1

        while(j >= 0 and li[j] > item):

            li[j+1] = li[j]

            j = j - 1

        li[j+1] = item

        print(li)

        print("---")



insertion_sort(li, n)

print(li)
