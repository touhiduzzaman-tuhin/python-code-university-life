def value(x, y):

    print(x, "-", y)

value(10, 20)

print("\n")

def value(x, y = 10):

    print(x, "-", y)

value(10)

print("\n")

def value(x, y = 10):

    print(x, "-", y)

value(10, 20)

print("\n")

def value(name, wish = "Happy Birth Day To "):

    print(wish, name)

value("Tuhin")

print("\n")

def value(name, wish = "Happy Birth Day To "):

    print(wish, name)

value("Tuhin", "Happy Frind Ship Day ")


print("\n")

var = 10

def value():

    print(var)

value()

print("\n")

var = 10

def value():

    print(var+2)

value()

print("\n")

var = 10

def value():

    # var = var + 2

    global var

    var = var + 2

    print(var)

value()


print("\n")

var = 10

def value():

    loc = var

    loc = loc + 5

    print(loc)

value()

print("\n")