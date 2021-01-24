# Sum Of series

"""

loop

depends on n value
O(n^3 + n^2) --> O(n^3)
O(2*n^3 + n^2) --> O(n^3)
O(n! + n^2) --> O(n!)
complexity


"""

n = int(input())

res = 0

for i in range(n):

    for j in range(n):

        res = res + 1

print(res)

n = int(input())

res = 0

for i in range(n):

    res += 1

print(res)

