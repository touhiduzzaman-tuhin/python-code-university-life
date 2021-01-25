n = int(input("Enter A Number : "))

def fact(n):

    if n == 1:

        return 1

    else:

        return n * fact(n-1)

v = fact(n)

print(v)