n = int(input("Enter Any Number : "))

for i in range(1, n+1, 1):

    for j in range(1, i+1, 1):

        if i % 2 == 0:

            print(0, end=" ")

        else:

            print(1, end=" ")

    print("\n")