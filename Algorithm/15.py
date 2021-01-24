# Binary Search

x = [5, 6, 2, 3, 9, 8, 1, 7]

y = 9

x.sort()

print(x)

n = len(x)

left = 0

right = n - 1

while left <= right:

    mid = (left + right) // 2

    if x[mid] == y:

        print("Found Sorted in index: ", mid)

        break

    if x[mid] < y:

        left = left + 1

    else:

        right = right - 1



