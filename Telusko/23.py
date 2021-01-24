x = int(input("Enter How Many Candy You Want : "))

ave = 10

for i in range(x):

    if i > 10:

        print("Out Of The stock")
        break

    print("Candy")

print("End")

print("----")



for i in range(1, 101):

    if i % 3 == 0:
        continue

    print(i)

print("End")

print("----")

for i in range(1, 101):

    if i % 3 == 0 or i % 5 == 0:
        continue

    print(i)

print("End")

print("----")

for i in range(1, 101):

    if i % 2 != 0:
        pass

    else:

        print(i)

print("End")

print("----")

x = int(input("Enter A Number : "))

if x <= 1:

    print("Not Prime")

for i in range(2, x):

    if x % i == 0:

        print("Not Prime")
        break

else:
    print("Prime Number")

print("----")

