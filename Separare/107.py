def func(x, y, z = None):

    x = x * x

    y = y * y

    if z is None:

        z = []

    return x, y, z

v = func(10, 20)

print(v)