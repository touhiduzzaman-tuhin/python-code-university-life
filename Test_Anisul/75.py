x = int(input("Enter Start Index : "))

y = int(input("Enter End  Index : "))

z = int(input("Enter Difference : "))

n = int(input("Enter Condition state : "))


while x <= y:

    print(x)

    if x > n:
        break


    x = x + z

