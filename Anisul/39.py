n = []

n.append(1)
n.append(2)
n.append(3)
n.append(4)
n.append(5)

print(n)

n.pop()

print("Last Item Is: ", n[-1])

print(n)

n.pop()
n.pop()
n.pop()
n.pop()

print(n)

if not n:
    print("Empty List")