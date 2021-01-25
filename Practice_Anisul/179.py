def large(x, y):

    if x > y:

        return x
    else:

        return y

x = int(input("Enter A Number : "))

y = int(input("Enter A Number : "))

v = large(x, y)

print("Max Number : ", v)