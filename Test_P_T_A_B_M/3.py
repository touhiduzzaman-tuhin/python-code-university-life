# Linear Search

li = [1, 2, 13, 4, 5, 6]

n = 13

l = len(li)

for i in range(l):

    if li[i] == n:

        print("Found At :", i+1, "Position")

        break

else:
    print("Not Found")