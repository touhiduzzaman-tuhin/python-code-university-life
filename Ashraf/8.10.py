n = int(input("Enter Any Number : "))

for i in range(1, n+1, 1):

    for j in range(1, i+1, 1):

        print(chr(64+i), end=" ")

    print("\n")