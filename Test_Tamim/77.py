x = [1, 2, 3, 4, 5]

y = range(6, 21)

x.extend(y)

print(x)

even = []

for i in x:

    if i % 2 == 0:

        even.append(i)


print(even)