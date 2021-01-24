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

            return i, 1

    return 0


a = int(input("Enter Search Element: "))

p, v = linear_saerch(li, a)

if v == 1:

    print("Found At :", p+1)

else:

    print("Not Found")