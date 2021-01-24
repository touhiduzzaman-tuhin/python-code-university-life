from array import *

vals = array('i', [2, -4, 5, 6, 7, 8])

print(vals)

print(vals[0])
print(vals[1])

print(vals.typecode)

print(vals.buffer_info())

num = array('I', [5, 6, 8, 9])

print(num)

num1 = array('f', [6.1, 7.08, 8.8, 8])

print(num1)

num2 = array('d', [6.1, 7.08, 8.8, 8])

print(num2)

num3 = array('i', [5, -6, 8, 9])

print(num3)

num4 = array('u', ['t', 'u', 'h', 'i', 'n'])

print(num4)

num5 = array('b', [-7, 6, 8, 9])

print(num5)

num6 = array('B', [0, 6, 8, 9])

print(num6)


li = array('i', [1, 2, 3, 4, 5, 6])

print(li)

print(li[0])
print(li[1])
print(li[2])

print(li[-1])
print(li[-2])

print(li.buffer_info())

print(li.typecode)

li.remove(4)

print(li)

li.reverse()

print(li)

print(li.index(2))

print(li.count(3))

print(len(li))

print(li.__len__())

li.insert(1, 9)

print(li)

li.append(10)

print(li)

li.pop()

print(li)

li.pop(0)

print(li)

for i in range(5):

    print(li[i])

print("---")

for i in range(len(li)):

    print(li[i])

print("---")

for i in li:

    print(i)

print("---")

i = 0

while i < len(li):

    print(li[i])

    i += 1

print("---")

print(li)



newli = array(li.typecode, (x for x in li))

print(newli)

li1 = array(li.typecode, (x*x for x in li))

for i in li1:

    print(i)

print("----")

#Sort

print("---")

x = int(input("Enter A Number : "))

def fact(x):

    if x <= 1:

        return 1

    else:

        return fact(x-1) * x

v = fact(x)

print(v)