x = int(input("Enter Start Index : "))

y = int(input("Enter End  Index : "))

z = int(input("Enter Difference : "))

sum = 0

while x <= y:

    sum += x

    x += z

print("Result : ", sum)
