
n = int(input("Enter Any Number : "))

sum = 0

for i in range(1, n+1, 1):

    sum += (i+4) * (i+5) * (i+6)


print("Sum : ", sum)