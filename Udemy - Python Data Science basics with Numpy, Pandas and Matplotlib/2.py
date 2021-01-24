x = "My Name is Tuhin"

print(x)

x = "My Name's is Tuhin"

print(x)

x = 'My Name is Tuhin'

print(x)

x = 'My Name\'s is Tuhin'

print(x)

x = 'My Name"s is Tuhin'

print(x)

x = 'My Name \nis Tuhin'

print(x)

x = """
my name is tuhin
i am a student
"""

print(x)

x = 'My Name is Tuhin'

print(x[0])
print(x[2:8])
print(x[:8])
print(x[3:])

print(x[-1])
print(x[::1])

print(x.lower())

print(x.upper())

print(x.replace('n', 'm'))

print(x.find('M'))

a = "Hello"

b = "Tuhin"

print(a + b)

print(a + " " + b)

print("{} {}".format(a, b))

print("{} , {} How are You".format(a, b))

c = f"{a} {b} Good"

print(c)

c = f"{a.lower()} {b.upper()} Nad"

print(c)

print(help(str.upper))