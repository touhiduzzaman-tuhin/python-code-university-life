n1 = {1, 2, 3, 4, 5}

print(n1)

n1 = {1, 2, 3, 4, 5, 5}

print(n1)

n2 = set([4, 5, 6])

print(n2)

n2.add(7)

print(n2)

n2.remove(6)

print(n2)

print(7 in n2)
print(7 not in n2)

print("Union : ", n1 | n2)
print("Intersection: ", n1 & n2)
print("Difference : ", n1- n2)
