a = 10

print("A : ", a)

print("ID A : ", id(a))


def test():

    global a

    a = 20

    print("A Fun : ", a)

    print("Id A Fun : ", id(a))

    x = globals()['a']

    print("X :", x)

    print("Id X :", id(x))


test()

print("After A:", a)

print("After Id A :", id(a))
