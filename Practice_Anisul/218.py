file = open("Test.txt", "r+")

l = file.readlines()

n = len(l)

print(n)

file.close()