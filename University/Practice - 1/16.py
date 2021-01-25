x = int(input("Enter A Year : "))

if(x % 100 != 0 and x % 4 == 0):
    print("Leap Year")

elif(x % 100 == 0 and x % 400 == 0):
    print("Leap Year")

else:
    print("Not Leap Year")