x = int(input("Enter A Number : "))

for i in range(x):

    print(" "* (x-i-1) + (chr(64+x-i)+ " ")*(i+1))