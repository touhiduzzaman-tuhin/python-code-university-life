file = open("student.txt", "r")

print(file.readable())

print(file.writable())

print("\n")

file1 = open("student.txt", "w")

print(file1.readable())

print(file1.writable())

print("\n")

file2 = open("student.txt", "w+")

print(file2.readable())

print(file2.writable())

print("\n")


file.close()