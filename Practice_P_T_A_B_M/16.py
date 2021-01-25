# Bubble Sort

li = [6, 1, 2, 3, 4, 5]

print(li)

n = len(li)

c = 0

for i in range(n):

    for j in range(n-i-1):

        c += 1

        if li[j] > li[j+1]:

            temp = li[j]

            li[j] = li[j+1]

            li[j+1] = temp

print(li)

print(c)