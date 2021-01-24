# Insertion Sort

li = [5, 4, 3, 1, 6]

n = len(li)

for i in range(1, n):

    item = li[i]

    j = i - 1

    while(j >= 0 and li[j] > item):

        li[j+1] = li[j]

        j = j - 1

    li[j+1] = item



print(li)