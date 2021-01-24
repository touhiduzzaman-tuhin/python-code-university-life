print(bool(True))
print(bool(False))
print(bool(0))
print(bool(-1))
print(bool(1))
print(bool(100))
print(bool(00000000))
print(bool(0.000000000000000001))

print(bool(" "))
print(bool(' '))
print(bool('Tuhin'))
print(bool(''))
print(bool(""))

a = True

b = False

print(a)
print(b)

print(not (a))
print(not (b))

print(a or b)
print(a and b)


x = [1, 2, 3, 4, 5, 6]

print(bool(x[1]))
print(bool(x[1:4]))


print(1 in x)
print(9 in x)

x = ['a', 'b', 'c']

print(type(x[0]))

print('a' in x)