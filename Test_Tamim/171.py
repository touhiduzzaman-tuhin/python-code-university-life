class A:

    pass

a = A()

class B(A):

    pass

b = B()

print(issubclass(A, B))
print(issubclass(B, A))