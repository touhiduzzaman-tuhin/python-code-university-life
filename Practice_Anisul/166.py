n = []

print(n)

n.append(1)
n.append(2)
n.append(3)
n.append(4)
n.append(5)

print(n)

print("Last Item : ", n[-1])

n.pop()

print("Last Item : ", n[-1])

n.pop()
n.pop()
n.pop()
n.pop()

print(n)

if not n:

    print("Enpty List")
