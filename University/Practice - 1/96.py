x = int(input("Enter Number of rows : "))


for i in range(x):

    print(" "* (x-i-1),end=" ")

    for j in range(i+1):

        print(chr(64+x-i), end=" ")

    print()