a = 10

def test():

    global a

    a = 20

    print("A : ", a)

    x = globals()['a']

    print("X : ", x)

test()

print("A~ : ", a)