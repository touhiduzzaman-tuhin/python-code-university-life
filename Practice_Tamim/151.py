def divide(x, y):

    try:

        z = x / y

    except ZeroDivisionError:

        print("Zero Not Devide")

    except TypeError:

        print("Data Type Not Support")

    except ValueError:

        print("Value Not Support")

    else:

        print("Result : ", z)

    finally:

        print("Finally print")

a = 10

b = 0

v = divide(a, b)

print(v)