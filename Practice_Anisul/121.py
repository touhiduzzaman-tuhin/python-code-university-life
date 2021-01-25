
# 1*3*5....n


n = int(input("Enter Last Index: "))

sum = 1

for i in range(1, n+1, 2):

    sum *= i

print("Result : ", sum)