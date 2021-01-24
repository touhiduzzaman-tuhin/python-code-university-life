# Binary Search

li = []

n = int(input("Enter How many Number : "))

for i in range(n):
    e = int(input())

    li.append(e)

print(li)

li.sort()

print(li)

a = int(input("Enter Search number :"))

def binary_serach(li, n, a):

    s = 0

    en = n-1

    while s <= en:

        mid = (s+en) // 2

        if li[mid] == a:

            return 1, mid

        else:

            if li[mid] < a:

                s = mid + 1

            else:

                en = mid - 1

    return -1


v, p = binary_serach(li, n, a)

if v == 1:

    print("Found At :", p+1)

else:

    print("Not Found")