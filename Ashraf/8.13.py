n = int(input("Enter Any Number : "))

for i in range(n, n >= 1, -1):

    for j in range(1, n+2-i, 1):

        print(i, end=" ")

    print("\n")