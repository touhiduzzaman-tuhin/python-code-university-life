# Selection Sort

list = [5, 2, 6, 3, 4]

n = len(list)

for i in range(n):

    min = i

    for j in range(i+1, n):

        if list[min] > list[j]:

            min = j


    if min != i:

        list[min], list[i] = list[i], list[min]

print(list)