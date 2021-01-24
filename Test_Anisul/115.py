# 1+3+5+7+9......n

n = int(input("Enter Last Index: "))

sum = 0

for i in range(1, n+1, 2):

    sum += i

print("Result : ", sum)