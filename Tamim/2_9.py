x = set([])

print(x)

li = [1, 2, 3, 4, 5]

a = set(li)

print(a)

tpl = (3, 7, 5, 9, 10)

b = set(tpl)

print(b)

print(a & b)
print(a | b)
print(a ^ b)

print(7 in a)
print(7 in b)

c = set("abcd")

print(c)

li = [1, 1, 2, 2, 3, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7, 8]

print(li)

a = set(li)

print(a)

li = list(set(li))

print(li)