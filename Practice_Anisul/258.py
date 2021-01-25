class A:

    def display(self):

        print("This is Class A")

a = A()
a.display()

print("---")

class B(A):

    def display1(self):

        print("This is Class B")

b = B()
b.display()
b.display1()

