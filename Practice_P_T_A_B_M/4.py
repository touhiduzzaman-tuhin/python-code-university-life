# Linear Search

li = []

n = int(input("Enter How many number :"))

print("Enter", n, "Elements")

for i in range(n):

    e = int(input())

    li.append(e)

print("List : ", li)

a = int(input("Enter An Element that You want to search :"))

for i in range(len(li)):

    if li[i] == a:

        print(a, "Found At Position :", i+1)

        break

else:

    print("Not Found")