li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 33, 44]

n = 34

def Search(li, n):

    l = 0

    u = len(li) - 1

    while l <= u:

        mid = (l + u) // 2

        if li[mid] == n:

            return True

        else:

            if li[mid] < n:

                l = mid + 1

            else:

                u = mid - 1

    return False

if Search(li, n):

    print("Found")

else:

    print("Not Found")