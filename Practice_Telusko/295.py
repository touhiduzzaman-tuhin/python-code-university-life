li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_odd(lst):

    e = 0
    o = 0

    for i in lst:

        if i % 2 == 0:

            e += 1

        else:

            o += 1

    return e, o

a, b = even_odd(li)

print(li)

print("Even : ", a)
print("Odd : ", b)