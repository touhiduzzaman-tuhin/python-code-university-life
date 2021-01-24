tpl = (1, 2, 3.4, "Tuhin")

print(tpl)

print(tpl[0])
print(tpl[2])
print(tpl[3])

print(tpl[-1])
print(tpl[-2])
print(tpl[-3])

print(type(tpl))
print(type(tpl[1]))
print(type(tpl[2]))
print(type(tpl[3]))

li = list(tpl)

print(li)

print(type(li))

tpl1 = (1, 2, 3)

print(tpl)

print(type(tpl1))

a, b, c = tpl1

print(a)
print(b)
print(c)

x = (1, 2, 3, "Tuhin", 3.5)

for i in x:

    print(i)

x = (1, 2, 3, (4, 5, 6))

print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])