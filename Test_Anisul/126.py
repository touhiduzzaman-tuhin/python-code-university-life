# 1*4*9*16*25....n

n = int(input("Enter Last Index: "))

sum = 1

for i in range(1, n+1, 1):

    sum *= i*i

print("Result : ", sum)