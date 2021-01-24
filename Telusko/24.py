for i in range(4):

    for j in range(4):

        print("# ", end="")

    print()

print("---")

for i in range(4):

    for j in range(i+1):

        print("# ", end="")

    print()

print("-----")

for i in range(4):

    for j in range(4-i):

        print("# ", end="")

    print()

print("----")

for i in range(1, 5):

    for j in range(i, 5):

        print((str(j) + " "), end="")


    print()


print("-----")

for i in range(4):

    for j in range(4):

        print(chr(j+65) + " ", end="")

    print()

print("----")