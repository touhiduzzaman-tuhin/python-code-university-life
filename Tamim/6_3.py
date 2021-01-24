def gen(n):

     i = 0

     while i < n:

         yield i

         i += 1


x = gen(20)

print(x)

for i in x:
    print(i)

for i in x:
    print(i)

print(x.__next__())