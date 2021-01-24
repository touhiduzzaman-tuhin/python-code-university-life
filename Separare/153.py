def gen(x):

    i = 0

    while i < x:

        yield i

        i = i + 1



x = gen(20)

print(x)

