x = int(input("Enter A Number : "))

for i in range(x):

    for j in range(x-i):

        print(str(j+1), end=" ")

    print()