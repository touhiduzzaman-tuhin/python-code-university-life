# Sum Of series

"""

loop

depends on n value
n = 10 ---> 10 * 2 = 20 operation
n = 10o ---> 10 * 2 = 200 operation

complexity

O(2n)
2*0(n)
O(n)
Linear Complexity

"""

n = int(input())

res = 0

i = n

while i >= 1:

    res = res + 1

    i -= 1

print(res)

