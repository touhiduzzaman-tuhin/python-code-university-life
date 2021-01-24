li = [1, 2, 3, 4, 5, 6, 7, 8]

print(li)

li.reverse()

print(li)

li.sort()

print(li)

li.count(2)

print(li)

print(len(li))

li.append(9)

print(li)

li.insert(0, 0)

print(li)


li2 = range(10,20)

li.extend(li2)

print(li)


print(li.count(9))

print(li2.count(9))

li.remove(5)

print(li)

li.pop()

print(li)

print(li.pop(0))

print(li)

x = [0] * 100

print(x, "\n")

a = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

b = a

print(a)
print(b)

a[0] = 9

print(a)
print(b)

b.pop()

print(a)
print(b)