def divide(a, b):

    try:
        result = a / b


    except ZeroDivisionError:

        print("Number Not Divide by zero")

    except TypeError:

        print("Data Type Not Supported")

    else:

        return result

    finally:

        print("Inside Finally")

a = 1

b = 0

v = divide(a, b)
