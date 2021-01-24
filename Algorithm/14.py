# Linear Search

n = int(input("How Many Number : "))

x = int(input("Enter Search Number: "))

for i in range(n):

    if x == i:

        print("Found")

        break

else:

    print("Not Found")