# Bubble Sort

list = [5, 2, 6, 3, 4]

n = len(list)

c = 0

for i in range(n):

    for j in range(n-1):

        c += 1

        if list[j] > list[j+1]:

            list[j], list[j+1] = list[j+1], list[j]


print(list)

print(c)