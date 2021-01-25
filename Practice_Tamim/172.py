class A:

    pass

a = A()

class B:

    pass

b = B()

print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, B))
print(isinstance(b, A))