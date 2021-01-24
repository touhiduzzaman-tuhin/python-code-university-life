class A:

    pass

a = A()

class B(A):

    pass

b = B()

print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, B))
print(isinstance(b, A))