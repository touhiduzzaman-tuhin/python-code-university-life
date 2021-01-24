x = int(input("Enter Number of Rows: "))

for i in range(x):

    for j in range(x-i):

        print(str(j+1), end=" ")

    print()