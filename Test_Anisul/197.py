def Square(x):

    res = x * x

    return res

x = [1, 2, 3, 4, 5]

n = list(map(Square, x))

print(n)