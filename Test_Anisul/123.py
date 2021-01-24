
# 4*8*12....n


n = int(input("Enter Last Index: "))

sum = 1

for i in range(4, n+1, 4):

    sum *= i

print("Result : ", sum)