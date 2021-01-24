gen = (x for x in range(10))

print(gen.__next__())
print(gen.__next__())

print("\n")
print("\n")

for i in gen:
    print(i)

