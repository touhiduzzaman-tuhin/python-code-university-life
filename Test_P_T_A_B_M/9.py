# Binary Search

li = [1, 5, 7, 3, 2, 9]

li.sort()

n = 5

s = 0

e = len(li) - 1


while s <= e:

    mid = (s+e) // 2

    if li[mid] == n:

        print("Found")
        break

    if li[mid] < n:

        s = mid + 1

    else:

        e = mid - 1