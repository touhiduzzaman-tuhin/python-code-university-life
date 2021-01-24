def update(x):

    x = 8

    print(x)

update(10)

print("----")


def update(x):
    x = 8

    print(x)

a  = 10

update(a)

print("----")


def update(x):
    x = 8

    print("X : ", x)


a = 10

print("A : ",a)

update(a)

print("A : ",a)

print("----")


def update(x):

    print(id(x))

    x = 8

    print(id(x))

    print(x)


a = 10

print(id(a))

update(a)

print("----")

def update(li):

    print(id(li))

    li[0] = 15

    print(id(li))

    print(li)


lst = [10, 20, 25]

print(id(lst))

print(lst)

update(lst)

print(id(lst))

print(lst)