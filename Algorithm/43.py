# Binary Search

li = []

n = int(input("Enter How many Number : "))

print("Enter the elements : ")

for i in range(n):
    e = int(input())

    li.append(e)

print(li)

print("---")

li.sort()

print(li)

print("---")

a = int(input("Enter The Search Element : "))


def binary_search(li, n, a):
    
    s = 0

    e = n - 1

    while s <= e:

        mid = (s + e) // 2

        if li[mid] == a:

            return 1, mid

        else:

            if li[mid] < a:

                s = mid + 1

            else:

                e = mid - 1

    return -1


v, k = binary_search(li, n, a)

if v == 1:

    print("Found At : ", k + 1)

else:

    print("Not Found")