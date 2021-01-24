a = 10

def tuhin():

    print(a)

tuhin()
print(a)
print("---")

a = 10

def tuhin():

    a = 15

    print(a)

tuhin()
print(a)
print("---")

a = 10

def tuhin():

    global a

    a = 15

    print(a)

tuhin()
print(a)
print("---")

a = 10

def tuhin():

    x = globals()['a']

    print(x)

tuhin()
print(a)
print("---")

a = 10

def tuhin():

    a = 9

    print("A : ", a)

    x = globals()['a']

    print("X : ", x)

tuhin()
print("A : ", a)
print("---")


a = 10
print("Initial A : ", id(a))

def tuhin():

    a = 9

    print("Local A : ", id(a))

    print("A : ", a)

    x = globals()['a']

    print("Global X : ",id(x))

    print("X : ", x)

tuhin()

print("A : ", a)

print("Last A : ", id(a))

print("---")
