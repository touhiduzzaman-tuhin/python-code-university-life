n = int(input("Enter A Number : "))

if n <= 1:

    print("Not Prime")

for i in range(2, n):

    if n % i == 0:

        print("Not Prime")

        break

else:

    print("Prime")