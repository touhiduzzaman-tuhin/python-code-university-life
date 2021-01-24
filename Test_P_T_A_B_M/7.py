# Linear Search

li = []

n = int(input("Enter How Many Number :"))

print("Enter Elements :")

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

def linear_saerch(lst, a):

    for i in range(n):

        if li[i] == a:

            print("Found At :", i+1)

            break

    else:

        print("Not Found")


a = int(input("Enter Search Element: "))

linear_saerch(li, a)
