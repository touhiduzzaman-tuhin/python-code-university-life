def divide(a, b):

    try:
        result = a / b

        return result

    except ZeroDivisionError:

        print("Number Not Divide by zero")

a = 1

b = 5

v = divide(a, b)

print(v)