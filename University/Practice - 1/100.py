x = int(input("Enter Number of rows : "))


for i in range(x):

    print(" "*(x-i-1) + "* "*(i+1))

for i in range(x-1):

     print(" " * (i + 1) + "* " * (x- i - 1))
