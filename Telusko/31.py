from numpy import *

ar = array([1, 2, 3, 4])

print(ar)

print("---")

ar = array([1, 2, 3, 4])

ar = ar + 5

print(ar)

print("---")

ar1 = array([1, 2, 3, 4, 5])
ar2 = array([6, 7, 8, 9, 1])

ar = ar1 + ar2

print(ar)

print("---")

ar1 = array([1, 2, 3, 4, 5])
ar2 = array([6, 7, 8, 9, 1])

print(concatenate([ar1, ar2]))

print("---")


arr = array([1, 2, 3, 4, 5])

print(sum(arr))
print(min(arr))
print(max(arr))
print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(square(arr))
print("-----------")









ar1 = array([1, 2, 3, 4, 5])

ar = ar1

print(ar)
print(ar1)

print(id(ar))
print(id(ar1))

ar = ar + 5

print(ar)
print(ar1)

print(id(ar))
print(id(ar1))

print("---")

ar = array(([1, 2, 4]))

ar1 = ar

ar[1] = 7

print(ar)
print(ar1)

print(id(ar1))
print(id(ar))

print("-----")

ar = array(([1, 2, 4]))

ar1 = ar.view()

print(ar)
print(ar1)

print(id(ar1))
print(id(ar))

print("---")

ar = array(([1, 2, 4]))

ar1 = ar.copy()

print(ar)
print(ar1)

print(id(ar1))
print(id(ar))
