f = open("example.txt", "r")

print(f.read())

print("-----")

print(f.read(10))

print("---")

print(f.readlines())

print("\n")

print(f.readline())
print(f.readline())
print(f.readline())

print("\n")

for i in f:

    print(i)