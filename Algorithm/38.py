# Linear Search

li = []

n = int(input("Enter How Many Number : "))

print("Enter Elements :")

for i in range(n):

    e = int(input())

    li.append(e)


print(li)

print("----")

a = int(input("Enter Search Element : "))

print("---")

def linear_search(li, n, a):

    for i in range(n):

        if li[i] == a:

            print("Found At :", i+1)

            break

    else:

        print("Not Found")

linear_search(li, n, a)