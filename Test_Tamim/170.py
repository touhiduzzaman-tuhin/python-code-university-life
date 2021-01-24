class A:

    pass

a = A()

class B:

    pass

b = B()

print(issubclass(A, B))
print(issubclass(B, A))