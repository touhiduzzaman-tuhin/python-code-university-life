x = int(input("Enter A Year : "))

if x % 4 == 0 and x % 100 != 0:

    print("Not Leap Year")

elif x % 100 != 0 and x % 400 != 0:

    print("Not Leap Year")

else:

    print("Leap Year")