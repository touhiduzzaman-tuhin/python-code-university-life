def fact(n):

    if n == 1:

        return 1

    else:

        return n * fact(n-1)

v = fact(6)

print("Factorial : ", v)