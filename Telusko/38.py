def count(lst):

    even = 0

    odd = 0

    for i in lst:

        if i % 2 == 0 :

            even += 1

        else:

            odd += 1

    return even, odd


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even, odd = count(lst)

print("Even : ", even)

print("Odd : ", odd)

print("-----")

def count(lst):

    even = 0

    odd = 0

    for i in lst:

        if i % 2 == 0 :

            even += 1

        else:

            odd += 1

    return even, odd


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even, odd = count(lst)

print("Even : {}, Odd : {}".format(even, odd))


print("-----")

def count(lst):

    even = 0

    odd = 0

    for i in lst:

        if i % 2 == 0 :

            even += 1

        else:

            odd += 1

    return even, odd


n = int(input("Enter Your List Length : "))

lst = []

for i in range(n):

    n = int(input())

    lst.append(n)


print(lst)

even, odd = count(lst)

print("Even : ", even)

print("Odd : ", odd)

print("-----")

def Student(name):

    u = 0

    l = 0

    for i in name:

        ln = len(i)

        if ln > 5:

            u += 1

        else:

            l += 1

    return u, l



name = []

x = int(input("How Many Students : "))

print("Enter Students Name : ")

for i in range(x):

    n = str(input())

    name.append(n)

upper5, lower5 = Student(name)

print("Upper Students :  ", upper5)

print("Lower Students :  ", lower5)