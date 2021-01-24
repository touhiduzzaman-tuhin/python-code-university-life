file = open("student.txt", "r+")

line = file.readlines()

print(line)

print("\n")

file = open("student.txt", "r+")

text = file.read()

print(text)

size = len(text)

print(size)

print("\n")

file = open("student.txt", "r+")

line1 = file.readlines()[0]

print(line1)

print("\n")

file = open("student.txt", "r+")

for i in file:

    print(i)

file.close()