def fact(n):

    if n == 0:

        return 1

    return n * fact(n-1)

n = int(input("Enter A number : "))

v = fact(n)

print(v)

print("----")
def fact(n):

    if n == 1:

        return 1

    return n * fact(n-1)

n = int(input("Enter A number : "))

v = fact(n)

print(v)