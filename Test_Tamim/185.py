li = [1, 2, 3, 4]

print(li)

new_li = iter(li)

for i in new_li:
    
    print(i)

print(new_li.__next__())