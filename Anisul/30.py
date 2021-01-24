import random

number = int(input("Enter A Number 1 to 5 : "))

randomNumber = random.randint(1, 5)

if number == randomNumber:
    print("You Have won")

else:

    print("You have Lost")

    print("Random Number is : ", randomNumber)