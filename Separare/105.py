def func(x, y, z=0):
    x = x * x

    y = y * y

    z = z * z

    return x, y, z


a, b, c = func(10, 20, 30)

print(a)
print(b)
print(c)

