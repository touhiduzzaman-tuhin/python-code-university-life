def calculate(a, b):

    res = a*a + 2*a*b + b*b

    return res

v = calculate(2, 3)

print(v)


def cube(a):

    res = a*a*a

    return res

v = cube(2)

print(v)



# (lamda parameters : expresions) (value)

x =( lambda a, b: a*a + 2*a*b + b*b) (2, 3)


print(x)


y = (lambda a: a*a*a)(2)

print(y)