def func(x, li):

    print("Type of X", type(x))

    print("Type of Li", type(li))

    x = 500

    li.append(4)

    return x

a = 10

my_li = [1, 2, 3]

print("List Before Function : ", my_li)

y = func(a, my_li)

print("List After Function : ", my_li)

print("Value of A : ", a)

print("Value of Y : ", y)