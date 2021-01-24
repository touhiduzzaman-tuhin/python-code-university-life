x = int(input("Enter A Number : "))

y = int(input("Enter A Number : "))

z = int(input("Enter A Number : "))

if x > y:

    if x > z:

        print("Maximum : ", x)

    else:

        print("Maximum : ", z)

else:

    if y > z:

        print("Maximum : ", y)

    else:

        print("Maximum : ", z)