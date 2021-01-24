file = open("Test.txt", "r+")

l = file.read()

n = len(l)

print(n)

file.close()