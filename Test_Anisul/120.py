
# 1*2*3*4*5....n

n = int(input("Enter Last Index: "))

sum = 1

for i in range(1, n+1, 1):

    sum *= i

print("Result : ", sum)