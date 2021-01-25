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

        for i in range(2, n):

            a, b = b, a + b

            print(b, i)


fact(n)