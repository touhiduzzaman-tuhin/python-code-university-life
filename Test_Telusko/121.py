x = int(input("Enter A Number : "))

if x == 0:

    print("Zero Number")

elif x >= 0:

    print("Positive Number")

    if x % 2 == 0:

        print("Even Number")

    else:

        print("Odd Number")

else:

    print("Negative Number")