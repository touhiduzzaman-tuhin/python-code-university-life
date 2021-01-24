# Sum Of series

"""

loop

depends on n value
n = 10 ---> 10 * 10 * 10 = 1000 operation
n = 20 ---> 20 * 20 * 20 = 8000 operation

complexity

O(n^3)


"""

n = int(input())

res = 0

for i in range(n):

    for j in range(n):

        for j in range(n):

            res = res + 1

print(res)

