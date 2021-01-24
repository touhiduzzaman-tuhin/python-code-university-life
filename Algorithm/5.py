# Sum Of series

"""

loop

depends on n value
n = 10 ---> 10 * 3 = 30 operation
n = 20 ---> 20 * 3 = 60 operation

complexity

O(3n)
3*O(n)
O(n)
"""

n = int(input())

res = 0

for i in range(n):

    for j in range(3):

        res = res + 1

print(res)

