# Selection Sort

li = []

n = int(input("Enter How Many Number : "))

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

print("----")

def selection_sort(li, n):

    for i in range(n):

        min = i

        for j in range(i, n):

            if li[j] < li[min]:

                min = j

        if min != i:

            temp = li[i]

            li[i] = li[min]

            li[min] = temp

        print(li)

selection_sort(li,n)

print("----")

print(li)