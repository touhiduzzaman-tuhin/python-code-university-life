import numpy as np

li = np.zeros(10)

print(li)

print("---")

li = np.ones(10)

print(li)

print("---")

li = li + 4

print(li)

print("---")

li = np.arange(10, 51)

print(li)

print("---")

li = np.arange(10, 51, 2)

print(li)

print("---")

li = np.arange(0, 9).reshape(3, 3)

print(li)

print("---")

li = np.eye(3)

print(li)

print("---")

li = np.random.rand(1)

print(li)

print("---")

li = np.random.randn(25)

print(li)

print("---")


li = np.linspace(0.01, 1, 100).reshape(10, 10)

print(li)

print("--")

li = np.arange(1, 101).reshape(10, 10)/100

print(li)

print("--")

li = np.linspace(0, 1, 20)

print(li)

print("---")

li = np.arange(1, 26).reshape(5, 5)

print(li)

print("--")

n = li[2:, 1:]

print(n)

print("--")

print(li[3, 4])

print("---")

print(li[:3,1:2])

print("---")

print(li[4])

print("---")

print(li[3:])

print("---")

print(np.sum(li))

print("--")

print(np.std(li))

print("---")


print(li.sum(axis=0))
