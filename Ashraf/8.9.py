n = int(input("Enter Any Number : "))

for i in range(1, n+1, 1):

    for j in range(1, i+1, 1):

        print((i+j-1)%2, end=" ")

    print("\n")