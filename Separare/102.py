def func(x, li):

    print("Type of A : ", type(x))

    print("Type of List : ", type(li))

    x = 500

    li.append(4)

    return x

a = 10

my_li = [1, 2, 3]

print("Lis Before Function: ", my_li)

v = func(a, my_li)

print("List after function: ", v)

print("value of A : ", a)
print("value of X : ", v)