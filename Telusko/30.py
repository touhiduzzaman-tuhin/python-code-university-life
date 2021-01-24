from numpy import *

arr = array([1, 2, 3, 4])

print(arr)

print("---")

arr = zeros([6])

print(arr)

print("---")

arr = zeros(5)

print(arr)

print("---")

arr = zeros(5, int)

print(arr)

print("---")

arr = ones(5)

print(arr)

print("---")

arr = ones(5, int)

print(arr)

print("----")

arr = arange(1, 10)

print(arr)

print("---")

arr = arange(1, 10, 3)

print(arr)

print("---")

arr = linspace(1, 10)

print(arr)

print("---")

arr = linspace(1, 10, 5)

print(arr)

print("---")

arr = linspace(1, 20, 20)

print(arr)

print("---")

arr = logspace(1, 10)

print(arr)

print("---")

arr = logspace(1, 10, 5)

print(arr)

print("---")

arr = logspace(1, 10, 5)

print('%.3f' %arr[2])

print("---")

arr = logspace(1, 40, 5)

print('%.2f' %arr[4])

print("---")