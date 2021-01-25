li = []

n = int(input("How many Number "))


for i in range(n):

    ele = int(input())

    li.append(ele)

tpl = tuple(li)

print(tpl)

print(type(tpl))