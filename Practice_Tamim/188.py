def gen(n):

    for i in n:

        yield i

        i += 1


v = gen(20)

print(v)