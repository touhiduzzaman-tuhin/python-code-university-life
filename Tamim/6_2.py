s = "Bangladesh"


for ch in s:
    print(ch)

for i in [1, 3, 5, 7, 9]:
    print(i)

s = "Bangladesh"

st = iter(s)

print(st)

print(st.__next__())
print(st.__next__())
print(st.__next__())

li = [1, 3, 5, 7]

new_li = iter(li)

print(new_li)

for i in new_li:
    print(i)

print(new_li.__next__())

