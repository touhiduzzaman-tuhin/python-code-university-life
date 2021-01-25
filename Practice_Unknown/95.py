x = int(input("Enter First Index : "))

y = int(input("Enter Last Index : "))

z = int(input("Enter Difference : "))

if x > y:

    x, y = y, x

a = int(input("Condition Check Index : "))

for i in range(x, y+1, z):

    print(i)

    if i > a:
        continue