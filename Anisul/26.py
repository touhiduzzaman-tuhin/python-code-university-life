#1+2+3+4+5+n

sum = 0

n = int(input("Enter Last Number : "))

for i in range(1, n+1, 1):

    sum += i

print(sum)

sum = 0

for i in range(1, n+1, 2):

    sum += i

print(sum)


sum = 0

for i in range(2, n+1, 2):

    sum += i

print(sum)

sum = 0

for i in range(4, n+1, 4):

    sum += i

print(sum)


sum = 0

for i in range(1, n+1, 2):

    sum += i*i

print(sum)

sum = 0

for i in range(2, n+1, 2):

    sum += i*i

print(sum)