
n = int(input("Enter Any Number : "))

sum = 0

for i in range(1, n+1, 1):

    sum += (i+1) * (i+1) * i * i


print("Sum : ", sum)