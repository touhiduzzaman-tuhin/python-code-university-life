# Sum Of series

"""

loop

depends on n value
n = 10 ---> 10 * 2 = 20 operation
n = 10o ---> 10 * 2 = 200 operation

complexity

O(2 * n/20)
2*0(n/20)
O(n/20)
O(n)
Linear Complexity

"""

n = int(input())

res = 0

for i in range(1, n+1, 20):

    res = res + i

print(res)

