# Linear Search

li = []

n = int(input("Enter How Many Number : "))

for i in range(n):

    e = int(input())

    li.append(e)


print(li)

a = int(input("Enter Search Number :"))


def linear_search(li, n, a):

    for i in range(n):

        if li[i] == a:

            return 1

    return -1


if linear_search(li, n, a):

    print("Found")

else:

    print("Not Found")