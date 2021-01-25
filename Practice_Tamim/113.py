def func(x, li):

    print(x)

    print("Type of X : ", type(x))

    print("Type of List : ", type(li))

    x = 500

    li.append(4)

    return x

a = 10

my_li = [1, 2, 3]

print("List Before Call : ", my_li)

v = func(a, my_li)

print("List After Call : ", my_li)

print("Value Of A: ", a)

print("Value Of X: ", v)