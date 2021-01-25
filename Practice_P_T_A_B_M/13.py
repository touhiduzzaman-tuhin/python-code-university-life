# Selection Sort

li = [5, 7, 4, 8, 2, 3]

print(li)

n = len(li)

for i in range(n):

    min = i

    for j in range(i+1, n):

        if li[j] < li[min]:

            min = j

    if min != i:

        li[i] , li[min] = li[min], li[i]


print(li)