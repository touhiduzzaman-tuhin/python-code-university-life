try:

    x = int(input("Enter A Number : "))

    y = int(input("Enter Another Number : "))

    res = x / y

    print("Result : ", res)

except TypeError:

    print("Type Error Found")

except ValueError:

    print("value Error Found")

except NameError:

    print("Name Error Found")

except ZeroDivisionError:

    print("Not Devide By Zero")

finally:

    print("Print It")