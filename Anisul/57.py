try:
    list = [10, 0, 20]

    res = list[0]/list[3]

    print(res)

except (ZeroDivisionError, IndexError, ValueError):
    print("Error Found")


finally:
    print("All Time Print")
