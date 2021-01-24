class A:

    def display(self):

        print("This is Class A")

class B(A):

    def display1(self):

        print("This is Class B")

class C(B):

    def display2(self):

        print("This is Class C")

c = C()
c.display1()
c.display()
c.display2()