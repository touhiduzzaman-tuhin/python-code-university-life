try:
    list = [10, 0, 20]

    res = list[0]/list[3]

    print(res)

except ZeroDivisionError:
    print("Not Divide By Zero")

except IndexError:
    print("Index Not Found")

except ValueError:
    print("Wrong Value Entered")


finally:
    print("All Time Print")
