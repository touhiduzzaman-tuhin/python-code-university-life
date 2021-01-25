n = int(input("Enter a Number : "))

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

        for i in range(n-1):

            a, b = b, a + b

            if b > n:

                break

            else:

                print(b)


fact(n)