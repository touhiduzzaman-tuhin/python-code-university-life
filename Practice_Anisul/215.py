file = open("Test.txt", "r+")

x = file.readlines()[1]

print(x)

file.close()