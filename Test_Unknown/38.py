x = int(input("Enter A Number Starting Pont : "))

y = int(input("Enter Another Number Ending Point : "))

if x % 2 == 0:
    
    x  = x +1

for i in range(x, y+1, 2):

    print(i)