
n = int(input("Enter Any Number : "))

sum = 0

for i in range(1, n+1, 1):

    sum += (2*i-1) * (2*i+1) * (2*i+3) * (2*i+5)


print("Sum : ", sum)