def func(x, y, z = 0):

    x = x * x

    y = y * y

    z = z * z

    return x, y, z


v = func(10, 20)

a, b, c = v

print(a)
print(b)
print(c)