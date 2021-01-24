# 2+4+6+8......n

n = int(input("Enter Last Index: "))

sum = 0

for i in range(2, n+1, 2):

    sum += i

print("Result : ", sum)