# Binary search

li = []

n = int(input("Enter How many numbers : "))

for i in range(n):

    e = int(input())

    li.append(e)

print(li)


li.sort()

print(li)

a = int(input("Enter Search Number :"))



def binary_search(lst):

    s = 0

    e = len(li) - 1

    while s <= e:

        mid = (s + e) // 2

        if li[mid] == a:

            return 1, mid

        if li[mid] < a:

            s = mid + 1

        else:

            e = mid - 1

    return -1

v, p = binary_search(li)

if v == 1:

    print("Found At :", p+1)

else:

    print("Not Found")