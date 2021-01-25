import random

b = int(input("Enter The end Value : "))

x = int(input("Enter Any Number from 0 to end : "))

n = random.random() * (b)

if x == n:

    print("You Have won")

else:

    print("You Have lost")

    print("Random Number is : ", n)