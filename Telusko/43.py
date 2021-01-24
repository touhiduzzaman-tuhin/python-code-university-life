def Square(n):

    return n * n


n = int(input("Enter A Number : "))

v = Square(n)

print("Square : ", v)

print("---")

f = lambda x: x * x

n = int(input("Enter A Number : "))

v = f(n)

print("Square : ", v)

print("---")


m = int(input("Enter A Number : "))

f = (lambda x: x * x)(m)


print("Square : ", f)

print("---")


a = int(input("Enter A Number : "))

b = int(input("Enter Another Number : "))

f = (lambda a, b: a + b)(a, b)


print("Result : ", f)

print("---")

