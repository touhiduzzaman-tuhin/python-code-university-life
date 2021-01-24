x = int(input("Enter Number of rows : "))


for i in range(x-1):

    print(" "*i, end=" ")

    for j in range(x-i):

        print(chr(65+j), end=" ")

    print()