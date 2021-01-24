li = [1, 2, 3, 4, 5, 6]

print(li)

print(li[0])
print(li[1])
print(li[2])

print("-----")

li = [1, 2, 3, 4, 5, 6, "Tuhin"]

print(li)

print("--------")

li = [1, 2, 3, [3, 4, 5], 4, 5, 6]

print(li)
print(li[0])
print(li[3])
print(li[3][0])

print("--------")

li = [1, [1, 2, 3, [3, 4]], 2, 3, 4, 5, 6]

print(li)
print(li[0])
print(li[1])
print(li[1][3])
print(li[1][3][1])

print("----------")

li = [1, 2, 3, 4, 5, 6]

print(li)

li.append(7)

print(li)

li.insert(0, 0)

print(li)

li.extend([1, 2, 3])

print(li)

li = li + [1, 4, 6, 7]

print(li)

li.remove(3)

print(li)

li.remove(li[0])

print(li)

li.pop()

print(li)

li.pop(0)

print(li)

li.sort()

print(li)

l = li.index(5)

print(l)

l = li.count(4)

print(l)
