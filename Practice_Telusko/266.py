def update(x):

    print(id(x))
    print(id(a))

    x = 12

    print(id(x))

a = 10

print(id(a))

update(a)

print(id(a))