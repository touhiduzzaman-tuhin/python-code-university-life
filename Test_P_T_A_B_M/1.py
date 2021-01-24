# Linear Search

li = [1, 2, 9, 4, 5, 6]

n = 9
j = 0

for i in li:

    j += 1

    if i == n:

        print("Found At :", j, "Position")

        break

else:

    print("Not Found")