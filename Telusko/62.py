a = 5

b = 3

print(a / b)

print("Thank You")

print("----")

a = 5

b = 2

try:

    print(a / b)

except Exception:

    print("Not Divide By Zero")

print("Thank You")

print("---")

a = 5

b = 0

try:

    print(a / b)

except Exception as e:

    print("Not Divide By Zero And Error name is : ", e)

print("Thank You")

print("---")

a = 5

b = 0

try:

    print("Features Open")

    print(a / b)

except Exception:

    print("Not Divide By Zero")

finally:

    print("Features Close")

print("Thank You")

print("-----")

a = 5

b = 3

try:

    print("Features Open")

    print(a / b)

    n = int(input("Enter A Number : "))

    print(n)

except ZeroDivisionError:

    print("Not Divide by Zero")

except ValueError:

    print("Invalid input")

except Exception as e:

    print("Something Wrong : ", e)

finally:

    print("Features Close")

print("Thank You")