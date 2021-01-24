a = 3.6

print(a)

print(type(a))

a = 3

print(a)
print(type(a))

a = 3 + 6j

print(a)
print(type(a))

a = 3

print(a)

b = float(a)

print(b)

print(type(b))

a = 3.5

print(a)

b = int(a)

print(a)
print(type(b))

a = 5

b = 4

c = complex(a, b)

print(c)

print(a > b)

c = a > b

print(c)

print(type(c))

a = True

print(a)

b = int(a)

print(b)

a = False

print(a)

b = int(a)

print(b)

li = [1, 2, 3, 4, 5]

print(type(li))

tpl = (1, 2, 3, 4, 5)

print(type(tpl))

s = {1, 2, 3, 4}

print(type(s))

s = "Tuhin"

print(type(s))

s = 'a'

print(type(s))

r = range(10)

print(r)

li = list(range(10))

print(li)

li = list(range(2, 10, 2))

print(li)

li = list(range(1, 10, 2))

print(li)

print(type(r))

d = {

    "Tuhin" : "rangpur",
    "Shanto" : "Dhaka",
    "Shahed" : "Pabna",
    "Arif" : "Bogra"
}

print(d)

print(d.keys())

print(d.values())

print(type(d))

print(d["Tuhin"])

print(d.get("Arif"))