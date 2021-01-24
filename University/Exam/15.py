x = int(input("Enter A number :"))

if(x > 100 and x < 0):

    print("Marks Invalid")

elif(x > 80):

    print("A+")

elif(x > 75):

    print("A")

elif(x > 70):

    print("A-")

elif(x > 65):

    print("B+")

elif(x > 60):

    print("B")

elif(x > 55):

    print("B-")

elif(x > 50):

    print("C")

elif(x > 45):

    print("C-")

elif(x > 40):

    print("D")

else:

    print("Fail")