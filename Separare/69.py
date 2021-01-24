li = [1, 2, 3, 4, 5]

li2 = range(6, 21)

li.extend(li2)

print(li)

print("\n")

even = []

for i in li:

    if i % 2 == 0:

        even.append(i)


print(even)