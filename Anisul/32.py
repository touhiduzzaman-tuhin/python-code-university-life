import random

number = int(input("Enter A Number 1 to 20 : "))

randomNumber = int(random.random() * 20)

if number == randomNumber:

    print("You Have won")

else:

    print("You have Lost")

    print("Random Number is : ", randomNumber)