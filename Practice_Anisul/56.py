x = int(input("Enter Your Marks : "))

if x > 100 and x < 0:

    print("Invalid Marks")

elif x >= 80 and x <= 100:

    print("A+")

elif x >= 70 and x <= 79:

    print("A")

elif x >= 60 and x <= 69:

    print("A-")

elif x >= 50 and x <= 59:

    print("B")

elif x >= 40 and x <= 49:

    print("C")

elif x >= 33 and x <= 39:

    print("D")

else:

    print("Fail")