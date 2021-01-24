from numpy import *

arr = array([

    [1, 2, 3],
    [4, 5, 6 ]
])

print(arr)

print(arr.ndim)
print(arr.size)
print(arr.shape)
print(arr.dtype)

arr1 = arr.flatten()

print(arr1)

arr2 = arr1.reshape(3, 2)

print(arr2)

print("----")

arr = array([

    [1, 2, 3, 4, 5, 6],
    [2, 5, 7, 8, 9, 8]
])

print(arr)

print(arr.flatten())

print(arr.reshape(4, 3))

print(arr.reshape(2, 2, 3))

print("-----")

arr = array([

    [1, 2, 3, 4, 5, 6],
    [2, 5, 7, 8, 9, 8]
])


m = matrix(arr)

print(m)

print("-----")

m = matrix('3, 4, 5 ; 7, 8, 9')

print(m)

print("-----")

m = matrix('1, 4, 5;3, 4, 5 ; 7, 8, 9')

print(m)

print("----")

print(diagonal(m))

print("---")

m1 =  matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')
m2 =  matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')

m3 = m1 + m2

m4 = m1 * m2

print(m1)
print(m2)

print(m3)
print(m4)