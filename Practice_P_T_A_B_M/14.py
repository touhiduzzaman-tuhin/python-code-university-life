# Selection sort

li = []

n = int(input("Enter How many number : "))

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

for i in range(n):

    min = i

    for j in range(i+1, n):
        
        if li[j] < li[min]:

            min = j

    if min != i:

        li[min], li[i] = li[i], li[min]

print(li)