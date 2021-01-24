def divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        print("Number Not Divide By Zero")

a = 5

b = 1

v = divide(a, b)

print(v)