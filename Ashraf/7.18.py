
n = int(input("Enter Any Number : "))

sum = 0

for i in range(1, n+1, 1):

    sum += (3*i-1) * (3*i+2) * (3*i+5)


print("Sum : ", sum)