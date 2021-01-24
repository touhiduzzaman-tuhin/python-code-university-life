li = [x for x in range(10)]

print(li)

gen = (x for x in range(10))

print(gen)

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

print("\n")
print("\n")

for x in gen:
    print(x)

print(gen.__next__())

gen = (x for x in range(10))

print(sum(gen))