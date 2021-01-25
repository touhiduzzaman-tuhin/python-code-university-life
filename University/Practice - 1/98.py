x = int(input("Enter Number of rows : "))


for i in range(x):

    for j in range(i+1):

        print(chr(65+j), end=" ")

    print()

for i in range(x-1):

    for j in range(x-i-1):

        print(chr(65+j), end=" ")

    print()