from random import randint

x = int(input("Enter A Number from 0 to 5 : "))

n = randint(1, 5)

if x == n:

    print("You Have Won")

else:

    print("You Have Lost")

    print("Random Number is : ", n)