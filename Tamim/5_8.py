class A:

    pass

a = A()

print(a.__class__)

class B(A):

    pass

b = B()

print(b.__class__)

print("\n")

print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, B))
print(isinstance(b, A))

print("\n")

print(issubclass(A, B))
print(issubclass(B, A))

print("\n")

print(issubclass(bool, int))




class Student:

    pass

tuhin = Student()

tuhin.name = "Touhiduzzaman"
tuhin.id = "162-15-7727"
tuhin.batch = 44
tuhin.sec = "G"
tuhin.sem = 10

print(tuhin)

print(tuhin.batch)
print(tuhin.name)
print(tuhin.id)