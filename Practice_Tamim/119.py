def func(x, y, z = None):

    x = x * x

    y = y * y

    if z == None:

        z = []


    return x, y, z

v = func(10, 20)

a, b, c = v

print(a)
print(b)
print(c)