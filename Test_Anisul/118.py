# 1+9+25......n

n = int(input("Enter Last Index: "))

sum = 0

for i in range(1, n+1, 2):

    sum += i*i

print("Result : ", sum)