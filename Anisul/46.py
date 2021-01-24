
def Square(x):

    return (x*x)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


res = list(map(Square, num))

print(res)


num = [1, 2, 3, 4, 5]

res = list(filter(lambda x : x % 2 == 0, num))

print(res)