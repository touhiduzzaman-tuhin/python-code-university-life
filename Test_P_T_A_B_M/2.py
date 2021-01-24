# Linear Search

li = [1, 2, 12, 4, 5, 6, 3]

n = 12

c = 0

p = 0

for i in li:

    p += 1

    if i == n:

        c += 1

        break

if c == 1:

    print("Found At :", p , "Position")

else:

    print("Not Found")