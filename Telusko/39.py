def fib(n):

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


n = int(input("How Many Numbers : "))

fib(n)

print("------")


def fib(n):
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

            if b > n:
                break

            print(b)


n = int(input("How Many Numbers : "))

fib(n)

print("------")

def fib(n):

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

            print(b)


n = int(input("Enter Last Number : "))

fib(n)

print("------")