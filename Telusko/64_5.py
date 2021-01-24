f = open('text', 'r')


f1 = open('abcd', 'a')

for i in f:

    f1.write(i)

print("--")


f.close()