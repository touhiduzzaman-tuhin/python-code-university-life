file = open("Test.txt", "r+")

l = file.readlines()[0]

n = len(l)

print(n)

file.close()