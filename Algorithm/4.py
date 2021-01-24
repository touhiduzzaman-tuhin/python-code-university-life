# Sum Of series

"""

loop

depends on n value
n = 10 ---> 10 * 10 = 100 operation
n = 20 ---> 20 * 20 = 400 operation

complexity

O(n^2)


"""

n = int(input())

res = 0

for i in range(n):

    for j in range(n):

        res = res + 1

print(res)

