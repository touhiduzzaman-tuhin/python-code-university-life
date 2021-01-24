class A:

    def display(self):

        print("This is Class A")

class B:

    def display1(self):

        print("This is Class B")

class C(A,B):

    def display2(self):

        print("This is Class C")

c = C()
c.display1()
c.display()
c.display2()