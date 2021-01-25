from random import randint

a = int(input("Enter The start Value : "))

b = int(input("Enter The end Value : "))

x = int(input("Enter Any Number from start to end : "))

n = randint(a, b)

if x == n:

    print("You Have won")

else:

    print("You Have lost")

    print("Random Number is : ", n)