# Binary Search

li = [5, 7, 3, 8, 5, 2]

li.sort()

n = 17

def binary_search(lst, n):

    s = 0

    e = len(li) - 1

    while s <= e:

        mid = (s+e) // 2

        if li[mid] == n:

            return True

        else:

            if li[mid] < n:

                s = mid + 1

            else:

                e = mid - 1

    return False

if binary_search(li, n):

    print("Found")

else:

    print("Not Found")

