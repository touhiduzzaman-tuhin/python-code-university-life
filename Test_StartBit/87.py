f = open('test', 'r+')

print(f.readline())

print(f.readline(10))

print(f.readline())

f.close()