def divide(a, b):

    try:
        result = a / b
    except ZeroDivisionError:
        print("You Can't Divide By zero")
    except TypeError:
        print("Data Type Not Supported")
    else:
        return result
    finally:
        print("Inside Finally")


a = 5
b = 1

print(divide(a, b))

print("\n")

a = 1
b = 5

print(divide(a, b))

print("\n")

a = 5
b = 0

print(divide(a, b))

print("\n")

a = "5"
b = "1"

print(divide(a, b))


for i in range(10):
    print(i)

else:
    print("Inside Else")

print("\n")
print("\n")

for i in range(10):
    print(i)
    break

else:
    print("Inside Else")