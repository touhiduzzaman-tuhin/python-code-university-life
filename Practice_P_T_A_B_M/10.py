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

s = 0

e = len(li) - 1

while s <= e:

    mid = (s+e) // 2

    if li[mid] == a:

        print("Found At: ", mid+1)

        break

    if li[mid] < a:

        s = mid + 1

    else:

        e = mid - 1

else:

    print("Not Found")