# Selection Sort

li = []

n = int(input("Enter How Many Number : "))

print("Enter Elements :")

for i in range(n):

    e = int(input())

    li.append(e)


print(li)

print("----")


def selection_sort(li, n):

    for i in range(n):

        min = i

        for j in range(i+1, n):

            if li[min] > li[j]:

                min = j

        temp = li[min]

        li[min] = li[i]

        li[i] = temp

        print(li)

        print("---")



selection_sort(li, n)

print(li)