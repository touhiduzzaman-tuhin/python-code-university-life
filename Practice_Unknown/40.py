x = int(input("Enter A Number : "))

y = int(input("Enter A Number : "))


if x > y:

    x, y = y, x

if x % 2 == 1:

    x = x + 1

for i in range(x, y+1, 2):

    print(i)