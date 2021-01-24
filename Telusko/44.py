from functools import reduce

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(n):

    return n % 2 == 0

n = list(filter(even, li))

print(n)

print("-----")

a = list(filter(lambda x : x % 2 == 1, li))

print(a)

print("----")

b = list(map(lambda x: x*2, a))

print(b)

print("----")

c = reduce(lambda x, y: x + y, b)

print(c)

print("----")

d = list(map(lambda x: x / 2, b))

print(d)