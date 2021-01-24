import sys

print(sys.getrecursionlimit())

print("----")

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

print("--")
i = 0

def greet():

    global i

    i += 1

    print("Hello", i)

    greet()

greet()

print("---")
