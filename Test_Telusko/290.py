a = 10

def test():

    a = 20

    print("A : ", a)

    x = globals()['a']

    print("X : ", x)

test()

print("A~ : ", a)