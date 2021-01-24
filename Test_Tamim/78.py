x = [1, 2, 3, 4, 5]

y = range(6, 21)

x.extend(y)

print(x)

odd = []

for i in x:

    if i % 2 == 1:

        odd.append(i)

print(odd)