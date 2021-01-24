gen = (x for x in range(10))

v = sum(gen)

print(v)

print("\n")

print(gen.__next__())