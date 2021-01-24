with open("test2.txt", "r") as f:

    for i in f:

        print(i)

with open("test2.txt", "r") as f:
    print(f.read(10))
    print(f.read(10))

with open("test2.txt", "r") as f:
    print(f.readline())

with open("test2.txt", "r") as f:

    size = 10

    while (f.read() != ''):

        print(f.read(size))