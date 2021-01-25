n = int(input("Enter A Number : "))

def fact(n):

    a = 0

    b = 1

    if n < 0:

        print("Invalid Number")

    elif n == 1:

        print(a)

    else:

        print(a)
        print(b)

        while b < n:

            a, b = b, a + b

            print(b)


fact(n)