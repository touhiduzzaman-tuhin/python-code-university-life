def fnc(x, y, z = 0):

    x = x * x

    y = y * y

    z = z * z

    return x, y, z

v = fnc(10, 20, 30)

a, b, c = fnc(10, 20, 30)

print(v)

print(a)
print(b)
print(c)

print("\n")

a, b, c = fnc(10, 20)

print(a)
print(b)
print(c)

def func(x, y, z = None):

    x = x * x

    y = y * y

    if z is None:
        z = []

    return x, y, z


v = func(10, 20)

print(v)

def fun(x, y, z = None):

    x = x * x

    y = y * y

    if z is None:
        z = []

    return (x, y, z)


a, b, c = fun(10, 20)

print(a)
print(b)
print(c)