def great():

    print("Hello")

    print("Good Morning")

great()

print("----")

def add(x, y):

    z = x + y

    print(z)

add(10, 21)

print("----")

def add1(x, y):

    z = x + y

    return z

v = add1(12, 13)

print(v)

print("---")

def add_sub(x, y):

    a = x + y

    b = x - y
    
    return a, b

res1, res2 = add_sub(12, 16)

print(res1)
print(res2)