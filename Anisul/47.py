#List Comprehension


#expression for loop

num = [1, 2, 3, 4, 5]

res = [x*x for x in num]


print(res)

res = [x for x in num if x % 2 == 0]

print(res)