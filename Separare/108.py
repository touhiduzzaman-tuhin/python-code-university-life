def func(x, y, z = None):

    x = x * x

    y = y * y

    if z is None:

        z = []

    return x, y, z

a, b, c = func(10, 20)

print(a)
print(b)
print(c)