gen = (x for x in range(10))

for i in gen:
    print(i)

print(gen.__next__())