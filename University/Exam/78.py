x = int(input("Enter A Number : "))

for i in range(x):

    print(" "* (x-i-1) + (chr(65+i)+ " ")*(i+1))