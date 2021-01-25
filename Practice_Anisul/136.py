x = input("Enter A List: ")

x = x.split()

sum = 0

for i in x:

    sum += int(i)

print("Result : ", sum)