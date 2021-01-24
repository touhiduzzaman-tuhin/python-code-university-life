def gen(n):

    for i in range(1, n):

        yield i

        i += 1

v = gen(20)

for i in v:

    print(i)