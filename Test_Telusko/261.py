def cal(a, b):

    x = a + b

    y = a - b

    n = a * b

    d = a / b

    m = a % b

    return x, y, n, d, m


a, b, c, d, e = cal(10, 20)



print("Add : ", a)

print("Sub : ", b)

print("Mul : ", c)

print("Div : ", d)

print("Mod : ", e)
