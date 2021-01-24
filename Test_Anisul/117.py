# 4+8+12+16+20......n

n = int(input("Enter Last Index: "))

sum = 0

for i in range(4, n+1, 4):

    sum += i

print("Result : ", sum)