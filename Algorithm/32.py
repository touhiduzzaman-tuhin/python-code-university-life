# Binary Search

li = []

n = int(input("Enter How Many Number : "))

for i in range(n):

    e = int(input())

    li.append(e)



print(li)

print("--")

li.sort()

print(li)

print("--")

a = int(input("Enter Search Number :"))


def binary_search(li, n, a):

    s = 0

    e = n - 1

    while s <= e:

        mid = (s+e) // 2

        if li[mid] == a:

            print("Found At :", mid+1)

            break

        else:

            if li[mid] < a:

                s = mid + 1

            else:

                e = mid - 1

    else:

        print("Not Found")




binary_search(li, n, a)