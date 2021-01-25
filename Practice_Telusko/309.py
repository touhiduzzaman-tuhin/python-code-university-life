n = int(input("Enter A Number : "))

def fact(n):

    f = 1

    for i in range(1, n+1):

        f *= i

    return f

v = fact(n)

print(v)
