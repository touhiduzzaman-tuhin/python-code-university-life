with open('test2', 'r') as f:

    size = 4

    while (f.read() != ''):

        print(f.read(size))