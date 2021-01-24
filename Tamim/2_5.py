stack = []

stack.append(1)
stack.append(3)
stack.append(5)
stack.append(7)

print(stack)

print(stack.pop())

print(stack)

print("\n")

queue = []

queue.append(0)
queue.append(2)
queue.append(4)
queue.append(6)

print(queue)

print(queue.pop(0))

print(queue)

li = [1, 2, 3, 4, 5]

li2 = range(6, 21)

li.extend(li2)

print(li)

even = []

for i in li:
    if i % 2 == 0:
        even.append(i)

print(even)

odd = [i for i in li if i % 2 == 1]

print(odd)
