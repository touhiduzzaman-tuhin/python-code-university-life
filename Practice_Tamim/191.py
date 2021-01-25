def gen(n):

    i = 0

    while n > i:

        yield i

        i += 1

v = gen(20)

for i in v:

    print(i)
