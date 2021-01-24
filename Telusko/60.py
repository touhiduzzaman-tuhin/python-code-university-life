num = [1, 2, 3, 4, 5]

print(num[0])
print(num[2])

print("--")

print(num)

print("--")

for i in num:

    print(i)

print("--")

for i in range(len(num)):

    print(num[i])

print("--")

num = [1, 2, 3, 4, 5]

it = iter(num)

print(it.__next__())

print(next(it))

print("--")

for i in num:

    print(i)

print("--")

for i in it:

    print(i)


print("----")

class Topten:

    def __init__(self):

        self.num = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.num <= 10:

            val = self.num

            self.num += 1

            return val

        else:

            raise StopIteration

v = Topten()

print(next(v))

print(v.__next__())

print("--")

for i in v:

    print(i)
