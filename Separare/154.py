def gen(n):

    i = 0

    while i < n:

        yield i

        i += 1

x = gen(20)

for i in x:
    print(i)