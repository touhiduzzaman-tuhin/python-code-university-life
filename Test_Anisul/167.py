from collections import deque

n = deque([])

n.append(1)
n.append(2)
n.append(3)
n.append(4)
n.append(5)

print(n)

n.popleft()

print(n)