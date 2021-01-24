tpl = ('jan', 'man', 'god', 'bad', 'mam', 'dog')

print(tpl)

print(type(tpl))

print(tpl[0])
print(tpl[4])
print(tpl[2:5])
print(tpl[2:])
print(tpl[:4])

print(tpl[::1])
print(tpl[::-1])
print(tpl[-1])

print(tpl.__len__())

print(len(tpl))

tpl1 = tpl

print(tpl1)


et = ()

print(et)

et = tuple()

print(et)

print('jan' in tpl)
print('Jan' in tpl)

for i in tpl:

    print(i)