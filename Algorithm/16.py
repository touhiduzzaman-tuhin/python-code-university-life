# Binary Seach Again

list = [6, 7, 8, 2, 3, 5, 9]

print(list)

list.sort()

print(list)

n = len(list)

x = 9

left = 0

right = n - 1

while left <= right:

    mid = (left + right) // 2

    if list[mid] == x:

        print("Found Sorted index at : ", mid)

        break

    if list[mid] < x:

        left = left + 1

    else:

        right -= 1

