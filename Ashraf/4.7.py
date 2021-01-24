x = int(input("Enter A Number : "))

y = int(input("Enter A Number : "))

z = int(input("Enter A Number : "))

if x > y:

    if y > z:

        print("Minimum : ", z)

    else:

        print("Minimum : ", y)

else:

    if x > z:

        print("Minimum : ", z)

    else:

        print("Minimum : ", x)