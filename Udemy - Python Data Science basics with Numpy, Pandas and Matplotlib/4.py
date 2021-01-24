li = ['jan', 'feb', 'mar', 'apr', 'may']

print(li)

print(type(li))

print(li[0])
print(li[2])
print(li[2:4])
print(li[2:7])
print(li[2:])
print(li[:3])

print(li[-1])

print(li[::1])
print(li[::-1])

lst = li

print(lst)

li[0] = 'pan'

print(li)
print(lst)

lst[3] = 'kon'

print(li)
print(lst)

li.append('tuh')

print(li)

li.insert(0, 'mon')

print(li)

li.sort()

print(li)

li.reverse()

print(li)

print(li.index('may'))

print(li.count('jan'))

li.pop()

print(li)

li.pop(0)

print(li)

li.remove('may')

print(li)

print(li.__len__())

print(len(li))

li.extend(['kon', 'lol', 'bol'])

print(li)

li1 = li.copy()

print(li1)

del li[2]

print(li)

for i in li:

    print(li)

print("---")

for i in range(len(li)):

    print(li[i])

print("----")

print('lol' in li)

print(sorted(li))


li.sort(reverse=True)

print(li)

li = [1, 9, 7, 3, 4, 5]

print(li)

li.sort()

print(li)

for i in li:

    print(li)

print("---")

for i, j in enumerate(li):

    print(i, j)

print("----")

for i, j in enumerate(li, start=10):

    print(i, j)

print("---")

print(li)

li = ['kona', 'tuhin', 'rana', 'shahed']

print(li)

li1 = ' +'.join(li)

print(li1)

li1 = '$'.join(li)

print(li1)

li2 = list(li1)

print(li2)

li1 = ' & '.join(li)

print(li1)

li2 = li1.split(' ')

print(li2)


el = []

print(el)

el = list()

print(el)

