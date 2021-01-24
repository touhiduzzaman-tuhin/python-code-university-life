li = []

n = int(input("How many Number : "))

print("Enter Elements :")

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

def odd_even(lst):

    e = 0

    o = 0

    for i in lst:

        if i % 2 == 0:

            e += 1

        else:

            o += 1

    return e, o

a, b = odd_even(li)

print("Even :", a)
print("Odd :", b)