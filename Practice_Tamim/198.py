gen = (x for x in range(5))

for i in gen:

    print(i)

print(gen.__next__())