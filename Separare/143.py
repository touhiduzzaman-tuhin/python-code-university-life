def divide(a, b):

    try:
        result = a / b

        return result

    except TypeError:

        print("Data Type Not Supported")

a = "1"

b = "5"

v = divide(a, b)
