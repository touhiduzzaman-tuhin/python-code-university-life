# Linear Search

li = []

n = int(input("Enter How many Number : "))

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

a = int(input("Enter Search number :"))

def linear_serach(li, n, a):

    for i in range(n):

        if li[i] == a:

            print("Found at :", i+1)
            break

    else:

        print("Not Found")

linear_serach(li, n, a)