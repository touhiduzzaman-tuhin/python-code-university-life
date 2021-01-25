x = int(input("Enter A Number : "))

y = int(input("Enter A Number : "))

z = int(input("Enter A Number : "))



if x > y:

    if y > z:

        print("Min : ", z)

    else:

        print("Min : ", y)

else:

    if x > z:

        print("Min : ", z)

    else:

        print("Min : ", x)