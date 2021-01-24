x = str(input("Enter Any String : "))

print(x)

a = int(input("Enter The Start Index : "))

b = int(input("Enter The End Index : "))

if a > b:

    a, b = b, a

print(x[a:b])