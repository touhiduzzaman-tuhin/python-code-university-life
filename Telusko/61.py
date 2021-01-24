def Topten():

    return 5


v = Topten()

print(v)

print("---")

def Topten():

    yield 5


v = Topten()

print(v)

print("---")

def Topten():

    yield 5


v = Topten()

print(v.__next__())

print("--")
def Topten():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7


v = Topten()

print(v.__next__())

print(next(v))

print("---")

for i in v:

    print(i)


print("---")

def Topten():

    i = 1

    while i <= 10:

        yield i

        i += 1


v = Topten()

for i in v:

    print(i)

print("----")


def Topten():
    i = 1

    while i <= 10:

        sq = i * i

        yield sq

        i += 1


v = Topten()

for i in v:
    print(i)