try:

    list = [10, 0, 20]

    res = list[1]/list[3]

    print(res)

except (ValueError, NameError, IndexError, ZeroDivisionError):

    print("Error Found")

finally:

    print("Print It")