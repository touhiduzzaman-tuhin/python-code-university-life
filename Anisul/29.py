from random import randint

number = int(input("Enetr A Number 1 to 5 : "))

randomNumber = randint(1, 5)

if number == randomNumber:

    print("You Have Won")

else:

    print("You Have Lost")

    print("Random Number is : ", randomNumber)