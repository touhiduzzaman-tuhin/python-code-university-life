n = int(input("Enter Any Number : "))

c = 0

while n > 0:

    c += 1

    n = n // 10

    print(n)


print("Length : ", c)