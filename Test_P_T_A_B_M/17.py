# Bubble Sort

li = [10, 5, 2, 8, 7]

print(li)

n = len(li)

c = 0

for i in range(n):

    for j in range(n-1):

        c += 1

        if li[j] > li[j+1]:

            temp = li[j]

            li[j] = li[j+1]

            li[j+1] = temp

print(li)

print(c)