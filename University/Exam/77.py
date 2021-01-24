x = int(input("Enter A Number : "))

for i in range(x):

    print(" " * (x-i-1) + str("* ")*(i+1))