li = [10, 20, 30, 40, 50]

print(li)

i = 0

while i < 5:

    print(li[i])

    i = i + 1


print("\n")

i = 0

n = len(li)

while i < n:

    print(li[i])

    i += 1


print("\n")

for i in li:
    print(i)


print("\n")

sum = 0

for i in li:

    sum += i

print(sum)